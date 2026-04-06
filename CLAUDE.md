# Cross-Repository Working Conventions

## Who I am

PhD researcher at UCD (Decarb-AI Centre / Innovate for Ireland iScholar) working on AI for subseasonal-to-seasonal (S2S) weather and climate prediction. Background in operational aeronautical meteorology (Met Éireann) and atmospheric science (MSc, University of Reading). My work spans ML-based forecast verification, compound extreme weather events, satellite data processing, and science communication.

## Repository overview

| Repo | Purpose |
|------|---------|
| **S2S_AI** | Primary research: verification of ECMWF seasonal reforecasts against observations at Irish point locations. Python, xarray, CDS/MARS APIs. Has its own CLAUDE.md with detailed data and scoring conventions. |
| **S2S_Thesis** | PhD thesis (LaTeX/BibTeX). Literature review and methodology covering S2S predictability, compound hydroclimatic extremes, and verification methods. ~600 BibTeX entries managed via Zotero. |
| **ClassImbalance** | Published paper implementation: class-imbalanced rural image segmentation with cross-dataset knowledge transfer. PyTorch/Lightning, 5-stage ablation. Has its own CLAUDE.md. |
| **EUMETSAT_GIFS** | Satellite storm animations from MSG SEVIRI data for science communication. Python, Satpy, Cartopy. |
| **research-literature-monitor** | Automated daily RSS screening of academic feeds, scored by Claude Haiku. Python, Feedparser, Anthropic API. |
| **LaineyLouiseWard.github.io** | Personal portfolio site. Astro 5, TypeScript, GitHub Pages. |
| **the-ensemble-site** | Interdisciplinary PhD student blog on AI and climate. Astro 5, Tailwind, MDX, Vercel. Has its own CLAUDE.md. |

Repos with their own CLAUDE.md (S2S_AI, ClassImbalance, the-ensemble-site) define repo-specific conventions that take precedence over anything here.

## README structure

Every repo README should follow this structure:

1. **Title and one-line purpose** — what the repo does, not what it is
2. **Broader context** — how it fits into the wider research programme or why it exists (1–3 sentences)
3. **Tech stack** — languages, key libraries, deployment target
4. **Getting started** — setup and run instructions (environment, install, entry point)
5. **Project structure** — brief directory layout if not obvious
6. **Data** — where data comes from, what's tracked vs gitignored, any access requirements
7. **Licence / citation** — if applicable

Keep READMEs factual and scannable. No badges walls, no aspirational feature lists, no boilerplate.

## General working preferences

- **Be concise.** Lead with the answer or action. Skip preamble, filler, and restating what I said.
- **Don't over-engineer.** Make the minimal change that solves the problem. No speculative abstractions, unnecessary error handling for impossible cases, or feature flags for single-use code.
- **Don't add unrequested extras.** No docstrings, type annotations, or comments on code you didn't change. Only comment where logic isn't self-evident.
- **No redundancy.** Don't summarise what you just did — I can read the diff. Don't re-explain what I already know.
- **Prefer editing to creating.** Modify existing files rather than creating new ones unless genuinely necessary.
- **No hard-coded absolute paths.** Use repo-root-relative paths or config files.
- **Reproducibility matters.** Research code should be runnable by someone else with the same data and environment. Pin dependencies, document data provenance, use config files as single source of truth.
- **Respect existing conventions.** Check for repo-level CLAUDE.md and follow it. Match the style of surrounding code.
- **When proposing changes to research code,** state: which files change, what inputs/outputs are affected, and any assumptions.

## Environment

- OS: Linux (Ubuntu)
- Editor: VS Code with Claude Code, GitHub Copilot
- Python: Conda environments (per-repo)
- Web: Astro, npm
- Writing: LaTeX, Zotero (with MCP integration)
- Version control: Git + GitHub
