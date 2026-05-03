"""
Templates de animações Manim para matemática.
Cada template gera código Python Manim com transições suaves.
Estratégia: computamos valores em Python e os inserimos no código como literais,
evitando nested f-strings com LaTeX (que quebraria por causa de \\frac, \\Delta etc).
"""
from math import gcd, sqrt


def _hdr(titulo_txt: str) -> str:
    """Cabeçalho padrão com título azul no topo."""
    return (
        'titulo = Text(' + repr(titulo_txt) + ', font_size=44, color=BLUE).to_edge(UP)\n'
        '        self.play(Write(titulo))\n'
        '        self.wait(0.5)'
    )


# -------------------- Função Quadrática --------------------
def gen_funcao_quadratica(p):
    a, b, c = float(p["a"]), float(p["b"]), float(p["c"])
    if a == 0:
        raise ValueError("Em uma função quadrática, 'a' não pode ser zero.")
    xv = -b / (2 * a)
    yv = a * xv ** 2 + b * xv + c
    delta = b ** 2 - 4 * a * c
    has_zeros = a != 0 and delta >= 0
    if has_zeros:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
    code = f'''from manim import *

class FuncaoQuadratica(Scene):
    def construct(self):
        {_hdr("Função Quadrática")}

        formula = MathTex(r"f(x) = {a:g}x^2 + ({b:g})x + ({c:g})", font_size=44, color=YELLOW).next_to(titulo, DOWN)
        self.play(FadeIn(formula, shift=UP))
        self.wait(1)

        axes = Axes(
            x_range=[-6, 6, 1], y_range=[-8, 8, 2],
            x_length=9, y_length=5,
            axis_config={{"include_numbers": True, "stroke_color": GREY_B}},
        ).shift(DOWN * 0.5)
        graph = axes.plot(lambda x: {a}*x**2 + {b}*x + {c}, color=BLUE, x_range=[-6, 6])
        graph_label = MathTex("f(x)").set_color(BLUE).next_to(graph.get_end(), UR, buff=0.1)

        self.play(Create(axes), run_time=1.5)
        self.play(Create(graph), run_time=2)
        self.play(Write(graph_label))
        self.wait(0.5)

        # Vértice
        vertice = Dot(axes.c2p({xv}, {yv}), color=YELLOW, radius=0.12)
        v_lbl = MathTex(r"V({xv:.2f},\ {yv:.2f})", color=YELLOW).scale(0.7).next_to(vertice, UR if {a} > 0 else DR)
        self.play(GrowFromCenter(vertice), Write(v_lbl))
        self.wait(0.8)
'''
    if has_zeros:
        code += f'''
        # Zeros
        z1 = Dot(axes.c2p({x1}, 0), color=GREEN, radius=0.12)
        z2 = Dot(axes.c2p({x2}, 0), color=GREEN, radius=0.12)
        z1l = MathTex(r"x_1={x1:.2f}", color=GREEN).scale(0.6).next_to(z1, DOWN)
        z2l = MathTex(r"x_2={x2:.2f}", color=GREEN).scale(0.6).next_to(z2, DOWN)
        self.play(GrowFromCenter(z1), GrowFromCenter(z2))
        self.play(Write(z1l), Write(z2l))
'''
    elif a != 0:
        code += '''
        sem_raiz = Text("Sem raízes reais (Δ < 0)", font_size=28, color=RED).to_edge(DOWN)
        self.play(Write(sem_raiz))
'''
    code += '''
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''
    return code


# -------------------- Bhaskara --------------------
def gen_bhaskara(p):
    a, b, c = float(p["a"]), float(p["b"]), float(p["c"])
    if a == 0:
        raise ValueError("Em Bhaskara, o coeficiente 'a' não pode ser zero (não seria do 2º grau).")
    delta = b * b - 4 * a * c
    code = f'''from manim import *

