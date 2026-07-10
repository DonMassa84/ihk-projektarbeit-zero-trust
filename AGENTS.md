# AGENTS.md – Onboarding für KI-Assistenten

Dieses Repository enthält die IHK-Projektarbeit **"Zero-Trust-Sicherheitskonzept mit GitHub-Integration"** von Daniel Massa (Prüflingsnummer 615951).

## Schnellstart für eine neue KI-Session

1. **Zustand erfassen:**
   ```bash
   git log --oneline -5
   git status --short
   python3 quality_gate/ihk_gate.py 2>&1 | head -5
   ```

2. **Aktuelle Build-Konfiguration prüfen:**
   ```bash
   cat quality_gate/config/gate.json
   ```

3. **Offene Issues (V13-Gap-Analyse):**
   ```bash
   cat tools/v13_gap_reports/MARKDOWN_GAP_REPORT.md | head -10
   ```

4. **Master-Prompt lesen (vollständiger Kontext):**
   ```bash
   cat quality_gate/prompts/OPENCODE_MASTER_PROMPT.md
   ```

## Wichtige Dateien

| Datei | Zweck |
|-------|-------|
| `dokumentation.md` | **Einzige Textquelle** – alle Änderungen hier |
| `erklaerung.pdf` | Eidesstattliche Erklärung (wird hinten angehängt) |
| `quality_gate/ihk_gate.py --build` | PDF bauen + Quality Gate ausführen |
| `quality_gate/config/gate.json` | Schwellwerte, Verbote, Stack-Definition |
| `quality_gate/manual_review.json` | Manuelle Kategorie-Scores |
| `tools/reference_build_v13.py` | ReportLab-Referenzbuild (63 Seiten) |
| `tools/v13_gap_reports/` | Gap-Analyse V13 vs. dokumentation.md |

## Build-Befehle

```bash
# Produktiv-Build (21 Seiten, Pandoc/XeLaTeX)
python3 quality_gate/ihk_gate.py --build

# Nur Quality Gate (ohne Build)
python3 quality_gate/ihk_gate.py

# V13-Referenz-Build (63 Seiten, ReportLab)
python3 -m venv .venv-v13
source .venv-v13/bin/activate
pip install -r requirements-v13.txt
MPLBACKEND=Agg python3 tools/reference_build_v13.py

# Freeze (SHA256 + GIT_HEAD)
bash quality_gate/freeze_release.sh
```

## Git-Strategie

- `main` ist der einzige Branch
- Jeder Commit dokumentiert eine abgeschlossene Änderung
- Kein Force-Push
- Zwei Remotes:
  - `origin` → github.com/DonMassa84/zero-trust-github-integration
  - `zielrepo` → github.com/DonMassa84/ihk-projektarbeit-zero-trust

## Entscheidungen (nicht rückgängig machen)

| Entscheidung | Begründung |
|-------------|------------|
| Pandoc/XeLaTeX bleibt Haupt-Build | V13-ReportLab koppelt Inhalt/Layout zu stark |
| V13 ist Golden Reference | Qualitätspraktiken übernehmen, nicht den Build |
| 96/100 Quality Gate erreicht | 0 Blocker, 0 Warnings, 0 Validierungsfehler |
