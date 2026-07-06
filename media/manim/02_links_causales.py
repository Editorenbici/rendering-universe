from manim import *
import random

class LinksCausales(Scene):
    def construct(self):
        self.camera.background_color = "#080808"
        self.camera.frame_width = 10
        self.camera.frame_height = 6

        # Sprinkling: puntos aleatorios en una nube
        random.seed(42)
        n = 50
        points = [
            np.array([random.uniform(-3.5, 3.5), random.uniform(-2, 2), 0])
            for _ in range(n)
        ]
        dots = VGroup(*[Dot(p, color=WHITE, radius=0.035) for p in points])

        # Conexiones: pares aleatorios, mayoría gris tenue
        pale_lines = VGroup()
        true_lines = VGroup()
        true_pairs = set()
        # Elegimos 12 links "verdaderos"
        true_set = {tuple(sorted((random.randint(0, n-1), random.randint(0, n-1))))
                    for _ in range(20)}
        true_set = [pair for pair in true_set if pair[0] != pair[1]][:12]

        for i in range(n):
            for j in range(i+1, n):
                if (i, j) in true_set or (j, i) in true_set:
                    continue
                if random.random() < 0.06:  # pocos pares
                    pale_lines.add(Line(points[i], points[j],
                                        color="#444444",
                                        stroke_width=0.8))

        for i, j in true_set:
            true_lines.add(Line(points[i], points[j],
                                color="#00e5ff",
                                stroke_width=2.2))

        # Animación secuencial
        self.play(FadeIn(dots, lag_ratio=0.02), run_time=3)
        self.wait(0.2)
        self.play(FadeIn(pale_lines, lag_ratio=0.01), run_time=2.5)
        self.wait(0.3)
        self.play(FadeIn(true_lines, lag_ratio=0.02), run_time=2)
        self.wait(0.4)

        # Texto mínimo
        t1 = Text("No cuenta el pasado crudo.", font_size=30, color=WHITE)
        t2 = Text("Cuentan los links.", font_size=34, color="#00e5ff")
        t3 = Text("pre-registrado, medido, publicado", font_size=22, color="#888888")
        t1.to_edge(UP)
        t2.next_to(t1, DOWN)
        t3.to_edge(DOWN)

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(FadeIn(t3, shift=DOWN*0.3))
        self.wait(1.5)
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3),
                  FadeOut(true_lines), FadeOut(pale_lines), FadeOut(dots))