class Bhaskara(Scene):
    def construct(self):
        {_hdr("Fórmula de Bhaskara")}

        eq = MathTex(r"{a:g}x^2 + ({b:g})x + ({c:g}) = 0", font_size=48).shift(UP*1.5)
        self.play(Write(eq))
        self.wait(1)

        formula = MathTex(r"x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}", font_size=44, color=YELLOW).shift(UP*0.2)
        self.play(FadeIn(formula, shift=UP))
        self.wait(1)

        delta_txt = MathTex(r"\\Delta = b^2 - 4ac = ({b:g})^2 - 4 \\cdot ({a:g}) \\cdot ({c:g}) = {delta:g}", font_size=34, color=GREEN).shift(DOWN*1.2)
        self.play(Write(delta_txt))
        self.wait(1.5)
'''
    if delta < 0:
        code += '''
        res = Text("Δ < 0  →  Sem raízes reais", font_size=36, color=RED).shift(DOWN*2.8)
        self.play(Write(res))
'''
    elif delta == 0:
        x = -b / (2 * a)
        code += f'''
        res = MathTex(r"x = {x:.4g}", font_size=44, color=RED).shift(DOWN*2.8)
        self.play(Write(res))
'''
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        code += f'''
        res1 = MathTex(r"x_1 = {x1:.4g}", font_size=44, color=RED).shift(DOWN*2.6 + LEFT*2.5)
        res2 = MathTex(r"x_2 = {x2:.4g}", font_size=44, color=RED).shift(DOWN*2.6 + RIGHT*2.5)
        self.play(Write(res1), Write(res2))
'''
    code += '''
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''
    return code


# -------------------- Pitágoras --------------------
def gen_pitagoras(p):
    a = float(p["a"])
    b = float(p["b"])
    if a <= 0 or b <= 0:
        raise ValueError("Os catetos devem ser positivos.")
    c = sqrt(a * a + b * b)
    return f'''from manim import *
import numpy as np

class Pitagoras(Scene):
    def construct(self):
        {_hdr("Teorema de Pitágoras")}

        a, b, c = {a}, {b}, {c}
        scale = 0.8
        A = np.array([-b*scale/2, -a*scale/2, 0])
        B = np.array([ b*scale/2, -a*scale/2, 0])
        C = np.array([-b*scale/2,  a*scale/2, 0])

        triangulo = Polygon(A, B, C, color=WHITE, stroke_width=4).set_fill(BLUE, opacity=0.3)
        self.play(Create(triangulo), run_time=1.5)

        right_angle = Square(side_length=0.3, color=YELLOW).move_to(A + np.array([0.15, 0.15, 0]))
        self.play(Create(right_angle))

        lbl_a = MathTex(r"a = {a:g}", color=GREEN).next_to(triangulo, LEFT)
        lbl_b = MathTex(r"b = {b:g}", color=ORANGE).next_to(triangulo, DOWN)
        lbl_c = MathTex(r"c = {c:.3g}", color=RED).next_to(Line(B, C).get_center(), UR, buff=0.1)
        self.play(Write(lbl_a), Write(lbl_b), Write(lbl_c))
        self.wait(1)

        sq_a = Polygon(A, C, C + np.array([-a*scale,0,0]), A + np.array([-a*scale,0,0]),
                       color=GREEN, fill_opacity=0.5)
        sq_b = Polygon(A, B, B + np.array([0,-b*scale,0]), A + np.array([0,-b*scale,0]),
                       color=ORANGE, fill_opacity=0.5)

        self.play(Create(sq_a))
        a2 = MathTex(r"a^2={a*a:.3g}", color=GREEN).move_to(sq_a.get_center())
        self.play(Write(a2))
        self.wait(0.3)
        self.play(Create(sq_b))
        b2 = MathTex(r"b^2={b*b:.3g}", color=ORANGE).move_to(sq_b.get_center())
        self.play(Write(b2))
        self.wait(0.8)

        formula = MathTex(r"a^2 + b^2 = c^2", font_size=48, color=YELLOW).to_edge(DOWN, buff=1)
        self.play(Write(formula))
        calc = MathTex(r"{a*a:.3g} + {b*b:.3g} = {c*c:.3g}", font_size=40, color=RED).next_to(formula, DOWN)
        self.play(Write(calc))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''


# -------------------- Função Linear --------------------
def gen_funcao_linear(p):
    m = float(p["m"])
    n = float(p["n"])
    return f'''from manim import *

