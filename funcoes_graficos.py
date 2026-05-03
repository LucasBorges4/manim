from manim import *

class FuncaoLinear(Scene):
    def construct(self):
        titulo = Text("Função do 1º Grau (Linear)", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"f(x) = ax + b", font_size=48)
        self.play(Write(formula))
        self.wait(2)

        explica = VGroup(
            Text("a → coeficiente angular (inclinação)", font_size=24, color=YELLOW),
            Text("b → coeficiente linear (intersecção com y)", font_size=24, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        explica.next_to(formula, DOWN, buff=1)
        self.play(Write(explica))
        self.wait(3)
        self.play(FadeOut(formula), FadeOut(explica))

        # Exemplo com gráfico
        exemplo_txt = Text("Exemplo: f(x) = 2x + 1", font_size=36, color=YELLOW).shift(UP * 3)
        self.play(Write(exemplo_txt))

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 7, 1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=5
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label(r"x", edge=RIGHT, direction=RIGHT * 0.5)
        y_label = axes.get_y_axis_label(r"f(x)", edge=UP, direction=UP * 0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Gráfico da função
        graph = axes.plot(lambda x: 2*x + 1, color=RED, x_range=[-2.5, 2.5])
        graph_label = MathTex(r"y = 2x + 1", color=RED).next_to(graph.point_from_proportion(0.7), UR, buff=0.2)

        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Destacar a e b
        ponto_b = Dot(axes.c2p(0, 1), color=GREEN, radius=0.1)
        label_b = Text("b = 1", font_size=20, color=GREEN).next_to(ponto_b, UP)
        self.play(Create(ponto_b), Write(label_b))
        self.wait(1)

        # Mostrar inclinação
        incl_text = Text("a = 2 (crescente)", font_size=24, color=YELLOW)
        incl_text.to_corner(UR)
        self.play(Write(incl_text))
        self.wait(3)

class FuncaoQuadratica(Scene):
    def construct(self):
        titulo = Text("Função do 2º Grau (Quadrática)", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"f(x) = ax^2 + bx + c", font_size=48)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))

        # Parábola
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 8, 2],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=5
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label(r"x", edge=RIGHT, direction=RIGHT * 0.5)
        y_label = axes.get_y_axis_label(r"f(x)", edge=UP, direction=UP * 0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Parábola para a > 0
        parabola_pos = axes.plot(lambda x: x**2 - 2, color=RED, x_range=[-3.5, 3.5])
        parabola_pos_label = Text("a > 0 (concavidade voltada para cima)", font_size=20, color=RED)
        parabola_pos_label.to_corner(UR)

        self.play(Create(parabola_pos), Write(parabola_pos_label))
        self.wait(2)

        # Destacar vértice
        vertex_dot = Dot(axes.c2p(0, -2), color=YELLOW, radius=0.1)
        vertex_label = Text("Vértice", font_size=20, color=YELLOW).next_to(vertex_dot, UP)
        self.play(Create(vertex_dot), Write(vertex_label))
        self.wait(2)

        self.play(FadeOut(parabola_pos), FadeOut(parabola_pos_label), FadeOut(vertex_dot), FadeOut(vertex_label))

        # Parábola para a < 0
        parabola_neg = axes.plot(lambda x: -x**2 + 3, color=BLUE, x_range=[-3.5, 3.5])
        parabola_neg_label = Text("a < 0 (concavidade voltada para baixo)", font_size=20, color=BLUE)
        parabola_neg_label.to_corner(UR)

        self.play(Create(parabola_neg), Write(parabola_neg_label))
        self.wait(2)

        #zeros da função
        zeros = VGroup(
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=32, color=YELLOW),
            Text("(Fórmula de Bhaskara)", font_size=24, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        zeros.to_corner(DL)
        self.play(Write(zeros))
        self.wait(4)

class DominioContraDominio(Scene):
    def construct(self):
        titulo = Text("Domínio e Contradomínio", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        definicoes = VGroup(
            Text("Domínio (D):", font_size=28, color=YELLOW),
            Text("Conjunto de todos os valores que x pode assumir", font_size=24),
            Text("Contradomínio (CD):", font_size=28, color=GREEN).shift(DOWN * 1.5),
            Text("Conjunto de todos os valores que f(x) pode assumir", font_size=24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)

        self.play(Write(definicoes))
        self.wait(5)

class FuncaoExponencial(Scene):
    def construct(self):
        titulo = Text("Função Exponencial", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"f(x) = a^x", font_size=48)
        self.play(Write(formula))
        self.wait(2)

        condicao = MathTex(r"a > 0 \text{ e } a \neq 1", font_size=32, color=YELLOW)
        condicao.next_to(formula, DOWN)
        self.play(Write(condicao))
        self.wait(2)
        self.play(FadeOut(formula), FadeOut(condicao))

        # Gráfico
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 8, 2],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=5
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label(r"x", edge=RIGHT, direction=RIGHT * 0.5)
        y_label = axes.get_y_axis_label(r"f(x)", edge=UP, direction=UP * 0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        exp_grow = axes.plot(lambda x: 2**x, color=RED, x_range=[-2.5, 2.5])
        exp_grow_label = MathTex(r"y = 2^x", color=RED).next_to(exp_grow.point_from_proportion(0.8), UR, buff=0.2)

        self.play(Create(exp_grow), Write(exp_grow_label))
        self.wait(2)

        exp_decay = axes.plot(lambda x: (1/2)**x, color=BLUE, x_range=[-2.5, 2.5])
        exp_decay_label = MathTex(r"y = (\frac{1}{2})^x", color=BLUE).next_to(exp_decay.point_from_proportion(0.2), UL, buff=0.2)

        self.play(Create(exp_decay), Write(exp_decay_label))
        self.wait(2)

        caracteristica = Text("Crescente se a > 1\nDecrescente se 0 < a < 1", font_size=24)
        caracteristica.to_corner(UR)
        self.play(Write(caracteristica))
        self.wait(4)

class FuncaoLogaritmica(Scene):
    def construct(self):
        titulo = Text("Função Logarítmica", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"f(x) = \log_a x", font_size=48)
        self.play(Write(formula))
        self.wait(2)

        relacao = MathTex(r"a^y = x \iff \log_a x = y", font_size=32, color=YELLOW)
        relacao.next_to(formula, DOWN, buff=1)
        self.play(Write(relacao))
        self.wait(3)
        self.play(FadeOut(formula), FadeOut(relacao))

        # Gráfico
        axes = Axes(
            x_range=[0.1, 8, 2],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=5
        ).shift(DOWN * 0.5 + LEFT * 0.5)

        x_label = axes.get_x_axis_label(r"x", edge=RIGHT, direction=RIGHT * 0.5)
        y_label = axes.get_y_axis_label(r"\log_a x", edge=UP, direction=UP * 0.5)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        log_base2 = axes.plot(lambda x: np.log(x) / np.log(2), color=RED, x_range=[0.1, 8])
        log_label = MathTex(r"y = \log_2 x", color=RED).next_to(log_base2.point_from_proportion(0.7), UR, buff=0.2)

        self.play(Create(log_base2), Write(log_label))
        self.wait(3)

        propriedade = VGroup(
            MathTex(r"\log_a (xy) = \log_a x + \log_a y", font_size=28),
            MathTex(r"\log_a \left(\frac{x}{y}\right) = \log_a x - \log_a y", font_size=28),
            MathTex(r"\log_a (x^b) = b \log_a x", font_size=28),
        ).arrange(DOWN, buff=0.3).to_corner(DL)
        self.play(Write(propriedade))
        self.wait(4)

if __name__ == "__main__":
    pass