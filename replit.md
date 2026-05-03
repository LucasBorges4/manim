# Manim Educational Math Animations

A collection of Manim (Mathematical Animation Engine) scripts for creating educational math animations for high school students. Content is in Portuguese (Brazilian).

## Project Structure

- `example.py` — Basic Manim example (SquareToCircle)
- `advanced_example.py` — More advanced Manim demo
- `aritmetica_basica.py` — Basic arithmetic (primes, GCD, LCM, sign rules)
- `calculo_i_review.py` — Calculus I review
- `direction_field_edo.py` / `direction_field_edo2.py` / `direction_field_edo3.py` — ODE direction fields
- `equacoes_sistemas.py` — Equations and linear systems
- `estatistica_probabilidade.py` — Statistics and probability
- `exponential_resolution.py` — Exponential functions
- `fracao.py` / `fracao_suave.py` / `fracoes_ensino_medio.py` — Fractions
- `funcoes_graficos.py` — Functions and graphs
- `geometria_basica.py` — Basic geometry
- `norma_produto_escalar.py` — Vectors: norm and dot product
- `potencias_radiciacao.py` — Powers and radicals
- `soma_matrizes_r2.py` — Matrix addition in R²
- `trigonometria.py` — Trigonometry

## Setup

Manim Community v0.19.0 is installed via Nix. System dependencies (cairo, pango, ffmpeg, ghostscript) are also installed via Nix.

## How to Render Videos

```bash
manim -pql <filename>.py <ClassName>
```

**Quality flags:**
- `-pql` — Low quality, plays after render (good for development)
- `-pqm` — Medium quality
- `-pqh` — High quality
- `-pqf` — 4K quality

**Examples:**
```bash
manim -pql example.py SquareToCircle
manim -pql aritmetica_basica.py NumerosPrimos
manim -pql trigonometria.py CircunferenciaTrigonometrica
```

Rendered videos are saved to `media/videos/<filename>/<quality>/`.

## Dependencies

- **Nix packages:** cairo, pango, pkg-config, ffmpeg, ghostscript, cairomm, pangomm, harfbuzz
- **Python (via Nix):** manim 0.19.0 (installed via `nix profile install nixpkgs#python312Packages.manim`)
- **requirements.txt:** manim, numpy, scipy, pycairo, pango, ffmpeg-python
