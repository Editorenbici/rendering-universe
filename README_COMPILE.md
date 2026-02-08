# How to Compile "The Rendering Universe"

To generate the high-quality PDF with the diagrams, you need a LaTeX distribution and Inkscape (for the SVG images).

## Option 1: Overleaf (Recommended for ease)
1. Go to [Overleaf.com](https://www.overleaf.com/).
2. Create a details "New Project" -> "Upload Project".
3. Upload the entire `Final_Paper` folder (zip it first if needed).
4. **Important**: Ensure your compiler is set to `pdfLaTeX` (usually default).
5. Overleaf includes `inkscape` automatically, so it should just work!

## Option 2: Local Compilation (Windows)
1. **Install LaTeX**: Download and install [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/).
2. **Install Inkscape**: Download [Inkscape](https://inkscape.org/) and add it to your System PATH.
3. **Run Compilation**:
   Open a terminal in this folder and run:
   ```cmd
   pdflatex -shell-escape main.tex
   ```
   *Note: `-shell-escape` is required for the `svg` package to convert images.*

## Troubleshooting
- If images don't appear, ensure `inkscape` is in your PATH.
- If you get "Package svg Error", check the log file.
