"""
Templates de TRANSIÇÕES de vídeo Manim.

Cada template é um ESQUELETO ANIMADO — define o fluxo de transições do vídeo
(intro, sequência de revelações, ênfases, saída) e expõe SLOTS de LaTeX/texto
que o usuário preenche com seu conteúdo matemático.

Estratégia segura para LaTeX:
  Os textos do usuário são injetados no código via `repr(s)`, que produz um
  literal Python válido com escapes corretos (ex.: '\\frac' fica '\\\\frac' no
  source, e Python parsa de volta para '\\frac' que MathTex aceita como `\frac`).
"""

# -------------------- Helpers --------------------

def _split_lines(s: str) -> list[str]:
    """Quebra por linhas, ignora linhas vazias, faz trim."""
    if isinstance(s, list):
        return [str(x).strip() for x in s if str(x).strip()]
    return [ln.strip() for ln in str(s).splitlines() if ln.strip()]


def _color_options():
    return [{"value": c, "label": c.title().replace("_", " ")} for c in [
        "BLUE", "RED", "GREEN", "YELLOW", "ORANGE", "PURPLE", "PINK", "TEAL",
        "WHITE", "GREY_B", "GOLD", "MAROON",
    ]]


# -------------------- 1. Apresentação --------------------
def gen_apresentacao(p):
    titulo = str(p.get("titulo", "Teorema"))
    enunciado = str(p.get("enunciado", r"a^2 + b^2 = c^2"))
    autoria = str(p.get("autoria", ""))
    cor_titulo = str(p.get("cor_titulo", "BLUE"))
    cor_destaque = str(p.get("cor_destaque", "YELLOW"))
    return f'''from manim import *

class Apresentacao(Scene):
    def construct(self):
        # 1. Título com Write + slide para o topo
        titulo = Text({titulo!r}, font_size=52, color={cor_titulo})
        self.play(Write(titulo), run_time=1.4)
        self.wait(0.5)
        self.play(titulo.animate.to_edge(UP).scale(0.7))

        # 2. Enunciado central com FadeIn
        enunciado = MathTex({enunciado!r}, font_size=64, color=WHITE)
        self.play(FadeIn(enunciado, shift=UP*0.5), run_time=1.2)
        self.wait(0.8)

        # 3. Caixa pulsando ao redor
        self.play(Circumscribe(enunciado, color={cor_destaque}, run_time=1.5))
        self.wait(0.5)

        # 4. Autoria opcional
        if {autoria!r}:
            autoria = Text({autoria!r}, font_size=24, color=GREY_B, slant=ITALIC).next_to(enunciado, DOWN, buff=0.8)
            self.play(FadeIn(autoria, shift=UP*0.3))
            self.wait(1)

        # 5. Saída suave
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1)
'''


# -------------------- 2. Passo a passo --------------------
def gen_passo_a_passo(p):
    titulo = str(p.get("titulo", "Resolução"))
    passos = _split_lines(p.get("passos", "x + 2 = 5\nx = 5 - 2\nx = 3"))
    if len(passos) < 2:
        raise ValueError("Informe ao menos 2 passos (LaTeX), um por linha.")
    if len(passos) > 8:
        raise ValueError("Máximo de 8 passos.")
    cor_destaque = str(p.get("cor_destaque", "GREEN"))
    return f'''from manim import *

class PassoAPasso(Scene):
    def construct(self):
        # Cabeçalho fixo
        titulo = Text({titulo!r}, font_size=42, color=BLUE).to_edge(UP)
        self.play(Write(titulo), run_time=1)
        linha = Line(LEFT*5, RIGHT*5, color=GREY_B).next_to(titulo, DOWN, buff=0.3)
        self.play(Create(linha))

        passos_latex = {passos!r}

        # Primeiro passo aparece com Write
        atual = MathTex(passos_latex[0], font_size=56).move_to(ORIGIN)
        self.play(Write(atual), run_time=1.3)
        self.wait(0.7)

        # Demais passos: TransformMatchingTex revelando a transformação
        for i, latex in enumerate(passos_latex[1:], start=1):
            novo = MathTex(latex, font_size=56).move_to(atual)
            # Indicador de passo à esquerda
            tag = Text(f"passo {{i+1}}", font_size=22, color=GREY_B).to_edge(LEFT).shift(DOWN*0.3)
            self.play(FadeIn(tag, shift=RIGHT*0.3))
            try:
                self.play(TransformMatchingTex(atual, novo), run_time=1.4)
            except Exception:
                self.play(ReplacementTransform(atual, novo), run_time=1.4)
            atual = novo
            self.wait(0.7)
            self.play(FadeOut(tag))

        # Destaque do resultado final
        self.play(atual.animate.set_color({cor_destaque}).scale(1.15), run_time=0.8)
        self.play(Circumscribe(atual, color={cor_destaque}, run_time=1.4))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
'''