class FuncaoLinear(Scene):
    def construct(self):
        {_hdr("Função Linear")}

        formula = MathTex(r"f(x) = {m:g}x + ({n:g})", font_size=44, color=YELLOW).next_to(titulo, DOWN)
        self.play(FadeIn(formula, shift=UP))
        self.wait(0.8)

        axes = Axes(x_range=[-5,5,1], y_range=[-5,5,1], x_length=8, y_length=5,
                    axis_config={{"include_numbers": True, "stroke_color": GREY_B}}).shift(DOWN*0.3)
        self.play(Create(axes))

        graph = axes.plot(lambda x: {m}*x + {n}, color=GREEN, x_range=[-5,5])
        self.play(Create(graph), run_time=2)
        self.wait(0.5)

        # Intercepto
        p0 = Dot(axes.c2p(0, {n}), color=RED, radius=0.12)
        p0_lbl = MathTex(r"(0,\ {n:g})", color=RED).scale(0.7).next_to(p0, RIGHT)
        self.play(GrowFromCenter(p0), Write(p0_lbl))
        self.wait(0.5)

        # Triângulo de inclinação
        x0v, x1v = 1, 2
        tri = Polygon(axes.c2p(x0v, {m}*x0v+{n}), axes.c2p(x1v, {m}*x0v+{n}),
                      axes.c2p(x1v, {m}*x1v+{n}),
                      color=ORANGE, fill_opacity=0.4)
        self.play(Create(tri))
        dx = MathTex(r"\\Delta x = 1", color=ORANGE).scale(0.6).next_to(
            Line(axes.c2p(x0v, {m}*x0v+{n}), axes.c2p(x1v, {m}*x0v+{n})).get_center(), DOWN, buff=0.1)
        dy = MathTex(r"\\Delta y = {m:g}", color=ORANGE).scale(0.6).next_to(
            Line(axes.c2p(x1v, {m}*x0v+{n}), axes.c2p(x1v, {m}*x1v+{n})).get_center(), RIGHT, buff=0.1)
        self.play(Write(dx), Write(dy))
        self.wait(0.8)

        slope = MathTex(r"m = \\frac{{\\Delta y}}{{\\Delta x}} = {m:g}", color=ORANGE, font_size=40).to_edge(DOWN)
        self.play(Write(slope))
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''


