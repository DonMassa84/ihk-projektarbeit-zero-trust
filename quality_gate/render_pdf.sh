#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="${1:-$PWD}"
cd "$ROOT"

PDF="$(python3 - <<'PY'
import json
from pathlib import Path
cfg=json.loads(Path("quality_gate/config/gate.json").read_text())
print(cfg["output_pdf"])
PY
)"

rm -rf quality_gate/rendered/*
mkdir -p quality_gate/rendered/pages

pdftoppm -png -r 120 "$PDF" quality_gate/rendered/pages/page >/dev/null

if command -v montage >/dev/null 2>&1; then
  montage quality_gate/rendered/pages/page-*.png \
    -thumbnail 240x340 -tile 4x -geometry +8+8 \
    quality_gate/rendered/contact_sheet.png
  echo "CONTACT_SHEET=quality_gate/rendered/contact_sheet.png"
else
  echo "Hinweis: ImageMagick 'montage' fehlt; Einzelseiten wurden gerendert."
fi
