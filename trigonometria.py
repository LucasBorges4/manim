from manim import *
import math

class CircunferenciaTrigonometrica(Scene):
    def construct(self):
        titulo = Text("Circunferência Trigonométrica", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Círculo unitário
        circle = Circle(radius=1.5, color=WHITE, stroke_width=3)
        axes = VGroup(
            Line(LEFT * 2, RIGHT * 2, color=GRAY),
            Line(DOWN * 2, UP * 2, color=GRAY)
        )

        self.play(Create(axes), Create(circle))
        self.wait(1)

        # Pontos nos eixos
        x_axis_points = VGroup(
            Dot(RIGHT * 1.5, color=RED, radius=0.08),
            MathTex(r"(1, 0)", font_size=20, color=RED).next_to(RIGHT * 1.5, DR, buff=0.1),
        )
        y_axis_points = VGroup(
            Dot(UP * 1.5, color=BLUE, radius=0.08),
            MathTex(r"(0, 1)", font_size=20, color=BLUE).next_to(UP * 1.5, UL, buff=0.1),
        )
        origin_dot = Dot(ORIGIN, color=YELLOW, radius=0.06)

        self.play(Create(x_axis_points), Create(y_axis_points), Create(origin_dot))
        self.wait(1)

        # Arco e ângulo
        angle = 60 * DEGREES
        arc = Arc(radius=0.4, start_angle=0, angle=angle, color=GREEN)
        angle_line = Line(ORIGIN, RIGHT * 1.5 * math.cos(angle) + UP * 1.5 * math.sin(angle), color=YELLOW)

        self.play(Create(angle_line))
        self.play(Create(arc))
        self.wait(1)

        # Seno e cosseno
        sin_line = Line(
            RIGHT * 1.5 * math.cos(angle),
            RIGHT * 1.5 * math.cos(angle) + UP * 1.5 * math.sin(angle),
            color=RED,
            stroke_width=4
        )
        cos_line = Line(
            ORIGIN,
            RIGHT * 1.5 * math.cos(angle),
            color=BLUE,
            stroke_width=4
        )

        self.play(Create(sin_line), Create(cos_line))
        self.wait(1)

        labels = VGroup(
            MathTex(r"\cos\theta", font_size=28, color=BLUE).next_to(cos_line, DOWN, buff=0.1),
            MathTex(r"\sin\theta", font_size=28, color=RED).next_to(sin_line, RIGHT, buff=0.1),
        )
        self.play(Write(labels))
        self.wait(2)

        # Identidade fundamental
        identity = MathTex(r"\sin^2\theta + \cos^2\theta = 1", font_size=40, color=YELLOW)
        identity.to_corner(DOWN)
        self.play(Write(identity))
        self.wait(4)

class FuncoesTrigonometricas(Scene):
    def construct(self):
        titulo = Text("Funções Seno e Cosseno", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": WHITE},
            x_length=8,
            y_length=4
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label(r"\theta", edge=RIGHT)
        y_label = axes.get_y_axis_label(r"f(\theta)", edge=UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Gráfico do seno
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED, x_range=[0, 2*PI])
        sin_label = MathTex(r"y = \sin\theta", color=RED).next_to(axes.c2p(PI, 1), UR)

        self.play(Create(sin_graph), Write(sin_label))
        self.wait(2)

        # Gráfico do cosseno
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE, x_range=[0, 2*PI])
        cos_label = MathTex(r"y = \cos\theta", color=BLUE).next_to(axes.c2p(1.5*PI, 0.8), UR)

        self.play(Create(cos_graph), Write(cos_label))
        self.wait(2)

        # Marcar pontos importantes
        angles = [0, PI/2, PI, 3*PI/2, 2*PI]
        sin_vals = [0, 1, 0, -1, 0]
        cos_vals = [1, 0, -1, 0, 1]

        for angle, s_val, c_val in zip(angles, sin_vals, cos_vals):
            sin_dot = Dot(axes.c2p(angle, s_val), color=RED, radius=0.06)
            cos_dot = Dot(axes.c2p(angle, c_val), color=BLUE, radius=0.06)
            self.play(Create(sin_dot), Create(cos_dot), run_time=0.3)

        self.wait(3)

        # Identidade
        identity = MathTex(r"\cos\theta = \sin(\theta + \frac{\pi}{2})", font_size=32, color=YELLOW)
        identity.to_corner(DOWN)
        self.play(Write(identity))
        self.wait(4)

class RelacoesFundamentais(Scene):
    def construct(self):
        titulo = Text("Identidades Trigonométricas", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        identidades = VGroup(
            MathTex(r"\sin^2\theta + \cos^2\theta = 1", font_size=32),
            MathTex(r"\tan\theta = \frac{\sin\theta}{\cos\theta}", font_size=32),
            MathTex(r"1 + \tan^2\theta = \sec^2\theta", font_size=32),
            MathTex(r"1 + \cot^2\theta = \csc^2\theta", font_size=32),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(identidades))
        self.wait(5)

        # Ângulos notáveis
        self.play(FadeOut(identidades))

        angulos_titulo = Text("Ângulos Notáveis", font_size=36, color=YELLOW).shift(UP * 2.5)
        self.play(Write(angulos_titulo))

        tabela = VGroup(
            VGroup(
                Text("30° = π/6", font_size=24),
                MathTex(r"\sin = \frac{1}{2}", font_size=24, color=RED),
                MathTex(r"\cos = \frac{\sqrt{3}}{2}", font_size=24, color=BLUE),
                MathTex(r"\tan = \frac{\sqrt{3}}{3}", font_size=24, color=GREEN),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("45° = π/4", font_size=24),
                MathTex(r"\sin = \frac{\sqrt{2}}{2}", font_size=24, color=RED),
                MathTex(r"\cos = \frac{\sqrt{2}}{2}", font_size=24, color=BLUE),
                MathTex(r"\tan = 1", font_size=24, color=GREEN),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("60° = π/3", font_size=24),
                MathTex(r"\sin = \frac{\sqrt{3}}{2}", font_size=24, color=RED),
                MathTex(r"\cos = \frac{1}{2}", font_size=24, color=BLUE),
                MathTex(r"\tan = \sqrt{3}", font_size=24, color=GREEN),
            ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.6)
        tabela.shift(DOWN * 0.5)

        self.play(Write(tabela))
        self.wait(5)

class LeidosSenosCos(Scene):
    def construct(self):
        titulo = Text("Lei dos Senos e Lei dos Cossenos", font_size=38, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Triângulo genérico
        vertices = [
            LEFT * 2 + UP * 1.5,
            RIGHT * 2 + UP * 1.5,
            DOWN * 2
        ]

        triangle = Polygon(*vertices, color=YELLOW, stroke_width=3)
        labels = VGroup(
            MathTex(r"A", font_size=32).move_to(vertices[0] + UP * 0.5),
            MathTex(r"B", font_size=32).move_to(vertices[1] + UP * 0.5),
            MathTex(r"C", font_size=32).move_to(vertices[2] + DOWN * 0.5),
        )

        self.play(Create(triangle), Write(labels))
        self.wait(1)

        # Lados a, b, c
        side_a = Line(vertices[1], vertices[2], color=RED)
        side_b = Line(vertices[0], vertices[2], color=BLUE)
        side_c = Line(vertices[0], vertices[1], color=GREEN)

        side_labels = VGroup(
            MathTex(r"a", font_size=28, color=RED).move_to(side_a.get_center() + RIGHT * 0.3),
            MathTex(r"b", font_size=28, color=BLUE).move_to(side_b.get_center() + LEFT * 0.3),
            MathTex(r"c", font_size=28, color=GREEN).move_to(side_c.get_center() + UP * 0.3),
        )

        self.play(Create(side_a), Create(side_b), Create(side_c), Write(side_labels))
        self.wait(1)

        # Lei dos Senos
        lei_senos = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}",
            font_size=32,
            color=YELLOW
        )
        lei_senos.to_corner(UP)
        self.play(Write(lei_senos))
        self.wait(3)

        # Lei dos Cossenos
        self.play(FadeOut(triangle), FadeOut(labels), FadeOut(side_a), FadeOut(side_b), FadeOut(side_c), FadeOut(side_labels))

        lei_cossenos = VGroup(
            MathTex(r"c^2 = a^2 + b^2 - 2ab\cos C", font_size=32, color=RED),
            MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A", font_size=32, color=BLUE),
            MathTex(r"b^2 = a^2 + c^2 - 2ac\cos B", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.5)
        lei_cossenos.shift(DOWN * 1)

        self.play(Write(lei_cossenos))
        self.wait(4)

class FaseAmplitudePeriodo(Scene):
    def construct(self):
        titulo = Text("Funções Trigonométricas: Fase, Amplitude e Período", font_size=36, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        axes = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-2.5, 2.5, 1],
            axis_config={"color": WHITE},
            x_length=8,
            y_length=4
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label(r"x", edge=RIGHT)
        y_label = axes.get_y_axis_label(r"f(x)", edge=UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Função geral: f(x) = A·sin(Bx + C) + D
        formula_geral = MathTex(
            r"f(x) = A\cdot\sin(Bx + C) + D",
            font_size=32
        ).to_corner(UL)
        self.play(Write(formula_geral))
        self.wait(2)

        # Gráfico com amplitude e período
        graph = axes.plot(lambda x: 2 * np.sin(x), color=RED, x_range=[0, 4*PI])
        graph_label = Text("A = 2, B = 1, C = 0, D = 0", font_size=20, color=RED)
        graph_label.next_to(axes.c2p(PI, 2), UR)

        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Destacar amplitude
        amplitude_line = Line(
            axes.c2p(0, 0),
            axes.c2p(0, 2),
            color=YELLOW,
            stroke_width=3
        )
        amplitude_brace = Brace(amplitude_line, RIGHT)
        amplitude_text = Text("Amplitude = |A| = 2", font_size=20, color=YELLOW)
        amplitude_brace.put_at_tip(amplitude_text)

        self.play(Create(amplitude_line), Create(amplitude_brace), Write(amplitude_text))
        self.wait(2)

        self.play(FadeOut(amplitude_line), FadeOut(amplitude_brace), FadeOut(amplitude_text))

        # Destacar período
        periodo_start = axes.c2p(0, 0)
        periodo_end = axes.c2p(2*PI, 0)
        periodo_line = Line(periodo_start, periodo_end, color=GREEN, stroke_width=3)
        periodo_brace = Brace(periodo_line, DOWN)
        periodo_text = Text("Período = 2π/B = 2π", font_size=20, color=GREEN)
        periodo_brace.put_at_tip(periodo_text)

        self.play(Create(periodo_line), Create(periodo_brace), Write(periodo_text))
        self.wait(4)

class IdentidadesSomaDiferenca(Scene):
    def construct(self):
        titulo = Text("Fórmulas de Soma e Diferença", font_size=38, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formulas = VGroup(
            MathTex(r"\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta", font_size=28),
            MathTex(r"\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta", font_size=28),
            MathTex(r"\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}", font_size=28),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(formulas))
        self.wait(5)

        # Exemplo
        self.play(FadeOut(formulas))

        exemplo_titulo = Text("Exemplo: Calcular sen(75°)", font_size=32, color=YELLOW).shift(UP * 2.5)
        self.play(Write(exemplo_titulo))

        exemplo = VGroup(
            MathTex(r"75^\circ = 45^\circ + 30^\circ", font_size=32),
            MathTex(r"\sin(75^\circ) = \sin(45^\circ)\cos(30^\circ) + \cos(45^\circ)\sin(30^\circ)", font_size=32),
            MathTex(r"= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}", font_size=32),
            MathTex(r"= \frac{\sqrt{6} + \sqrt{2}}{4}", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.4)
        exemplo.shift(DOWN * 0.5)

        for linha in exemplo:
            self.play(Write(linha))
            self.wait(1.5)

        self.wait(3)

if __name__ == "__main__":
    pass