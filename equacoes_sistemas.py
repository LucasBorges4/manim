from manim import *

class EquacaoPrimeiroGrau(Scene):
    def construct(self):
        titulo = Text("Equação do 1º Grau", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        forma = MathTex(r"ax + b = 0", font_size=48)
        self.play(Write(forma))
        self.wait(2)
        self.play(FadeOut(forma))

        # Exemplo 1
        ex1_titulo = Text("Exemplo 1:", font_size=32, color=YELLOW).shift(UP * 2.5 + LEFT * 3)
        self.play(Write(ex1_titulo))

        ex1 = VGroup(
            MathTex(r"2x + 4 = 10", font_size=36),
            MathTex(r"2x = 10 - 4", font_size=36),
            MathTex(r"2x = 6", font_size=36),
            MathTex(r"x = \frac{6}{2}", font_size=36),
            MathTex(r"x = 3", font_size=36, color=GREEN),
        ).arrange(DOWN, buff=0.5)
        ex1.shift(UP * 0.5)

        for linha in ex1:
            self.play(Write(linha))
            self.wait(1.5)

        self.wait(2)
        self.play(FadeOut(ex1_titulo), FadeOut(ex1))

        # Exemplo 2 com coeficiente negativo
        ex2_titulo = Text("Exemplo 2:", font_size=32, color=YELLOW).shift(UP * 2.5 + LEFT * 3)
        self.play(Write(ex2_titulo))

        ex2 = VGroup(
            MathTex(r"-3x + 7 = 1", font_size=36),
            MathTex(r"-3x = 1 - 7", font_size=36),
            MathTex(r"-3x = -6", font_size=36),
            MathTex(r"x = \frac{-6}{-3}", font_size=36),
            MathTex(r"x = 2", font_size=36, color=GREEN),
        ).arrange(DOWN, buff=0.5)
        ex2.shift(UP * 0.5)

        for linha in ex2:
            self.play(Write(linha))
            self.wait(1.5)

        self.wait(3)

class EquacaoSegundoGrau(Scene):
    def construct(self):
        titulo = Text("Equação do 2º Grau (Quadrática)", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        forma = MathTex(r"ax^2 + bx + c = 0", font_size=48)
        self.play(Write(forma))
        self.wait(2)

        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", font_size=40, color=YELLOW)
        formula.next_to(forma, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(3)
        self.play(FadeOut(forma), FadeOut(formula))

        # Exemplo completo
        texto_ex = Text("Exemplo:", font_size=32, color=GREEN).shift(UP * 2.5)
        self.play(Write(texto_ex))

        equacao = MathTex(r"x^2 - 5x + 6 = 0", font_size=40)
        self.play(Write(equacao))
        self.wait(2)

        # Identificar coeficientes
        coefs = VGroup(
            MathTex(r"a = 1", font_size=28, color=BLUE).shift(LEFT * 3 + UP * 1.5),
            MathTex(r"b = -5", font_size=28, color=YELLOW).shift(UP * 1.5),
            MathTex(r"c = 6", font_size=28, color=RED).shift(RIGHT * 3 + UP * 1.5),
        )
        self.play(Write(coefs))
        self.wait(2)

        # Delta
        delta_titulo = Text("Δ = b² - 4ac", font_size=28)
        delta_calc = MathTex(r"\Delta = (-5)^2 - 4 \times 1 \times 6", font_size=32)
        delta_res = MathTex(r"\Delta = 25 - 24 = 1", font_size=32, color=YELLOW)

        delta_grupo = VGroup(delta_titulo, delta_calc, delta_res).arrange(DOWN, buff=0.3)
        delta_grupo.shift(DOWN * 1.5)
        self.play(Write(delta_grupo))
        self.wait(3)

        # Resultado final
        x1_x2 = MathTex(r"x_1 = 3 \quad x_2 = 2", font_size=40, color=GREEN)
        x1_x2.shift(DOWN * 3)
        self.play(Write(x1_x2))
        self.wait(3)

class SistemasLineares(Scene):
    def construct(self):
        titulo = Text("Sistemas Lineares (2×2)", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        sistema = VGroup(
            MathTex(r"\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}", font_size=40),
        )
        self.play(Write(sistema))
        self.wait(2)

        metodo1 = Text("Método: Adição", font_size=32, color=YELLOW).shift(UP * 2)
        self.play(Write(metodo1))

        passo1 = MathTex(r"(x+y) + (x-y) = 5 + 1", font_size=36).shift(UP * 0.5)
        passo2 = MathTex(r"2x = 6", font_size=36).shift(DOWN * 0.5)
        passo3 = MathTex(r"x = 3", font_size=36, color=GREEN).shift(DOWN * 1.5)
        passo4 = MathTex(r"3 + y = 5", font_size=36).shift(DOWN * 2.5)
        passo5 = MathTex(r"y = 2", font_size=36, color=GREEN).shift(DOWN * 3.5)

        self.play(Write(passo1))
        self.wait(1.5)
        self.play(Write(passo2))
        self.wait(1.5)
        self.play(Write(passo3))
        self.wait(1.5)
        self.play(Write(passo4))
        self.wait(1.5)
        self.play(Write(passo5))
        self.wait(3)

class RegradeSignosAplicada(Scene):
    def construct(self):
        titulo = Text("Regra de Sinais nas Equações", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        exemplos = VGroup(
            MathTex(r"+2x = 6 \implies x = 3", font_size=32),
            MathTex(r"-2x = 6 \implies x = -3", font_size=32),
            MathTex(r"+2x = -6 \implies x = -3", font_size=32),
            MathTex(r"-2x = -6 \implies x = 3", font_size=32),
        ).arrange(DOWN, buff=0.5)

        for i, ex in enumerate(exemplos):
            ex.shift(UP * (1.5 - i * 0.5))

        self.play(Write(exemplos))
        self.wait(3)

class InconsistenteDeterminado(Scene):
    def construct(self):
        titulo = Text("Sistemas: Possibilidades", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        determ = VGroup(
            Text("Determinado", font_size=32, color=GREEN),
            MathTex(r"\frac{a_1}{a_2} \neq \frac{b_1}{b_2}", font_size=36),
        ).arrange(DOWN, buff=0.3)
        determ.shift(UP * 1.5)
        self.play(Write(determ))
        self.wait(2)

        imp = VGroup(
            Text("Impossível (Inconsistente)", font_size=32, color=RED),
            MathTex(r"\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}", font_size=36),
        ).arrange(DOWN, buff=0.3)
        self.play(Write(imp))
        self.wait(2)

        indeterm = VGroup(
            Text("Indeterminado", font_size=32, color=YELLOW),
            MathTex(r"\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}", font_size=36),
        ).arrange(DOWN, buff=0.3)
        indeterm.shift(DOWN * 2)
        self.play(Write(indeterm))
        self.wait(3)

if __name__ == "__main__":
    pass