# -------------------- 3. Comparação --------------------
def gen_comparacao(p):
    titulo = str(p.get("titulo", "Comparação"))
    label_a = str(p.get("label_a", "Forma A"))
    label_b = str(p.get("label_b", "Forma B"))
    latex_a = str(p.get("latex_a", r"(a+b)^2"))
    latex_b = str(p.get("latex_b", r"a^2 + 2ab + b^2"))
    cor_a = str(p.get("cor_a", "BLUE"))
    cor_b = str(p.get("cor_b", "ORANGE"))
    return f'''from manim import *

class Comparacao(Scene):
    def construct(self):
        titulo = Text({titulo!r}, font_size=42, color=WHITE).to_edge(UP)
        self.play(Write(titulo))

        # Linha vertical separando os dois lados
        divisor = DashedLine(UP*2.5, DOWN*2.5, color=GREY_B)

        # Lado A entra pela esquerda
        rotulo_a = Text({label_a!r}, font_size=28, color={cor_a}).move_to(LEFT*3.5 + UP*1.5)
        eq_a = MathTex({latex_a!r}, font_size=56, color={cor_a}).move_to(LEFT*3.5)

        # Lado B entra pela direita
        rotulo_b = Text({label_b!r}, font_size=28, color={cor_b}).move_to(RIGHT*3.5 + UP*1.5)
        eq_b = MathTex({latex_b!r}, font_size=56, color={cor_b}).move_to(RIGHT*3.5)

        self.play(Create(divisor))
        self.play(
            FadeIn(rotulo_a, shift=RIGHT*0.5),
            FadeIn(rotulo_b, shift=LEFT*0.5),
        )
        self.play(
            Write(eq_a),
            Write(eq_b),
            run_time=1.4,
        )
        self.wait(1)

        # Setas duplas indicando equivalência
        seta = MathTex(r"\\Longleftrightarrow", font_size=72, color=YELLOW)
        self.play(GrowFromCenter(seta))
        self.wait(0.5)

        # Pulsa ambos
        self.play(
            Indicate(eq_a, color={cor_a}, scale_factor=1.15),
            Indicate(eq_b, color={cor_b}, scale_factor=1.15),
        )
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
'''


