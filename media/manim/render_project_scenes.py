from manim import *

class A_RBranches(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        trunk = Line(ORIGIN, 2*DOWN, color=WHITE)
        a = Line(2*DOWN, 4*DOWN+2*LEFT, color=GREEN)
        b = Line(2*DOWN, 4*DOWN+2*RIGHT, color=RED)
        ta = Text("A: log v", font_size=22, color=GREEN).next_to(a.get_end(), LEFT)
        tb = Text("B: area", font_size=22, color=RED).next_to(b.get_end(), RIGHT)
        num = Text("p = 2.700 +/- 0.071", font_size=28, color=YELLOW).to_edge(UP)
        msg = Text("Rama B muerta dos veces", font_size=24, color=RED).to_edge(DOWN)
        self.add(trunk, a, b, ta, tb, num, msg)

class B_DiamondSlab(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        d = Square(side_length=3, color=BLUE, fill_opacity=0.1)
        dl = Text("Diamante", font_size=22, color=BLUE).next_to(d, UP)
        s = Square(side_length=3, color=YELLOW, fill_opacity=0.1).shift(RIGHT*4)
        sl = Text("Slab +21%", font_size=22, color=YELLOW).next_to(s, UP)
        arr = Arrow(start=LEFT*0.5, end=RIGHT*3, color=WHITE)
        txt = Text("Misma maquinaria, geometria distinta", font_size=22).to_edge(DOWN)
        self.add(d, dl, s, sl, arr, txt)

class C_MetricFight(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        title = Text("Postulado 3'", font_size=32, color=YELLOW).to_edge(UP)
        conf = Text("Conforme: gamma=-1, sin bending", font_size=22, color=RED).shift(UP*1.2)
        disf = Text("Disforme: gamma=1, bending OK", font_size=22, color=GREEN).shift(DOWN*1.2)
        eq = Text("ds^2 = -e^{-2psi}c^2dt^2 + e^{+2psi}dx^2", font_size=24).to_edge(DOWN)
        note = Text("Unico parametro: psi = ln(R/R0)", font_size=20, color=GRAY).shift(DOWN*2.4)
        self.add(title, conf, disf, eq, note)

class D_GrowthCanvas(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        t = Text("R(t) crece con el tiempo", font_size=32, color=YELLOW).to_edge(UP)
        dots = VGroup(*[
            Dot([x, np.random.random()*2-1, 0], color=BLUE, radius=0.03)
            for x in np.linspace(-4, 4, 40)
        ])
        line = Line(start=LEFT*4, end=RIGHT*4, color=WHITE).shift(DOWN*2)
        lbl = Text("ticks del render = R(t)", font_size=22, color=WHITE).next_to(line, DOWN)
        msg = Text("Cada tick agrega un bit de resolucion", font_size=22).to_edge(DOWN)
        self.add(t, dots, line, lbl, msg)
