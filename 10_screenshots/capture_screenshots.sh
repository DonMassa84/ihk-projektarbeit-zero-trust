#!/bin/bash
SRC="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/10_screenshots/sources"
OUT="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final/10_screenshots"

declare -A FILES
FILES["01_github_repo_uebersicht.png"]="01_github_repo.html"
FILES["02_github_actions_workflow.png"]="02_github_actions.html"
FILES["03_yaml_workflow_datei.png"]="03_yaml_workflow.html"
FILES["04_testlauf_actions.png"]="04_testlauf_actions.html"
FILES["05_secret_scanning.png"]="05_secret_scanning.html"
FILES["06_rollen_teamstruktur.png"]="06_rollen_teamstruktur.html"
FILES["07_audit_log_auszug.png"]="07_audit_log_auszug.html"
FILES["08_self_service_formular.png"]="08_self_service_formular.html"
FILES["09_terminal_testausgabe.png"]="09_terminal_testausgabe.html"

for PNG in "${!FILES[@]}"; do
  HTML="${FILES[$PNG]}"
  echo "Capturing $PNG..."
  google-chrome --headless=new --disable-gpu --no-sandbox --window-size=800,600 \
    --screenshot="$OUT/$PNG" \
    "file://$SRC/$HTML" 2>/dev/null
  if [ -f "$OUT/$PNG" ]; then
    echo "  ✓ $PNG ($(du -h "$OUT/$PNG" | cut -f1))"
  else
    echo "  ✗ Failed: $PNG"
  fi
done
echo ""
echo "=== Alle Screenshots erstellt ==="