# -------------------- Círculo Trigonométrico --------------------
def gen_circulo_trig(p):
    voltas = float(p["voltas"])
    return f'''from manim import *
import numpy as np

class CirculoTrigonometrico(Scene):
    def construct(self):
        {_hdr("Círculo Trigonométrico")}

        plane = NumberPlane(x_range=[-2,2,1], y_range=[-2,2,1], x_length=5, y_length=5,
                            background_line_style={{"stroke_opacity": 0.4}}).shift(LEFT*3 + DOWN*0.3)
        circle = Circle(radius=plane.get_x_axis().get_unit_size()*1, color=YELLOW).move_to(plane.c2p(0,0))
        self.play(Create(plane), Create(circle))

        theta = ValueTracker(0)

        def get_point():
            t = theta.get_value()
            return plane.c2p(np.cos(t), np.sin(t))

        radius = always_redraw(lambda: Line(plane.c2p(0,0), get_point(), color=WHITE))
        dot = always_redraw(lambda: Dot(get_point(), color=RED, radius=0.1))
        sin_line = always_redraw(lambda: Line(
            plane.c2p(np.cos(theta.get_value()), 0), get_point(), color=GREEN, stroke_width=5))
        cos_line = always_redraw(lambda: Line(
            plane.c2p(0,0), plane.c2p(np.cos(theta.get_value()), 0), color=ORANGE, stroke_width=5))

        self.add(radius, sin_line, cos_line, dot)

        labels = VGroup(
            MathTex(r"\\theta = ", color=WHITE),
            MathTex(r"\\sin\\theta = ", color=GREEN),
            MathTex(r"\\cos\\theta = ", color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).shift(RIGHT*3 + DOWN*0.3)

        theta_val = always_redraw(lambda: DecimalNumber(theta.get_value(), num_decimal_places=2,
                                   color=WHITE).next_to(labels[0], RIGHT))
        sin_val = always_redraw(lambda: DecimalNumber(np.sin(theta.get_value()), num_decimal_places=2,
                                  color=GREEN).next_to(labels[1], RIGHT))
        cos_val = always_redraw(lambda: DecimalNumber(np.cos(theta.get_value()), num_decimal_places=2,
                                  color=ORANGE).next_to(labels[2], RIGHT))

        self.play(Write(labels))
        self.add(theta_val, sin_val, cos_val)

        self.play(theta.animate.set_value(2*PI*{voltas}), run_time=6, rate_func=linear)
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''


# -------------------- Derivada Visual --------------------
def gen_derivada_visual(p):
    funcao = p["funcao"]
    if funcao == "quadratica":
        f_expr = "x**2"
        df_expr = "2*x"
        label = "f(x) = x^2"
        x_min, x_max = -3, 3
    elif funcao == "cubica":
        f_expr = "x**3 - 3*x"
        df_expr = "3*x**2 - 3"
        label = "f(x) = x^3 - 3x"
        x_min, x_max = -2.5, 2.5
    else:
        f_expr = "np.sin(x)"
        df_expr = "np.cos(x)"
        label = r"f(x) = \\sin(x)"
        x_min, x_max = "-PI", "PI"
    return f'''from manim import *
import numpy as np

class DerivadaVisual(Scene):
    def construct(self):
        {_hdr("Derivada como Inclinação")}

        f = lambda x: {f_expr}
        df = lambda x: {df_expr}

        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-5,5,1], x_length=9, y_length=5,
                    axis_config={{"include_numbers": True, "stroke_color": GREY_B}}).shift(DOWN*0.3)
        graph = axes.plot(f, color=BLUE, x_range=[{x_min}, {x_max}])
        graph_lbl = MathTex(r"{label}", color=BLUE).to_corner(UR).shift(DOWN*0.8 + LEFT*0.3)

        self.play(Create(axes))
        self.play(Create(graph), Write(graph_lbl), run_time=2)

        x_t = ValueTracker({x_min})

        dot = always_redraw(lambda: Dot(axes.c2p(x_t.get_value(), f(x_t.get_value())), color=RED, radius=0.1))

        def get_tangent():
            xv = x_t.get_value()
            slope = df(xv)
            return axes.plot(lambda x: slope*(x - xv) + f(xv), color=YELLOW, x_range=[xv-1.2, xv+1.2])
        tangent = always_redraw(get_tangent)

        slope_label = always_redraw(lambda: MathTex(
            "f'(" + f"{{x_t.get_value():.2f}}" + ") = " + f"{{df(x_t.get_value()):.2f}}",
            color=YELLOW
        ).to_edge(DOWN))

        self.add(dot, tangent, slope_label)
        self.play(x_t.animate.set_value({x_max}), run_time=8, rate_func=smooth)
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''


