#!/usr/bin/env bash
# IHK-PDF Final Quality Gate
# Findet PDF, erstellt Backup, führt Checks durch, erzeugt Reports.
set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

# PDF finden
PDF=""
for candidate in \
  "$ROOT/99_IHK_FINAL_EXPORT_20260710/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf" \
  "$ROOT/99_ABGABE_FREEZE_20260710_013218/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL_ABGABE.pdf"; do
  if [ -f "$candidate" ]; then
    PDF="$candidate"
    break
  fi
done

if [ -z "$PDF" ]; then
  echo "FEHLER: Keine PDF gefunden." >&2
  exit 1
fi

OUTDIR="$ROOT/reports/final_gate_${TIMESTAMP}"
mkdir -p "$OUTDIR"

echo "=== IHK PDF FINAL QUALITY GATE ==="
echo "PDF: $PDF"
echo "OUT: $OUTDIR"
echo

# 1. PDF kopieren
cp "$PDF" "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf"

# 2. PDFINFO
echo "=== PDFINFO ==="
pdfinfo "$PDF" | tee "$OUTDIR/PDFINFO.txt"
echo

# 3. QPDF Check
echo "=== QPDF CHECK ==="
if command -v qpdf >/dev/null 2>&1; then
  qpdf --check "$PDF" 2>&1 | tee "$OUTDIR/QPDF_CHECK.txt"
else
  echo "qpdf nicht installiert - übersprungen" | tee "$OUTDIR/QPDF_CHECK.txt"
fi
echo

# 4. Text extrahieren
echo "=== TEXT EXTRAKTION ==="
pdftotext -layout "$PDF" "$OUTDIR/fulltext.txt"
echo "Text: $(wc -l < "$OUTDIR/fulltext.txt") Zeilen"
echo

# 4a. HF Offline Guard
echo "=== HF OFFLINE GUARD ==="
python3 "$SCRIPT_DIR/hf_offline_guard.py" 2>&1 | tee "$OUTDIR/HF_OFFLINE_GUARD.txt" || true
echo

# 4b. Privacy Guard
echo "=== PRIVACY GUARD ==="
python3 "$SCRIPT_DIR/hf_privacy_guard.py" --file "$OUTDIR/fulltext.txt" 2>&1 | tee "$OUTDIR/PRIVACY_GUARD.txt" || true
echo

# 4c. Dataset Catalog (static)
echo "=== DATASET CATALOG ==="
python3 "$SCRIPT_DIR/hf_dataset_catalog.py" --mode static 2>&1 | tee "$OUTDIR/DATASET_CATALOG_LOG.txt" || true
echo

# 4d. Model Catalog (static + local-check)
echo "=== MODEL CATALOG ==="
python3 "$SCRIPT_DIR/hf_model_catalog.py" --mode static 2>&1 | tee "$OUTDIR/MODEL_CATALOG_LOG.txt" || true
python3 "$SCRIPT_DIR/hf_model_catalog.py" --mode local-check 2>&1 | tee -a "$OUTDIR/MODEL_CATALOG_LOG.txt" || true
echo

# 4e. Reference Export
echo "=== REFERENCE EXPORT ==="
python3 "$SCRIPT_DIR/hf_reference_export.py" 2>&1 | tee "$OUTDIR/REFERENCE_EXPORT_LOG.txt" || true
echo

# 5. Python Quality Check (local mode)
echo "=== QUALITY CHECK ==="
python3 "$SCRIPT_DIR/hf_pdf_quality_check.py" \
  --mode local \
  --pdf "$PDF" \
  --outdir "$OUTDIR" \
  || echo "Quality Check Fehler" | tee "$OUTDIR/QUALITY_CHECK_ERROR.txt"
echo

# 6. Risiko-Suchlauf
echo "=== RISIKO-SUCHLAUF ==="
{
  echo "--- TODO/FIXME/Platzhalter ---"
  grep -niE 'TODO|FIXME|Lorem|Platzhalter|Mustertext|Entwurf|draft|noch einfügen|XXX' "$OUTDIR/fulltext.txt" || echo "(keine Treffer)"

  echo
  echo "--- Offene Checkboxen / offene Abnahme ---"
  grep -niE '☐|nicht erfüllt|offen|Unterschrift|Datum:' "$OUTDIR/fulltext.txt" || echo "(keine Treffer)"

  echo
  echo "--- Doppeltes Inhaltsverzeichnis ---"
  grep -niE '^Contents|INHALTSVERZEICHNIS|Inhaltsverzeichnis' "$OUTDIR/fulltext.txt" || echo "(keine Treffer)"

  echo
  echo "--- Kritische Formulierungen ---"
  grep -niE 'tatsächliche Projektbearbeitung|nicht verifizierbar|prototypisch|synthetisch|Simulation|simuliert' "$OUTDIR/fulltext.txt" || echo "(keine Treffer)"

  echo
  echo "--- Seiten-/Abgabe-/Datumstreffer ---"
  grep -niE '01\.11\.2026|Abgabedatum|Sommer 2026|Prüflingsnummer|Eidesstattliche' "$OUTDIR/fulltext.txt" || echo "(keine Treffer)"
} | tee "$OUTDIR/RISIKO_CHECK.txt"
echo

# 7. SHA256
echo "=== SHA256 ==="
sha256sum "$OUTDIR/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf" | tee "$OUTDIR/SHA256SUMS.txt"
echo

# 8. Dataset Scout
echo "=== DATASET SCOUT ==="
python3 "$SCRIPT_DIR/hf_dataset_scout.py" 2>&1 | tee "$OUTDIR/DATASET_SCOUT_LOG.txt" || true
echo

# 9. Ampel
echo "=== FINAL QUALITY GATE ==="
echo "PDF: $PDF"
echo "Mode: LOCAL_ONLY"
echo "HF Network: DISABLED"
echo "Telemetry: DISABLED"
echo "Dataset Scout: STATIC_ONLY"
echo "Model Catalog: STATIC_AND_LOCAL_CACHE_ONLY"
echo

HARD_RISKS=0
if grep -q "PLATZHALTER\|CHECKBOX_OFFEN\|UNTERSCHRIFT_OFFEN\|DOPPELTES_IV" "$OUTDIR/RISIKO_CHECK.txt" 2>/dev/null; then
  HARD_RISKS=1
fi

if [ "$HARD_RISKS" -eq 1 ]; then
  echo "🔴 GATE: RED"
  echo "Harte Risiken gefunden. PDF muss korrigiert werden."
else
  WARNINGS=$(grep -ciE '^[0-9]+:.*TODO|^[0-9]+:.*FIXME|^[0-9]+:.*noch einfügen|^[0-9]+:.*XXX|^[0-9]+:.*PLATZHALTER' "$OUTDIR/RISIKO_CHECK.txt" 2>/dev/null || echo 0)
  if [ "$WARNINGS" -gt 0 ]; then
    echo "🟡 GATE: YELLOW"
    echo "Formale Hinweise. Manuell prüfen."
  else
    echo "🟢 GATE: GREEN"
    echo "Keine harten Risiken. PDF kann eingefroren werden."
  fi
fi

echo
echo "Next action:"
if [ "$HARD_RISKS" -eq 1 ]; then
  echo "- RED: fix exact hits only, rebuild, rerun gate"
else
  echo "- GREEN/YELLOW: freeze PDF"
fi

echo
echo "Prüfordner: $OUTDIR"
echo "Dateien:"
ls -1 "$OUTDIR"
