#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="${1:-$PWD}"
cd "$ROOT"

python3 quality_gate/ihk_gate.py --root "$ROOT" --build

STAMP="$(date +%Y%m%d_%H%M%S)"
FREEZE="quality_gate/freeze/IHK_RELEASE_${STAMP}"
mkdir -p "$FREEZE"

python3 - <<PY
import json, shutil
from pathlib import Path
root=Path("$ROOT")
cfg=json.loads((root/"quality_gate/config/gate.json").read_text())
for rel in [cfg["source_markdown"], cfg["output_pdf"], "quality_gate/reports/gate.json", "quality_gate/reports/gate.md"]:
    p=root/rel
    shutil.copy2(p, Path("$FREEZE")/p.name)
PY

(
  cd "$FREEZE"
  sha256sum * > SHA256SUMS.txt
)
git rev-parse HEAD > "$FREEZE/GIT_HEAD.txt" 2>/dev/null || true
git status --porcelain > "$FREEZE/GIT_STATUS.txt" 2>/dev/null || true

echo "FREEZE=$FREEZE"
echo "Status: GREEN – interner Qualitätsgate-Stand, keine offizielle IHK-Bewertung."