# -------------------- Soma de Frações --------------------
def gen_soma_fracoes(p):
    n1 = int(p["n1"]); d1 = int(p["d1"])
    n2 = int(p["n2"]); d2 = int(p["d2"])
    if d1 == 0 or d2 == 0:
        raise ValueError("Denominadores não podem ser zero.")
    mmc = abs(d1 * d2) // gcd(d1, d2)
    a = n1 * (mmc // d1)
    b_ = n2 * (mmc // d2)
    soma_n = a + b_
    g = gcd(abs(soma_n), mmc) if soma_n != 0 else 1
    sn, sd = (soma_n // g, mmc // g) if g else (soma_n, mmc)

    code = f'''from manim import *

class SomaFracoes(Scene):
    def construct(self):
        {_hdr("Soma de Frações")}

        f1 = MathTex(r"\\frac{{{n1}}}{{{d1}}}", font_size=72, color=GREEN).shift(LEFT*3 + UP*0.3)
        plus = MathTex("+", font_size=72).shift(LEFT*1 + UP*0.3)
        f2 = MathTex(r"\\frac{{{n2}}}{{{d2}}}", font_size=72, color=ORANGE).shift(UP*0.3 + RIGHT*0.5)
        eq = MathTex("=", font_size=72).next_to(f2, RIGHT, buff=0.5)
        result = MathTex(r"?", font_size=72, color=YELLOW).next_to(eq, RIGHT, buff=0.5)

        self.play(Write(f1), Write(plus), Write(f2), Write(eq), Write(result))
        self.wait(1)

        passo1 = MathTex(r"\\text{{MMC}}({d1}, {d2}) = {mmc}", font_size=36, color=BLUE).shift(DOWN*1.5)
        self.play(Write(passo1))
        self.wait(0.8)

        f1e = MathTex(r"\\frac{{{a}}}{{{mmc}}}", font_size=60, color=GREEN).move_to(f1)
        f2e = MathTex(r"\\frac{{{b_}}}{{{mmc}}}", font_size=60, color=ORANGE).move_to(f2)
        self.play(Transform(f1, f1e), Transform(f2, f2e))
        self.wait(0.8)

        result_final = MathTex(r"\\frac{{{soma_n}}}{{{mmc}}}", font_size=72, color=YELLOW).move_to(result)
        self.play(Transform(result, result_final))
        self.wait(0.8)
'''
    if (sn, sd) != (soma_n, mmc):
        code += f'''
        simpl = MathTex(r"= \\frac{{{sn}}}{{{sd}}}", font_size=72, color=RED).next_to(result, RIGHT, buff=0.4)
        self.play(Write(simpl))
'''
    code += '''
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''
    return code


# -------------------- Sistema Linear 2x2 --------------------
def gen_sistema_linear(p):
    a1 = float(p["a1"]); b1 = float(p["b1"]); c1 = float(p["c1"])
    a2 = float(p["a2"]); b2 = float(p["b2"]); c2 = float(p["c2"])
    det = a1 * b2 - a2 * b1
    code = f'''from manim import *

class SistemaLinear(Scene):
    def construct(self):
        {_hdr("Sistema Linear 2x2")}

        sistema = MathTex(
            r"\\begin{{cases}} {a1:g}x + ({b1:g})y = {c1:g} \\\\ {a2:g}x + ({b2:g})y = {c2:g} \\end{{cases}}",
            font_size=40
        ).to_edge(LEFT).shift(RIGHT*0.5 + UP*0.3)
        self.play(Write(sistema))
        self.wait(0.8)

        axes = Axes(x_range=[-6,6,1], y_range=[-6,6,1], x_length=6, y_length=6,
                    axis_config={{"include_numbers": True, "stroke_color": GREY_B}}).shift(RIGHT*3)
        self.play(Create(axes))
'''
    if b1 != 0:
        code += f'        r1 = axes.plot(lambda x: ({c1} - {a1}*x)/{b1}, color=GREEN, x_range=[-6,6])\n'
    else:
        code += f'        r1 = Line(axes.c2p({c1/a1 if a1 else 0},-6), axes.c2p({c1/a1 if a1 else 0},6), color=GREEN)\n'
    if b2 != 0:
        code += f'        r2 = axes.plot(lambda x: ({c2} - {a2}*x)/{b2}, color=ORANGE, x_range=[-6,6])\n'
    else:
        code += f'        r2 = Line(axes.c2p({c2/a2 if a2 else 0},-6), axes.c2p({c2/a2 if a2 else 0},6), color=ORANGE)\n'

    code += '''        self.play(Create(r1), run_time=1.5)
        self.play(Create(r2), run_time=1.5)
        self.wait(0.4)
'''
    if det != 0:
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        code += f'''
        ponto = Dot(axes.c2p({x}, {y}), color=YELLOW, radius=0.14)
        lbl = MathTex(r"({x:.2f},\\ {y:.2f})", color=YELLOW).scale(0.7).next_to(ponto, UR)
        self.play(GrowFromCenter(ponto), Write(lbl))
        sol = MathTex(r"x = {x:.2f}, \\quad y = {y:.2f}", color=YELLOW).to_edge(DOWN)
        self.play(Write(sol))
'''
    else:
        code += '''
        sol = Text("Sistema impossível ou indeterminado", font_size=28, color=RED).to_edge(DOWN)
        self.play(Write(sol))
'''
    code += '''        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
'''
    return code


# -------------------- Registry --------------------
TEMPLATES = {
    "funcao_quadratica": {
        "title": "Função Quadrática",
        "description": "Visualize f(x) = ax² + bx + c com vértice e zeros.",
        "icon": "📈",
        "category": "Funções",
        "scene": "FuncaoQuadratica",
        "params": [
            {"name": "a", "label": "Coeficiente a", "type": "number", "default": 1, "step": 0.5},
            {"name": "b", "label": "Coeficiente b", "type": "number", "default": -2, "step": 0.5},
            {"name": "c", "label": "Coeficiente c", "type": "number", "default": -3, "step": 0.5},
        ],
        "generator": gen_funcao_quadratica,
    },
    "bhaskara": {
        "title": "Fórmula de Bhaskara",
        "description": "Resolução passo a passo de equação do segundo grau.",
        "icon": "🧮",
        "category": "Equações",
        "scene": "Bhaskara",
        "params": [
            {"name": "a", "label": "Coeficiente a", "type": "number", "default": 1, "step": 1},
            {"name": "b", "label": "Coeficiente b", "type": "number", "default": -5, "step": 1},
            {"name": "c", "label": "Coeficiente c", "type": "number", "default": 6, "step": 1},
        ],
        "generator": gen_bhaskara,
    },
    "pitagoras": {
        "title": "Teorema de Pitágoras",
        "description": "Demonstração visual de a² + b² = c².",
        "icon": "📐",
        "category": "Geometria",
        "scene": "Pitagoras",
        "params": [
            {"name": "a", "label": "Cateto a", "type": "number", "default": 3, "step": 0.5},
            {"name": "b", "label": "Cateto b", "type": "number", "default": 4, "step": 0.5},
        ],
        "generator": gen_pitagoras,
    },
    "funcao_linear": {
        "title": "Função Linear",
        "description": "Visualize f(x) = mx + n com inclinação e intercepto.",
        "icon": "📊",
        "category": "Funções",
        "scene": "FuncaoLinear",
        "params": [
            {"name": "m", "label": "Coeficiente angular (m)", "type": "number", "default": 2, "step": 0.5},
            {"name": "n", "label": "Coeficiente linear (n)", "type": "number", "default": 1, "step": 0.5},
        ],
        "generator": gen_funcao_linear,
    },
    "circulo_trig": {
        "title": "Círculo Trigonométrico",
        "description": "Animação do seno e cosseno no círculo unitário.",
        "icon": "🔄",
        "category": "Trigonometria",
        "scene": "CirculoTrigonometrico",
        "params": [
            {"name": "voltas", "label": "Número de voltas", "type": "number", "default": 1, "step": 1},
        ],
        "generator": gen_circulo_trig,
    },
    "derivada_visual": {
        "title": "Derivada Visual",
        "description": "Reta tangente percorrendo a curva.",
        "icon": "📉",
        "category": "Cálculo",
        "scene": "DerivadaVisual",
        "params": [
            {"name": "funcao", "label": "Função", "type": "select",
             "options": [
                 {"value": "quadratica", "label": "f(x) = x²"},
                 {"value": "cubica", "label": "f(x) = x³ - 3x"},
                 {"value": "seno", "label": "f(x) = sin(x)"},
             ],
             "default": "quadratica"},
        ],
        "generator": gen_derivada_visual,
    },
    "soma_fracoes": {
        "title": "Soma de Frações",
        "description": "Soma visual com MMC e simplificação.",
        "icon": "➗",
        "category": "Aritmética",
        "scene": "SomaFracoes",
        "params": [
            {"name": "n1", "label": "Numerador 1", "type": "number", "default": 1, "step": 1},
            {"name": "d1", "label": "Denominador 1", "type": "number", "default": 2, "step": 1},
            {"name": "n2", "label": "Numerador 2", "type": "number", "default": 1, "step": 1},
            {"name": "d2", "label": "Denominador 2", "type": "number", "default": 3, "step": 1},
        ],
        "generator": gen_soma_fracoes,
    },
    "sistema_linear": {
        "title": "Sistema Linear 2×2",
        "description": "Resolução gráfica de sistema linear.",
        "icon": "🔢",
        "category": "Equações",
        "scene": "SistemaLinear",
        "params": [
            {"name": "a1", "label": "a₁ (eq. 1)", "type": "number", "default": 1, "step": 1},
            {"name": "b1", "label": "b₁ (eq. 1)", "type": "number", "default": 1, "step": 1},
            {"name": "c1", "label": "c₁ (eq. 1)", "type": "number", "default": 5, "step": 1},
            {"name": "a2", "label": "a₂ (eq. 2)", "type": "number", "default": 2, "step": 1},
            {"name": "b2", "label": "b₂ (eq. 2)", "type": "number", "default": -1, "step": 1},
            {"name": "c2", "label": "c₂ (eq. 2)", "type": "number", "default": 1, "step": 1},
        ],
        "generator": gen_sistema_linear,
    },
}


def get_template_meta():
    return [
        {
            "id": tid,
            "title": t["title"],
            "description": t["description"],
            "icon": t["icon"],
            "category": t["category"],
            "params": t["params"],
        }
        for tid, t in TEMPLATES.items()
    ]


def _validate_param(p_def, value):
    """Coage e valida um valor de parâmetro contra sua definição."""
    import math
    if p_def["type"] == "number":
        try:
            v = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Parâmetro '{p_def['label']}' deve ser numérico.")
        if math.isnan(v) or math.isinf(v):
            raise ValueError(f"Parâmetro '{p_def['label']}' inválido (NaN/Infinito).")
        return v
    if p_def["type"] == "select":
        valid = {o["value"] for o in p_def["options"]}
        if value not in valid:
            raise ValueError(f"Valor inválido para '{p_def['label']}'.")
        return value
    return value


def generate_code(template_id: str, params: dict) -> str:
    if template_id not in TEMPLATES:
        raise ValueError(f"Template '{template_id}' não encontrado")
    t = TEMPLATES[template_id]
    final_params = {}
    for p_def in t["params"]:
        raw = params.get(p_def["name"], p_def["default"])
        final_params[p_def["name"]] = _validate_param(p_def, raw)
    return t["generator"](final_params)


def get_scene_class(template_id: str) -> str:
    return TEMPLATES[template_id]["scene"]
