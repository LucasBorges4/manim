from manim import *

class MatrixAdditionScene(Scene):
    def construct(self):
        # Título
        title = Text("Soma de Matrizes no R²", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
        # Exemplo de matrizes 2x2
        matrix_a = Matrix([[1, 2], [3, 4]], color=GREEN)
        matrix_b = Matrix([[2, 1], [0, 2]], color=RED)
        matrix_c = Matrix([[3, 3], [3, 6]], color=YELLOW)
        
        matrix_a_label = Text("A =", font_size=32).next_to(matrix_a, LEFT)
        matrix_b_label = Text("B =", font_size=32).next_to(matrix_b, LEFT)
        matrix_c_label = Text("A + B =", font_size=32).next_to(matrix_c, LEFT)
        
        # Posicionar matrizes A e B
        group_a = VGroup(matrix_a_label, matrix_a).arrange(RIGHT, buff=0.2)
        group_b = VGroup(matrix_b_label, matrix_b).arrange(RIGHT, buff=0.2)
        group_c = VGroup(matrix_c_label, matrix_c).arrange(RIGHT, buff=0.2)
        
        matrices_row = VGroup(group_a, group_b, group_c).arrange(RIGHT, buff=1)
        matrices_row.shift(UP * 1.5)
        
        # Mostrar matriz A
        self.play(Create(group_a))
        self.wait(1)
        
        # Mostrar matriz B
        self.play(Create(group_b))
        self.wait(1)
        
        # Mostrar fórmula da soma
        formula = MathTex("C_{ij} = A_{ij} + B_{ij}", color=WHITE)
        formula.next_to(matrices_row, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(2)
        
        # Destacar elementos sendo somados
        for i in range(2):
            for j in range(2):
                # Destacar elemento Aij
                a_entries = matrix_a.get_entries()
                b_entries = matrix_b.get_entries()
                c_entries = matrix_c.get_entries()
                
                a_elem = a_entries[i*2 + j]
                b_elem = b_entries[i*2 + j]
                c_elem = c_entries[i*2 + j]
                
                self.play(
                    a_elem.animate.set_color(YELLOW).scale(1.5),
                    b_elem.animate.set_color(YELLOW).scale(1.5),
                    run_time=0.5
                )
                
                # Mostrar resultado em C
                c_elem.set_color(YELLOW)
                self.play(
                    FadeIn(c_elem),
                    a_elem.animate.set_color(matrix_a.get_color()).scale(1),
                    b_elem.animate.set_color(matrix_b.get_color()).scale(1),
                    run_time=0.5
                )
                
                if i < 1 or j < 1:
                    self.play(
                        c_elem.animate.set_color(matrix_c.get_color()).scale(1),
                        run_time=0.3
                    )
                self.wait(0.5)
        
        self.wait(1)
        self.play(FadeOut(formula))
        
        # Generalização
        general_title = Text("Generalização", font_size=36, color=BLUE)
        general_title.next_to(matrices_row, DOWN, buff=1.5)
        self.play(Write(general_title))
        self.wait(1)
        
        general_formula = MathTex("(A + B)_{ij} = A_{ij} + B_{ij}", color=WHITE)
        general_formula.next_to(general_title, DOWN, buff=0.5)
        self.play(Write(general_formula))
        self.wait(2)
        
        # Matriz genérica m x n
        m_label = Tex("m", color=GREEN).next_to(group_a, UP)
        n_label = Tex("n", color=GREEN).next_to(group_a, RIGHT)
        
        self.play(Write(m_label), Write(n_label))
        self.wait(1)
        
        # Exemplo com dimensões diferentes
        example_text = Text("Soma de matrizes com dimensões diferentes não é definida", 
                           font_size=28, color=RED)
        example_text.next_to(general_formula, DOWN, buff=1)
        
        self.play(Write(example_text))
        self.wait(2)
        
        # Transição para mostrar que a soma é elemento a elemento
        self.play(FadeOut(example_text))
        
        element_wise = Text("Soma elemento a elemento", font_size=32, color=YELLOW)
        element_wise.next_to(general_formula, DOWN, buff=1)
        self.play(Write(element_wise))
        self.wait(2)
        
        # Mostrar cada soma com setas
        arrows_group = VGroup()
        for i in range(2):
            for j in range(2):
                a_pos = matrix_a.get_entries()[i*2 + j].get_center()
                b_pos = matrix_b.get_entries()[i*2 + j].get_center()
                c_pos = matrix_c.get_entries()[i*2 + j].get_center()
                
                arrow_a = Arrow(a_pos, c_pos, color=GREEN, buff=0.3)
                arrow_b = Arrow(b_pos, c_pos, color=RED, buff=0.3)
                
                self.play(GrowArrow(arrow_a), GrowArrow(arrow_b), run_time=0.5)
                arrows_group.add(arrow_a, arrow_b)
        
        self.wait(2)
        
        # Limpar tudo exceto título
        self.play(
            FadeOut(matrices_row),
            FadeOut(general_title),
            FadeOut(general_formula),
            FadeOut(element_wise),
            FadeOut(arrows_group),
            FadeOut(m_label),
            FadeOut(n_label),
            FadeOut(title)
        )
        
        # Conclusão
        conclusion = MathTex("A + B \\in \\mathbb{R}^{m \\times n}", color=BLUE, font_size=60)
        self.play(Write(conclusion))
        self.wait(3)
        
        self.play(FadeOut(conclusion))


class VectorRepresentation(Scene):
    def construct(self):
        # Mostrar matrizes como transformações de vetores no R²
        title = Text("Matrizes como Transformações no R²", font_size=42, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        
        # Plano cartesiano
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": GREY, "stroke_width": 2}
        )
        self.play(Create(plane))
        self.wait(1)
        
        # Matriz exemplo
        matrix_example = Matrix([[2, 0], [0, 2]], color=GREEN)
        matrix_example_label = Text("A = [[2, 0], [0, 2]]", font_size=28)
        matrix_group = VGroup(matrix_example_label, matrix_example).arrange(DOWN, buff=0.3)
        matrix_group.to_corner(UR)
        
        self.play(Create(matrix_group))
        self.wait(1)
        
        # Vetores base
        i_hat = Arrow(ORIGIN, RIGHT*2, color=RED, buff=0)
        j_hat = Arrow(ORIGIN, UP*2, color=RED, buff=0)
        
        i_label = MathTex("\\hat{i}", color=RED).next_to(i_hat, RIGHT, buff=0.1)
        j_label = MathTex("\\hat{j}", color=RED).next_to(j_hat, UP, buff=0.1)
        
        self.play(Create(i_hat), Create(j_hat))
        self.play(Write(i_label), Write(j_label))
        self.wait(1)
        
        # Explicar que as colunas da matriz são as imagens das bases
        explanation = Text("Colunas de A = transformação das bases", font_size=24, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # Mostrar como as colunas formam a matriz
        col1 = matrix_example.get_columns()[0]
        col2 = matrix_example.get_columns()[1]
        
        col1_label = Text("Coluna 1", font_size=20, color=GREEN).next_to(col1, UP, buff=0.5)
        col2_label = Text("Coluna 2", font_size=20, color=GREEN).next_to(col2, UP, buff=0.5)
        
        self.play(Indicate(col1), Write(col1_label))
        self.wait(1)
        self.play(Indicate(col2), Write(col2_label))
        self.wait(1)
        
        self.play(FadeOut(col1_label), FadeOut(col2_label))
        
        # Generalizar para qualquer matriz
        general_matrix = Matrix([["a", "b"], ["c", "d"]], element_to_mobject_config={"font_size": 32}).set_color(GREEN)
        general_matrix.next_to(matrix_group, DOWN, buff=0.5)
        
        self.play(FadeOut(matrix_group), FadeOut(i_label), FadeOut(j_label))
        self.play(Create(general_matrix))
        
        general_label = Text("Matriz genérica no R²", font_size=24, color=YELLOW)
        general_label.next_to(general_matrix, DOWN, buff=0.3)
        self.play(Write(general_label))
        self.wait(2)
        
        self.play(FadeOut(general_label), FadeOut(general_matrix), FadeOut(title))
        
        # Conclusão final
        final = Text("A soma de matrizes é definida elemento a elemento\npara matrizes de mesma dimensão", 
                    font_size=36, color=BLUE).center()
        self.play(Write(final))
        self.wait(3)
        self.play(FadeOut(final))


if __name__ == "__main__":
    pass