"""
Manim Compiler - Compilador de linguagem natural para animações matemáticas.

Este módulo fornece a camada de compilação que:
1. Interpreta solicitações em linguagem natural
2. Seleciona templates e snippets apropriados
3. Compõe código Manim completo
4. Disparça renderização automática

Uso:
    from manim_compiler import compile_video
    code = compile_video("Mostre a fórmula de Bhaskara com exemplo numérico")
    # ou
    compile_video("Mostre a fórmula de Bhaskara com exemplo numérico", render=True)
"""

import hashlib
import json
import re
from pathlib import Path
from typing import Optional

from manim_templates import TEMPLATES, generate_code
from manim_snippets import SNIPPETS, render_snippet, get_snippet


# ---------- Cache ----------
CACHE_DIR = Path("cache_compilacao")
CACHE_DIR.mkdir(exist_ok=True)


def _cache_key(params: dict, template_id: str) -> str:
    """Gera chave de cache determinística."""
    content = json.dumps(params, sort_keys=True) + template_id
    return hashlib.md5(content.encode()).hexdigest()


def _cached_code(template_id: str, params: dict) -> Optional[str]:
    """Retorna código cached se existe."""
    key = _cache_key(params, template_id)
    cache_file = CACHE_DIR / f"{key}.py"
    if cache_file.exists():
        return cache_file.read_text()
    return None


def _save_cache(template_id: str, params: dict, code: str) -> None:
    """Salva código no cache."""
    key = _cache_key(params, template_id)
    (CACHE_DIR / f"{key}.py").write_text(code)


# ---------- Parser de Linguagem Natural ----------
INTENT_PATTERNS = {
    "apresentacao": [
        r"mostre\s+(?:a\s+)?(fórmula|teorema|identidade|regra)",
        r"(teorema|axioma|identidade)\s+(?:de\s+)?(\w+)",
        r"como\s+é\s+que\s+(?:se\s+)?(calcula|resolve)",
    ],
    "passo_a_passo": [
        r"resolve\s+(?:passo\s+a\s+passo\s+)?(\w+)",
        r"como\s+resolver\s+(\w+)",
        r"mostre\s+a\s+resolução\s+de",
        r"passo\s+a\s+passo",
    ],
    "definicao_exemplo": [
        r"definição\s+de\s+(\w+)",
        r"o\s+que\s+é\s+(\w+)",
        r"explicação\s+de\s+(\w+)",
        r"exemplo\s+de\s+(\w+)",
    ],
    "lista_cascata": [
        r"propriedades\s+de\s+(\w+)",
        r"lista\s+de\s+(\w+)",
        r"características\s+de\s+(\w+)",
        r"axiomas?\s+de\s+(\w+)",
    ],
    "comparacao": [
        r"compare\s+(\w+)\s+e\s+(\w+)",
        r"diferença\s+entre\s+(\w+)\s+e\s+(\w+)",
        r"equivalência\s+de\s+(\w+)",
        r"formas\s+diferentes\s+de",
    ],
    "sequencia": [
        r"demonstração\s+de\s+equivalência",
        r"mostre\s+que\s+(.+?)\s+é\s+igual",
        r"sequência\s+de\s+igualdades",
        r"transformação\s+algébrica",
    ],
}


def parse_intent(text: str) -> tuple[str, dict]:
    """
    Analisa texto e retorna (template_id, params).

    Exemplos:
        >>> parse_intent("Mostre a fórmula de Bhaskara")
        ('apresentacao', {'titulo': 'Fórmula de Bhaskara', ...})
    """
    text_lower = text.lower().strip()

    # Padrões especiais
    if any(k in text_lower for k in ["bhaskara", "bháskara", "equação do segundo grau"]):
        return "apresentacao", {
            "titulo": "Fórmula de Bhaskara",
            "enunciado": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            "cor_titulo": "GREEN",
            "cor_destaque": "YELLOW",
        }

    if any(k in text_lower for k in ["pitágoras", "pitagoras"]):
        return "apresentacao", {
            "titulo": "Teorema de Pitágoras",
            "enunciado": r"a^2 + b^2 = c^2",
            "cor_titulo": "BLUE",
            "cor_destaque": "GOLD",
        }

    if "resolução" in text_lower or "resolver" in text_lower:
        eq_match = re.search(r"([a-z]=.+?)(?:\.|$|\s*exemplo)", text_lower)
        eq = eq_match.group(1) if eq_match else "2x + 4 = 10"
        return "passo_a_passo", {
            "titulo": "Resolução",
            "passos": f"{eq}\nx = ...",
            "cor_destaque": "GREEN",
        }

    # Match genérico
    for template_id, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            match = re.search(pattern, text_lower)
            if match:
                return template_id, {"titulo": match.group(1).title() if match.group(1) else "Tema"}

    return "apresentacao", {"titulo": "Conteúdo", "enunciado": text[:50]}


# ---------- Composição ----------
def compose_scene(intents: list[tuple[str, dict]]) -> str:
    """
    Compõe múltiplas cenas em uma única scene file.

    Args:
        intents: Lista de (template_id, params)
    """
    scenes = []
    for template_id, params in intents:
        code = _cached_code(template_id, params)
        if code is None:
            code = generate_code(template_id, params)
            _save_cache(template_id, params, code)
        scenes.append(code)

    return "\n\n\n".join(scenes)


# ---------- API Principal ----------
def compile_video(
    prompt: str,
    render: bool = False,
    quality: str = "l",
    scene_name: Optional[str] = None,
    output_file: Optional[str] = None,
) -> str:
    """
    Compila uma solicitação em código Manim.

    Args:
        prompt: Solicitação em linguagem natural
        render: Se True, executa o render
        quality: Qualidade do vídeo (l/m/h)
        scene_name: Nome da cena (se vazio, usa primeiro template)
        output_file: Se True, salva em arquivo

    Returns:
        Código Python gerado
    """
    template_id, params = parse_intent(prompt)
    code = _cached_code(template_id, params)
    if code is None:
        code = generate_code(template_id, params)
        _save_cache(template_id, params, code)

    if output_file:
        Path(output_file).write_text(code)

    if render:
        from app import _run_manim
        scene = scene_name or TEMPLATES[template_id]["scene"]
        _run_manim(code, scene, quality)

    return code


# ---------- Batch Processor ----------
def compile_batch(prompts: list[str], output_dir: str = "generated") -> list[str]:
    """Compila múltiplas solicitações."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    codes = []

    for i, prompt in enumerate(prompts):
        code = compile_video(prompt)
        file_path = output_path / f"scene_{i}.py"
        file_path.write_text(code)
        codes.append(str(file_path))

    return codes


# ---------- CLI ----------
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python manim_compiler.py <prompt> [--render] [--output FILE]")
        sys.exit(1)

    prompt = sys.argv[1]
    render = "--render" in sys.argv
    output = "--output" in sys.argv and sys.argv[sys.argv.index("--output") + 1]

    code = compile_video(prompt, render=render, output_file=output)
    print(f"Código gerado:\n{code[:200]}...")