from manim import *

class NumerosPrimos(Scene):
    def construct(self):
        titulo = Text("Números Primos", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        definicao = Text("Um número primo é aquele\nque só é divisível por 1 e por ele mesmo", font_size=32, color=WHITE)
        self.play(Write(definicao))
        self.wait(3)
        self.play(FadeOut(definicao))

        exemplos = VGroup(
            Text("2 ✓", color=GREEN),
            Text("3 ✓", color=GREEN),
            Text("5 ✓", color=GREEN),
            Text("7 ✓", color=GREEN),
            Text("11 ✓", color=GREEN),
        ).arrange(RIGHT, buff=0.5)

        contra = VGroup(
            Text("4 ✗", color=RED),
            Text("6 ✗", color=RED),
            Text("8 ✗", color=RED),
            Text("9 ✗", color=RED),
            Text("10 ✗", color=RED),
        ).arrange(RIGHT, buff=0.5)

        grupo = VGroup(exemplos, contra).arrange(DOWN, buff=1)
        self.play(Create(grupo))
        self.wait(3)

class CrivoDeEratostenes(Scene):
    def construct(self):
        titulo = Text("Crivo de Eratóstenes", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        numeros = VGroup(*[Text(str(i), font_size=24) for i in range(2, 31)])
        numeros.arrange_in_grid(rows=5, cols=6, buff=0.3)

        self.play(Create(numeros))
        self.wait(1)

        for primo in [2, 3, 5, 7]:
            idx = primo - 2
            circ = Circle(radius=0.3, color=YELLOW, fill_opacity=0).move_to(numeros[idx].get_center())
            self.play(Create(circ), numeros[idx].animate.set_color(YELLOW))
            self.wait(0.5)

            for i in range(primo * 2, 31, primo):
                idx_eliminar = i - 2
                self.play(
                    numeros[idx_eliminar].animate.set_color(RED).set_opacity(0.3),
                    run_time=0.2
                )

        result = Text("Primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29", font_size=28, color=GREEN)
        result.next_to(numeros, DOWN)
        self.play(Write(result))
        self.wait(3)

class MDC_MMC(Scene):
    def construct(self):
        titulo = Text("MDC e MMC", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        exemplo = Text("Exemplo: 12 e 18", font_size=36, color=YELLOW).shift(UP * 2)
        self.play(Write(exemplo))
        self.wait(1)

        fat12 = Text("12 = 2² × 3", font_size=28, color=GREEN).shift(LEFT * 3)
        fat18 = Text("18 = 2 × 3²", font_size=28, color=BLUE).shift(RIGHT * 3)
        self.play(Write(fat12), Write(fat18))
        self.wait(2)

        mdc_text = Text("MDC = 2 × 3 = 6", font_size=32, color=RED).shift(DOWN * 1.5)
        mmc_text = Text("MMC = 2² × 3² = 36", font_size=32, color=PURPLE).shift(DOWN * 3)
        self.play(Write(mdc_text), Write(mmc_text))
        self.wait(3)

class RegrasDeSigno(Scene):
    def construct(self):
        titulo = Text("Regras de Sinais", font_size=48, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        grid = VGroup()
        for i, (op, res, cor) in enumerate([
            ("(+) × (+) =", "(+)", GREEN),
            ("(+) × (-) =", "(-)", RED),
            ("(-) × (+) =", "(-)", RED),
            ("(-) × (-) =", "(+)", GREEN),
        ]):
            line = VGroup(
                Text(op, font_size=28),
                Text(res, font_size=32, color=cor)
            ).arrange(RIGHT, buff=0.5)
            line.shift(UP * (1.5 - i * 0.8))
            grid.add(line)

        self.play(Create(grid))
        self.wait(3)

if __name__ == "__main__":
    pass