# -------------------- 4. Lista em cascata --------------------
def gen_lista_cascata(p):
    titulo = str(p.get("titulo", "Propriedades"))
    itens = _split_lines(p.get("itens", "Comutativa\nAssociativa\nDistributiva"))
    if not itens:
        raise ValueError("Informe ao menos 1 item.")
    if len(itens) > 8:
        raise ValueError("Máximo de 8 itens.")
    destaque_idx_raw = p.get("destaque_idx", 0)
    try:
        destaque_idx = int(destaque_idx_raw)
    except (TypeError, ValueError):
        destaque_idx = 0
    if destaque_idx < 0 or destaque_idx >= len(itens):
        destaque_idx = -1  # nenhum
    eh_latex_raw = p.get("eh_latex", False)
    eh_latex = str(eh_latex_raw).strip().lower() in ("true", "1", "yes", "sim")
    cor_destaque = str(p.get("cor_destaque", "YELLOW"))
    return f'''from manim import *

class ListaCascata(Scene):
    def construct(self):
        titulo = Text({titulo!r}, font_size=46, color=BLUE).to_edge(UP)
        self.play(Write(titulo))
        sublinhado = Underline(titulo, color=BLUE_B)
        self.play(Create(sublinhado))

        itens_raw = {itens!r}
        eh_latex = {eh_latex}
        destaque_idx = {destaque_idx}
        Constructor = MathTex if eh_latex else Text

        # Cria todos os mobjects empilhados
        itens = VGroup()
        for txt in itens_raw:
            bullet = Dot(color=BLUE, radius=0.08)
            try:
                rotulo = Constructor(txt, font_size=36)
            except Exception:
                rotulo = Text(txt, font_size=36)
            linha = VGroup(bullet, rotulo).arrange(RIGHT, buff=0.3)
            itens.add(linha)
        itens.arrange(DOWN, buff=0.45, aligned_edge=LEFT).next_to(sublinhado, DOWN, buff=0.6).shift(LEFT)

        # FadeIn sequencial em cascata
        for linha in itens:
            self.play(FadeIn(linha, shift=RIGHT*0.4), run_time=0.55)
        self.wait(0.8)

        # Destaca o item escolhido
        if 0 <= destaque_idx < len(itens):
            alvo = itens[destaque_idx]
            self.play(
                alvo.animate.set_color({cor_destaque}).scale(1.1),
                Flash(alvo.get_center(), color={cor_destaque}, flash_radius=0.8),
            )
            self.wait(1)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
'''


# -------------------- 5. Definição → Exemplo --------------------
def gen_definicao_exemplo(p):
    titulo_def = str(p.get("titulo_def", "Definição"))
    latex_def = str(p.get("latex_def", r"f(x) = ax^2 + bx + c, \quad a \neq 0"))
    titulo_ex = str(p.get("titulo_ex", "Exemplo"))
    latex_ex = str(p.get("latex_ex", r"f(x) = 2x^2 - 3x + 1"))
    return f'''from manim import *

class DefinicaoExemplo(Scene):
    def construct(self):
        # ---------- Definição ----------
        cab_def = Text({titulo_def!r}, font_size=44, color=BLUE).to_edge(UP)
        caixa = SurroundingRectangle(cab_def, color=BLUE_B, buff=0.2, corner_radius=0.1)
        self.play(Write(cab_def))
        self.play(Create(caixa))

        eq_def = MathTex({latex_def!r}, font_size=56).move_to(ORIGIN)
        self.play(FadeIn(eq_def, shift=UP*0.4), run_time=1.2)
        self.wait(1.2)

        # Slide a definição para cima e diminui
        bloco_def = VGroup(cab_def, caixa, eq_def)
        self.play(bloco_def.animate.scale(0.55).to_edge(UP).shift(DOWN*0.2), run_time=1)
        linha = Line(LEFT*5.5, RIGHT*5.5, color=GREY_B).next_to(bloco_def, DOWN, buff=0.25)
        self.play(Create(linha))

        # ---------- Exemplo ----------
        cab_ex = Text({titulo_ex!r}, font_size=42, color=GREEN).next_to(linha, DOWN, buff=0.4)
        self.play(Write(cab_ex))

        eq_ex = MathTex({latex_ex!r}, font_size=60, color=GREEN).next_to(cab_ex, DOWN, buff=0.6)
        self.play(Write(eq_ex), run_time=1.4)
        self.wait(0.5)
        self.play(Circumscribe(eq_ex, color=GREEN, run_time=1.4))
        self.wait(1.8)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
'''


