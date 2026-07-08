#!/bin/bash
# Render Mermaid-Diagramme als PNG via Chrome Headless
# Alternative: npm install -g @mermaid-js/mermaid-cli

SRC_DIR="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/04_diagramme_mermaid"
OUT_DIR="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/04_diagramme_mermaid/png"
mkdir -p "$OUT_DIR"

TMP_HTML="/tmp/mermaid_render.html"

for MD_FILE in "$SRC_DIR"/*.md; do
  BASENAME=$(basename "$MD_FILE" .md)
  
  # Extract mermaid code block from md file
  MERMAID_CODE=$(sed -n '/```mermaid/,/```/p' "$MD_FILE" | sed '1d;$d')
  
  if [ -z "$MERMAID_CODE" ]; then
    echo "⚠ No mermaid code in $BASENAME"
    continue
  fi
  
  # Create HTML with mermaid
  cat > "$TMP_HTML" <<HTML
<!DOCTYPE html>
<html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>body{margin:0;padding:20px;background:white}svg{max-width:100%;height:auto}</style>
</head><body>
<div class="mermaid">
$MERMAID_CODE
</div>
<script>mermaid.initialize({startOnLoad:true,theme:'default'})</script>
</body></html>
HTML

  echo "Rendering $BASENAME..."
  google-chrome --headless=new --disable-gpu --no-sandbox --window-size=1200,900 \
    --screenshot="$OUT_DIR/${BASENAME}.png" \
    "file://$TMP_HTML" 2>/dev/null
  
  if [ -f "$OUT_DIR/${BASENAME}.png" ]; then
    echo "  ✓ $BASENAME.png ($(du -h "$OUT_DIR/${BASENAME}.png" | cut -f1))"
  else
    echo "  ✗ Failed: $BASENAME"
  fi
done

echo ""
echo "=== Diagramme gerendert: $OUT_DIR ==="
