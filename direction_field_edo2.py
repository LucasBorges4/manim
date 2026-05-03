from manim import *
import numpy as np

class DirectionFieldEDO2(Scene):
    def construct(self):
        # Configuração dos eixos
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
            x_length=10,
            y_length=6
        )
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Título da equação
        equation = MathTex(r"y' = -2 + x - y").to_edge(UP)
        
        # Parâmetros do campo
        x_min, x_max = -5, 5
        y_min, y_max = -3, 3
        density = 0.5  # espaçamento entre as setas
        
        # Criar setas do campo de direções
        arrows = VGroup()
        
        # Gerar grid de pontos
        x_vals = np.arange(x_min, x_max + density, density)
        y_vals = np.arange(y_min, y_max + density, density)
        
        scale_factor = 0.3  # fator para o comprimento das setas
        
        for x in x_vals:
            for y in y_vals:
                # Calcular a inclinação (dy/dx) da EDO
                slope = -2 + x - y
                
                # Vetor direção: (dx, dy) = (1, slope)
                dx = 1
                dy = slope
                
                # Normalizar o vetor para comprimento consistente
                length = np.sqrt(dx**2 + dy**2)
                if length > 0:
                    dx = dx / length * scale_factor
                    dy = dy / length * scale_factor
                
                # Posição da seta (no plano xy)
                start_point = axes.c2p(x, y)
                end_point = axes.c2p(x + dx, y + dy)
                
                # Criar seta
                arrow = Arrow(
                    start_point, 
                    end_point,
                    buff=0,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.15,
                    color=YELLOW
                )
                arrows.add(arrow)
        
        # Animar
        self.play(Create(axes), Write(labels))
        self.play(Write(equation))
        self.wait(1)
        
        # Aparecer o campo de direções gradativamente
        self.play(Create(arrows, lag_ratio=0.01), run_time=4)
        self.wait(2)
        
        # Destacar algumas curvas solução
        solution_curves = VGroup()
        
        # Cores para as curvas
        colors = [RED, GREEN, BLUE, PURPLE, ORANGE]
        
        # Soluções da EDO y' = -2 + x - y
        # dy/dx = -2 + x - y  =>  dy/dx + y = x - 2 (linear)
        # Fator integrante: e^{∫dx} = e^x
        # d/dx(y * e^x) = (x-2)*e^x
        # y * e^x = ∫(x-2)*e^x dx = (x-3)*e^x + C
        # y = x - 3 + C*e^{-x}
        
        def solution_function(x, C):
            return x - 3 + C * np.exp(-x)
        
        x_curve = np.linspace(-5, 5, 200)
        
        for i, C in enumerate([-3.0, -1.5, 0.0, 1.5, 3.0]):
            y_curve = solution_function(x_curve, C)
            
            # Filtrar pontos dentro dos limites
            mask = (y_curve >= y_min) & (y_curve <= y_max)
            if np.any(mask):
                curve_points = axes.c2p(x_curve[mask], y_curve[mask])
                curve = VMobject(color=colors[i % len(colors)])
                curve.set_points_smoothly(curve_points)
                solution_curves.add(curve)
        
        # Animar as curvas solução aparecendo
        self.play(
            Create(solution_curves, lag_ratio=0.5),
            run_time=3
        )
        self.wait(2)
        
        # Destacar a Equação Diferencial novamente
        self.play(
            equation.animate.scale(1.2).set_color(YELLOW),
            run_time=1
        )
        self.wait(1)
        self.play(
            equation.animate.scale(1/1.2).set_color(WHITE),
            run_time=1
        )
        self.wait(2)
        
        # Fim
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)

if __name__ == "__main__":
    pass