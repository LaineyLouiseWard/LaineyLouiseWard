#!/usr/bin/env python3
"""Convert PDFs to markdown files using MinerU.

MinerU handles layout detection, table extraction, formula-to-LaTeX
conversion, and OCR. Uses GPU when available, falls back to CPU.

Each PDF is converted via MinerU's CLI in a subprocess so that GPU
memory is fully reclaimed between papers.

Two modes:
  - Default (Zotero): queries Zotero SQLite for PDFs and metadata.
  - --pdf-dir: converts all PDFs in a given directory (no Zotero needed).
    Derives output filename from the PDF filename. Useful for loose PDFs
    like ECMWF technical memos that aren't in Zotero.
"""

import argparse
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

ZOTERO_DB = Path.home() / "Zotero" / "zotero.sqlite"
ZOTERO_STORAGE = Path.home() / "Zotero" / "storage"
OUTPUT_DIR = Path.home() / "Documents" / "zotero-md"
MANIFEST_PATH = Path(__file__).parent / "manifest.json"
MINERU_BIN = Path.home() / "miniconda3" / "envs" / "MH-Index-Review" / "bin" / "mineru"


def get_zotero_metadata():
    """Query Zotero SQLite for PDF metadata. Returns dict keyed by storage key."""
    uri = f"file:///{ZOTERO_DB}?immutable=1"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("""
        SELECT
            i_att.key AS storage_key,
            title_val.value AS title,
            date_val.value AS date_raw,
            ia.path AS pdf_path
        FROM items i_att
        JOIN itemAttachments ia ON ia.itemID = i_att.itemID
        JOIN items i_parent ON i_parent.itemID = ia.parentItemID
        LEFT JOIN itemData id_title ON id_title.itemID = i_parent.itemID AND id_title.fieldID = 1
        LEFT JOIN itemDataValues title_val ON title_val.valueID = id_title.valueID
        LEFT JOIN itemData id_date ON id_date.itemID = i_parent.itemID AND id_date.fieldID = 6
        LEFT JOIN itemDataValues date_val ON date_val.valueID = id_date.valueID
        WHERE ia.contentType = 'application/pdf'
          AND i_att.itemID NOT IN (SELECT itemID FROM deletedItems)
          AND ia.parentItemID NOT IN (SELECT itemID FROM deletedItems)
    """)

    rows = c.fetchall()

    c.execute("""
        SELECT i_att.key AS storage_key, ia.parentItemID
        FROM items i_att
        JOIN itemAttachments ia ON ia.itemID = i_att.itemID
        WHERE ia.contentType = 'application/pdf'
          AND i_att.itemID NOT IN (SELECT itemID FROM deletedItems)
          AND ia.parentItemID NOT IN (SELECT itemID FROM deletedItems)
    """)
    key_to_parent = {r["storage_key"]: r["parentItemID"] for r in c.fetchall()}

    parent_ids = tuple(set(key_to_parent.values()))
    authors_by_item = {}
    if parent_ids:
        placeholders = ",".join("?" * len(parent_ids))
        c.execute(f"""
            SELECT ic.itemID, c.lastName, ic.orderIndex
            FROM itemCreators ic
            JOIN creators c ON c.creatorID = ic.creatorID
            WHERE ic.itemID IN ({placeholders})
            ORDER BY ic.itemID, ic.orderIndex
        """, parent_ids)
        for r in c.fetchall():
            authors_by_item.setdefault(r["itemID"], []).append(r["lastName"])

    conn.close()

    metadata = {}
    for row in rows:
        key = row["storage_key"]
        parent_id = key_to_parent.get(key)
        authors = authors_by_item.get(parent_id, []) if parent_id else []

        year = None
        if row["date_raw"]:
            m = re.search(r"(\d{4})", row["date_raw"])
            if m:
                year = m.group(1)

        pdf_path_str = row["pdf_path"] or ""
        if pdf_path_str.startswith("storage:"):
            pdf_filename = pdf_path_str[len("storage:"):]
        else:
            pdf_filename = pdf_path_str

        pdf_path = ZOTERO_STORAGE / key / pdf_filename

        metadata[key] = {
            "title": row["title"] or "Untitled",
            "authors": authors,
            "year": year,
            "pdf_path": str(pdf_path),
        }

    return metadata


def slugify(title, first_author, year):
    """Generate a clean filename slug from metadata."""
    def strip_accents(s):
        return "".join(
            c for c in unicodedata.normalize("NFKD", s)
            if not unicodedata.combining(c)
        )

    parts = []
    if first_author:
        parts.append(strip_accents(first_author).lower())
    if year:
        parts.append(year)

    title_clean = strip_accents(title).lower()
    title_clean = re.sub(r"[^a-z0-9\s]", "", title_clean)
    words = [w for w in title_clean.split() if len(w) > 2][:8]
    parts.extend(words)

    slug = "-".join(parts)
    if len(slug) > 80:
        slug = slug[:80].rsplit("-", 1)[0]

    return slug or "unknown"


