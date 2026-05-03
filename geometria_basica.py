from manim import *

class AreasPerimetros(Scene):
    def construct(self):
        titulo = Text("Áreas e Perímetros", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formulas = VGroup(
            VGroup(
                Text("Quadrado", font_size=28),
                MathTex(r"A = l^2", font_size=32),
                MathTex(r"P = 4l", font_size=32),
            ).arrange(DOWN, buff=0.3),
            VGroup(
                Text("Retângulo", font_size=28),
                MathTex(r"A = b \times h", font_size=32),
                MathTex(r"P = 2(b + h)", font_size=32),
            ).arrange(DOWN, buff=0.3),
            VGroup(
                Text("Triângulo", font_size=28),
                MathTex(r"A = \frac{b \times h}{2}", font_size=32),
                MathTex(r"P = a + b + c", font_size=32),
            ).arrange(DOWN, buff=0.3),
            VGroup(
                Text("Círculo", font_size=28),
                MathTex(r"A = \pi r^2", font_size=32),
                MathTex(r"C = 2\pi r", font_size=32),
            ).arrange(DOWN, buff=0.3),
        ).arrange_in_grid(rows=2, cols=2, buff=1)

        self.play(Create(formulas))
        self.wait(5)

class TeoremaPitagoras(Scene):
    def construct(self):
        titulo = Text("Teorema de Pitágoras", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"a^2 + b^2 = c^2", font_size=56, color=YELLOW)
        self.play(Write(formula))
        self.wait(2)

        descricao = Text("Em um triângulo retângulo:\nO quadrado da hipotenusa\ninguala soma dos quadrados\n dos catetos",
                       font_size=28).next_to(formula, DOWN, buff=1)
        self.play(Write(descricao))
        self.wait(4)

        # Exemplo visual
        exemplo = VGroup(
            Text("Exemplo:", font_size=28),
            MathTex(r"3^2 + 4^2 = c^2", font_size=32),
            MathTex(r"9 + 16 = c^2", font_size=32),
            MathTex(r"25 = c^2", font_size=32),
            MathTex(r"c = 5", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.3)
        exemplo.shift(DOWN * 2)
        self.play(Write(exemplo))
        self.wait(3)

class RelacoesTrigonometricas(Scene):
    def construct(self):
        titulo = Text("Relações Trigonométricas", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        triangulo = VGroup()
        # Pontos do triângulo
        A = ORIGIN
        B = RIGHT * 3
        C = RIGHT * 2 + UP * 2.4

        # Triângulo
        tri = Polygon(A, B, C, color=YELLOW, stroke_width=3)
        triangulo.add(tri)

        # Ângulos
        arc_right = Arc(radius=0.5, start_angle=0, angle=np.arctan(2.4/1), color=RED)
        triangulo.add(arc_right)

        # Lados
        lado_a = Line(B, C, color=BLUE)
        lado_b = Line(A, C, color=RED)
        lado_c = Line(A, B, color=GREEN)

        labels = VGroup(
            MathTex(r"a", font_size=24, color=BLUE).move_to(lado_a.get_center() + UP * 0.3 + RIGHT * 0.2),
            MathTex(r"b", font_size=24, color=RED).move_to(lado_b.get_center() + LEFT * 0.3),
            MathTex(r"c", font_size=24, color=GREEN).move_to(lado_c.get_center() + DOWN * 0.3),
        )

        triangulo.add(lado_a, lado_b, lado_c, labels)

        self.play(Create(triangulo))
        self.wait(2)

        formulas = VGroup(
            MathTex(r"\sin(\theta) = \frac{\text{cateto oposto}}{\text{hipotenusa}} = \frac{a}{c}", font_size=28),
            MathTex(r"\cos(\theta) = \frac{\text{cateto adjacente}}{\text{hipotenusa}} = \frac{b}{c}", font_size=28),
            MathTex(r"\tan(\theta) = \frac{\text{cateto oposto}}{\text{cateto adjacente}} = \frac{a}{b}", font_size=28),
        ).arrange(DOWN, buff=0.5)

        formulas.shift(RIGHT * 3 + UP * 0.5)
        self.play(Write(formulas))
        self.wait(5)

class VolumeFiguras(Scene):
    def construct(self):
        titulo = Text("Volume das Figuras", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formulas = VGroup(
            VGroup(
                Text("Paralelepípedo/Cubo", font_size=24),
                MathTex(r"V = b \times h \times l", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Prisma", font_size=24),
                MathTex(r"V = A_\text{base} \times h", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Cilindro", font_size=24),
                MathTex(r"V = \pi r^2 h", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Esfera", font_size=24),
                MathTex(r"V = \frac{4}{3} \pi r^3", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Cone", font_size=24),
                MathTex(r"V = \frac{1}{3} \pi r^2 h", font_size=28),
            ).arrange(DOWN, buff=0.2),
        ).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.8))

        self.play(Create(formulas))
        self.wait(5)

class SemelhancaTriangulos(Scene):
    def construct(self):
        titulo = Text("Semelhança de Triângulos", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        conceito = Text("Dois triângulos são semelhantes\nse têm os ângulos congruentes", font_size=32)
        self.play(Write(conceito))
        self.wait(3)
        self.play(FadeOut(conceito))

        # Propriedade
        prop = MathTex(r"\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}", font_size=48, color=YELLOW)
        self.play(Write(prop))
        self.wait(3)

        # Exemplo
        exemplo = VGroup(
            Text("Exemplo de aplicação:", font_size=28),
            MathTex(r"\frac{3}{6} = \frac{4}{x}", font_size=32),
            MathTex(r"3x = 24", font_size=32),
            MathTex(r"x = 8", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        exemplo.shift(DOWN * 1.5)
        self.play(Write(exemplo))
        self.wait(4)

if __name__ == "__main__":
    pass