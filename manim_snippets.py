"""
Biblioteca de snippets Manim — pequenos blocos parametrizados de código
focados em TRANSIÇÕES e ANIMAÇÕES reutilizáveis.

Cada snippet expõe metadados ricos (params, tags, descrição, exemplo, código)
de forma que tanto a UI quanto uma IA possam compô-los para construir cenas.

Estrutura:
    {
      id, title, category, description, tags,
      params: [{name, type, default, label, hint?}],
      imports: [...],
      code: "código com {placeholders}",
      requires?: ["nome_de_outro_snippet"],
    }

Uso programático:
    render_snippet(snippet_id, {"texto": "Olá"}) -> str
"""
from typing import Any

# ---------- Helpers ----------

def _q(s: str) -> str:
    """Escapa string para repr Python (para placeholders de texto)."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


# ---------- Catálogo ----------
SNIPPETS: list[dict[str, Any]] = [
    # -------------------- INTRO --------------------
    {
        "id": "intro_titulo",
        "title": "Título Animado (entrada)",
        "category": "Introdução",
        "description": "Título no topo com Write + leve slide. Ideal para abrir uma cena.",
        "tags": ["titulo", "texto", "intro"],
        "params": [
            {"name": "texto", "type": "string", "default": "Meu Título", "label": "Texto"},
            {"name": "cor", "type": "color", "default": "BLUE", "label": "Cor"},
            {"name": "tamanho", "type": "number", "default": 44, "label": "Tamanho da fonte"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'titulo = Text("{texto_q}", font_size={tamanho:g}, color={cor}).to_edge(UP)\n'
            'self.play(Write(titulo), run_time=1.2)\n'
            'self.wait(0.4)'
        ),
    },
    {
        "id": "intro_subtitulo",
        "title": "Subtítulo (FadeIn)",
        "category": "Introdução",
        "description": "Subtítulo abaixo do título com FadeIn vindo de baixo.",
        "tags": ["subtitulo", "texto", "fadein"],
        "params": [
            {"name": "texto", "type": "string", "default": "Conceito chave", "label": "Texto"},
            {"name": "cor", "type": "color", "default": "GREY_B", "label": "Cor"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'subtitulo = Text("{texto_q}", font_size=28, color={cor}).next_to(titulo, DOWN, buff=0.3)\n'
            'self.play(FadeIn(subtitulo, shift=UP*0.4))\n'
            'self.wait(0.4)'
        ),
        "requires_var": ["titulo"],
    },

    # -------------------- TRANSIÇÕES --------------------
    {
        "id": "transition_fade_all",
        "title": "Fade-out de todos os mobjects",
        "category": "Transições",
        "description": "Limpa a cena com FadeOut em tudo que está visível.",
        "tags": ["fadeout", "limpar", "transicao"],
        "params": [
            {"name": "duracao", "type": "number", "default": 0.8, "label": "Duração (s)"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(*[FadeOut(m) for m in self.mobjects], run_time={duracao:g})'
        ),
    },
    {
        "id": "transition_slide_left",
        "title": "Slide para a esquerda (saída)",
        "category": "Transições",
        "description": "Tira todos os mobjects deslizando para a esquerda.",
        "tags": ["slide", "saida", "transicao"],
        "params": [
            {"name": "distancia", "type": "number", "default": 6, "label": "Distância"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(*[m.animate.shift(LEFT*{distancia:g}).set_opacity(0) for m in self.mobjects], run_time=0.9)\n'
            'self.remove(*self.mobjects)'
        ),
    },
    {
        "id": "transition_zoom_in",
        "title": "Zoom-in num ponto",
        "category": "Transições",
        "description": "Aproxima a câmera num ponto (escala todos os mobjects).",
        "tags": ["zoom", "camera", "transicao"],
        "params": [
            {"name": "fator", "type": "number", "default": 1.6, "label": "Fator de zoom"},
            {"name": "x", "type": "number", "default": 0, "label": "Centro X"},
            {"name": "y", "type": "number", "default": 0, "label": "Centro Y"},
        ],
        "imports": ["from manim import *", "import numpy as np"],
        "code": (
            'centro = np.array([{x:g}, {y:g}, 0])\n'
            'self.play(*[m.animate.scale({fator:g}, about_point=centro) for m in self.mobjects], run_time=1.2)'
        ),
    },
    {
        "id": "transition_morph",
        "title": "Transformar A em B (morph)",
        "category": "Transições",
        "description": "Anima a transformação suave entre dois mobjects pelo nome.",
        "tags": ["transform", "morph", "transicao"],
        "params": [
            {"name": "origem", "type": "string", "default": "obj_a", "label": "Variável origem"},
            {"name": "destino", "type": "string", "default": "obj_b", "label": "Variável destino"},
            {"name": "duracao", "type": "number", "default": 1.5, "label": "Duração (s)"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(Transform({origem}, {destino}), run_time={duracao:g})\n'
            'self.wait(0.4)'
        ),
    },

    # -------------------- ÊNFASE --------------------
    {
        "id": "highlight_indicate",
        "title": "Pulsar / Indicar mobject",
        "category": "Ênfase",
        "description": "Faz o mobject pulsar (Indicate) chamando atenção.",
        "tags": ["destaque", "indicate", "pulsar"],
        "params": [
            {"name": "alvo", "type": "string", "default": "formula", "label": "Variável alvo"},
            {"name": "fator", "type": "number", "default": 1.3, "label": "Fator de escala"},
            {"name": "cor", "type": "color", "default": "YELLOW", "label": "Cor do flash"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(Indicate({alvo}, scale_factor={fator:g}, color={cor}))\n'
            'self.wait(0.3)'
        ),
    },
    {
        "id": "highlight_circumscribe",
        "title": "Circular (Circumscribe)",
        "category": "Ênfase",
        "description": "Desenha um retângulo/círculo amarelo ao redor de um mobject.",
        "tags": ["destaque", "circulo", "circumscribe"],
        "params": [
            {"name": "alvo", "type": "string", "default": "formula", "label": "Variável alvo"},
            {"name": "cor", "type": "color", "default": "YELLOW", "label": "Cor"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(Circumscribe({alvo}, color={cor}, run_time=1.2))'
        ),
    },
    {
        "id": "highlight_flash",
        "title": "Flash radial",
        "category": "Ênfase",
        "description": "Flash de raios partindo de um ponto.",
        "tags": ["flash", "destaque"],
        "params": [
            {"name": "alvo", "type": "string", "default": "ponto", "label": "Variável (mobject ou ponto)"},
            {"name": "cor", "type": "color", "default": "YELLOW", "label": "Cor"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'self.play(Flash({alvo}, color={cor}, flash_radius=0.6))'
        ),
    },

    # -------------------- EQUAÇÕES --------------------
    {
        "id": "equacao_write",
        "title": "Equação com Write",
        "category": "Equações",
        "description": "Cria um MathTex e o escreve com Write.",
        "tags": ["equacao", "mathtex", "write"],
        "params": [
            {"name": "var", "type": "string", "default": "eq", "label": "Nome da variável"},
            {"name": "latex", "type": "string", "default": r"a^2 + b^2 = c^2", "label": "LaTeX"},
            {"name": "cor", "type": "color", "default": "WHITE", "label": "Cor"},
            {"name": "tamanho", "type": "number", "default": 48, "label": "Tamanho"},
        ],
        "imports": ["from manim import *"],
        "code": (
            '{var} = MathTex(r"{latex}", font_size={tamanho:g}, color={cor})\n'
            'self.play(Write({var}), run_time=1.2)\n'
            'self.wait(0.5)'
        ),
    },
    {
        "id": "equacao_transform",
        "title": "Transformar equação A → B",
        "category": "Equações",
        "description": "Substitui suavemente uma equação por outra com TransformMatchingTex.",
        "tags": ["equacao", "transform", "matching"],
        "params": [
            {"name": "origem", "type": "string", "default": "eq", "label": "Variável origem"},
            {"name": "latex_destino", "type": "string", "default": r"x = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}", "label": "LaTeX destino"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'eq_nova = MathTex(r"{latex_destino}", font_size=48).move_to({origem})\n'
            'self.play(TransformMatchingTex({origem}, eq_nova), run_time=1.6)\n'
            '{origem} = eq_nova\n'
            'self.wait(0.6)'
        ),
    },

    # -------------------- GRÁFICOS --------------------
    {
        "id": "axes_2d",
        "title": "Eixos 2D animados",
        "category": "Gráficos",
        "description": "Cria Axes 2D com Create animado.",
        "tags": ["axes", "graficos", "create"],
        "params": [
            {"name": "xmin", "type": "number", "default": -6, "label": "X min"},
            {"name": "xmax", "type": "number", "default": 6, "label": "X max"},
            {"name": "ymin", "type": "number", "default": -4, "label": "Y min"},
            {"name": "ymax", "type": "number", "default": 4, "label": "Y max"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'axes = Axes(\n'
            '    x_range=[{xmin:g}, {xmax:g}, 1],\n'
            '    y_range=[{ymin:g}, {ymax:g}, 1],\n'
            '    x_length=9, y_length=5,\n'
            '    axis_config={{"include_numbers": True, "stroke_color": GREY_B}},\n'
            ')\n'
            'self.play(Create(axes), run_time=1.5)'
        ),
    },
    {
        "id": "plot_function",
        "title": "Plotar função (Create animado)",
        "category": "Gráficos",
        "description": "Desenha uma função no Axes existente com animação.",
        "tags": ["plot", "funcao", "graficos"],
        "params": [
            {"name": "expr", "type": "string", "default": "x**2", "label": "Expressão Python (de x)"},
            {"name": "cor", "type": "color", "default": "BLUE", "label": "Cor"},
            {"name": "var", "type": "string", "default": "graph", "label": "Nome da variável"},
        ],
        "imports": ["from manim import *"],
        "code": (
            '{var} = axes.plot(lambda x: {expr}, color={cor})\n'
            'self.play(Create({var}), run_time=2)'
        ),
        "requires_var": ["axes"],
    },
    {
        "id": "moving_dot",
        "title": "Ponto se movendo na curva",
        "category": "Gráficos",
        "description": "Anima um ponto percorrendo a curva existente (`graph`).",
        "tags": ["dot", "trace", "movimento"],
        "params": [
            {"name": "cor", "type": "color", "default": "RED", "label": "Cor"},
            {"name": "duracao", "type": "number", "default": 3, "label": "Duração (s)"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'dot = Dot(color={cor}).move_to(graph.get_start())\n'
            'self.add(dot)\n'
            'self.play(MoveAlongPath(dot, graph), run_time={duracao:g}, rate_func=linear)'
        ),
        "requires_var": ["graph"],
    },

    # -------------------- ANOTAÇÕES --------------------
    {
        "id": "arrow_label",
        "title": "Seta + rótulo apontando",
        "category": "Anotações",
        "description": "Cria uma seta apontando para um mobject e um rótulo de texto ao lado.",
        "tags": ["seta", "anotacao", "rotulo"],
        "params": [
            {"name": "alvo", "type": "string", "default": "vertice", "label": "Variável alvo"},
            {"name": "texto", "type": "string", "default": "Vértice", "label": "Texto do rótulo"},
            {"name": "direcao", "type": "select", "default": "UR", "label": "Direção", "options": [
                {"value": "UP", "label": "Cima"}, {"value": "DOWN", "label": "Baixo"},
                {"value": "LEFT", "label": "Esquerda"}, {"value": "RIGHT", "label": "Direita"},
                {"value": "UR", "label": "Sup. Direita"}, {"value": "UL", "label": "Sup. Esquerda"},
                {"value": "DR", "label": "Inf. Direita"}, {"value": "DL", "label": "Inf. Esquerda"},
            ]},
            {"name": "cor", "type": "color", "default": "YELLOW", "label": "Cor"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'rotulo = Text("{texto_q}", font_size=28, color={cor}).next_to({alvo}, {direcao}, buff=1.0)\n'
            'seta = Arrow(rotulo.get_corner(-{direcao}), {alvo}.get_center(), color={cor}, buff=0.15)\n'
            'self.play(GrowArrow(seta), Write(rotulo))\n'
            'self.wait(0.5)'
        ),
    },
    {
        "id": "number_counter",
        "title": "Contador animado (DecimalNumber)",
        "category": "Anotações",
        "description": "Número que conta de A até B com easing suave.",
        "tags": ["numero", "contador", "valuetracker"],
        "params": [
            {"name": "inicio", "type": "number", "default": 0, "label": "Valor inicial"},
            {"name": "fim", "type": "number", "default": 100, "label": "Valor final"},
            {"name": "casas", "type": "number", "default": 0, "label": "Casas decimais"},
            {"name": "duracao", "type": "number", "default": 2, "label": "Duração (s)"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'tracker = ValueTracker({inicio:g})\n'
            'numero = always_redraw(lambda: DecimalNumber(tracker.get_value(), num_decimal_places={casas:g}, font_size=72).move_to(ORIGIN))\n'
            'self.add(numero)\n'
            'self.play(tracker.animate.set_value({fim:g}), run_time={duracao:g}, rate_func=smooth)'
        ),
    },

    # -------------------- GEOMETRIA --------------------
    {
        "id": "triangulo_construct",
        "title": "Construir triângulo passo a passo",
        "category": "Geometria",
        "description": "Cria um triângulo desenhando os 3 lados em sequência.",
        "tags": ["triangulo", "geometria", "construcao"],
        "params": [
            {"name": "cor", "type": "color", "default": "WHITE", "label": "Cor das linhas"},
        ],
        "imports": ["from manim import *", "import numpy as np"],
        "code": (
            'A = np.array([-2, -1.2, 0])\n'
            'B = np.array([ 2, -1.2, 0])\n'
            'C = np.array([ 0,  1.6, 0])\n'
            'lado_ab = Line(A, B, color={cor}, stroke_width=4)\n'
            'lado_bc = Line(B, C, color={cor}, stroke_width=4)\n'
            'lado_ca = Line(C, A, color={cor}, stroke_width=4)\n'
            'self.play(Create(lado_ab))\n'
            'self.play(Create(lado_bc))\n'
            'self.play(Create(lado_ca))\n'
            'triangulo = VGroup(lado_ab, lado_bc, lado_ca)'
        ),
    },
    {
        "id": "circle_grow",
        "title": "Círculo crescendo do centro",
        "category": "Geometria",
        "description": "Círculo que aparece crescendo do centro.",
        "tags": ["circulo", "grow", "geometria"],
        "params": [
            {"name": "raio", "type": "number", "default": 1.5, "label": "Raio"},
            {"name": "cor", "type": "color", "default": "BLUE", "label": "Cor da borda"},
            {"name": "preenchimento", "type": "color", "default": "BLUE", "label": "Cor do preenchimento"},
            {"name": "opacidade", "type": "number", "default": 0.3, "label": "Opacidade do preenchimento"},
        ],
        "imports": ["from manim import *"],
        "code": (
            'circulo = Circle(radius={raio:g}, color={cor}).set_fill({preenchimento}, opacity={opacidade:g})\n'
            'self.play(GrowFromCenter(circulo), run_time=1.2)'
        ),
    },
    {
        "id": "rotate_anim",
        "title": "Rotação contínua",
        "category": "Geometria",
        "description": "Rotaciona um mobject suavemente N voltas.",
        "tags": ["rotacao", "spin"],
        "params": [
            {"name": "alvo", "type": "string", "default": "circulo", "label": "Variável alvo"},
            {"name": "voltas", "type": "number", "default": 1, "label": "Número de voltas"},
            {"name": "duracao", "type": "number", "default": 2, "label": "Duração (s)"},
        ],
        "imports": ["from manim import *", "import numpy as np"],
        "code": (
            'self.play(Rotate({alvo}, angle={voltas:g}*2*np.pi, run_time={duracao:g}, rate_func=smooth))'
        ),
    },

    # -------------------- CENAS COMPLETAS --------------------
    {
        "id": "scene_skeleton",
        "title": "Esqueleto de Scene completa",
        "category": "Esqueletos",
        "description": "Estrutura mínima de uma Scene Manim. Use como ponto de partida.",
        "tags": ["scene", "skeleton", "boilerplate"],
        "params": [
            {"name": "nome", "type": "string", "default": "MinhaCena", "label": "Nome da classe"},
        ],
        "imports": [],
        "code": (
            'from manim import *\n\n'
            'class {nome}(Scene):\n'
            '    def construct(self):\n'
            '        # Seu código aqui\n'
            '        titulo = Text("Olá!", font_size=48)\n'
            '        self.play(Write(titulo))\n'
            '        self.wait(1)\n'
            '        self.play(*[FadeOut(m) for m in self.mobjects])\n'
        ),
        "is_full_scene": True,
    },
]


# ---------- API ----------

CATEGORIES = sorted({s["category"] for s in SNIPPETS})
_BY_ID = {s["id"]: s for s in SNIPPETS}


def list_snippets() -> list[dict]:
    """Retorna metadados (sem o código completo) para listagem."""
    return [
        {k: v for k, v in s.items() if k != "code"}
        for s in SNIPPETS
    ]


def get_snippet(snippet_id: str) -> dict:
    if snippet_id not in _BY_ID:
        raise ValueError(f"Snippet '{snippet_id}' não encontrado.")
    return _BY_ID[snippet_id]


def render_snippet(snippet_id: str, params: dict | None = None) -> dict:
    """
    Substitui placeholders no código e devolve {code, imports, full}.
    `params` pode estar incompleto: usa defaults para o que faltar.
    """
    s = get_snippet(snippet_id)
    params = params or {}
    fmt = {}
    for p in s["params"]:
        v = params.get(p["name"], p["default"])
        if p["type"] == "number":
            try:
                fmt[p["name"]] = float(v)
            except (TypeError, ValueError):
                fmt[p["name"]] = float(p["default"])
        else:
            fmt[p["name"]] = v
            # versão escapada para uso dentro de strings
            if isinstance(v, str):
                fmt[p["name"] + "_q"] = _q(v)
    try:
        code = s["code"].format(**fmt)
    except KeyError as e:
        raise ValueError(f"Placeholder ausente em '{snippet_id}': {e}")
    return {
        "id": s["id"],
        "code": code,
        "imports": s.get("imports", []),
        "is_full_scene": s.get("is_full_scene", False),
    }


def manifest_for_ai() -> dict:
    """
    Manifesto JSON otimizado para consumo por IA — descreve cada snippet com
    nome, descrição, parâmetros e exemplo de código já renderizado com defaults.
    """
    items = []
    for s in SNIPPETS:
        rendered = render_snippet(s["id"], {p["name"]: p["default"] for p in s["params"]})
        items.append({
            "id": s["id"],
            "title": s["title"],
            "category": s["category"],
            "description": s["description"],
            "tags": s.get("tags", []),
            "params": s["params"],
            "imports": s.get("imports", []),
            "requires_var": s.get("requires_var", []),
            "is_full_scene": s.get("is_full_scene", False),
            "example_code": rendered["code"],
            "template": s["code"],
        })
    return {
        "version": "1.0",
        "description": (
            "Biblioteca de snippets Manim para construir cenas matemáticas. "
            "Cada snippet é um bloco de código Python parametrizado. "
            "Para compor uma cena, escolha snippets compatíveis (veja 'requires_var' "
            "para variáveis de pré-requisito) e concatene seus códigos dentro de "
            "`def construct(self):` de uma classe Scene."
        ),
        "categories": CATEGORIES,
        "usage": {
            "list": "GET /api/snippets",
            "detail": "GET /api/snippets/<id>",
            "render": "POST /api/snippets/<id>/render  body: {params: {...}}",
            "manifest_for_ai": "GET /api/snippets/manifest",
        },
        "snippets": items,
    }
