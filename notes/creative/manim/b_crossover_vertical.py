"""
Video B — "El crossover" — versión vertical 9:16 (1080×1920)
"""

from manim import *

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"
AMBER = "#F59E0B"

B_VALS = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
PH_MEAN = [0.4680,0.3625,0.0882,0.1349,0.1080,0.0963,-0.0086,-0.1361,-0.1145]
PH_ERR  = [0.0739,0.0645,0.0896,0.0647,0.0889,0.0714,0.0793,0.0788,0.0787]

class CrossoverVertical(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        axes = Axes(
            x_range=[-0.5, 4.5, 1], y_range=[-0.4, 0.7, 0.2],
            x_length=8, y_length=5,
            axis_config={"color": GRIS, "stroke_width": 1},
        )
        self.play(Create(axes), run_time=1.5)
        zero_line = DashedLine(axes.c2p(0,0), axes.c2p(4.2,0), color=AMBER, stroke_width=1, dash_length=0.06)
        self.play(Create(zero_line), run_time=0.5)
        dots = VGroup(); bars = VGroup()
        for b, mn, er in zip(B_VALS, PH_MEAN, PH_ERR):
            pt = axes.c2p(b, mn)
            dots.add(Dot(pt, color=CURSOR, radius=0.06))
            bars.add(Line(axes.c2p(b, mn-er), axes.c2p(b, mn+er), color=CURSOR, stroke_width=2))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], *[Create(b) for b in bars], lag_ratio=0.15), run_time=2.5)
        self.wait(0.5)
        cross_b = None
        for i in range(len(PH_MEAN)-1):
            if PH_MEAN[i]>0 and PH_MEAN[i+1]<0:
                cross_b = np.interp(0, [PH_MEAN[i], PH_MEAN[i+1]], [B_VALS[i], B_VALS[i+1]])
                break
        if cross_b:
            arrow = Arrow(axes.c2p(cross_b-0.3, 0.1), axes.c2p(cross_b, 0), color=CURSOR, stroke_width=2, buff=0.02)
            self.play(GrowArrow(arrow), run_time=1)
        title = Text("sesgo → tiempo en espacio", font_size=36, color=BLANCO, font="JetBrains Mono")
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=1)
        etiq = Text("toy 1+1D — HIPÓTESIS", font_size=18, color=AMBER, font="JetBrains Mono")
        etiq.next_to(title, DOWN, buff=0.2)
        self.play(Write(etiq), run_time=1)
        self.wait(2)
