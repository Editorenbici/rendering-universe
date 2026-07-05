#!/usr/bin/env python3
"""
Generate Exp 24 background figures F1-F3 from existing JSON outputs.

No matplotlib dependency is required. Figures are written as SVG so the script
can run in a minimal/headless Python environment.
"""

from __future__ import annotations

import argparse
import html
import json
import math
from pathlib import Path
from typing import Callable, Iterable

import numpy as np


COLORS = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e"]


def expected_links_2d(rho: float, R: float, n_quad: int = 8192) -> float:
    u = (np.arange(n_quad, dtype=float) + 0.5) * (2.0 * R / n_quad)
    expo = -0.5 * rho * u * (2.0 * R - u)
    integrand = (1.0 - np.exp(expo)) / u
    return float(np.sum(integrand) * (2.0 * R / n_quad))


def expected_links_4d(rho: float, R: float) -> float:
    return float(np.pi * np.sqrt(6.0) * np.sqrt(rho) * R * R)


def load_rows(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["rows"]


def grouped_by_rho(rows: list[dict]) -> dict[float, list[dict]]:
    groups: dict[float, list[dict]] = {}
    for row in rows:
        groups.setdefault(float(row["rho"]), []).append(row)
    return {rho: sorted(sub, key=lambda r: r["R"]) for rho, sub in sorted(groups.items())}


class SvgPlot:
    def __init__(
        self,
        path: Path,
        title: str,
        xlabel: str,
        ylabel: str,
        *,
        width: int = 760,
        height: int = 540,
    ):
        self.path = path
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.width = width
        self.height = height
        self.left = 92
        self.right = 28
        self.top = 58
        self.bottom = 78
        self.parts: list[str] = []

    @property
    def x0(self):
        return self.left

    @property
    def x1(self):
        return self.width - self.right

    @property
    def y0(self):
        return self.height - self.bottom

    @property
    def y1(self):
        return self.top

    def map_x(self, x: float, xmin: float, xmax: float) -> float:
        return self.x0 + (x - xmin) / (xmax - xmin) * (self.x1 - self.x0)

    def map_y(self, y: float, ymin: float, ymax: float) -> float:
        return self.y0 - (y - ymin) / (ymax - ymin) * (self.y0 - self.y1)

    def add_axes(self, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
        self.parts.append(
            f'<rect x="{self.x0}" y="{self.y1}" width="{self.x1-self.x0}" '
            f'height="{self.y0-self.y1}" fill="white" stroke="#222" stroke-width="1"/>'
        )
        for i in range(6):
            tx = xmin + i * (xmax - xmin) / 5
            ty = ymin + i * (ymax - ymin) / 5
            px = self.map_x(tx, xmin, xmax)
            py = self.map_y(ty, ymin, ymax)
            self.parts.append(f'<line x1="{px:.2f}" y1="{self.y1}" x2="{px:.2f}" y2="{self.y0}" stroke="#ddd"/>')
            self.parts.append(f'<line x1="{self.x0}" y1="{py:.2f}" x2="{self.x1}" y2="{py:.2f}" stroke="#ddd"/>')
            self.parts.append(f'<text x="{px:.2f}" y="{self.y0+22}" text-anchor="middle" font-size="12">{tx:.2g}</text>')
            self.parts.append(f'<text x="{self.x0-10}" y="{py+4:.2f}" text-anchor="end" font-size="12">{ty:.2g}</text>')
        self.parts.append(f'<text x="{self.width/2}" y="28" text-anchor="middle" font-size="20" font-weight="600">{html.escape(self.title)}</text>')
        self.parts.append(f'<text x="{self.width/2}" y="{self.height-24}" text-anchor="middle" font-size="15">{html.escape(self.xlabel)}</text>')
        self.parts.append(
            f'<text x="24" y="{self.height/2}" text-anchor="middle" font-size="15" '
            f'transform="rotate(-90 24 {self.height/2})">{html.escape(self.ylabel)}</text>'
        )

    def add_line(self, points: list[tuple[float, float]], xmin, xmax, ymin, ymax, color="#222", dashed=False) -> None:
        pts = " ".join(f"{self.map_x(x,xmin,xmax):.2f},{self.map_y(y,ymin,ymax):.2f}" for x, y in points)
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        self.parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"{dash}/>')

    def add_point(self, x, y, xmin, xmax, ymin, ymax, color, label=None) -> None:
        px = self.map_x(x, xmin, xmax)
        py = self.map_y(y, ymin, ymax)
        self.parts.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="5" fill="{color}" stroke="white" stroke-width="1"/>')
        if label:
            self.parts.append(f'<title>{html.escape(label)}</title>')

    def add_errorbar(self, x, y, yerr, xmin, xmax, ymin, ymax, color) -> None:
        px = self.map_x(x, xmin, xmax)
        py1 = self.map_y(y - yerr, ymin, ymax)
        py2 = self.map_y(y + yerr, ymin, ymax)
        self.parts.append(f'<line x1="{px:.2f}" y1="{py1:.2f}" x2="{px:.2f}" y2="{py2:.2f}" stroke="{color}" stroke-width="1.3"/>')
        self.parts.append(f'<line x1="{px-5:.2f}" y1="{py1:.2f}" x2="{px+5:.2f}" y2="{py1:.2f}" stroke="{color}" stroke-width="1.3"/>')
        self.parts.append(f'<line x1="{px-5:.2f}" y1="{py2:.2f}" x2="{px+5:.2f}" y2="{py2:.2f}" stroke="{color}" stroke-width="1.3"/>')

    def add_legend(self, labels: list[tuple[str, str]]) -> None:
        x = self.x1 - 128
        y = self.y1 + 24
        for i, (label, color) in enumerate(labels):
            yy = y + i * 22
            self.parts.append(f'<circle cx="{x}" cy="{yy}" r="5" fill="{color}"/>')
            self.parts.append(f'<text x="{x+12}" y="{yy+4}" font-size="13">{html.escape(label)}</text>')

    def write(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">',
            '<rect width="100%" height="100%" fill="#fafafa"/>',
            *self.parts,
            "</svg>",
        ]
        self.path.write_text("\n".join(svg) + "\n", encoding="utf-8")


def minmax(vals: Iterable[float], pad: float = 0.08) -> tuple[float, float]:
    vals = list(vals)
    lo, hi = min(vals), max(vals)
    span = hi - lo or abs(hi) or 1.0
    return lo - pad * span, hi + pad * span


def log10(x: float) -> float:
    return math.log10(x)


def figure_f1(rows: list[dict], out_dir: Path) -> Path:
    rows4 = [r for r in rows if int(r["dim"]) == 4]
    xs = [expected_links_4d(r["rho"], r["R"]) for r in rows4]
    ys = [r["links_mean"] for r in rows4]
    xmin, xmax = minmax(xs + ys)
    ymin, ymax = xmin, xmax
    path = out_dir / "F1_exp24_4d_area_law.svg"
    plot = SvgPlot(path, "F1. 4D link abundance vs area law", "pi sqrt(6) sqrt(rho) R^2", "measured v_link")
    plot.add_axes(xmin, xmax, ymin, ymax)
    plot.add_line([(xmin, ymin), (xmax, ymax)], xmin, xmax, ymin, ymax, color="#111", dashed=True)
    labels = []
    for i, rho in enumerate(sorted({float(r["rho"]) for r in rows4})):
        color = COLORS[i % len(COLORS)]
        labels.append((f"rho={rho:g}", color))
        for r in rows4:
            if float(r["rho"]) == rho:
                x = expected_links_4d(r["rho"], r["R"])
                plot.add_errorbar(x, r["links_mean"], r["links_sem"], xmin, xmax, ymin, ymax, color)
                plot.add_point(x, r["links_mean"], xmin, xmax, ymin, ymax, color)
    plot.add_legend(labels)
    plot.write()
    return path


def figure_f2(rows: list[dict], out_dir: Path) -> Path:
    rows4 = [r for r in rows if int(r["dim"]) == 4]
    xs = [log10(r["R"]) for r in rows4]
    ys = [log10(r["epsilon_mean"]) for r in rows4]
    xmin, xmax = minmax(xs)
    ymin, ymax = minmax(ys)
    path = out_dir / "F2_exp24_4d_epsilon_scaling.svg"
    plot = SvgPlot(path, "F2. 4D fractional link efficiency", "log10 R", "log10 epsilon_link")
    plot.add_axes(xmin, xmax, ymin, ymax)
    labels = []
    for i, (rho, sub) in enumerate(grouped_by_rho(rows4).items()):
        color = COLORS[i % len(COLORS)]
        labels.append((f"rho={rho:g}", color))
        pts = [(log10(r["R"]), log10(r["epsilon_mean"])) for r in sub]
        plot.add_line(pts, xmin, xmax, ymin, ymax, color=color)
        for r in sub:
            plot.add_point(log10(r["R"]), log10(r["epsilon_mean"]), xmin, xmax, ymin, ymax, color)
    plot.add_legend(labels)
    plot.write()
    return path


def figure_f3(rows: list[dict], out_dir: Path) -> Path:
    rows2 = [r for r in rows if int(r["dim"]) == 2]
    xs = [expected_links_2d(r["rho"], r["R"]) for r in rows2]
    ys = [r["links_mean"] for r in rows2]
    xmin, xmax = minmax(xs + ys)
    ymin, ymax = xmin, xmax
    path = out_dir / "F3_exp24_2d_link_law.svg"
    plot = SvgPlot(path, "F3. 2D link abundance vs finite-cone law", "finite-cone 2D expectation", "measured v_link")
    plot.add_axes(xmin, xmax, ymin, ymax)
    plot.add_line([(xmin, ymin), (xmax, ymax)], xmin, xmax, ymin, ymax, color="#111", dashed=True)
    labels = []
    for i, rho in enumerate(sorted({float(r["rho"]) for r in rows2})):
        color = COLORS[i % len(COLORS)]
        labels.append((f"rho={rho:g}", color))
        for r in rows2:
            if float(r["rho"]) == rho:
                x = expected_links_2d(r["rho"], r["R"])
                plot.add_errorbar(x, r["links_mean"], r["links_sem"], xmin, xmax, ymin, ymax, color)
                plot.add_point(x, r["links_mean"], xmin, xmax, ymin, ymax, color)
    plot.add_legend(labels)
    plot.write()
    return path


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("outputs/exp24_epsilon_link_scaling.json"))
    parser.add_argument("--out-dir", type=Path, default=Path("outputs/figures/exp24"))
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    rows = load_rows(args.input)
    paths = [figure_f1(rows, args.out_dir), figure_f2(rows, args.out_dir), figure_f3(rows, args.out_dir)]
    print(json.dumps({"status": "OK", "figures": [str(p) for p in paths]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
