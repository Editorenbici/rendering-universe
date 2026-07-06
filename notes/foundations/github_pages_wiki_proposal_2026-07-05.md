# GitHub Pages proposal for `wiki/`

Date: 2026-07-05

Status: proposal only. Do not publish until the author flips the switch.

## Recommendation

Use GitHub Pages from the same repository, serving from `/docs` on `master`.

Reason: the project already has a public repo and a `wiki/` directory. A same-repo Pages site keeps provenance close to the code while avoiding a second repo to maintain. GitHub Pages cannot directly serve `wiki/` as the source folder, so the clean path is:

1. Keep author-facing source notes in `wiki/`.
2. Generate or copy a small curated public site into `docs/`.
3. Enable Pages from `master` / `/docs` only when the author approves.

## Minimal site shape

Language: Spanish first.

Theme: plain static HTML or Jekyll `minima`; no heavy framework.

Pages:

- `index.md`: one-paragraph project description, current status, and link to Paper 1.
- `experimentos.md`: status table copied from `notes/experiments_manifest.md`, with dead/frozen results visible.
- `metodo.md`: preregistration, audit, negative results, and reproducibility.
- `rendernum.md`: `N_R` arithmetic and link to the pip-installable package.
- `papers.md`: Paper 1, planned Paper 2, planned Paper 3.

## Guardrails

- No cosmology victory language.
- No "confirmed theory" language.
- Frozen sectors must be visible: Exp 20 and dark-matter sector stay labeled as frozen.
- The site should point to the repo as the evidence source, not replace it.
- The first public version should be static and boring enough to trust.

## Implementation sketch

Suggested files, when approved:

```text
docs/
  _config.yml
  index.md
  experimentos.md
  metodo.md
  rendernum.md
  papers.md
```

Suggested `_config.yml`:

```yaml
title: Render Universe
description: Conteo causal, links y aritmetica de resolucion finita.
theme: minima
lang: es
```

GitHub switch, done by the author:

1. Repository settings.
2. Pages.
3. Source: `Deploy from a branch`.
4. Branch: `master`, folder: `/docs`.
5. Save.

## Alternative

Use a separate `rendering-universe-pages` repo only if the author wants the public site to evolve independently from the research repo. I do not recommend this for now: one repo is easier to audit.

