from manim import *

class ExponentialResolution(Scene):
    def construct(self):
        # Configurações de cores
        base_color = BLUE
        exponent_color = GREEN
        result_color = RED
        
        # Criar texto inicial
        exp_text = Tex("2^3 = ?")
        exp_text.scale(2)
        self.play(Write(exp_text))
        self.wait(1)
        
        # Separar base e expoente
        base = Integer(2).scale(1.5).set_color(base_color)
        exponent = Integer(3).scale(1.5).set_color(exponent_color)
        
        # Posicionar base e expoente
        base.next_to(exp_text[0][0], DOWN * 1.5)
        exponent.next_to(base, RIGHT * 1.5)
        
        # Animar separação
        self.play(
            ReplacementTransform(exp_text[0][0], base),
            ReplacementTransform(exp_text[0][2], exponent),
            exp_text[0][1].animate.set_color(WHITE).scale(0.5).shift(UP * 0.5)
        )
        self.wait(1)
        
        # Criar multiplicações
        multiplications = VGroup()
        for i in range(3):
            multiplicand = Integer(2).scale(1.5).set_color(base_color)
            multiplicand.next_to(base, DOWN * 1.5)
            multiplications.add(multiplicand)
            
        # Animar multiplicações
        self.play(
            *[ReplacementTransform(base.copy(), m) for m in multiplications]
        )
        self.wait(0.5)
        
        # Criar sinal de multiplicação
        times = Tex("\times").scale(1.5).set_color(YELLOW)
        times.move_to(multiplications[1].get_center())
        
        # Animar sinais de multiplicação
        self.play(
            Write(times),
            multiplications[1].animate.next_to(times, LEFT * 1.5),
            multiplications[2].animate.next_to(times, RIGHT * 1.5)
        )
        self.wait(0.5)
        
        # Calcular resultado
        result = Integer(8).scale(2).set_color(result_color)
        result.next_to(multiplications, DOWN * 2)
        
        # Animar cálculo
        self.play(
            FadeIn(result),
            multiplications.animate.shift(UP * 1)
        )
        self.wait(1)
        
        # Mostrar equação final
        final_eq = Tex("2^3 = 2 \times 2 \times 2 = 8")
        final_eq.scale(1.5)
        final_eq.next_to(result, DOWN * 2)
        
        self.play(Write(final_eq))
        self.wait(2)
        
        # Conclusão
        conclusion = Tex("Exponencial: base multiplicada por ela mesma expoente vezes")
        conclusion.scale(0.8).to_edge(DOWN)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        # Limpar tela
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)