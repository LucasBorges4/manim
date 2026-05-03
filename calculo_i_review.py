from manim import *
import numpy as np

class CalculoIReview(Scene):
    def construct(self):
        # Título inicial rápido
        title = Text("Cálculo I - Revisão Completa", font_size=56, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # 1. Limites
        self.show_section("1. Limites", color=YELLOW)
        limite = MathTex(
            r"\lim_{x \to a} f(x) = L",
            font_size=60
        )
        self.play(Write(limite))
        self.wait(1)
        
        exemplo_lim = MathTex(
            r"\lim_{x \to 2} (x^2 - 1) = 3",
            font_size=48,
            color=GREEN
        ).next_to(limite, DOWN, buff=0.5)
        self.play(Write(exemplo_lim))
        self.wait(1.5)
        self.play(FadeOut(limite, exemplo_lim))

        # 2. Continuidade
        self.show_section("2. Continuidade", color=RED)
        cont = MathTex(
            r"\lim_{x \to a} f(x) = f(a)",
            font_size=60
        )
        self.play(Write(cont))
        self.wait(1)
        
        conds = VGroup(
            Text("1. f(a) existe", font_size=28),
            Text("2. Limite existe", font_size=28),
            Text("3. São iguais", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT)
        conds.next_to(cont, DOWN, buff=0.5)
        self.play(Write(conds))
        self.wait(1.5)
        self.play(FadeOut(cont, conds))

        # 3. Derivada
        self.show_section("3. Derivada", color=BLUE)
        deriv = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=50
        )
        self.play(Write(deriv))
        self.wait(1)
        
        regras = VGroup(
            MathTex(r"(x^n)' = n \cdot x^{n-1}", font_size=32),
            MathTex(r"(e^x)' = e^x", font_size=32),
            MathTex(r"(\ln x)' = \frac{1}{x}", font_size=32),
        ).arrange(RIGHT, buff=0.5)
        regras.next_to(deriv, DOWN, buff=0.5)
        self.play(Write(regras))
        self.wait(1.5)
        self.play(FadeOut(deriv, regras))

        # 4. Regra da cadeia
        self.show_section("4. Regra da Cadeia", color=YELLOW)
        cadeia = MathTex(
            r"\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)",
            font_size=56
        )
        self.play(Write(cadeia))
        self.wait(2)
        self.play(FadeOut(cadeia))

        # 5. Derivadas implícitas
        self.show_section("5. Derivada implícita", color=ORANGE)
        implicit = MathTex(
            r"x^2 + y^2 = 25 \Rightarrow 2x + 2y \cdot y' = 0",
            font_size=48
        )
        self.play(Write(implicit))
        self.wait(1.5)
        result = MathTex(
            r"y' = -\frac{x}{y}",
            font_size=48,
            color=GREEN
        ).next_to(implicit, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(1.5)
        self.play(FadeOut(implicit, result))

        # 6. Máximos e Mínimos
        self.show_section("6. Extremos", color=RED)
        extremos = VGroup(
            MathTex(r"f'(c) = 0 \text{ ou } f'(c) \text{ não existe}", font_size=42),
            MathTex(r"\text{Teste da 1ª derivada}", font_size=36),
            MathTex(r"\text{Teste da 2ª derivada: } f''(c) > 0 \to \text{min}", font_size=36),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(extremos))
        self.wait(2)
        self.play(FadeOut(extremos))

        # 7. Integral
        self.show_section("7. Integral", color=GREEN)
        integral = MathTex(
            r"\int f(x)dx = F(x) + C",
            font_size=60
        )
        self.play(Write(integral))
        self.wait(1)
        
        formulas_int = VGroup(
            MathTex(r"\int x^n dx = \frac{x^{n+1}}{n+1} + C", font_size=32),
            MathTex(r"\int e^x dx = e^x + C", font_size=32),
            MathTex(r"\int \frac{1}{x} dx = \ln|x| + C", font_size=32),
        ).arrange(RIGHT, buff=0.5)
        formulas_int.next_to(integral, DOWN, buff=0.5)
        self.play(Write(formulas_int))
        self.wait(1.5)
        self.play(FadeOut(integral, formulas_int))

        # 8. Integrais definidas
        self.show_section("8. Integral Definida", color=BLUE)
        int_def = MathTex(
            r"\int_a^b f(x)dx = F(b) - F(a)",
            font_size=60
        )
        self.play(Write(int_def))
        self.wait(1)
        
        area_vis = Text("Área sob a curva", font_size=36, color=YELLOW).next_to(int_def, DOWN)
        self.play(Write(area_vis))
        self.wait(2)
        self.play(FadeOut(int_def, area_vis))

        # 9. Teorema Fundamental do Cálculo
        self.show_section("9. TFC", color=YELLOW)
        tfc = MathTex(
            r"\frac{d}{dx}\int_a^x f(t)dt = f(x)",
            font_size=60
        )
        self.play(Write(tfc))
        self.wait(2)
        self.play(FadeOut(tfc))

        # 10. Métodos de Integração
        self.show_section("10. Técnicas de Integração", color=ORANGE)
        tecnicas = VGroup(
            Text("• Substituição (u-du)", font_size=32),
            Text("• Partes (uv - ∫vdu)", font_size=32),
            Text("• Frações parciais", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(tecnicas))
        self.wait(2)
        self.play(FadeOut(tecnicas))

        # 11. Aplicações de Integrais
        self.show_section("11. Aplicações", color=RED)
        aplicacoes = VGroup(
            Text("Área entre curvas", font_size=32),
            Text("Volume (discos/eixos)", font_size=32),
            Text("Comprimento de curva", font_size=32),
            Text("Trabalho (F·dx)", font_size=32),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.5, 0.3))
        self.play(Write(aplicacoes))
        self.wait(2)
        self.play(FadeOut(aplicacoes))

        # 12. Limites importantes
        self.show_section("12. Limites Clássicos", color=GREEN)
        limites = VGroup(
            MathTex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1", font_size=40),
            MathTex(r"\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e", font_size=40),
            MathTex(r"\lim_{x \to 0} \frac{e^x - 1}{x} = 1", font_size=40),
        ).arrange(DOWN, buff=0.5)
        self.play(Write(limites))
        self.wait(2)
        self.play(FadeOut(limites))

        # 13. Regra de L'Hopital
        self.show_section("13. L'Hôpital", color=PURPLE)
        lhopital = MathTex(
            r"\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ ou } \frac{\infty}{\infty}",
            font_size=48
        )
        self.play(Write(lhopital))
        self.wait(1)
        
        regra = MathTex(
            r"\Rightarrow \lim_{x \to a} \frac{f'(x)}{g'(x)}",
            font_size=48,
            color=YELLOW
        ).next_to(lhopital, DOWN)
        self.play(Write(regra))
        self.wait(1.5)
        self.play(FadeOut(lhopital, regra))

        # 14. Funções Inversas
        self.show_section("14. Funções Inversas", color=TEAL)
        inversa = MathTex(
            r"(f^{-1})'(y) = \frac{1}{f'(x)}",
            font_size=56
        )
        self.play(Write(inversa))
        self.wait(2)
        self.play(FadeOut(inversa))

        # 15. Crescimento e Decrescimento
        self.show_section("15. Crescimento/Decrescimento", color=ORANGE)
        cresc = VGroup(
            MathTex(r"f'(x) > 0 \to \text{Crescente}", font_size=42, color=GREEN),
            MathTex(r"f'(x) < 0 \to \text{Decrescente}", font_size=42, color=RED),
            MathTex(r"f'(x) = 0 \to \text{Crítico (possível extremo)}", font_size=42, color=YELLOW),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(cresc))
        self.wait(2)
        self.play(FadeOut(cresc))

        # Final - Todos os tópicos rapidamente
        topics = VGroup(
            Text("Limites", font_size=28),
            Text("Continuidade", font_size=28),
            Text("Derivadas", font_size=28),
            Text("Integrais", font_size=28),
            Text("Aplicações", font_size=28),
        ).arrange(RIGHT, buff=0.4)
        
        self.play(Write(topics))
        self.wait(0.5)
        self.play(FadeOut(topics))

        # Mensagem final
        final = Text("Bons estudos!\nPratique muito!", font_size=60, color=BLUE, line_spacing=1.5)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))
        
    def show_section(self, text, color=WHITE):
        """Exibe o título da seção rapidamente"""
        section = Text(text, font_size=48, color=color)
        self.play(Write(section))
        self.wait(0.3)
        self.play(FadeOut(section))

if __name__ == "__main__":
    pass