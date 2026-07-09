#!/bin/bash
# strip_for_abgabe.sh
# Entfernt Arbeitsmarker ([Q: ...], OFFENE PUNKTE) aus der Markdown-Datei
# vor dem finalen PDF-Export.
#
# Usage: ./strip_for_abgabe.sh input.md output.md

set -euo pipefail

INPUT="${1:-}"
OUTPUT="${2:-}"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: $0 <input.md> <output.md>"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "Error: Input file '$INPUT' not found."
    exit 1
fi

echo "=== Strip for Abgabe ==="
echo "Input:  $INPUT"
echo "Output: $OUTPUT"

# 1. Alle Arbeitsmarker entfernen ([Q: ...], [BELEG FEHLT: ...], [WIDERSPRUCH: ...], [REDACTED: ...])
echo "[1/3] Removing work markers ([Q:], [BELEG FEHLT], [WIDERSPRUCH], [REDACTED])..."
perl -pe 's/\s*\[(Q|BELEG FEHLT|WIDERSPRUCH|REDACTED)[^\]]*\]//g' "$INPUT" > "${OUTPUT}.tmp1"

# 2. OFFENE PUNKTE-Abschnitt komplett entfernen
#    Alles von "## OFFENE PUNKTE" bis zum Ende der Datei
echo "[2/3] Removing OFFENE PUNKTE section..."
sed -E '/^## OFFENE PUNKTE/,$d' "${OUTPUT}.tmp1" > "${OUTPUT}.tmp2"

# 3. Aufräumen: mehrfache Leerzeilen reduzieren, Leerzeichen am Zeilenende entfernen
echo "[3/3] Cleaning up whitespace..."
sed -E \
    -e 's/[[:space:]]+$//' \
    -e '/^$/N;/^\n$/D' \
    "${OUTPUT}.tmp2" > "$OUTPUT"

# 4. Bereinigen
rm -f "${OUTPUT}.tmp1" "${OUTPUT}.tmp2"

# 5. Prüfen: Darf keine [Q:, OFFENE PUNKTE, BELEG FEHLT, WIDERSPRUCH, REDACTED] enthalten
echo ""
echo "=== Qualitätskontrolle ==="
VIOLATIONS=0
for PATTERN in '\[Q:' 'OFFENE PUNKTE' 'BELEG FEHLT' 'WIDERSPRUCH' 'REDACTED'; do
    if grep -q "$PATTERN" "$OUTPUT" 2>/dev/null; then
        echo "  ❌ GEFUNDEN: $PATTERN"
        VIOLATIONS=$((VIOLATIONS + 1))
    else
        echo "  ✅ OK: $PATTERN nicht vorhanden"
    fi
done

echo ""
if [ "$VIOLATIONS" -eq 0 ]; then
    echo "✅ FINAL GATE GREEN – $OUTPUT ist abgabebereit"
    echo "   Dateigröße: $(wc -c < "$OUTPUT") Bytes"
    echo "   Zeilenanzahl: $(wc -l < "$OUTPUT")"
    exit 0
else
    echo "❌ FINAL GATE RED – $VIOLATIONS Verstöße gefunden"
    exit 1
fi
