from manim import *
from math import gcd

class SomaFracoes(Scene):
    def construct(self):
        n1, d1 = 1, 2
        n2, d2 = 1, 3
        mmc = d1*d2 // gcd(d1, d2)
        a = n1 * (mmc // d1)
        b = n2 * (mmc // d2)
        soma_n = a + b
        g = gcd(abs(soma_n), mmc) if soma_n != 0 else 1
        sn, sd = soma_n // g, mmc // g

        titulo = Text("Soma de Frações", font_size=44, color=BLUE).to_edge(UP)
        self.play(Write(titulo))

        f1 = MathTex(rf"\frac{{ {n1} }}{{ {d1} }}", font_size=72, color=GREEN).shift(LEFT*3 + UP*0.5)
        plus = MathTex("+", font_size=72).shift(LEFT*1 + UP*0.5)
        f2 = MathTex(rf"\frac{{ {n2} }}{{ {d2} }}", font_size=72, color=ORANGE).shift(LEFT*0 + UP*0.5).shift(RIGHT*0.5)
        eq = MathTex("=", font_size=72).next_to(f2, RIGHT, buff=0.5)
        result = MathTex(rf"\frac{{ ? }}{{ ? }}", font_size=72, color=YELLOW).next_to(eq, RIGHT, buff=0.5)

        self.play(Write(f1), Write(plus), Write(f2), Write(eq), Write(result))
        self.wait(1)

        passo1 = MathTex(rf"\text{MMC}({d1}, {d2}) = {mmc}", font_size=36, color=BLUE).shift(DOWN*1.5)
        self.play(Write(passo1))
        self.wait(1)

        f1e = MathTex(rf"\frac{{ {a} }}{{ {mmc} }}", font_size=60, color=GREEN).move_to(f1)
        f2e = MathTex(rf"\frac{{ {b} }}{{ {mmc} }}", font_size=60, color=ORANGE).move_to(f2)
        self.play(Transform(f1, f1e), Transform(f2, f2e))
        self.wait(1)

        result_final = MathTex(rf"\frac{{ {soma_n} }}{{ {mmc} }}", font_size=72, color=YELLOW).move_to(result)
        self.play(Transform(result, result_final))
        self.wait(1)

        if (sn, sd) != (soma_n, mmc):
            simpl = MathTex(rf"= \frac{{ {sn} }}{{ {sd} }}", font_size=72, color=RED).next_to(result, RIGHT, buff=0.4)
            self.play(Write(simpl))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
