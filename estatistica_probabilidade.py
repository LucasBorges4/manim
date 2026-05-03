from manim import *

class MediaMedianaModa(Scene):
    def construct(self):
        titulo = Text("Medidas de Tendência Central", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        dados = VGroup(
            Text("Dados: 3, 5, 7, 8, 9, 10, 10, 12", font_size=28),
        )
        self.play(Write(dados))
        self.wait(2)

        # Média
        media_titulo = Text("Média", font_size=32, color=YELLOW).shift(UP * 1.5 + LEFT * 3)
        media_calc = MathTex(r"\bar{x} = \frac{\sum x_i}{n}", font_size=28)
        media_num = MathTex(r"\bar{x} = \frac{3+5+7+8+9+10+10+12}{8} = \frac{64}{8} = 8", font_size=28)

        media_group = VGroup(media_titulo, media_calc, media_num).arrange(DOWN, buff=0.3)
        self.play(Write(media_group))
        self.wait(2)

        # Mediana
        mediana_titulo = Text("Mediana", font_size=32, color=GREEN).shift(UP * 1.5 + RIGHT * 3)
        mediana_desc = Text("Valor central (ordenado)", font_size=24)
        mediana_num = MathTex(r"Me = \frac{8 + 9}{2} = 8.5", font_size=28)

        mediana_group = VGroup(mediana_titulo, mediana_desc, mediana_num).arrange(DOWN, buff=0.3)
        self.play(Write(mediana_group))
        self.wait(2)

        # Moda
        self.play(FadeOut(media_group), FadeOut(mediana_group))

        moda_titulo = Text("Moda", font_size=32, color=RED)
        moda_desc = Text("Valor que mais aparece", font_size=24)
        moda_num = Text("Mo = 10 (aparece 2 vezes)", font_size=28, color=RED)

        moda_group = VGroup(moda_titulo, moda_desc, moda_num).arrange(DOWN, buff=0.3)
        self.play(Write(moda_group))
        self.wait(4)

class VarianciaDesvioPadrao(Scene):
    def construct(self):
        titulo = Text("Variância e Desvio Padrão", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Dados e média
        dados_txt = Text("Dados: 2, 4, 4, 4, 5, 5, 7, 9", font_size=28).shift(UP * 2.5)
        self.play(Write(dados_txt))

        media_txt = Text("Média = 5", font_size=28, color=YELLOW).next_to(dados_txt, DOWN)
        self.play(Write(media_txt))
        self.wait(2)

        # Variância
        var_formula = MathTex(
            r"\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}",
            font_size=36,
            color=GREEN
        )
        var_formula.shift(UP * 0.5)
        self.play(Write(var_formula))
        self.wait(2)

        # Cálculo passo a passo
        calculo = VGroup(
            MathTex(r"(2-5)^2 = 9", font_size=24),
            MathTex(r"(4-5)^2 = 1", font_size=24),
            MathTex(r"(4-5)^2 = 1", font_size=24),
            MathTex(r"(4-5)^2 = 1", font_size=24),
            MathTeX(r"(5-5)^2 = 0", font_size=24),
            MathTex(r"(5-5)^2 = 0", font_size=24),
            MathTex(r"(7-5)^2 = 4", font_size=24),
            MathTex(r"(9-5)^2 = 16", font_size=24),
        ).arrange(DOWN, buff=0.2)
        calculo.shift(DOWN * 1.5)
        calculo.align_to(LEFT * 3)

        soma = MathTex(r"\sum = 32", font_size=28, color=YELLOW).next_to(calculo, RIGHT, buff=1)
        resultado = MathTex(r"\sigma^2 = \frac{32}{8} = 4", font_size=32, color=GREEN).next_to(soma, DOWN, buff=0.5)

        self.play(Write(calculo))
        self.wait(3)
        self.play(Write(soma), Write(resultado))
        self.wait(3)

        # Desvio padrão
        self.play(FadeOut(var_formula), FadeOut(calculo), FadeOut(soma), FadeOut(resultado))

        dp_formula = MathTex(r"\sigma = \sqrt{\sigma^2}", font_size=40, color=YELLOW)
        dp_calc = MathTex(r"\sigma = \sqrt{4} = 2", font_size=40, color=YELLOW)
        dp_group = VGroup(dp_formula, dp_calc).arrange(DOWN, buff=0.5)

        self.play(Write(dp_group))
        self.wait(4)

class ProbabilidadeBasica(Scene):
    def construct(self):
        titulo = Text("Probabilidade Básica", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(r"P(A) = \frac{\text{ casos favoráveis}}{\text{ casos possíveis}}", font_size=40)
        self.play(Write(formula))
        self.wait(3)
        self.play(FadeOut(formula))

        # Exemplo: dado
        exemplo_titulo = Text("Exemplo: Lancar um dado", font_size=32, color=YELLOW).shift(UP * 2.5)
        self.play(Write(exemplo_titulo))

        # Desenhar dado
        dado = Square(side_length=1.2, color=WHITE, stroke_width=3)
        ponto = Dot(ORIGIN, radius=0.08, color=WHITE)

        self.play(Create(dado))
        self.wait(1)

        # Valor 3
        texto_tres = Text("3", font_size=48, color=YELLOW).move_to(dado.get_center())
        self.play(Write(texto_tres))
        self.wait(1)

        calc = VGroup(
            MathTex(r"P(\text{obter 3}) = \frac{1}{6}", font_size=36),
            MathTex(r"P(\text{obter ímpar}) = \frac{3}{6} = \frac{1}{2}", font_size=36),
            MathTex(r"P(\text{obter } \leq 4) = \frac{4}{6} = \frac{2}{3}", font_size=36),
        ).arrange(DOWN, buff=0.5)
        calc.shift(DOWN * 1.5)

        for linha in calc:
            self.play(Write(linha))
            self.wait(1.5)

        self.wait(3)

class OperacoesComProbabilidades(Scene):
    def construct(self):
        titulo = Text("Operações com Probabilidades", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        operacoes = VGroup(
            VGroup(
                Text("União (A ∪ B)", font_size=28),
                MathTex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Intersecção (A ∩ B)", font_size=28),
                MathTex(r"P(A \cap B) = P(A) \cdot P(B|A)", font_size=28),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("Probabilidade Condicional", font_size=28),
                MathTex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}", font_size=28),
            ).arrange(DOWN, buff=0.2),
        ).arrange(DOWN, buff=0.8)

        self.play(Write(operacoes))
        self.wait(5)

class EventosIndependentes(Scene):
    def construct(self):
        titulo = Text("Eventos Independentes", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        definicao = Text("Dois eventos são independentes\nse a ocorrência de um não afeta o outro", font_size=28)
        definicao.shift(UP * 2)
        self.play(Write(definicao))
        self.wait(3)

        formula = MathTex(r"P(A \cap B) = P(A) \cdot P(B)", font_size=44, color=GREEN)
        self.play(Write(formula))
        self.wait(2)

        # Exemplo com moeda
        exemplo_titulo = Text("Exemplo: Lançar moeda 2 vezes", font_size=28, color=YELLOW).shift(DOWN * 2)
        self.play(Write(exemplo_titulo))

        exemplo_calc = VGroup(
            MathTex(r"P(\text{ cara}) = \frac{1}{2}", font_size=28),
            MathTex(r"P(\text{ duas caras}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.5)
        exemplo_calc.next_to(exemplo_titulo, DOWN, buff=0.5)

        self.play(Write(exemplo_calc))
        self.wait(4)

class DistribuicaoBinomial(Scene):
    def construct(self):
        titulo = Text("Distribuição Binomial", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        formula = MathTex(
            r"P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}",
            font_size=40,
            color=YELLOW
        )
        self.play(Write(formula))
        self.wait(2)

        explicacao = VGroup(
            Text("n = número de ensaios", font_size=24),
            Text("k = número de sucessos", font_size=24),
            Text("p = probabilidade de sucesso", font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explicacao.to_corner(DL)
        self.play(Write(explicacao))
        self.wait(3)

        # Exemplo: 3 lançamentos de moeda
        self.play(FadeOut(formula), FadeOut(explicacao))

        exemplo_titulo = Text("Exemplo: 3 lançamentos, P(sair cara) = 0.5", font_size=28, color=GREEN).shift(UP * 2.5)
        self.play(Write(exemplo_titulo))

        resultado = MathTex(
            r"P(X=2) = {3 \choose 2} \cdot 0.5^2 \cdot 0.5^1 = 3 \cdot 0.25 \cdot 0.5 = 0.375",
            font_size=32
        ).shift(DOWN * 1)
        self.play(Write(resultado))
        self.wait(4)

class DiagramaDeVenn(Scene):
    def construct(self):
        titulo = Text("Diagrama de Venn", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Círculos
        circle_a = Circle(radius=1.2, color=BLUE, fill_opacity=0.3).shift(LEFT * 0.8)
        circle_b = Circle(radius=1.2, color=RED, fill_opacity=0.3).shift(RIGHT * 0.8)

        label_a = Text("A", font_size=32, color=BLUE).next_to(circle_a, UP)
        label_b = Text("B", font_size=32, color=RED).next_to(circle_b, UP)

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(2)

        # Operações
        operacoes = VGroup(
            VGroup(
                Text("A ∪ B", font_size=28),
                Text("(União)", font_size=20),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("A ∩ B", font_size=28),
                Text("(Interseção)", font_size=20),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("A'", font_size=28),
                Text("(Complementar)", font_size=20),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.5)
        operacoes.shift(DOWN * 2.5)

        for op in operacoes:
            self.play(Write(op))
            self.wait(0.5)

        self.wait(2)

        # Destacar interseção
        intersection = Intersection(circle_a, circle_b, color=PURPLE, fill_opacity=0.5)
        self.play(FadeIn(intersection))
        label_i = Text("A ∩ B", font_size=24, color=PURPLE).move_to(intersection.get_center())
        self.play(Write(label_i))
        self.wait(3)

class MedidasPosicao(Scene):
    def construct(self):
        titulo = Text("Medidas de Posição: Quartis", font_size=42, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        dados = [3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18]
        dados_txt = Text(f"Dados ordenados: {', '.join(map(str, dados))}", font_size=22)
        dados_txt.shift(UP * 3)
        self.play(Write(dados_txt))
        self.wait(2)

        # Q1, Q2, Q3
        n = len(dados)
        q1_idx = n // 4
        mediana_idx = n // 2
        q3_idx = 3 * n // 4

        q1_val = dados[q1_idx]
        q2_val = dados[mediana_idx]
        q3_val = dados[q3_idx]

        quartis = VGroup(
            MathTex(f"Q_1 = {q1_val}", font_size=32, color=YELLOW),
            MathTex(f"Q_2 \text{(Mediana)} = {q2_val}", font_size=32, color=GREEN),
            MathTex(rf"Q_3 = {q3_val}", font_size=32, color=RED),
        ).arrange(DOWN, buff=0.5)

        quartis.shift(DOWN * 1.5)
        self.play(Write(quartis))
        self.wait(2)

        # AIQ
        aiq_txt = MathTex(f"AIQ = Q_3 - Q_1 = {q3_val} - {q1_val} = {q3_val - q1_val}", font_size=32, color=PURPLE)
        aiq_txt.next_to(quartis, DOWN, buff=0.8)
        self.play(Write(aiq_txt))
        self.wait(4)

        explicacao = Text(
            "AIQ contém 50% dos dados centrais",
            font_size=24,
            color=PURPLE
        ).next_to(aiq_txt, DOWN, buff=0.5)
        self.play(Write(explicacao))
        self.wait(4)

class CorrelacaoRegressao(Scene):
    def construct(self):
        titulo = Text("Correlação e Regressão Linear", font_size=38, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Equação da reta
        reta_titulo = Text("Reta de Regressão", font_size=32, color=YELLOW).shift(UP * 2.5)
        self.play(Write(reta_titulo))

        formula = MathTex(r"y = a + bx", font_size=40)
        self.play(Write(formula))
        self.wait(2)

        b_formula = MathTex(
            r"b = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}",
            font_size=30
        )
        a_formula = MathTex(
            r"a = \bar{y} - b\bar{x}",
            font_size=30
        )
        formulas = VGroup(b_formula, a_formula).arrange(DOWN, buff=0.5)
        formulas.shift(DOWN * 1)
        self.play(Write(formulas))
        self.wait(4)

        # Coeficiente de correlação
        self.play(FadeOut(formula), FadeOut(formulas))

        correl_titulo = Text("Coeficiente de Correlação (r)", font_size=32, color=GREEN).shift(UP * 2)
        self.play(Write(correl_titulo))

        r_formula = MathTex(
            r"r = \frac{n\sum xy - \sum x \sum y}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}",
            font_size=28,
            color=GREEN
        )
        self.play(Write(r_formula))
        self.wait(2)

        r_interpretacao = VGroup(
            Text("r = 1 → Correlação positiva perfeita", font_size=24, color=BLUE),
            Text("r = -1 → Correlação negativa perfeita", font_size=24, color=RED),
            Text("r ≈ 0 → Sem correlação linear", font_size=24, color=GRAY),
        ).arrange(DOWN, buff=0.3)
        r_interpretacao.shift(DOWN * 2)
        self.play(Write(r_interpretacao))
        self.wait(5)

if __name__ == "__main__":
    pass