from manim import *
import numpy as np

class DirectionFieldEDO3(Scene):
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
        equation = MathTex(r"y' = e^{-x} + y").to_edge(UP)
        
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
                slope = np.exp(-x) + y
                
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
        
        # Soluções da EDO y' = e^{-x} + y
        # dy/dx = e^{-x} + y  =>  dy/dx - y = e^{-x} (linear)
        # Fator integrante: e^{-∫dx} = e^{-x}
        # d/dx(y * e^{-x}) = e^{-x} * e^{-x} = e^{-2x}
        # y * e^{-x} = ∫e^{-2x} dx = -1/2 e^{-2x} + C
        # y = -1/2 e^{-x} + C e^{x}
        
        def solution_function(x, C):
            return -0.5 * np.exp(-x) + C * np.exp(x)
        
        x_curve = np.linspace(-5, 5, 200)  # reduzir densidade de pontos
        
        for i, C in enumerate([-0.5, -0.25, 0.0, 0.25, 0.5]):
            y_curve = solution_function(x_curve, C)
            
            # Filtrar pontos dentro dos limites e garantir que tenha pontos suficientes
            mask = (y_curve >= y_min) & (y_curve <= y_max)
            if np.sum(mask) >= 2:  # precisa de pelo menos 2 pontos para criar uma curva
                curve_points = axes.c2p(x_curve[mask], y_curve[mask])
                if len(curve_points) >= 2:  # garantir que tem pelo menos 2 pontos
                    curve = VMobject(color=colors[i % len(colors)])
                    try:
                        curve.set_points_smoothly(curve_points)
                        solution_curves.add(curve)
                    except ValueError:
                        print(f"Erro ao criar curva para C={C}, pontos={len(curve_points)}")
        
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