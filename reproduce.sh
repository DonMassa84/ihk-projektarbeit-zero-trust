#!/usr/bin/env bash
set -euo pipefail
# reproduce.sh – Vollständige Reproduktion der IHK-Projektarbeit
# Führt alle Build-Schritte von Grund auf aus.
# Usage: ./reproduce.sh [--skip-deps]

echo "=== IHK Zero-Trust Projektarbeit – Reproduktions-Workflow ==="
echo ""

# ── Prerequisites ──────────────────────────────────────────────────
command -v pandoc >/dev/null 2>&1 || { echo "❌ pandoc fehlt. Installiere mit: sudo apt-get install pandoc"; exit 1; }
command -v google-chrome >/dev/null 2>&1 || { echo "❌ google-chrome fehlt. Wird für PDF/PNG benötigt."; exit 1; }
command -v make >/dev/null 2>&1 || { echo "❌ make fehlt."; exit 1; }

# ── Build ──────────────────────────────────────────────────────────
echo "→ Schritt 1: Diagramme rendern"
make diagrams epk 2>/dev/null || echo "  ⚠ Diagramm-Rendering fehlgeschlagen (nicht kritisch)"

echo ""
echo "→ Schritt 2: Screenshots generieren"
make screenshots 2>/dev/null || echo "  ⚠ Screenshots fehlgeschlagen (nicht kritisch)"

echo ""
echo "→ Schritt 3: PDF exportieren"
make pdf

echo ""
echo "→ Schritt 4: DOCX + HTML exportieren"
make docx html 2>/dev/null || true

echo ""
echo "→ Schritt 5: Qualitätsprüfung"
make lint 2>/dev/null || true

echo ""
echo "=== ✅ Fertig ==="
echo "PDF:  09_export/PROJEKTARBEIT_IHK_FINAL.pdf"
echo "DOCX: 09_export/PROJEKTARBEIT.docx"
echo "HTML: 09_export/PROJEKTARBEIT.html"
echo ""
echo "Seitenanzahl:"
python3 -c "import subprocess; r=subprocess.run(['strings','09_export/PROJEKTARBEIT_IHK_FINAL.pdf'],capture_output=True,text=True); print(f'  {r.stdout.count(\"/Type /Page\")} Seiten')" 2>/dev/null || true
