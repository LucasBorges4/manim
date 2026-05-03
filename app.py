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
    data = request.get_json(force=True)
    template_id = data.get("template_id")
    params = data.get("params", {})
    quality = data.get("quality", "l")  # l, m, h
    if quality not in ("l", "m", "h"):
        quality = "l"

    try:
        code = generate_code(template_id, params)
        scene = get_scene_class(template_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Diretório de trabalho isolado
    job_id = uuid.uuid4().hex[:12]
    work_dir = RENDERS_DIR / job_id
    work_dir.mkdir(parents=True, exist_ok=True)

    script_path = work_dir / "scene.py"
    script_path.write_text(code, encoding="utf-8")

    quality_dir_map = {"l": "480p15", "m": "720p30", "h": "1080p60"}

    cmd = [
        "manim",
        "-q" + quality,
        "--media_dir", str(work_dir / "media"),
        "--disable_caching",
        "--format=mp4",
        str(script_path),
        scene,
    ]

    try:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=180,
                cwd=str(work_dir),
            )
        except subprocess.TimeoutExpired:
            return jsonify({"error": "Renderização excedeu o tempo limite (3 min)."}), 504

        if result.returncode != 0:
            log = (result.stderr or "") + "\n" + (result.stdout or "")
            log_tail = "\n".join(log.strip().splitlines()[-40:])
            return jsonify({"error": "Falha ao renderizar Manim.", "log": log_tail}), 500

        # Localiza o mp4 gerado
        video_dir = work_dir / "media" / "videos" / "scene" / quality_dir_map[quality]
        if not video_dir.exists():
            candidates = list((work_dir / "media" / "videos" / "scene").glob("*"))
            video_dir = candidates[0] if candidates else None

        if not video_dir or not video_dir.exists():
            return jsonify({"error": "Arquivo de vídeo não encontrado após render."}), 500

        # Procura especificamente pelo mp4 com o nome da scene (ignora partials)
        mp4_files = [f for f in video_dir.glob("*.mp4") if "partial" not in f.parts[-2]]
        if not mp4_files:
            return jsonify({"error": "Nenhum mp4 gerado."}), 500
        # Prefere o arquivo cujo nome corresponde à scene class
        preferred = [f for f in mp4_files if f.stem == scene]
        mp4 = preferred[0] if preferred else mp4_files[0]

        public_name = f"{job_id}.mp4"
        public_path = RENDERS_DIR / public_name
        shutil.copy(mp4, public_path)

        return jsonify({
            "video_url": f"/renders/{public_name}",
            "code": code,
            "scene": scene,
        })
    finally:
        # Sempre libera o diretório de trabalho, sucesso ou falha
        shutil.rmtree(work_dir, ignore_errors=True)


@app.route("/renders/<path:filename>")
def serve_render(filename):
    return send_from_directory(RENDERS_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
