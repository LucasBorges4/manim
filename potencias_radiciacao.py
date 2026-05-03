from manim import *

class Potencias(Scene):
    def construct(self):
        titulo = Text("Potenciação", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        conceito = VGroup(
            MathTex(r"a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ vezes}}", font_size=36),
            Text("base → multiplicanda\npotência → número de vezes", font_size=24)
        ).arrange(DOWN, buff=0.5)
        self.play(Write(conceito))
        self.wait(3)
        self.play(FadeOut(conceito))

        exemplos = VGroup(
            MathTex(r"2^3 = 2 \times 2 \times 2 = 8", font_size=32, color=GREEN),
            MathTex(r"5^2 = 5 \times 5 = 25", font_size=32, color=YELLOW),
            MathTex(r"3^4 = 3 \times 3 \times 3 \times 3 = 81", font_size=32, color=RED),
        ).arrange(DOWN, buff=0.7)

        for ex in exemplos:
            ex.shift(UP * 1)
        self.play(Write(exemplos))
        self.wait(3)
        self.play(FadeOut(exemplos))

        propriedades = VGroup(
            MathTex(r"a^m \times a^n = a^{m+n}", font_size=28),
            MathTex(r"(a^m)^n = a^{m \times n}", font_size=28),
            MathTex(r"a^{-n} = \frac{1}{a^n}", font_size=28),
            MathTex(r"a^0 = 1 \quad (a \neq 0)", font_size=28),
            MathTex(r"a^{\frac{m}{n}} = \sqrt[n]{a^m}", font_size=28),
        ).arrange(DOWN, buff=0.4)

        prop_titulo = Text("Propriedades", font_size=36, color=YELLOW).next_to(propriedades, UP)
        grupo = VGroup(prop_titulo, propriedades)

        self.play(Write(grupo))
        self.wait(4)

class Radiciacao(Scene):
    def construct(self):
        titulo = Text("Radiciação", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        definicao = MathTex(r"\sqrt[n]{a} = b \iff b^n = a", font_size=40)
        self.play(Write(definicao))
        self.wait(3)
        self.play(FadeOut(definicao))

        exemplos = VGroup(
            MathTex(r"\sqrt{16} = 4 \text{ pois } 4^2 = 16", font_size=32, color=GREEN),
            MathTex(r"\sqrt[3]{27} = 3 \text{ pois } 3^3 = 27", font_size=32, color=YELLOW),
            MathTex(r"\sqrt{\frac{9}{16}} = \frac{3}{4}", font_size=32, color=RED),
        ).arrange(DOWN, buff=0.7)
        self.play(Write(exemplos))
        self.wait(3)
        self.play(FadeOut(exemplos))

        propriedades = VGroup(
            MathTex(r"\sqrt[n]{a \times b} = \sqrt[n]{a} \times \sqrt[n]{b}", font_size=28),
            MathTex(r"\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}", font_size=28),
            MathTex(r"\sqrt[n]{a^m} = a^{\frac{m}{n}}", font_size=28),
        ).arrange(DOWN, buff=0.4)

        prop_titulo = Text("Propriedades da Radiciação", font_size=32, color=YELLOW).next_to(propriedades, UP)
        grupo = VGroup(prop_titulo, propriedades)
        self.play(Write(grupo))
        self.wait(4)

class SimplificacaoRaiz(Scene):
    def construct(self):
        titulo = Text("Simplificação de Raízes", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        passo1 = MathTex(r"\sqrt{50}", font_size=48)
        self.play(Write(passo1))
        self.wait(1)

        passo2 = MathTex(r"\sqrt{25 \times 2}", font_size=48)
        self.play(Transform(passo1, passo2))
        self.wait(1)

        passo3 = MathTex(r"\sqrt{25} \times \sqrt{2}", font_size=48)
        self.play(Transform(passo1, passo3))
        self.wait(1)

        passo4 = MathTex(r"5\sqrt{2}", font_size=48, color=GREEN)
        self.play(Transform(passo1, passo4))
        self.wait(3)

class OperacoesMisturadas(Scene):
    def construct(self):
        titulo = Text("Operações com Potências e Raízes", font_size=40, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        ex1 = MathTex(
            r"2^3 \times \sqrt{16} = 8 \times 4 = 32",
            font_size=36
        ).shift(UP * 1.5)
        self.play(Write(ex1))
        self.wait(2)

        ex2 = MathTex(
            r"\frac{3^2 + \sqrt{25}}{2} = \frac{9 + 5}{2} = 7",
            font_size=36
        )
        self.play(Write(ex2))
        self.wait(3)

if __name__ == "__main__":
    pass