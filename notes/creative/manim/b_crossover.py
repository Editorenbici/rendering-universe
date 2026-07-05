"""
Video B — "El crossover" (Exp 25: p_h(b) cruzando cero)
Manim 0.20.x, 1920x1080 + 9:16 crop-ready.
Paleta: identity visual 01.
Datos reales: outputs/exp25_formal_results.json, serie n1024_a0.20.
Etiqueta obligatoria: "toy 1+1D — HIPÓTESIS (Exp 25b pendiente)"
"""

from manim import *

CANVAS = "#0F0F12"
CURSOR = "#00FFC8"
GRIS = "#6B7280"
BLANCO = "#F8F9FA"
AMBER = "#F59E0B"

# Datos reales: n1024_a0.20
B_VALS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
PH_MEAN = [0.4680, 0.3625, 0.0882, 0.1349, 0.1080, 0.0963, -0.0086, -0.1361, -0.1145]
PH_ERR  = [0.0739, 0.0645, 0.0896, 0.0647, 0.0889, 0.0714, 0.0793, 0.0788, 0.0787]

class Crossover(Scene):
    def construct(self):
        self.camera.background_color = CANVAS

        # --- Ejes ---
        axes = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.4, 0.7, 0.2],
            x_length=12,
            y_length=6,
            axis_config={"color": GRIS, "stroke_width": 1},
            x_axis_config={"label_direction": DOWN, "numbers_to_include": [0, 1, 2, 3, 4]},
            y_axis_config={"label_direction": LEFT, "numbers_to_include": [-0.4, -0.2, 0, 0.2, 0.4, 0.6]},
        )
        labels = VGroup(
            MathTex(r"b", font_size=28, color=GRIS).next_to(axes.x_axis, DOWN, buff=0.4),
            MathTex(r"p_h", font_size=28, color=GRIS).next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI/2),
        )

        self.play(Create(axes), run_time=1.5), self.play(Write(labels), run_time=0.5)

        # --- Línea cero ---
        zero_line = DashedLine(
            axes.c2p(0, 0), axes.c2p(4.2, 0),
            color=AMBER, stroke_width=1, dash_length=0.08,
        )
        zero_label = MathTex(r"p_h = 0", font_size=22, color=AMBER).next_to(zero_line, RIGHT, buff=0.2)
        self.play(Create(zero_line), Write(zero_label), run_time=0.8)
        self.wait(0.3)

        # --- Puntos con barras de error ---
        dots = VGroup()
        error_bars = VGroup()
        for b, mean, err in zip(B_VALS, PH_MEAN, PH_ERR):
            pt = axes.c2p(b, mean)
            dot = Dot(pt, color=CURSOR, radius=0.08)
            bar = Line(
                axes.c2p(b, mean - err),
                axes.c2p(b, mean + err),
                color=CURSOR, stroke_width=2,
            )
            dots.add(dot)
            error_bars.add(bar)

        self.play(
            LaggedStart(
                *[GrowFromCenter(d) for d in dots],
                *[Create(b) for b in error_bars],
                lag_ratio=0.15,
            ),
            run_time=3,
        )
        self.wait(1)

        # --- Flecha cruzando cero ---
        cross_b = None
        for i in range(len(PH_MEAN) - 1):
            if PH_MEAN[i] > 0 and PH_MEAN[i+1] < 0:
                cross_b = np.interp(0, [PH_MEAN[i], PH_MEAN[i+1]], [B_VALS[i], B_VALS[i+1]])
                break
        if cross_b:
            cross_pt = axes.c2p(cross_b, 0)
            arrow = Arrow(
                axes.c2p(cross_b - 0.3, 0.15), cross_pt,
                color=CURSOR, stroke_width=3, buff=0.05,
            )
            cross_label = MathTex(f"cruce\\;b\\;\\approx{cross_b:.1f}", font_size=28, color=CURSOR)
            cross_label.next_to(arrow, UP, buff=0.2)
            self.play(GrowArrow(arrow), Write(cross_label), run_time=1.5)
            self.wait(1)

        # --- Título: "el sesgo convierte tiempo en espacio" ---
        title = Text(
            "el sesgo convierte\ntiempo en espacio",
            font_size=42, color=BLANCO, font="JetBrains Mono",
            line_spacing=1.2,
        )
        title.to_corner(UL, buff=0.5)
        self.play(Write(title), run_time=1.5)
        self.wait(1)

        # --- Etiqueta obligatoria ---
        etiq = Text(
            "toy 1+1D — HIPÓTESIS (Exp 25b pendiente)",
            font_size=20, color=AMBER, font="JetBrains Mono",
        )
        etiq.to_corner(DR, buff=0.4)
        self.play(Write(etiq), run_time=1)
        self.wait(2)

        # --- Punto final: dato de cierre ---
        cierre = Text(
            "p_h(0) = +0.47 ± 0.07\np_h(4) = −0.11 ± 0.08",
            font_size=26, color=GRIS, font="JetBrains Mono",
            line_spacing=1.5,
        )
        cierre.next_to(etiq, UP, buff=0.5, aligned_edge=RIGHT)
        self.play(Write(cierre), run_time=1.5)
        self.wait(3)
