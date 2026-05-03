from manim import *

class ResolucaoFracao(Scene):
    def construct(self):
        # 1. Problema Inicial
        titulo = Text("Soma de Frações", font_size=40).to_edge(UP)
        equacao_inicial = MathTex(
            "\\frac{1}{2}", "+", "\\frac{1}{3}", "=", "?"
        ).scale(1.5)
        
        # Transições suaves com easing
        self.play(Write(titulo), rate_func=smooth)
        self.wait(0.5)
        self.play(Write(equacao_inicial), rate_func=smooth)
        self.wait(1)

        # 2. Destacar necessidade de denominador comum
        denominadores = VGroup(equacao_inicial[0][2], equacao_inicial[2][2])
        self.play(
            denominadores.animate.set_color(YELLOW),
            rate_func=there_and_back_with_pause
        )
        
        comentario = Text("Precisamos do mesmo denominador (MMC)", font_size=24, color=YELLOW)
        comentario.next_to(equacao_inicial, DOWN, buff=1)
        self.play(FadeIn(comentario, rate_func=smooth))
        self.wait(2)
        self.play(FadeOut(comentario, rate_func=smooth))

        # 3. Transformação para denominador comum (6)
        passo_1 = MathTex(
            "\\frac{1 \\times 3}{2 \\times 3}", "+", "\\frac{1 \\times 2}{3 \\times 2}"
        ).scale(1.2)
        
        self.play(TransformMatchingTex(equacao_inicial, passo_1, rate_func=smooth))
        self.wait(1.5)

        # 4. Resultado da multiplicação
        passo_2 = MathTex(
            "\\frac{3}{6}", "+", "\\frac{2}{6}"
        ).scale(1.5)
        
        self.play(TransformMatchingTex(passo_1, passo_2, rate_func=smooth))
        self.wait(1.5)

        # 5. Soma dos numeradores
        passo_3 = MathTex(
            "\\frac{3 + 2}{6}"
        ).scale(1.5)
        
        self.play(TransformMatchingTex(passo_2, passo_3, rate_func=smooth))
        self.wait(1)

        # 6. Resultado Final
        resultado_final = MathTex(
            "\\frac{5}{6}"
        ).scale(2).set_color(GREEN)
        
        # Transição suave com destaque gradual
        self.play(
            Transform(passo_3, resultado_final, rate_func=smooth),
            resultado_final.animate.scale(2.2).set_color(GREEN).shift(UP*0.2),
            rate_func=smooth
        )
        self.play(resultado_final.animate.scale(2).shift(DOWN*0.2), rate_func=smooth)
        
        # Enquadrar o resultado com animação suave
        box = SurroundingRectangle(resultado_final, color=GREEN, buff=0.3)
        self.play(Create(box, rate_func=smooth))
        
        # Fade out suave do box
        self.play(FadeOut(box, rate_func=smooth))
        
        # Fade out suave da equação
        self.play(FadeOut(equacao_inicial, rate_func=smooth))
        
        self.wait(2)
        self.play(
            FadeOut(resultado_final, rate_func=smooth),
            titulo.animate.shift(UP*2).scale(0.8),
            rate_func=smooth
        )
        self.wait(1)
        self.play(
            titulo.animate.shift(DOWN*2).scale(1.25),
            rate_func=smooth
        )
        self.wait(2)