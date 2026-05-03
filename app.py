"""
Servidor Flask para o estúdio de animações Manim.
Recebe parâmetros de templates, gera código Python, executa Manim e retorna o vídeo.
"""
import os
import re
import shutil
import subprocess
import tempfile
import uuid
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory, render_template

from manim_templates import TEMPLATES, generate_code, get_template_meta, get_scene_class

SCENE_RE = re.compile(r"class\s+([A-Za-z_]\w*)\s*\(\s*Scene\s*\)\s*:")
QUALITY_DIR = {"l": "480p15", "m": "720p30", "h": "1080p60"}


def _run_manim(code: str, scene: str, quality: str):
    """Executa Manim em diretório isolado e retorna (success, payload, status_code)."""
    if quality not in QUALITY_DIR:
        quality = "l"

    job_id = uuid.uuid4().hex[:12]
    work_dir = RENDERS_DIR / job_id
    work_dir.mkdir(parents=True, exist_ok=True)
    script_path = work_dir / "scene.py"
    script_path.write_text(code, encoding="utf-8")

    cmd = [
        "manim", "-q" + quality,
        "--media_dir", str(work_dir / "media"),
        "--disable_caching", "--format=mp4",
        str(script_path), scene,
    ]

    try:
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=180, cwd=str(work_dir),
            )
        except subprocess.TimeoutExpired:
            return False, {"error": "Renderização excedeu o tempo limite (3 min)."}, 504

        if result.returncode != 0:
            log = (result.stderr or "") + "\n" + (result.stdout or "")
            log_tail = "\n".join(log.strip().splitlines()[-50:])
            return False, {"error": "Falha ao renderizar Manim.", "log": log_tail}, 500

        video_dir = work_dir / "media" / "videos" / "scene" / QUALITY_DIR[quality]
        if not video_dir.exists():
            candidates = list((work_dir / "media" / "videos" / "scene").glob("*"))
            video_dir = candidates[0] if candidates else None
        if not video_dir or not video_dir.exists():
            return False, {"error": "Arquivo de vídeo não encontrado após render."}, 500

        mp4_files = [f for f in video_dir.glob("*.mp4")]
        if not mp4_files:
            return False, {"error": "Nenhum mp4 gerado."}, 500
        preferred = [f for f in mp4_files if f.stem == scene]
        mp4 = preferred[0] if preferred else mp4_files[0]

        public_name = f"{job_id}.mp4"
        shutil.copy(mp4, RENDERS_DIR / public_name)
        return True, {"video_url": f"/renders/{public_name}", "scene": scene}, 200
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

APP_DIR = Path(__file__).parent.resolve()
RENDERS_DIR = APP_DIR / "renders"
RENDERS_DIR.mkdir(exist_ok=True)

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/templates")
def api_templates():
    return jsonify({"templates": get_template_meta()})


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(force=True)
    template_id = data.get("template_id")
    params = data.get("params", {})
    try:
        code = generate_code(template_id, params)
        return jsonify({"code": code, "scene": get_scene_class(template_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/render", methods=["POST"])
def api_render():
    """Renderiza a partir de um template + parâmetros."""
    data = request.get_json(force=True)
    template_id = data.get("template_id")
    params = data.get("params", {})
    quality = data.get("quality", "l")
    try:
        code = generate_code(template_id, params)
        scene = get_scene_class(template_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    ok, payload, status = _run_manim(code, scene, quality)
    if ok:
        payload["code"] = code
    return jsonify(payload), status


@app.route("/api/render-code", methods=["POST"])
def api_render_code():
    """Renderiza qualquer código Manim editado pelo usuário."""
    data = request.get_json(force=True)
    code = data.get("code", "")
    quality = data.get("quality", "l")
    scene_override = data.get("scene")

    if not code.strip():
        return jsonify({"error": "Código vazio."}), 400
    if len(code) > 200_000:
        return jsonify({"error": "Código muito grande (>200KB)."}), 413

    # Detecta a classe Scene no código
    scenes = SCENE_RE.findall(code)
    if scene_override and scene_override in scenes:
        scene = scene_override
    elif scenes:
        scene = scenes[0]
    else:
        return jsonify({"error": "Nenhuma classe Scene encontrada. Certifique-se de ter algo como: class MinhaCena(Scene):"}), 400

    ok, payload, status = _run_manim(code, scene, quality)
    if ok:
        payload["scenes"] = scenes
    return jsonify(payload), status


@app.route("/renders/<path:filename>")
def serve_render(filename):
    return send_from_directory(RENDERS_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
