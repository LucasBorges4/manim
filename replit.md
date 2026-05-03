# Manim Studio — Animações Matemáticas

Site em Python que monta templates Manim, executa o renderizador e devolve vídeos
matemáticos prontos. Frontend leve em HTML/CSS/JS, backend Flask.

## Estrutura

- `app.py` — Servidor Flask. Endpoints:
  - `GET /` — UI
  - `GET /api/templates` — lista templates
  - `POST /api/generate` — devolve o código Python Manim gerado
  - `POST /api/render` — gera o código, executa `manim` e devolve a URL do mp4
  - `GET /renders/<arquivo>` — serve os vídeos renderizados
- `manim_templates.py` — registry de templates parametrizados (8 templates):
  Função Quadrática, Bhaskara, Pitágoras, Função Linear, Círculo Trigonométrico,
  Derivada Visual, Soma de Frações, Sistema Linear 2×2.
- `manim_snippets.py` — biblioteca de **snippets** (blocos de código pequenos
  parametrizados) focados em transições e animações reutilizáveis. 20 snippets
  em 8 categorias (Introdução, Transições, Ênfase, Equações, Gráficos,
  Anotações, Geometria, Esqueletos). Exposto via API consumível por IA:
  - `GET /api/snippets` — lista
  - `GET /api/snippets/<id>` — detalhe
  - `POST /api/snippets/<id>/render` — substitui placeholders e devolve código
  - `GET /api/snippets/manifest` — manifesto JSON otimizado para LLM (descrição,
    params, requires_var, exemplo já renderizado, template bruto)
- `templates/index.html` — UI principal
- `static/style.css` — tema escuro estilo IDE
- `static/app.js` — interações: seleção de template, edição de parâmetros,
  preview de código com Prism.js, render e player de vídeo
- `renders/` — vídeos renderizados (cache temporário)
- Scripts originais Manim (`*.py` na raiz) — exemplos completos pré-existentes

## Como rodar

Workflow `Start application` roda `python3 app.py` na porta 5000.

## Dependências

- **Nix:** cairo, pango, pkg-config, ffmpeg, ghostscript, cairomm, pangomm, harfbuzz
- **Nix Python:** manim 0.19.0, flask, flask-cors
  (`nix profile install nixpkgs#python312Packages.{manim,flask,flask-cors}`)

## Templates

Cada template em `manim_templates.py` é uma função `gen_*(p)` que recebe os
parâmetros validados e devolve uma string com código Python Manim. Os valores
são interpolados como literais (não há f-string aninhada com LaTeX).

Para adicionar um template novo:
1. Escrever `gen_meu(p)` que retorna o código.
2. Adicionar entrada no dict `TEMPLATES` com `title`, `description`, `icon`,
   `category`, `scene` (nome da classe Scene gerada) e `params`.

## Renderização

`/api/render` gera código → escreve em diretório isolado → executa `manim -ql`
com `--media_dir` apontando para o diretório → copia o mp4 para `renders/` →
devolve URL pública. Timeout: 3 min.
