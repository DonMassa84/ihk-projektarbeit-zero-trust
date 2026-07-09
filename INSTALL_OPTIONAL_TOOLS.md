# Installation optionaler Tools — IHK Zero-Trust Projektarbeit

**Stand:** 09.07.2026  
**Ziel:** Vollständige Export-Pipeline (Markdown → DOCX/PDF/HTML) + Diagramm-Rendering + KI-Bildgenerierung

---

## 1. System-Pakete (Ubuntu / Debian / Mint)

```bash
# Basis: Pandoc, LaTeX, LibreOffice, GraphViz, Mermaid, PlantUML
sudo apt update && sudo apt install -y \
  pandoc \
  texlive-xetex texlive-lang-german texlive-fonts-recommended texlive-latex-extra \
  libreoffice \
  graphviz \
  default-jre \
  nodejs npm \
  python3-venv python3-pip \
  fonts-liberation fonts-dejavu \
  curl wget gnupg
```

### Mermaid CLI (mmdc) — für SVG-Export der Diagramme
```bash
# Via npm (Node.js 18+ erforderlich)
sudo npm install -g @mermaid-js/mermaid-cli

# Test
mmdc --version
```

### PlantUML — für UML/EPK/ERD
```bash
# JAR herunterlegen (oder via apt: plantuml)
mkdir -p ~/opt/plantuml
wget -q https://github.com/plantuml/plantuml/releases/download/v1.2024.1/plantuml-1.2024.1.jar \
  -O ~/opt/plantuml/plantuml.jar

# Wrapper-Skript
cat > ~/bin/plantuml << 'EOF'
#!/bin/bash
java -jar ~/opt/plantuml/plantuml.jar "$@"
EOF
chmod +x ~/bin/plantuml
export PATH="$HOME/bin:$PATH"
```

### Typst (Alternative zu LaTeX, schneller, moderner)
```bash
# Via cargo (Rust) oder binary
curl -L --proto '=https' --tlsv1.2 -sSf https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-gnu.tar.gz | tar xz -C /usr/local/bin
# oder: cargo install --locked typst-cli
```

### WeasyPrint (HTML → PDF, Alternative zu LaTeX)
```bash
# System-Deps
sudo apt install -y \
  python3-dev python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangocairo-1.0-0

# Python-Paket
pip3 install --break-system-packages weasyprint
```

---

## 2. Python Virtual Environment (empfohlen)

```bash
cd ~/openclaw-workspace/ihk_zero_trust_projektarbeit_final
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Core-Pakete (requirements.txt — Core)
```text
pandas>=2.0
matplotlib>=3.7
python-docx>=1.1
pypandoc>=1.13
jinja2>=3.1
pillow>=10.0
huggingface_hub>=0.20
datasets>=2.15
sentencepiece>=0.1.99
safetensors>=0.4
```

### Optional: KI / ML (für Bildgenerierung / Evaluation)
```bash
# Nur wenn GPU + CUDA verfügbar
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install diffusers transformers accelerate sentencepiece safetensors
```

---

## 3. Export-Tools im Projekt

### Pandoc + XeLaTeX (Standard, höchste PDF-Qualität)
```bash
# Test
cd ~/openclaw-workspace/ihk_zero_trust_projektarbeit_final
pandoc 09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md \
  --pdf-engine=xelatex \
  -V geometry:"top=2.5cm,bottom=2.5cm,left=3cm,right=2cm" \
  -V fontsize=12pt -V linestretch=1.5 \
  -V fontfamily=libertine -V lang=de-DE \
  --toc --toc-depth=3 --number-sections \
  -o test_output.pdf
```

### LibreOffice (DOCX → PDF Fallback)
```bash
# Headless Conversion
libreoffice --headless --convert-to pdf \
  --outdir 09_export \
  09_export/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.docx
```

### WeasyPrint (HTML → PDF, schnell, gut für Web-Preview)
```bash
python3 -c "
import weasyprint
weasyprint.HTML('09_export/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.html').write_pdf('export/weasyprint_output.pdf')
"
```

---

## 4. Diagramm-Export Scripts

### Mermaid → SVG (alle .mmd Dateien)
```bash
#!/bin/bash
# scripts/export_mermaid.sh
SRC="diagrams/mermaid"
OUT="diagrams/exported"
mkdir -p "$OUT"

