"""
Video A — "La escalera" — versión vertical 9:16 (1080×1920)
"""

from manim import *

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"

class EscaleraVertical(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        circle = Circle(radius=2, color=CURSOR, stroke_width=3)
        self.play(Create(circle), run_time=1)
        self.wait(0.3)
        pi_real = MathTex(r"\pi \approx 3.14", font_size=52, color=CURSOR)
        pi_real.to_edge(UP, buff=0.3)
        self.play(Write(pi_real), run_time=0.8)
        self.wait(0.3)

        # Pixelación gruesa
        self.play(circle.animate.set_opacity(0.2), run_time=0.3)
        coarse = VGroup()
        for x,y in [(-2,2),(-1,2),(0,2),(1,2),(2,2),(-2,1),(2,1),(-2,0),(2,0),(-2,-1),(2,-1),(-2,-2),(-1,-2),(0,-2),(1,-2),(2,-2)]:
            sq = Square(0.6, color=CURSOR, fill_opacity=0.6, fill_color=CURSOR)
            sq.move_to([x, y, 0])
            coarse.add(sq)
        self.play(FadeIn(coarse, run_time=1))
        self.wait(0.3)
        pi_four = MathTex(r"\pi = 4?", font_size=52, color=GRIS)
        pi_four.next_to(pi_real, DOWN, buff=0.3)
        self.play(Write(pi_four), run_time=0.8)
        self.wait(1)

        # Pixelación fina
        self.play(FadeOut(coarse, run_time=0.3), FadeOut(pi_four, run_time=0.3))
        fine = VGroup()
        for ang in np.linspace(0, 2*np.pi, 30, endpoint=False):
            sq = Square(0.2, color=CURSOR, fill_opacity=0.5, fill_color=CURSOR)
            sq.move_to([2.0*np.cos(ang), 2.0*np.sin(ang), 0])
            fine.add(sq)
        self.play(FadeIn(fine, run_time=1.5))
        pi_emerge = MathTex(r"\pi \to 3.14", font_size=52, color=CURSOR)
        pi_emerge.next_to(pi_real, DOWN, buff=0.3)
        self.play(Write(pi_emerge), run_time=0.8)
        self.wait(1)

        expl = Text("Medir con estructura:\noverlaps, no adyacencia", font_size=22, color=BLANCO, font="JetBrains Mono")
        expl.to_edge(DOWN, buff=0.3)
        self.play(Write(expl), run_time=1.5)
        self.wait(3)
