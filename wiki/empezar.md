# Empezar

Cómo reproducir los resultados del proyecto.

**Prerequisitos:**
- Git
- Python 3.11+
- Las dependencias están en `requirements.txt` (raíz del repo)

**Clonar:**
```bash
git clone https://github.com/Editorenbici/rendering-universe.git
cd rendering-universe
pip install -r requirements.txt
```

**Estructura del repo:**
```
rendering-universe/
├── FUNDAMENTOS.md       — fuente única de verdad
├── PROTOCOLO.md         — reglas de operación
├── paper/               — solo del autor
├── code/analysis/       — scripts de experimentos
├── notes/               — notas técnicas
│   ├── foundations/     — lo vigente
│   ├── literature/      — revisión bibliográfica
│   ├── creative/        — storyboards, guiones
│   └── archive/         — desactualizado pero histórico
├── outputs/             — resultados numéricos
├── wiki/                — este wiki
└── requirements.txt
```

**Reproducir un experimento:**
```bash
# Ejemplo: Exp 15 (BAO)
python3 code/analysis/15_bao_likelihood.py --data official  --out outputs/exp15_results.json

# Exp 22 (interval geometry)
python3 code/analysis/22_interval_geometry_background.py --out outputs/exp22_results.json
```

**Colab de Codex** — próximamente, notebooks interactivos para reproducir los experimentos sin instalación local.

**Nota:** Los experimentos con estado GATED (Exp 20, Exp 25) requieren datos externos con provenance verificada. Ver `notes/experiments_manifest.md` para el estado actual de cada uno.