# -------------------- 6. Sequência de Equivalências --------------------
def gen_sequencia(p):
    titulo = str(p.get("titulo", "Sequência"))
    expressoes = _split_lines(p.get("expressoes", r"a^2 - b^2"
                                                   "\n(a-b)(a+b)"))
    if len(expressoes) < 2:
        raise ValueError("Informe ao menos 2 expressões LaTeX, uma por linha.")
    if len(expressoes) > 6:
        raise ValueError("Máximo de 6 expressões.")
    sep = str(p.get("separador", "="))
    cor_seta = str(p.get("cor_seta", "YELLOW"))
    return f'''from manim import *

class Sequencia(Scene):
    def construct(self):
        titulo = Text({titulo!r}, font_size=42, color=BLUE).to_edge(UP)
        self.play(Write(titulo))

        expressoes = {expressoes!r}
        separador = {sep!r}

        # Constrói a primeira expressão central
        atual = MathTex(expressoes[0], font_size=52).move_to(ORIGIN + UP*0.5)
        self.play(Write(atual), run_time=1)
        self.wait(0.5)

        # Para cada nova expressão: seta + sinal + nova expressão abaixo
        for expr in expressoes[1:]:
            seta = MathTex(r"\\Downarrow", font_size=44, color={cor_seta}).next_to(atual, DOWN, buff=0.3)
            nova = MathTex(separador + r"\\;" + expr, font_size=52).next_to(seta, DOWN, buff=0.3)
            self.play(GrowFromEdge(seta, UP), run_time=0.5)
            self.play(Write(nova), run_time=1)
            # Sobe tudo para abrir espaço
            grupo = Group(*[m for m in self.mobjects if m is not titulo])
            if grupo.get_bottom()[1] < -3:
                self.play(grupo.animate.shift(UP*1.4), run_time=0.6)
            atual = nova
            self.wait(0.4)

        # Destaca a última
        self.play(Circumscribe(atual, color=GREEN, run_time=1.4))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
'''


