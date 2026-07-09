#!/bin/bash
set -Eeuo pipefail

PROJECT_DIR="${1:-$PWD}"
OUT_DIR="$PROJECT_DIR/99_FINAL_CHECK_FIX_$(date +%Y%m%d_%H%M%S)"
REPORT="$OUT_DIR/ANALYSIS_REPORT.md"

mkdir -p "$OUT_DIR"

echo "# IHK Projektarbeit - FINAL CHECK FIX TOOL" > "$REPORT"
echo "## Status: Korrekturbedarf erkannt" >> "$REPORT"
echo "---" >> "$REPORT"
echo "" >> "$REPORT"

PDF1="$PROJECT_DIR/09_export/PROJEKTARBEIT_IHK_FINAL.pdf"
PDF2="$PROJECT_DIR/09_export/PROJEKTARBEIT_ZERO_TRUST_ABGABE_FINAL.pdf"
echo "### 1. Eingabedateien:" >> "$REPORT"
echo "- $PDF1 ($(du -h "$PDF1" | cut -d' ' -f1))" >> "$REPORT"
echo "- $PDF2 ($(du -h "$PDF2" | cut -d' ' -f1))" >> "$REPORT"
echo "" >> "$REPORT"

# Check PDFs
if [ ! -f "$PDF1" ]; then
    echo "⚠️  WARNUNG: PDF1 nicht gefunden" >> "$REPORT"
fi

echo "### 2. Probleme identifiziert:" >> "$REPORT"
echo "1. **Inhaltsverzeichnis**: Doppelte Einträge, unsaubere „Contents“ neben manuellem deutschem Verzeichnis möglich." >> "$REPORT"
echo "2. **Abbildungen**: Doppelte Beschriftungen (z.B. „Abb. X: Titel Abb. X: Titel“)" >> "$REPORT"
echo "3. **Wahrheitsunsicherheiten**: Reporter wie 100 % F1-Score, erfundene Unterschriften, realen Nachweise, die Prototypen suggerieren." >> "$REPORT"
echo "4. **Abnahmereferenz**: Wenn keine echte Unterschrift vorhanden ist, Simulations-/Vorlage-Terminologie in Transkript." >> "$REPORT"
echo "5. **Zahlen**: Harte „IST“-Zahlen ohne Nachweis; bedürfen Plausibilisierung." >> "$REPORT"
echo "6. **Projektdatei**: Solide, konzise Projektmanagement-Matrizen, Abgaben von Seiten 1-20 klar definiert" >> "$REPORT"

echo "" >> "$REPORT"
echo "### 3. Empfehlungen:" >> "$REPORT"
echo "- Verwenden Sie **vorhandene Quelldateien** im Projektordner (z.B. from: 09_export/final)." >> "$REPORT"
echo "- Wenn keine Quelldatei vorhanden ist, extrahieren Sie den PDF-Text und basieren Sie die Arbeits-/Quellarbeit darauf." >> "$REPORT"
echo "- Überprüfen Sie Projektmanager, Projektstrukturplan und Risikomatrix auf Lücken." >> "$REPORT"
echo "- Entfernen Sie Duplikateinträge in Abbildungs-/Tabellenverzeichnissen." >> "$REPORT"

echo "---" >> "$REPORT"
echo "## Nächste Schritte:" >> "$REPORT"
echo "1. Analysieren Sie die Quelldateien (z.B. `09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`)." >> "$REPORT"
echo "2. Bestimmen Sie Basis: PDF -> Markdown via `pdftotext`." >> "$REPORT"
echo "3. Verwenden Sie **vorhandene Quelldateien** im Projektordner." >> "$REPORT"
echo "4. Füllen Sie inkonsistente Teile auf (Abschreiben aus Quelldateien)." >> "$REPORT"
echo "5. Führen Sie die korrektur verbundenen Arbeiten durch und erstellen Sie `00_input/` + `export/` nach Bedarf." >> "$REPORT"

echo "---" >> "$REPORT"
echo "## Status: Korrekturhinweis manuell erforderlich" >> "$REPORT"

echo "=== CHEAT SHEET ==="
echo "Statten Sie den Arbeitsort zuerst korrekt ein:"
echo "cd /media/schattenmacher/USB-STICK1/usb\ 07.11.25/zero-trust-github-project"
echo "oder:"
echo "cd /home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final"
echo ""
echo "Jetzt führen Sie aus:"
echo "./00_final_check_fix_tool.sh"
echo ""
echo "Dann prüfen:"
echo "cat 99_FINAL_*/ANALYSIS_REPORT.md"
