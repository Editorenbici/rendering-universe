"""
Video E — "Render" — versión vertical 9:16
"""

from manim import *
import numpy as np

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
VIOLETA = "#A78BFA"
GOLDEN = 137.508

class RenderDelUniversoVertical(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        pixel = Square(0.1, color=CURSOR, fill_opacity=1, fill_color=CURSOR)
        self.play(FadeIn(pixel, scale=0.01, run_time=1.5))
        self.wait(0.5)
        self.play(pixel.animate.scale(2), run_time=1.5)
        self.wait(0.3)
        self.play(FadeOut(pixel, run_time=0.3))

        for k in [2, 4]:
            grid = VGroup()
            s = 1.0 / k
            for i in range(k):
                for j in range(k):
                    sq = Square(s * 0.6, color=CURSOR, fill_opacity=0.6, fill_color=CURSOR)
                    sq.move_to([(i-k/2+0.5)*s*4, (j-k/2+0.5)*s*4, 0])
                    grid.add(sq)
            self.play(FadeIn(grid, scale=0.5, run_time=1.2))
            self.wait(0.3)
            self.play(FadeOut(grid, run_time=0.3))

        n = 150
        dots = VGroup(*[Dot([np.random.default_rng(i).uniform(-3.5,3.5), np.random.default_rng(i+1000).uniform(-3.5,3.5), 0], radius=0.025, color=CURSOR, fill_opacity=0.5) for i in range(n)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.015), run_time=2.5)
        self.wait(0.5)

        target = []
        for i in range(1, n+1):
            t = np.radians(i * GOLDEN)
            r = 3.0 * np.sqrt(i / n)
            target.append([r*np.cos(t), r*np.sin(t), 0])
        for b in range(0, n, 10):
            e = min(b+10, n)
            self.play(*[dots[j].animate.move_to(target[j]).set_color(VIOLETA).set_opacity(0.7) for j in range(b, e)], run_time=0.4)
        self.wait(0.5)

        self.play(*[dots[j].animate.set_color(CURSOR).set_opacity(0.9) for j in range(min(20, n))], run_time=0.8)
        cierre = MathTex(r"137.5^\circ", font_size=52, color=CURSOR).to_corner(DR, buff=0.3)
        self.play(Write(cierre), run_time=1)
        cierre2 = Text("vector → raster", font_size=24, color=GRIS, font="JetBrains Mono").next_to(cierre, UP, buff=0.2, aligned_edge=RIGHT)
        self.play(Write(cierre2), run_time=1)
        self.wait(2)
