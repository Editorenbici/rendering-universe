"""
Video: π=4 — la paradoja de la escalera (versión cinemática)
Sin narración. Música de fondo. La imagen cuenta sola.
Misma paleta. Más lento. Más drama.
"""

from manim import *
import numpy as np

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"

class EscaleraCinematic(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        # === APERTURA: Círculo perfecto ===
        titulo = Text("π = 3.14159...", font_size=48, color=GRIS, font="JetBrains Mono")
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        circle = Circle(radius=3, color=CURSOR, stroke_width=3)
        self.play(Create(circle, run_time=2))
        self.wait(1)

        # === PROBLEMA: Medir con píxeles ===
        self.play(circle.animate.set_opacity(0.15), run_time=1)
        pixeles = VGroup()
        for x, y in [(-2,3),(-1,3),(0,3),(1,3),(2,3),
                     (-3,2),(3,2),(-3,1),(3,1),(-3,0),(3,0),
                     (-3,-1),(3,-1),(-3,-2),(3,-2),
                     (-2,-3),(-1,-3),(0,-3),(1,-3),(2,-3)]:
            sq = Square(0.85, color=CURSOR, fill_opacity=0.55, fill_color=CURSOR)
            sq.move_to([x, y, 0])
            pixeles.add(sq)

        self.play(FadeIn(pixeles, scale=0.01, run_time=2))
        self.wait(1)

        # El círculo pixelado late
        self.play(pixeles.animate.set_opacity(0.8), run_time=1)
        self.wait(0.5)

        # Revelación: π=4
        pi_cuatro = MathTex(r"\pi = 4", font_size=72, color="#E53935")
        pi_cuatro.next_to(titulo, DOWN, buff=0.5)
        self.play(Write(pi_cuatro, run_time=1.5))
        self.wait(1.5)

        # === TRANSICIÓN: Más resolución no arregla nada ===
        self.play(FadeOut(pixeles, run_time=0.5), FadeOut(pi_cuatro, run_time=0.3))
        self.play(FadeOut(circle, run_time=0.3))

        # Grid más fino
        grid_fino = VGroup()
        for ang in np.linspace(0, 2*np.pi, 60, endpoint=False):
            x = 3 * np.cos(ang)
            y = 3 * np.sin(ang)
            sq = Square(0.18, color=GRIS, fill_opacity=0.4, fill_color=GRIS)
            sq.move_to([x, y, 0])
            grid_fino.add(sq)

        self.play(FadeIn(grid_fino, scale=0.5, run_time=2))
        self.wait(0.5)

        sigue_siendo_cuatro = MathTex(r"\text{sigue siendo } 4", font_size=48, color=GRIS)
        sigue_siendo_cuatro.next_to(titulo, DOWN, buff=0.5)
        self.play(Write(sigue_siendo_cuatro, run_time=1.5))
        self.wait(1)
        self.play(FadeOut(sigue_siendo_cuatro, run_time=0.3), FadeOut(grid_fino, run_time=0.5))

        # === SOLUCIÓN: Medir con estructura ===
        # Mostrar círculo con overlaps (los píxeles se conectan por diagonales también)
        solucion = Text(
            "El problema no es la resolución.\nEs cómo medís.",
            font_size=36, color=BLANCO, font="JetBrains Mono",
            line_spacing=1.3,
        )
        solucion.to_edge(UP, buff=0.5)
        self.play(Write(solucion), run_time=2)
        self.wait(1)

        # Círculo con estructura: overlaps visibles
        circle_final = Circle(radius=3, color=CURSOR, stroke_width=3)
        overlap_dots = VGroup()
        for ang in np.linspace(0, 2*np.pi, 80, endpoint=False):
            x = 3 * np.cos(ang)
            y = 3 * np.sin(ang)
            d = Dot([x, y, 0], radius=0.05, color=CURSOR, fill_opacity=0.8)
            overlap_dots.add(d)

        self.play(
            FadeIn(circle_final, run_time=1),
            LaggedStart(*[GrowFromCenter(d) for d in overlap_dots], lag_ratio=0.005),
            run_time=3,
        )
        self.wait(1)

        # π emerge
        pi_emerge = MathTex(r"\pi \to 3.14...", font_size=72, color=CURSOR)
        pi_emerge.next_to(solucion, DOWN, buff=0.5)
        self.play(Write(pi_emerge, run_time=2))
        self.wait(2)

        # === CIERRE ===
        self.play(FadeOut(pi_emerge, run_time=0.5), FadeOut(circle_final, run_time=0.5),
                  FadeOut(overlap_dots, run_time=0.5), FadeOut(solucion, run_time=0.3))
        self.wait(0.3)

        cierre = Text(
            "La distancia espacial en causal sets\nse mide con overlaps.\nNo con adyacencia.",
            font_size=28, color=GRIS, font="JetBrains Mono", line_spacing=1.3,
        )
        self.play(Write(cierre, run_time=2))
        self.wait(3)