for f in "$SRC"/*.mmd; do
  base=$(basename "$f" .mmd)
  echo "Exporting $base..."
  mmdc -i "$f" -o "$OUT/${base}.svg" -b transparent -w 1200
done
```

### PlantUML → SVG (alle .puml Dateien)
```bash
#!/bin/bash
# scripts/export_plantuml.sh
SRC="diagrams/plantuml"
OUT="diagrams/exported"
mkdir -p "$OUT"

for f in "$SRC"/*.puml; do
  base=$(basename "$f" .puml)
  echo "Exporting $base..."
  plantuml -tsvg -o "$OUT" "$f"
done
```

### Mermaid Theme Config (für IHK-Farben)
```json
// diagrams/mermaid/theme_ihk.json
{
  "themeVariables": {
    "primaryColor": "#2E5C8A",
    "primaryTextColor": "#1B1F24",
    "primaryBorderColor": "#D1D5DB",
    "lineColor": "#4B5563",
    "secondaryColor": "#4A8FC7",
    "tertiaryColor": "#F3F4F6",
    "background": "#FFFFFF",
    "mainBkg": "#FFFFFF",
    "secondBkg": "#F3F4F6",
    "tertiaryBkg": "#E5E7EB",
    "textColor": "#1B1F24",
    "fontFamily": "Liberation Sans, Arial, sans-serif",
    "fontSize": "12px",
    "nodeBorder": "#1B1F24",
    "clusterBkg": "#F9FAFB",
    "clusterBorder": "#2E5C8A"
  }
}
```
```bash
mmdc -i diagram.mmd -o diagram.svg -t diagrams/mermaid/theme_ihk.json
```

---

## 5. Build-Skript (All-in-One)

```bash
#!/bin/bash
# scripts/build_document.sh
set -Eeuo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$PROJECT_ROOT/09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md"
OUTDIR="$PROJECT_ROOT/09_export"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=== IHK Dokument Build $TIMESTAMP ==="
echo "Source: $SRC"
echo "Outdir: $OUTDIR"

# 1. Diagramme exportieren
echo "--- Exporting Mermaid diagrams ---"
bash "$PROJECT_ROOT/scripts/export_mermaid.sh"

echo "--- Exporting PlantUML diagrams ---"
bash "$PROJECT_ROOT/scripts/export_plantuml.sh"

# 2. DOCX (immer funktioniert)
echo "--- Building DOCX ---"
pandoc "$SRC" \
  -f markdown -t docx \
  -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.docx" \
  --metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
  --metadata author="Daniel Massa" \
  --metadata date="01.11.2026" \
  --reference-doc="$PROJECT_ROOT/templates/ihk_reference.docx" 2>/dev/null || \
  pandoc "$SRC" -f markdown -t docx -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.docx"

# 3. PDF via XeLaTeX (Preferred)
echo "--- Building PDF (XeLaTeX) ---"
if command -v xelatex &>/dev/null; then
  pandoc "$SRC" \
    -f markdown -t pdf \
    --pdf-engine=xelatex \
    -V geometry:"top=2.5cm,bottom=2.5cm,left=3cm,right=2cm" \
    -V fontsize=12pt -V linestretch=1.5 \
    -V fontfamily=liberation -V lang=de-DE \
    --toc --toc-depth=3 --number-sections \
    -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.pdf"
  echo "✅ PDF (XeLaTeX) created"
else
  echo "⚠️ xelatex nicht gefunden — versuche WeasyPrint..."
  # Fallback: WeasyPrint
  python3 -c "
import weasyprint, sys
weasyprint.HTML('$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.docx').write_pdf('$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.pdf')
  " 2>/dev/null && echo "✅ PDF (WeasyPrint) created" || echo "❌ PDF-Export fehlgeschlagen"
fi

# 4. HTML (Preview)
echo "--- Building HTML ---"
pandoc "$SRC" -f markdown -t html5 --standalone \
  -c "$PROJECT_ROOT/templates/ihk_style.css" \
  -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_${TIMESTAMP}.html"

echo "=== Build completed ==="
ls -lh "$OUTDIR/"*_${TIMESTAMP}.*
```

---

## 6. Prüfung der Installation

```bash
# Quick Check
echo "=== Tool Versions ==="
pandoc --version | head -1
xelatex --version | head -1 || echo "xelatex: NICHT INSTALLIERT"
libreoffice --version | head -1
mmdc --version 2>/dev/null || echo "mmdc: NICHT INSTALLIERT"
plantuml -version 2>/dev/null | head -1 || echo "plantuml: NICHT INSTALLIERT"
python3 -c "import weasyprint; print('weasyprint:', weasyprint.__version__)" 2>/dev/null || echo "weasyprint: NICHT INSTALLIERT"
typst --version 2>/dev/null || echo "typst: NICHT INSTALLED"

# Python Env
source .venv/bin/activate
python -c "import pandas, matplotlib, docx, pypandoc, jinja2, PIL, huggingface_hub, datasets; print('Python deps: OK')"
```

---

## 7. Troubleshooting

| Problem | Lösung |
|---------|--------|
| `xelatex: command not found` | `sudo apt install texlive-xetex texlive-lang-german texlive-fonts-recommended texlive-latex-extra` |
| `Font 'Liberation Sans' not found` | `sudo apt install fonts-liberation` oder `-V fontfamily=dejavu` |
| `mmdc: not found` | `sudo npm install -g @mermaid-js/mermaid-cli` (Node 18+) |
| `plantuml: java not found` | `sudo apt install default-jre` |
| `weasyprint: Cairo error` | `sudo apt install libcairo2 libpango-1.0-0 libgdk-pixbuf-2.0-0` |
| `pandoc: Could not find reference.docx` | `--reference-doc` weglassen oder `templates/ihk_reference.docx` anlegen |
| `Dateigröße > 50 MB` | Bilder komprimieren: `pngquant --quality=70-85 *.png` / `jpegoptim --max=85 *.jpg` |

---

## 8. Empfohlener Minimal-Setup (wenn Zeit knapp)

```bash
# Nur das Nötigste für PDF + DOCX
sudo apt install -y pandoc texlive-xetex texlive-lang-german texlive-fonts-recommended libreoffice
pip3 install --break-system-packages pypandoc python-docx
# Fertig. Baut DOCX + PDF (via XeLaTeX).
```

---

*Stand: 09.07.2026 | Nächstes Update nach Build-Test*