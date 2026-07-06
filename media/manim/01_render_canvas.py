from manim import *

class RenderCanvas(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Panel 1: void de baja resolucion
        low = Square(side_length=3, fill_opacity=0.1, color=BLUE)
        label_low = Text("R bajo", font_size=24).next_to(low, UP)
        dots_low = VGroup(*[
            Dot(point=[x, y, 0], color=BLUE, radius=0.04)
            for x in np.linspace(-1.2, 1.2, 6)
            for y in np.linspace(-1.2, 1.2, 6)
            if np.random.random() > 0.4
        ])
        msg1 = Text("Void: pocos pixeles", font_size=28).to_edge(DOWN)

        self.add(low, label_low, dots_low, msg1)
        self.wait(0.5)

        # Transicion a alta resolucion
        high = Square(side_length=3, fill_opacity=0.1, color=YELLOW)
        label_high = Text("R alto", font_size=24, color=YELLOW).next_to(high, UP)
        dots_high = VGroup(*[
            Dot(point=[x*0.9, y*0.9, 0], color=YELLOW, radius=0.03)
            for x in np.linspace(-1.2, 1.2, 14)
            for y in np.linspace(-1.2, 1.2, 14)
            if np.random.random() < 0.55
        ])
        mass = Dot(ORIGIN, color=RED, radius=0.12)
        label_mass = Text("Masa", font_size=22, color=RED).next_to(mass, DOWN)
        efeq = Text("c_eff = c * e^(-2psi)", font_size=28).to_edge(UP)
        out = Text("La gravedad es el render cambiando de escala", font_size=26).to_edge(DOWN)

        self.play(
            Transform(low, high), Transform(label_low, label_high),
            FadeIn(dots_high, lag_ratio=0.01), GrowFromCenter(mass), Write(label_mass)
        )
        self.wait(0.3)
        self.play(Write(efeq))
        self.wait(0.5)
        self.play(Write(out))
        self.wait(1.5)
