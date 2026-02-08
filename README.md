# The Rendering Universe: Resolution Cosmology

This repository contains the source code for the paper **"The Rendering Universe: Causal Refinement as Holographic Cosmology"**.

## Abstract
We propose **Resolution Cosmology**, a framework where cosmic expansion is reinterpreted not as spatial stretching, but as the dynamical increase of causal resolution $\mathcal{R}(t)$. This model resolves the vacuum catastrophe and explains the horizon problem through a "Cosmic Rendering" mechanism.

## Repository Structure

- `main.tex`: The main LaTeX source file.
- `figures/`: Contains the figures used in the paper.
    - Note: For arXiv submission, ensure `.pdf` versions of the figures are present in this folder.
- `README.md`: This file.

## Compilation

### Prerequisites
- LaTeX distribution (TeX Live, MikTeX, etc.)
- `pdflatex` or `latexmk`.

### Building
To generate the PDF:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## arXiv Submission
1.  Ensure all figures in `figures/` are in `.pdf` format.
2.  Include the `.bbl` file (generated after BibTeX compilation) in the root directory.
3.  Upload `main.tex`, `figures/*.pdf`, and `main.bbl`.

## License
[License Name] - Patricio Fernando Bustos Cabrera
