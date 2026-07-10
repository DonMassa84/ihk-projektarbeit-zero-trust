#!/usr/bin/env bash
set -Eeuo pipefail

# ── CONFIG ──────────────────────────────────────────────────────
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_SCRIPT="${REPO_DIR}/build_formal_final.py"
TEMPLATE="${REPO_DIR}/formal_template_final.tex"
SOURCE="${REPO_DIR}/docs/projektdokumentation.md"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUT_DIR="${REPO_DIR}/99_IHK_REBUILD_${TIMESTAMP}"
mkdir -p "${OUT_DIR}"

# ── BUILD LOG ───────────────────────────────────────────────────
exec > >(tee "${OUT_DIR}/BUILD_LOG.txt") 2>&1
echo "=== IHK PDF Build ${TIMESTAMP} ==="
echo "Repository: ${REPO_DIR}"
echo "Source:     ${SOURCE}"
echo "Script:     ${BUILD_SCRIPT}"
echo "Template:   ${TEMPLATE}"
echo ""

# ── 1. VALIDATE SOURCES ─────────────────────────────────────────
echo "=== 1/6 Validate Sources ==="
for f in "${SOURCE}" "${BUILD_SCRIPT}" "${TEMPLATE}"; do
  if [ ! -f "$f" ]; then echo "ERROR: $f not found"; exit 1; fi
done
echo "  All sources present."

# ── 2. BUILD PDF ────────────────────────────────────────────────
echo "=== 2/6 Build PDF ==="
cd "${REPO_DIR}"
rm -f 99_IHK_FINAL_EXPORT_20260710/tabellenverzeichnis.tex
python3 "${BUILD_SCRIPT}"
BUILD_PDF=$(ls -t 99_IHK_FINAL_EXPORT_20260710/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf 2>/dev/null | head -1)
if [ -z "${BUILD_PDF}" ]; then echo "ERROR: Build produced no PDF"; exit 1; fi
echo "  Built: ${BUILD_PDF}"

# ── 3. COPY TO OUTPUT ───────────────────────────────────────────
echo "=== 3/6 Copy to Output ==="
SEARCHABLE="${OUT_DIR}/PROJEKTARBEIT_ZERO_TRUST_SEARCHABLE.pdf"
cp "${BUILD_PDF}" "${SEARCHABLE}"
echo "  Searchable: ${SEARCHABLE}"

# ── 4. PDF VALIDATION ───────────────────────────────────────────
echo "=== 4/6 Validate PDF ==="

echo "  --- pdfinfo ---"
pdfinfo "${SEARCHABLE}" > "${OUT_DIR}/PDFINFO.txt"

echo "  --- pdffonts ---"
pdffonts "${SEARCHABLE}" > "${OUT_DIR}/PDFFONTS.txt"

echo "  --- pdftotext ---"
pdftotext "${SEARCHABLE}" "${OUT_DIR}/TEXT_EXTRACTION.txt"
WC=$(wc -w < "${OUT_DIR}/TEXT_EXTRACTION.txt")
echo "  Text extrahiert: ${WC} Wörter"

echo "  --- qpdf check ---"
qpdf --check "${SEARCHABLE}" 2>&1 | head -5

echo "  --- Unicode scan ---"
grep -nE '�|Figure [0-9]+: Abbildung|Tabelle [0-9]+: Tabelle|Abbildung [0-9]+: Abbildung' \
  "${OUT_DIR}/TEXT_EXTRACTION.txt" > "${OUT_DIR}/UNICODE_ERRORS.txt" || true
if [ -s "${OUT_DIR}/UNICODE_ERRORS.txt" ]; then
  echo "  WARNING: Unicode errors found!"
  cat "${OUT_DIR}/UNICODE_ERRORS.txt"
else
  echo "  Unicode check: CLEAN"
fi

echo "  --- Metadaten scan ---"
grep -nE 'ACCEPTED_CHANGES|MASTER_REVIEW|CHANGELOG_APPLIED|REJECTED_CHANGES|TODO|FIXME' \
  "${OUT_DIR}/TEXT_EXTRACTION.txt" > "${OUT_DIR}/METADATA_ERRORS.txt" || true
if [ -s "${OUT_DIR}/METADATA_ERRORS.txt" ]; then
  echo "  WARNING: Internal terms found!"
  cat "${OUT_DIR}/METADATA_ERRORS.txt"
else
  echo "  Metadaten scan: CLEAN"
fi

# ── 5. RENDER PAGES ─────────────────────────────────────────────
echo "=== 5/6 Render Pages ==="
RENDER_DIR="${OUT_DIR}/rendered"
mkdir -p "${RENDER_DIR}"
pdftoppm -png -r 150 "${SEARCHABLE}" "${RENDER_DIR}/page"
PAGES=$(ls "${RENDER_DIR}"/*.png | wc -l)
echo "  ${PAGES} pages rendered"

# ── 6. SHA256 + FINAL STATUS ────────────────────────────────────
echo "=== 6/6 Finalize ==="
cd "${OUT_DIR}"
sha256sum "$(basename "${SEARCHABLE}")" > SHA256SUMS.txt

cat > FINAL_STATUS.md << EOF
# Final Status

## Ergebnis
GREEN / YELLOW / RED

## Primäre PDF
SEARCHABLE: ${SEARCHABLE}

## Seitenzahl
${PAGES}

## SHA256
$(cut -d' ' -f1 SHA256SUMS.txt)

## Text durchsuchbar
$(if [ "${WC}" -gt 0 ]; then echo "JA (${WC} Wörter)"; else echo "NEIN"; fi)

## Unicode-Fehler
$(if [ -s UNICODE_ERRORS.txt ]; then echo "JA"; else echo "KEINE"; fi)

## Metadaten-Fehler
$(if [ -s METADATA_ERRORS.txt ]; then echo "JA"; else echo "KEINE"; fi)

## Git-Status
$(cd "${REPO_DIR}" && git status --short 2>/dev/null || echo "nicht verfügbar")

## Push
NEIN
EOF

echo ""
echo "=== BUILD COMPLETE ==="
echo "Output: ${OUT_DIR}"
echo "SHA256: $(cut -d' ' -f1 SHA256SUMS.txt)"
echo "Pages:  ${PAGES}"
echo "Words:  ${WC}"
echo ""
echo "Nächste Schritte:"
echo "  1. Visuelle Prüfung der gerenderten Seiten in ${RENDER_DIR}"
echo "  2. ggf. Flattened-Version erzeugen: mutool convert -o flatten.pdf searchable.pdf"
echo "  3. Entscheidungsbericht ausfüllen"
echo "  4. Kein Push ohne Freigabe"