# -------------------- TEMPLATES registry --------------------
TEMPLATES = {
    "apresentacao": {
        "id": "apresentacao",
        "title": "Apresentação de Teorema",
        "description": "Título com slide-up + enunciado em LaTeX + caixa de destaque + autoria opcional.",
        "icon": "📜",
        "category": "Apresentação",
        "scene": "Apresentacao",
        "generator": gen_apresentacao,
        "params": [
            {"name": "titulo", "type": "text", "default": "Teorema de Pitágoras", "label": "Título"},
            {"name": "enunciado", "type": "latex", "default": r"a^2 + b^2 = c^2", "label": "Enunciado (LaTeX)"},
            {"name": "autoria", "type": "text", "default": "", "label": "Autoria (opcional)"},
            {"name": "cor_titulo", "type": "select", "default": "BLUE", "label": "Cor do título", "options": _color_options()},
            {"name": "cor_destaque", "type": "select", "default": "YELLOW", "label": "Cor do destaque", "options": _color_options()},
        ],
    },
    "passo_a_passo": {
        "id": "passo_a_passo",
        "title": "Resolução Passo a Passo",
        "description": "Sequência de equações LaTeX que se transformam suavemente uma na outra (TransformMatchingTex).",
        "icon": "🧮",
        "category": "Resolução",
        "scene": "PassoAPasso",
        "generator": gen_passo_a_passo,
        "params": [
            {"name": "titulo", "type": "text", "default": "Resolvendo a equação", "label": "Título"},
            {"name": "passos", "type": "list_latex", "default": "2x + 4 = 10\n2x = 10 - 4\n2x = 6\nx = 3",
             "label": "Passos em LaTeX", "hint": "Um passo por linha (até 8)."},
            {"name": "cor_destaque", "type": "select", "default": "GREEN", "label": "Cor do resultado", "options": _color_options()},
        ],
    },
    "comparacao": {
        "id": "comparacao",
        "title": "Comparação Lado a Lado",
        "description": "Duas expressões LaTeX entram pelos lados, separadas por uma linha, com seta de equivalência.",
        "icon": "⚖️",
        "category": "Comparação",
        "scene": "Comparacao",
        "generator": gen_comparacao,
        "params": [
            {"name": "titulo", "type": "text", "default": "Produto Notável", "label": "Título"},
            {"name": "label_a", "type": "text", "default": "Forma fatorada", "label": "Rótulo A"},
            {"name": "latex_a", "type": "latex", "default": r"(a+b)^2", "label": "LaTeX A"},
            {"name": "label_b", "type": "text", "default": "Forma expandida", "label": "Rótulo B"},
            {"name": "latex_b", "type": "latex", "default": r"a^2 + 2ab + b^2", "label": "LaTeX B"},
            {"name": "cor_a", "type": "select", "default": "BLUE", "label": "Cor A", "options": _color_options()},
            {"name": "cor_b", "type": "select", "default": "ORANGE", "label": "Cor B", "options": _color_options()},
        ],
    },
    "lista_cascata": {
        "id": "lista_cascata",
        "title": "Lista em Cascata",
        "description": "Itens (texto ou LaTeX) aparecem em FadeIn sequencial. Permite destacar um item.",
        "icon": "📋",
        "category": "Lista",
        "scene": "ListaCascata",
        "generator": gen_lista_cascata,
        "params": [
            {"name": "titulo", "type": "text", "default": "Propriedades da Adição", "label": "Título"},
            {"name": "itens", "type": "list_text", "default": "Comutativa: a + b = b + a\nAssociativa: (a+b)+c = a+(b+c)\nElemento neutro: a + 0 = a\nElemento oposto: a + (-a) = 0",
             "label": "Itens (um por linha)", "hint": "Um item por linha (até 8)."},
            {"name": "eh_latex", "type": "select", "default": "false", "label": "Itens são LaTeX?",
             "options": [{"value": "true", "label": "Sim (MathTex)"}, {"value": "false", "label": "Não (texto)"}]},
            {"name": "destaque_idx", "type": "number", "default": -1, "label": "Índice a destacar (0-base, -1 = nenhum)"},
            {"name": "cor_destaque", "type": "select", "default": "YELLOW", "label": "Cor do destaque", "options": _color_options()},
        ],
    },
    "definicao_exemplo": {
        "id": "definicao_exemplo",
        "title": "Definição → Exemplo",
        "description": "Mostra a definição em destaque, depois move-a para o topo e revela um exemplo abaixo.",
        "icon": "💡",
        "category": "Conceito",
        "scene": "DefinicaoExemplo",
        "generator": gen_definicao_exemplo,
        "params": [
            {"name": "titulo_def", "type": "text", "default": "Definição", "label": "Título da definição"},
            {"name": "latex_def", "type": "latex", "default": r"f(x) = ax^2 + bx + c, \quad a \neq 0", "label": "Definição em LaTeX"},
            {"name": "titulo_ex", "type": "text", "default": "Exemplo", "label": "Título do exemplo"},
            {"name": "latex_ex", "type": "latex", "default": r"f(x) = 2x^2 - 3x + 1", "label": "Exemplo em LaTeX"},
        ],
    },
    "sequencia": {
        "id": "sequencia",
        "title": "Sequência de Equivalências",
        "description": "Cadeia A ⇒ B ⇒ C ⇒ ... com setas verticais e destaque final.",
        "icon": "⛓️",
        "category": "Demonstração",
        "scene": "Sequencia",
        "generator": gen_sequencia,
        "params": [
            {"name": "titulo", "type": "text", "default": "Diferença de Quadrados", "label": "Título"},
            {"name": "expressoes", "type": "list_latex", "default": "a^2 - b^2\n(a-b)(a+b)",
             "label": "Expressões LaTeX", "hint": "Uma por linha (até 6)."},
            {"name": "separador", "type": "select", "default": "=", "label": "Símbolo entre expressões",
             "options": [
                 {"value": "=", "label": "Igualdade ="},
                 {"value": r"\equiv", "label": "Equivalente ≡"},
                 {"value": r"\Rightarrow", "label": "Implica ⇒"},
                 {"value": r"\therefore", "label": "Portanto ∴"},
             ]},
            {"name": "cor_seta", "type": "select", "default": "YELLOW", "label": "Cor das setas", "options": _color_options()},
        ],
    },
}


# -------------------- API --------------------

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
    t = p_def["type"]
    if t == "number":
        try:
            v = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Parâmetro '{p_def['label']}' deve ser numérico.")
        if math.isnan(v) or math.isinf(v):
            raise ValueError(f"Parâmetro '{p_def['label']}' inválido (NaN/Infinito).")
        return v
    if t == "select":
        valid = {o["value"] for o in p_def["options"]}
        if value not in valid:
            raise ValueError(f"Valor inválido para '{p_def['label']}'.")
        return value
    if t in ("text", "latex"):
        return "" if value is None else str(value)
    if t in ("list_text", "list_latex"):
        if isinstance(value, list):
            return "\n".join(str(x) for x in value)
        return "" if value is None else str(value)
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
