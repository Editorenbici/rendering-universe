"""
Video E — "Render" (Big Bang → Girasol)
30-45 s. Sin texto, sin ecuaciones. Solo evolución visual.
Transiciones suaves con fade, no morphing entre grupos de distinto tamaño.
"""

from manim import *
import numpy as np

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
VIOLETA = "#A78BFA"
GOLDEN = 137.508

class RenderDelUniverso(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        # === FASE 1: Un solo píxel ===
        pixel = Square(0.15, color=CURSOR, fill_opacity=1, fill_color=CURSOR)
        self.play(FadeIn(pixel, scale=0.01, run_time=2))
        self.wait(1)
        self.play(pixel.animate.scale(2), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(pixel, run_time=0.5))

        # === FASE 2: Subdivisión (2×2 → 4×4) ===
        for k in [2, 4]:
            grid = VGroup()
            s = 1.0 / k
            for i in range(k):
                for j in range(k):
                    sq = Square(s * 0.7, color=CURSOR, fill_opacity=0.6, fill_color=CURSOR)
                    x = (i - k/2 + 0.5) * s * 5
                    y = (j - k/2 + 0.5) * s * 5
                    sq.move_to([x, y, 0])
                    grid.add(sq)
            self.play(FadeIn(grid, scale=0.5, run_time=1.5))
            self.wait(0.5)
            self.play(FadeOut(grid, run_time=0.3))

        # === FASE 3: Sprinkling ===
        n = 200
        dots = VGroup(*[
            Dot(
                [np.random.default_rng(i).uniform(-4.5, 4.5),
                 np.random.default_rng(i+1000).uniform(-4.5, 4.5), 0],
                radius=0.03, color=CURSOR, fill_opacity=0.5
            ) for i in range(n)
        ])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.01), run_time=3)
        self.wait(1)

        # === FASE 4: Los puntos migran al girasol ===
        target = []
        for i in range(1, n+1):
            theta = np.radians(i * GOLDEN)
            r = 3.8 * np.sqrt(i / n)
            target.append([r * np.cos(theta), r * np.sin(theta), 0])
        # Animar en lotes de 10 para no saturar
        for batch_start in range(0, n, 10):
            batch_end = min(batch_start + 10, n)
            self.play(
                *[dots[j].animate.move_to(target[j]).set_color(VIOLETA).set_opacity(0.7)
                  for j in range(batch_start, batch_end)],
                run_time=0.5,
            )
        self.wait(1)

        # === FASE 5: Iluminación final ===
        self.play(
            *[dots[j].animate.set_color(CURSOR).set_opacity(0.9)
              for j in range(0, min(30, n))],
            run_time=1,
        )
        self.wait(0.5)

        # Texto final
        cierre = MathTex(r"137.5^\circ", font_size=64, color=CURSOR)
        cierre.to_corner(DR, buff=0.5)
        self.play(Write(cierre), run_time=1.5)
        self.wait(1)
        cierre2 = Text("un vector  →  un raster", font_size=28, color=GRIS, font="JetBrains Mono")
        cierre2.next_to(cierre, UP, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(cierre2), run_time=1.5)
        self.wait(3)
