from manim import *

class FuncaoLinear(Scene):
    def construct(self):
        m, n = 2, 1

        titulo = Text("Função Linear", font_size=44, color=BLUE).to_edge(UP)
        formula = MathTex(rf"f(x) = {m}x + ({n})", font_size=44, color=YELLOW).next_to(titulo, DOWN)
        self.play(Write(titulo), FadeIn(formula, shift=UP))
        self.wait(1)

        axes = Axes(x_range=[-5,5,1], y_range=[-5,5,1], x_length=8, y_length=5,
                    axis_config={"include_numbers": True, "stroke_color": GREY_B}).shift(DOWN*0.3)
        self.play(Create(axes))

        graph = axes.plot(lambda x: m*x + n, color=GREEN, x_range=[-5,5])
        self.play(Create(graph), run_time=2)
        self.wait(0.5)

        # Intercepto
        p0 = Dot(axes.c2p(0, n), color=RED, radius=0.12)
        p0_lbl = MathTex(rf"(0, {n})", color=RED).scale(0.7).next_to(p0, RIGHT)
        self.play(GrowFromCenter(p0), Write(p0_lbl))
        self.wait(0.5)

        # Inclinação visual: triângulo de subida
        x0, x1 = 1, 2
        tri = Polygon(axes.c2p(x0, m*x0+n), axes.c2p(x1, m*x0+n), axes.c2p(x1, m*x1+n),
                      color=ORANGE, fill_opacity=0.4)
        self.play(Create(tri))
        delta_x = MathTex(r"\Delta x = 1", color=ORANGE).scale(0.6).next_to(
            Line(axes.c2p(x0,m*x0+n), axes.c2p(x1,m*x0+n)).get_center(), DOWN, buff=0.1)
        delta_y = MathTex(rf"\Delta y = {m}", color=ORANGE).scale(0.6).next_to(
            Line(axes.c2p(x1,m*x0+n), axes.c2p(x1,m*x1+n)).get_center(), RIGHT, buff=0.1)
        self.play(Write(delta_x), Write(delta_y))
        self.wait(1)

        slope = MathTex(rf"m = \frac{\Delta y}{\Delta x} = {m}", color=ORANGE).to_edge(DOWN)
        self.play(Write(slope))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
