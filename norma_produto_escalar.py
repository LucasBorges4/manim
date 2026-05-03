from manim import *

class NormAndDotProductScene(Scene):
    def construct(self):
        # Título
        title = Text("Norma e Produto Escalar", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
        # Introdução ao produto escalar
        intro_title = Text("Produto Escalar (Produto Interno)", font_size=36, color=GREEN)
        intro_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_title))
        self.wait(1)
        
        # Definição matemática
        definition = MathTex(
            r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos\theta",
            font_size=36
        )
        definition.next_to(intro_title, DOWN, buff=0.8)
        self.play(Write(definition))
        self.wait(2)
        
        # Fórmula para R²
        formula_r2 = MathTex(
            r"\vec{a} = (a_1, a_2),\ \vec{b} = (b_1, b_2)",
            r"\\\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2",
            font_size=32
        )
        formula_r2.next_to(definition, DOWN, buff=0.8)
        self.play(Write(formula_r2))
        self.wait(2)
        
        # Exemplo numérico
        example_title = Text("Exemplo:", font_size=32, color=YELLOW)
        example_title.next_to(formula_r2, DOWN, buff=0.8)
        self.play(Write(example_title))
        
        example = MathTex(
            r"\vec{a} = (1, 2),\ \vec{b} = (3, 1)",
            r"\\\vec{a} \cdot \vec{b} = 1 \\cdot 3 + 2 \\cdot 1 = 3 + 2 = 5",
            font_size=32
        )
        example.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(2)
        
        # Limpar parte do produto escalar
        self.play(
            FadeOut(intro_title),
            FadeOut(definition),
            FadeOut(formula_r2),
            FadeOut(example_title),
            FadeOut(example)
        )
        
        # Propriedades do produto escalar
        props_title = Text("Propriedades do Produto Escalar", font_size=36, color=GREEN)
        props_title.next_to(title, DOWN, buff=0.8)
        self.play(Write(props_title))
        self.wait(1)
        
        # Lista de propriedades
        props = VGroup(
            MathTex(r"1.\ \vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}\ \text{(Comutatividade)}", font_size=28),
            MathTex(r"2.\ (\vec{a} + \vec{b}) \cdot \vec{c} = \vec{a} \cdot \vec{c} + \vec{b} \cdot \vec{c}\ \text{(Distributividade)}", font_size=28),
            MathTex(r"3.\ (k\vec{a}) \cdot \vec{b} = k(\vec{a} \cdot \vec{b})\ \text{(Associatividade\ com\ escalar)}", font_size=28),
            MathTex(r"4.\ \vec{a} \cdot \vec{a} = |\vec{a}|^2 \geq 0\ \text{(Positividade)}", font_size=28),
            MathTex(r"5.\ \vec{a} \cdot \vec{a} = 0 \Leftrightarrow \vec{a} = \vec{0}\ \text{(Definitividade)}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        props.next_to(props_title, DOWN, buff=0.8)
        
        for i, prop in enumerate(props):
            self.play(Write(prop))
            self.wait(1.5)
        
        self.wait(2)
        
        # Limpar propriedades
        self.play(
            FadeOut(props_title),
            FadeOut(props)
        )
        
        # Introduzir norma
        norm_title = Text("Norma (Magnitude) de um Vetor", font_size=36, color=YELLOW)
        norm_title.next_to(title, DOWN, buff=0.8)
        self.play(Write(norm_title))
        self.wait(1)
        
        # Definição de norma
        norm_def = MathTex(
            r"|\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}}",
            r"\\= \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}",
            font_size=32
        )
        norm_def.next_to(norm_title, DOWN, buff=0.8)
        self.play(Write(norm_def))
        self.wait(2)
        
        # Exemplo de norma no R²
        norm_example_title = Text("Exemplo no R²:", font_size=32, color=GREEN)
        norm_example_title.next_to(norm_def, DOWN, buff=0.8)
        self.play(Write(norm_example_title))
        
        norm_example = MathTex(
            r"\vec{v} = (3, 4)",
            r"\\|\vec{v}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5",
            font_size=32
        )
        norm_example.next_to(norm_example_title, DOWN, buff=0.5)
        self.play(Write(norm_example))
        self.wait(2)
        
        # Visualização geométrica
        self.play(
            FadeOut(norm_title),
            FadeOut(norm_def),
            FadeOut(norm_example_title),
            FadeOut(norm_example)
        )
        
        # Plano cartesiano para mostrar norma
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 2}
        ).scale(1.2)
        plane.shift(DOWN * 1)
        
        self.play(Create(plane))
        self.wait(1)
        
        # Vetor (3,4)
        vector = Arrow(ORIGIN, RIGHT*3 + UP*4, color=RED, buff=0)
        vector_label = MathTex(r"\vec{v} = (3,4)", font_size=32, color=RED).next_to(vector.get_end(), UR, buff=0.1)
        
        self.play(Create(vector))
        self.play(Write(vector_label))
        self.wait(1)
        
        # Mostrar projeções nos eixos
        proj_x = Arrow(ORIGIN, RIGHT*3, color=GREEN, buff=0)
        proj_y = Arrow(RIGHT*3, RIGHT*3 + UP*4, color=BLUE, buff=0)
        
        proj_x_label = MathTex("3", font_size=28, color=GREEN).next_to(proj_x, DOWN, buff=0.1)
        proj_y_label = MathTex("4", font_size=28, color=BLUE).next_to(proj_y, RIGHT, buff=0.1)
        
        self.play(Create(proj_x), Write(proj_x_label))
        self.wait(0.5)
        self.play(Create(proj_y), Write(proj_y_label))
        self.wait(1)
        
        # Mostrar fórmula de Pitágoras
        pythagoras = MathTex(r"|\vec{v}|^2 = 3^2 + 4^2", font_size=36, color=YELLOW)
        pythagoras.to_corner(UR)
        self.play(Write(pythagoras))
        self.wait(1)
        
        pythagoras2 = MathTex(r"|\vec{v}|^2 = 9 + 16 = 25", font_size=36, color=YELLOW)
        pythagoras2.next_to(pythagoras, DOWN, buff=0.3)
        self.play(Write(pythagoras2))
        self.wait(1)
        
        pythagoras3 = MathTex(r"|\vec{v}| = 5", font_size=36, color=YELLOW)
        pythagoras3.next_to(pythagoras2, DOWN, buff=0.3)
        self.play(Write(pythagoras3))
        self.wait(2)
        
        # Limpar visualização
        self.play(
            FadeOut(plane),
            FadeOut(vector),
            FadeOut(vector_label),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(proj_x_label),
            FadeOut(proj_y_label),
            FadeOut(pythagoras),
            FadeOut(pythagoras2),
            FadeOut(pythagoras3)
        )
        
        # Conexão entre norma e produto escalar
        connection_title = Text("Conexão entre Produto Escalar e Norma", font_size=36, color=BLUE)
        connection_title.next_to(title, DOWN, buff=0.8)
        self.play(Write(connection_title))
        self.wait(1)
        
        connection = MathTex(
            r"|\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}}",
            r"\\\text{A norma é a raiz quadrada do produto escalar do vetor consigo mesmo}",
            font_size=32
        )
        connection.next_to(connection_title, DOWN, buff=0.8)
        self.play(Write(connection))
        self.wait(3)
        
        # Conclusão
        self.play(
            FadeOut(connection_title),
            FadeOut(connection)
        )
        
        conclusion = VGroup(
            Text("Resumo:", font_size=36, color=GREEN),
            BulletedList(
                "Produto escalar: operação que retorna um escalar",
                "Norma: medida do comprimento de um vetor",
                "Norma = √(produto escalar do vetor consigo mesmo)",
                font_size=28
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        self.play(FadeOut(conclusion))
        
        final = Text("Obrigado!", font_size=48, color=BLUE)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))