def load_manifest():
    if MANIFEST_PATH.exists():
        m = json.loads(MANIFEST_PATH.read_text())
        m.setdefault("converted", {})
        m.setdefault("failed", {})
        return m
    return {"version": 3, "converted": {}, "failed": {}}


def save_manifest(manifest):
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))


def make_frontmatter(meta, zotero_key):
    """Create YAML frontmatter string."""
    title = meta["title"].replace('"', '\\"')
    authors = json.dumps(meta["authors"])
    lines = [
        "---",
        f'title: "{title}"',
        f"authors: {authors}",
    ]
    if meta["year"]:
        lines.append(f"year: {meta['year']}")
    lines.append(f"zotero_key: {zotero_key}")
    lines.append("---\n")
    return "\n".join(lines)


def resolve_filename(slug, existing_filenames):
    """Handle duplicate slugs by appending -2, -3, etc."""
    candidate = slug
    counter = 2
    while candidate in existing_filenames:
        candidate = f"{slug}-{counter}"
        counter += 1
    return candidate


def convert_mineru(pdf_path, output_file, lang="en"):
    """Convert a single PDF using MinerU. Returns 0 on success, nonzero on failure."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"    ERROR: PDF missing at {pdf_path}", file=sys.stderr)
        return 3

    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = [
            str(MINERU_BIN),
            "-p", str(pdf_path),
            "-o", tmpdir,
            "-b", "pipeline",
            "-l", lang,
            "-m", "auto",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            stderr_tail = result.stderr[-500:] if result.stderr else ""
            print(f"    MinerU failed (exit {result.returncode})", file=sys.stderr)
            if stderr_tail:
                print(f"    {stderr_tail}", file=sys.stderr)
            return 1

        # Find the generated .md file in MinerU's output structure
        md_files = list(Path(tmpdir).rglob("*.md"))
        if not md_files:
            print("    ERROR: MinerU produced no markdown output", file=sys.stderr)
            return 1

        md_content = md_files[0].read_text()

        return md_content


def convert_one(key, meta, output_file, lang="en"):
    """Convert one paper: run MinerU, prepend frontmatter, write to OUTPUT_DIR."""
    result = convert_mineru(meta["pdf_path"], output_file, lang=lang)

    if isinstance(result, int):
        return result

    md_content = result
    frontmatter = make_frontmatter(meta, key)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / output_file
    output_path.write_text(frontmatter + "\n" + md_content)
    print(f"    WROTE {output_path}", file=sys.stderr)
    return 0


def slugify_filename(pdf_name):
    """Derive a slug from a PDF filename (for --pdf-dir mode)."""
    stem = Path(pdf_name).stem
    clean = stem.lower()
    clean = re.sub(r"[^a-z0-9\s_-]", "", clean)
    clean = re.sub(r"[\s_]+", "-", clean)
    clean = re.sub(r"-+", "-", clean).strip("-")
    if len(clean) > 80:
        clean = clean[:80].rsplit("-", 1)[0]
    return clean or "unknown"


def make_frontmatter_from_filename(pdf_name):
    """Create minimal YAML frontmatter from a PDF filename."""
    stem = Path(pdf_name).stem
    lines = [
        "---",
        f'source_pdf: "{pdf_name}"',
        "---\n",
    ]
    return "\n".join(lines)


def convert_pdf_dir(pdf_dir, output_dir=None, force=False, dry_run=False,
                    limit=0, lang="en"):
    """Convert all PDFs in a directory (no Zotero needed)."""
    pdf_dir = Path(pdf_dir)
    if not pdf_dir.is_dir():
        print(f"ERROR: {pdf_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    out = Path(output_dir) if output_dir else OUTPUT_DIR
    out.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {pdf_dir}")
        return

    to_convert = []
    for pdf in pdfs:
        slug = slugify_filename(pdf.name)
        output_file = out / f"{slug}.md"
        if not force and output_file.exists():
            print(f"  SKIP (exists): {output_file.name}")
            continue
        to_convert.append((pdf, slug, output_file))

    if limit > 0:
        to_convert = to_convert[:limit]

    print(f"Found {len(pdfs)} PDFs, {len(to_convert)} to convert")

    if dry_run:
        for pdf, slug, output_file in to_convert:
            print(f"  {pdf.name} -> {output_file.name}")
        return

    converted = 0
    failed = []
    for i, (pdf, slug, output_file) in enumerate(to_convert, 1):
        print(f"\n  [{i}/{len(to_convert)}] {pdf.name} -> {output_file.name}")
        result = convert_mineru(str(pdf), str(output_file), lang=lang)

        if isinstance(result, int):
            print(f"    FAILED (exit {result})")
            failed.append((pdf.name, result))
            continue

        frontmatter = make_frontmatter_from_filename(pdf.name)
        output_file.write_text(frontmatter + "\n" + result)
        print(f"    WROTE {output_file}")
        converted += 1

    print(f"\nDone: {converted} converted, {len(failed)} failed")
    if failed:
        for name, rc in failed:
            print(f"  {name}: exit {rc}")


def main():
    parser = argparse.ArgumentParser(description="Convert PDFs to markdown using MinerU")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be converted")
    parser.add_argument("--force", action="store_true", help="Re-convert already converted files")
    parser.add_argument("--retry-failed", action="store_true", help="Retry papers in the failed list")
    parser.add_argument("--limit", type=int, default=0, help="Max papers to convert (0=all)")
    parser.add_argument("--lang", default="en", help="OCR language (default: en)")
    parser.add_argument("--single", metavar="KEY", help="Convert a single paper by Zotero storage key")
    parser.add_argument("--pdf-dir", metavar="DIR",
                        help="Convert all PDFs in DIR (no Zotero needed)")
    parser.add_argument("--output-dir", metavar="DIR",
                        help="Output directory for --pdf-dir mode (default: ~/Documents/zotero-md)")
    args = parser.parse_args()

    if args.pdf_dir:
        convert_pdf_dir(
            args.pdf_dir,
            output_dir=args.output_dir,
            force=args.force,
            dry_run=args.dry_run,
            limit=args.limit,
            lang=args.lang,
        )
        return

    if args.single:
        metadata = get_zotero_metadata()
        if args.single not in metadata:
            print(f"ERROR: zotero key {args.single} not found", file=sys.stderr)
            sys.exit(2)
        meta = metadata[args.single]
        first_author = meta["authors"][0] if meta["authors"] else None
        slug = slugify(meta["title"], first_author, meta["year"])
        output_file = f"{slug}.md"
        print(f"  {output_file}", file=sys.stderr)
        rc = convert_one(args.single, meta, output_file, lang=args.lang)
        sys.exit(rc)

    print("Querying Zotero database...")
    metadata = get_zotero_metadata()
    print(f"Found {len(metadata)} PDFs in Zotero")

    manifest = load_manifest()
    existing_filenames = {v["output_file"].replace(".md", "") for v in manifest["converted"].values()}

    to_convert = {}
    for key, meta in metadata.items():
        if not args.force and key in manifest["converted"]:
            continue
        if not args.retry_failed and key in manifest["failed"]:
            continue
        pdf_path = Path(meta["pdf_path"])
        if not pdf_path.exists():
            print(f"  SKIP {key}: PDF not found at {pdf_path}")
            continue
        to_convert[key] = meta

    if args.limit > 0:
        to_convert = dict(list(to_convert.items())[:args.limit])

    print(f"{len(to_convert)} papers to convert")

    if args.dry_run:
        for key, meta in to_convert.items():
            first_author = meta["authors"][0] if meta["authors"] else None
            slug = slugify(meta["title"], first_author, meta["year"])
            slug = resolve_filename(slug, existing_filenames)
            print(f"  {key}: {slug}.md")
        return

    if not to_convert:
        print("Nothing to convert.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    converted_count = 0
    failed = []
    total = len(to_convert)

    for i, (key, meta) in enumerate(to_convert.items(), start=1):
        first_author = meta["authors"][0] if meta["authors"] else None
        slug = slugify(meta["title"], first_author, meta["year"])
        slug = resolve_filename(slug, existing_filenames)
        output_file = f"{slug}.md"

        print(f"\n  [{i}/{total}] {output_file}")

        rc = convert_one(key, meta, output_file, lang=args.lang)

        if rc == 0:
            manifest["converted"][key] = {"output_file": output_file, "converter": "mineru"}
            manifest["failed"].pop(key, None)
            existing_filenames.add(slug)
            save_manifest(manifest)
            converted_count += 1
        else:
            reason = f"mineru exit {rc}"
            print(f"    FAILED ({reason})")
            manifest["failed"][key] = {
                "output_file": output_file,
                "returncode": rc,
            }
            save_manifest(manifest)
            failed.append((key, reason))

    print(f"\nDone: {converted_count} converted, {len(failed)} failed")
    if failed:
        print("Failed papers (saved to manifest; rerun with --retry-failed to retry):")
        for key, reason in failed:
            print(f"  {key}: {reason}")


if __name__ == "__main__":
    main()
