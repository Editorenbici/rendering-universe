"""
Video C — "El girasol" (apertura vector/raster)
Manim 0.20.x. Golden angle → phyllotaxis → causal set analogy.
20-30 s. Paleta identidad visual.
"""

from manim import *
import numpy as np

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"
VIOLETA = "#A78BFA"

GOLDEN_ANGLE = 137.508  # degrees

class Girasol(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        # --- Texto inicial: "Un solo vector" ---
        intro = Text("¿Cuánta información\nnecesita un girasol?", font_size=36,
                     color=BLANCO, font="JetBrains Mono", line_spacing=1.3)
        intro.to_edge(UP, buff=0.5)
        self.play(Write(intro), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(intro, run_time=0.5))

        # --- Vector: ángulo áureo ---
        angle_text = Text("Un solo número:", font_size=28, color=GRIS,
                          font="JetBrains Mono")
        angle_text.to_corner(UL, buff=0.5)
        self.play(Write(angle_text), run_time=1)

        golden = MathTex(r"137.5^\circ", font_size=64, color=CURSOR)
        golden.next_to(angle_text, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(golden), run_time=1)
        self.wait(0.5)

        # --- La flor crece (phyllotaxis) ---
        seeds = VGroup()
        n_seeds = 200
        r_max = 3.5
        for i in range(1, n_seeds + 1):
            theta = np.radians(i * GOLDEN_ANGLE)
            r = r_max * np.sqrt(i / n_seeds)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            seed = Dot([x, y, 0], radius=0.04, color=CURSOR, fill_opacity=0.7)
            seeds.add(seed)

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in seeds],
                        lag_ratio=0.01),
            run_time=5,
        )
        self.wait(1)

        # --- El vector ---
        vector_label = Text("Vector: ángulo áureo 137.5°",
                            font_size=22, color=CURSOR, font="JetBrains Mono")
        vector_label.to_edge(DOWN, buff=0.6)
        vector_label.shift(LEFT * 3)
        self.play(Write(vector_label), run_time=1)

        raster_label = Text("Raster: ~200 semillas (eventos)",
                            font_size=22, color=GRIS, font="JetBrains Mono")
        raster_label.next_to(vector_label, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(raster_label), run_time=1)
        self.wait(1.5)

        # --- Transición: girasol → causal set ---
        self.play(FadeOut(seeds, run_time=0.5), FadeOut(golden, run_time=0.3),
                  FadeOut(vector_label, run_time=0.3), FadeOut(raster_label, run_time=0.3))

        # --- Causal set análogo ---
        dots_cs = VGroup()
        for i in range(120):
            theta = np.radians(i * GOLDEN_ANGLE * 0.5)  # tighter spiral
            r = 3.0 * np.sqrt(i / 120)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            d = Dot([x, y, 0], radius=0.04, color=VIOLETA, fill_opacity=0.6)
            dots_cs.add(d)

        cs_title = Text("Misma estructura:\nun vector, un raster",
                        font_size=28, color=BLANCO, font="JetBrains Mono",
                        line_spacing=1.3)
        cs_title.to_corner(UR, buff=0.4)
        self.play(Write(cs_title), run_time=1.5)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots_cs],
                        lag_ratio=0.015),
            run_time=4,
        )
        self.wait(0.5)

        # --- Cierre ---
        cierre = Text(
            "La planta guarda UN número (vector)\ny renderiza cada semilla (raster)",
            font_size=24, color=GRIS, font="JetBrains Mono", line_spacing=1.3,
        )
        cierre.to_edge(DOWN, buff=0.6)
        self.play(Write(cierre), run_time=2)
        self.wait(2)
