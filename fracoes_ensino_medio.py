from manim import *

class IntroducaoFracoes(Scene):
    def construct(self):
        titulo = Text("Introdução às Frações", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        definicao = Text("Uma fração representa\numa parte de um todo", font_size=32)
        self.play(Write(definicao))
        self.wait(2)
        self.play(FadeOut(definicao))

        pizza = Circle(radius=1.2, color=YELLOW, fill_opacity=1, stroke_width=2)
        frac_text = Text("1/4", font_size=36, color=WHITE).move_to(pizza.get_center())

        self.play(Create(pizza), Write(frac_text))
        self.wait(1)

        # Destacar uma fatia
        arc = Arc(radius=1.2, start_angle=PI/2, angle=PI/2, color=WHITE, fill_opacity=0.5)
        self.play(Create(arc))
        self.wait(2)

        numerador = Text("Numerador", font_size=28, color=RED).shift(UP * 2)
        denominador = Text("Denominador", font_size=28, color=BLUE).shift(DOWN * 2)
        setas = VGroup(
            Arrow(start=numerador.get_bottom(), end=frac_text.get_top(), color=RED, buff=0.2),
            Arrow(start=denominador.get_top(), end=pizza.get_bottom(), color=BLUE, buff=0.2)
        )
        self.play(Write(numerador), Write(denominador), Create(setas))
        self.wait(3)

class AdicaoFracoes(Scene):
    def construct(self):
        titulo = Text("Adição de Frações", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        caso1 = Text("Mesmo denominador", font_size=36, color=GREEN).shift(UP * 2.5)
        self.play(Write(caso1))

        ex1 = MathTex(
            r"\frac{1}{4} + \frac{2}{4} = \frac{3}{4}",
            font_size=42
        )
        self.play(Write(ex1))
        self.wait(2)

        self.play(FadeOut(caso1), FadeOut(ex1))

        caso2 = Text("Denominadores diferentes", font_size=36, color=YELLOW).shift(UP * 2.5)
        self.play(Write(caso2))

        ex2_step1 = MathTex(
            r"\frac{1}{2} + \frac{1}{3}",
            font_size=42
        )
        self.play(Write(ex2_step1))
        self.wait(2)

        ex2_step2 = MathTex(
            r"\frac{3}{6} + \frac{2}{6}",
            font_size=42
        )
        self.play(Transform(ex2_step1, ex2_step2))
        self.wait(2)

        ex2_step3 = MathTex(
            r"\frac{5}{6}",
            font_size=42
        )
        self.play(Transform(ex2_step1, ex2_step3))
        self.wait(3)

class MultiplicacaoDivisaoFracoes(Scene):
    def construct(self):
        titulo = Text("Multiplicação e Divisão", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        mult = Text("Multiplicação: Multiplica direto", font_size=32, color=GREEN).shift(UP * 2)
        mult_ex = MathTex(r"\frac{2}{3} \times \frac{3}{4} = \frac{6}{12} = \frac{1}{2}", font_size=40)
        mult_ex.next_to(mult, DOWN)

        div = Text("Divisão: Inverte e multiplica", font_size=32, color=YELLOW).shift(DOWN * 1.5)
        div_ex = MathTex(r"\frac{2}{3} \div \frac{3}{4} = \frac{2}{3} \times \frac{4}{3} = \frac{8}{9}", font_size=40)
        div_ex.next_to(div, DOWN)

        self.play(Write(mult), Write(mult_ex))
        self.wait(2)
        self.play(Write(div), Write(div_ex))
        self.wait(3)

if __name__ == "__main__":
    pass