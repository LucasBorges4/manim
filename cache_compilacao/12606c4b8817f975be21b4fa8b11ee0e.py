from manim import *

class Apresentacao(Scene):
    def construct(self):
        # 1. Título com Write + slide para o topo
        titulo = Text('Teorema de Pitágoras', font_size=52, color=BLUE)
        self.play(Write(titulo), run_time=1.4)
        self.wait(0.5)
        self.play(titulo.animate.to_edge(UP).scale(0.7))

        # 2. Enunciado central com FadeIn
        enunciado = MathTex('a^2 + b^2 = c^2', font_size=64, color=WHITE)
        self.play(FadeIn(enunciado, shift=UP*0.5), run_time=1.2)
        self.wait(0.8)

        # 3. Caixa pulsando ao redor
        self.play(Circumscribe(enunciado, color=GOLD, run_time=1.5))
        self.wait(0.5)

        # 4. Autoria opcional
        if '':
            autoria = Text('', font_size=24, color=GREY_B, slant=ITALIC).next_to(enunciado, DOWN, buff=0.8)
            self.play(FadeIn(autoria, shift=UP*0.3))
            self.wait(1)

        # 5. Saída suave
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1)
