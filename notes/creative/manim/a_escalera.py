"""
Video A — "La escalera" (π=4 en píxeles) — versión simplificada
Manim 0.20.x. Render ligero (<60s).
"""

from manim import *

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"

class Escalera(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        # --- Círculo suave ---
        circle = Circle(radius=3, color=CURSOR, stroke_width=3)
        self.play(Create(circle), run_time=1)
        self.wait(0.3)

        # Mostrar π ≈ 3.14
        pi_real = MathTex(r"\pi \approx 3.14", font_size=64, color=CURSOR)
        pi_real.to_corner(UR, buff=0.5)
        self.play(Write(pi_real), run_time=0.8)
        self.wait(0.5)

        # --- Pixelación gruesa ---
        # Reemplazar círculo por aproximación pixelada 8x8
        self.play(circle.animate.set_opacity(0.2), run_time=0.5)
        coarse = VGroup()
        for x, y in [(-2,3),(-1,3),(0,3),(1,3),(2,3),
                     (-3,2),(3,2),(-3,1),(3,1),(-3,0),(3,0),
                     (-3,-1),(3,-1),(-3,-2),(3,-2),
                     (-2,-3),(-1,-3),(0,-3),(1,-3),(2,-3)]:
            sq = Square(0.8, color=CURSOR, fill_opacity=0.6, fill_color=CURSOR)
            sq.move_to([x, y, 0])
            coarse.add(sq)
        self.play(FadeIn(coarse, scale=0.5, run_time=1))
        self.wait(0.3)

        # π = 4?
        pi_four = MathTex(r"\pi = 4\;?", font_size=64, color=GRIS)
        pi_four.next_to(pi_real, DOWN, buff=0.3)
        self.play(Write(pi_four), run_time=0.8)
        self.wait(1)

        # --- Pixelación fina ---
        self.play(FadeOut(coarse, run_time=0.3), FadeOut(pi_four, run_time=0.3))
        fine = VGroup()
        r = 3.0
        for ang in np.linspace(0, 2*np.pi, 40, endpoint=False):
            x = r * np.cos(ang)
            y = r * np.sin(ang)
            sq = Square(0.25, color=CURSOR, fill_opacity=0.5, fill_color=CURSOR)
            sq.move_to([x, y, 0])
            fine.add(sq)
        self.play(FadeIn(fine, scale=0.8, run_time=1.5))
        self.wait(0.5)

        # π emerge
        pi_emerge = MathTex(r"\pi \to 3.14...", font_size=64, color=CURSOR)
        pi_emerge.next_to(pi_real, DOWN, buff=0.3)
        self.play(Write(pi_emerge), run_time=0.8)
        self.wait(1)

        # --- Explicación ---
        expl = Text(
            "Medir por adyacencia → π = 4\nMedir con estructura → π emerge",
            font_size=26, color=BLANCO, font="JetBrains Mono",
        )
        expl.to_edge(DOWN, buff=0.5)
        self.play(Write(expl), run_time=1.5)
        self.wait(1)

        cierre = Text(
            "Distancia espacial en causal sets:\noverlaps, no adyacencia",
            font_size=22, color=GRIS, font="JetBrains Mono",
        )
        cierre.next_to(expl, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(cierre), run_time=1.5)
        self.wait(2)
