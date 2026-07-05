"""
Video C — "El girasol" — versión vertical 9:16 (1080×1920)
"""

from manim import *
import numpy as np

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"
VIOLETA = "#A78BFA"
GOLDEN_ANGLE = 137.508

class GirasolVertical(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        intro = Text("Un solo número:", font_size=28, color=GRIS, font="JetBrains Mono")
        intro.to_edge(UP, buff=0.3)
        self.play(Write(intro), run_time=1)
        golden = MathTex(r"137.5^\circ", font_size=52, color=CURSOR)
        golden.next_to(intro, DOWN, buff=0.2)
        self.play(Write(golden), run_time=1)
        self.wait(0.3)

        seeds = VGroup()
        for i in range(1, 151):
            theta = np.radians(i * GOLDEN_ANGLE)
            r = 2.8 * np.sqrt(i / 150)
            seeds.add(Dot([r*np.cos(theta), r*np.sin(theta), 0], radius=0.035, color=CURSOR, fill_opacity=0.7))
        self.play(LaggedStart(*[GrowFromCenter(s) for s in seeds], lag_ratio=0.015), run_time=4)
        self.wait(0.5)

        vlabel = Text("Vector: 137.5°", font_size=20, color=CURSOR, font="JetBrains Mono")
        vlabel.to_edge(DOWN, buff=0.6)
        vlabel.shift(LEFT)
        rlabel = Text("Raster: ~150 eventos", font_size=20, color=GRIS, font="JetBrains Mono")
        rlabel.next_to(vlabel, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(vlabel), Write(rlabel), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(seeds, run_time=0.3), FadeOut(vlabel, run_time=0.3), FadeOut(rlabel, run_time=0.3))

        dots_cs = VGroup()
        for i in range(100):
            theta = np.radians(i * GOLDEN_ANGLE * 0.5)
            r = 2.5 * np.sqrt(i / 100)
            dots_cs.add(Dot([r*np.cos(theta), r*np.sin(theta), 0], radius=0.03, color=VIOLETA, fill_opacity=0.6))
        cs_title = Text("Vector → Raster", font_size=28, color=BLANCO, font="JetBrains Mono")
        cs_title.to_corner(UR, buff=0.3)
        self.play(Write(cs_title), run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots_cs], lag_ratio=0.02), run_time=3)
        self.wait(0.5)
        analogia = Text("u_μ → ℛ(t) → ⊞", font_size=22, color=GRIS, font="JetBrains Mono")
        analogia.to_edge(DOWN, buff=0.3)
        self.play(Write(analogia), run_time=1.5)
        self.wait(2)