class AngleBetweenVectors(Scene):
    def construct(self):
        # Mostrar como calcular ângulo usando produto escalar
        title = Text("Ângulo entre Vetores", font_size=42, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
        # Fórmula do ângulo
        formula = MathTex(
            r"\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| |\vec{b}|}",
            font_size=48,
            color=YELLOW
        )
        self.play(Write(formula))
        self.wait(2)
        
        # Exemplo numérico
        example_title = Text("Exemplo:", font_size=32, color=GREEN)
        example_title.next_to(formula, DOWN, buff=1)
        self.play(Write(example_title))
        
        example = MathTex(
            r"\vec{a} = (1, 0),\ \vec{b} = (0, 1)",
            r"\\\vec{a} \cdot \vec{b} = 1 \\cdot 0 + 0 \\cdot 1 = 0",
            r"\\|\vec{a}| = 1,\ |\vec{b}| = 1",
            r"\\\cos\theta = \frac{0}{1 \\cdot 1} = 0",
            r"\\\theta = 90^\circ",
            font_size=28
        )
        example.next_to(example_title, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(3)
        
        self.play(FadeOut(title), FadeOut(formula), FadeOut(example_title), FadeOut(example))
        
        # Visualização dos vetores perpendiculares
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 2}
        ).scale(1.5)
        
        self.play(Create(plane))
        
        a_vec = Arrow(ORIGIN, RIGHT*2, color=RED, buff=0)
        b_vec = Arrow(ORIGIN, UP*2, color=BLUE, buff=0)
        
        a_label = MathTex(r"\vec{a}", font_size=28, color=RED).next_to(a_vec.get_end(), RIGHT, buff=0.1)
        b_label = MathTex(r"\vec{b}", font_size=28, color=BLUE).next_to(b_vec.get_end(), UP, buff=0.1)
        
        self.play(Create(a_vec), Write(a_label))
        self.play(Create(b_vec), Write(b_label))
        self.wait(1)
        
        # Mostrar ângulo reto
        right_angle = RightAngle(a_vec, b_vec, length=0.5, color=YELLOW)
        angle_90 = MathTex(r"90^\circ", font_size=32, color=YELLOW).move_to(UR*0.8)
        
        self.play(Create(right_angle), Write(angle_90))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))


if __name__ == "__main__":
    pass