#!/bin/bash
# Export-Skript: IHK Projektarbeit DOCX/PDF
# Voraussetzung: pandoc, texlive-xelatex (für PDF)

SOURCE="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md"
OUTDIR="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/09_export"

echo "=== IHK Export-Skript ==="
echo "Quelle: $SOURCE"
echo ""

# DOCX exportieren
echo "Exportiere DOCX..."
pandoc "$SOURCE" \
  -f markdown \
  -t docx \
  -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.docx" \
  --metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
  --metadata author="Daniel Massa" \
  --metadata date="01.11.2026"
echo "DOCX erstellt: $OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.docx"
echo ""

# PDF exportieren (wenn xelatex verfügbar)
if command -v xelatex &> /dev/null; then
  echo "Exportiere PDF..."
  pandoc "$SOURCE" \
    -f markdown \
    -t pdf \
    -o "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.pdf" \
    --pdf-engine=xelatex \
    --metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
    --metadata author="Daniel Massa" \
    --metadata date="01.11.2026"
  echo "PDF erstellt: $OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.pdf"
else
  echo "xelatex nicht gefunden. PDF-Export übersprungen."
  echo "Installation: sudo apt install texlive-xelatex texlive-lang-german"
fi

echo ""
echo "=== Export abgeschlossen ==="
