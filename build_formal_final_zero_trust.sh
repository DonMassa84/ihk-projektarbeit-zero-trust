#!/usr/bin/env bash
# build_formal_final_zero_trust.sh
# Formal-Final rebuild: 1-5 + Anhang 6 structure
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

TS=$(date +%Y%m%d_%H%M%S)
EXPORT="99_IHK_FINAL_EXPORT_20260710"
REPORTS="99_reports"
PDF="$EXPORT/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf"

echo "=== Formal Final Rebuild — $TS ==="

# 1. Create output dirs
mkdir -p "$EXPORT/images" "$REPORTS"

# 2. Build
python3 build_formal_final.py

# 3. Quality gate
TXT="$REPORTS/FORMAL_REBUILD_TEXTCHECK_${TS}.txt"
INFO="$REPORTS/FORMAL_REBUILD_PDFINFO_${TS}.txt"

pdftotext -layout "$PDF" "$TXT" 2>/dev/null || true
pdfinfo "$PDF" > "$INFO" 2>/dev/null || true

# 4. Check blockers
BLOCKERS="TODO|TODO_REALDATEN|PLATZHALTER|\[Name|Name des betrieblichen Betreuers|Name des IHK-Prüfers|EINTRAGEN|XXX|\boffen\b|\bausstehend\b|Testlauf ausstehend|Ausführung offen|Erfolgreiche Tests[[:space:]]+0|^# Anhang|# Anhang D|hardcoded"

if grep -nEi "$BLOCKERS" "$TXT" 2>/dev/null; then
    echo "FINAL-GATE: RED"
    exit 1
else
    echo "FINAL-GATE: GREEN"
fi

# 5. Info
PAGES=$(pdfinfo "$PDF" 2>/dev/null | grep Pages | awk '{print $2}')
SIZE=$(ls -lh "$PDF" | awk '{print $5}')
echo
echo "✓ Final PDF: $PDF"
echo "  Pages: $PAGES  Size: $SIZE"
echo "  Reports: $REPORTS/FORMAL_REBUILD_*_$TS.*"
