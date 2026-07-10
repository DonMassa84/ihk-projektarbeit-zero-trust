# OpenCode-Masterprompt: IHK-Projektarbeit Zero-Trust-Pilot

Arbeite ausschliesslich im aktuellen Repository `/media/schattenmacher/USB-STICK1/usb 07.11.25/zero-trust-github-project`.

## Ziel

Optimiere die kanonische Markdown-Masterdatei `dokumentation.md` so lange iterativ, bis
`python3 quality_gate/ihk_gate.py --build`
mit `IHK_GATE=GREEN` und mindestens **90/100** endet.

Der Score ist ein internes Qualitätsgate und keine offizielle IHK-Punktzusage.

## Repository-Struktur

```
.
├── dokumentation.md                    ← Markdown-Master (einzige Textquelle)
├── erklaerung.pdf                      ← Eidesstattliche Erklärung (feste PDF)
├── PROJEKTARBEIT_IHK_FINAL_SIGNED.pdf  ← aktuelles Build-Output (21 Seiten)
├── quality_gate/                       ← Qualitäts-Gate-System
│   ├── ihk_gate.py                     ← Prüf-Engine + Build-Orchestrator
│   ├── config/gate.json                ← Thresholds, Regeln, Stack-Definition
│   ├── manual_review.json              ← manuelle Score-Eingabe (7 Kategorien)
│   ├── build_pdf.py                    ← Pandoc/XeLaTeX-Baupipeline
│   ├── render_pdf.sh                   ← PDF→PNG-Rendering
│   ├── freeze_release.sh               ← SHA256-Freeze mit GIT_HEAD
│   ├── reports/                        ← Build-Artefakte (gitignoriert)
│   └── prompts/OPENCODE_MASTER_PROMPT.md ← dieser Prompt
├── tools/
│   ├── reference_build_v13.py          ← ReportLab V13-Alternativbuild (63 Seiten)
│   └── v13_gap_reports/                ← Gap-Analyse V13 vs dokumentation.md
│       ├── PORT_STATUS.md
│       ├── DEPENDENCIES.md
│       ├── PDF_COMPARISON.md
│       ├── MARKDOWN_GAP_REPORT.md
│       └── DECISION_GATE.md
├── 08_assets/v13/                      ← V13-Diagramm-PNGs (gitignoriert)
├── 09_export/reference_v13/            ← V13-Referenz-PDFs (gitignoriert)
├── 99_IHK_ABGABE_FREEZE_20260710_080840/ ← letzter SHA256-Freeze
├── requirements.txt                    ← Backend-Dependencies (FastAPI, etc.)
├── requirements-v13.txt               ← V13-Build-Dependencies
└── .gitignore
```

## Build Pipelines

### Produktiv: Pandoc/XeLaTeX (21 Seiten)
```bash
python3 quality_gate/ihk_gate.py --build
```
- Quellen: `dokumentation.md` + `erklaerung.pdf`
- Output: `PROJEKTARBEIT_IHK_FINAL_SIGNED.pdf`
- Qualitätsgate inkludiert (Blockers, Warnings, 7 Kategorien)

### Referenz: ReportLab V13 (63 Seiten)
```bash
python3 -m venv .venv-v13
source .venv-v13/bin/activate
pip install -r requirements-v13.txt
MPLBACKEND=Agg python3 tools/reference_build_v13.py
```
- Output: `09_export/reference_v13/PROJEKTARBEIT_ZERO_TRUST_IHK_V13_90_GATE.pdf`
- V13 ist **Golden Reference**, nicht Build-Ersatz

## Qualitätsgate-Kategorien (100 Punkte)

| Kategorie | Max | Min | Aktuell |
|-----------|----:|----:|--------:|
| Formale Qualität | 15 | 13 | 14 |
| Projektmanagement | 20 | 18 | 19 |
| Technische Konsistenz | 15 | 14 | 15 |
| Evidenz/Traceability | 20 | 18 | 19 |
| Wirtschaftlichkeit | 10 | 8 | 9 |
| Sprache/Visualisierung | 10 | 9 | 10 |
| Release-Integrität | 10 | 9 | 10 |
| **Gesamt** | **100** | **90** | **96** |

## Unverhandelbare Regeln
1. Keine direkte PDF-Manipulation. Änderungen ausschliesslich in Markdown, Build-Konfiguration, Tabellen- oder Diagrammquellen.
2. Keine Tatsachen erfinden: keine Personen, Rollen, Unterschriften, Abnahmen, Nutzerzahlen, Commit-Hashes, Laufzeiten, Testergebnisse, Einsparungen oder Produktivdaten.
3. Unbelegte Aussagen entweder mit realem Nachweis belegen oder als Plan/Ist kennzeichnen.
4. Keine Eidesstattliche Erklärung ändern oder simulieren.
5. Alle Änderungen dokumentieren.
6. Der manuelle Review-Score in `quality_gate/manual_review.json` wird unabhaengig durch einen menschlichen Pruefer eingetragen.

## Bekannte Lücken (aus V13-Gap-Analyse)
- **Testfall-Anzahl:** dokumentation.md sagt 14/14 bestanden, V13 sagt 12/12 mit offenen Commit/Laufzeit-Spalten → **fachlicher Widerspruch**
- Fehlende Sektionen (Sperrvermerk, Zero-Trust-Prinzipien, RACI, Schnittstellen)
- Anhangsstruktur nicht an V13 A1-A12 angeglichen
- Keine automatischen Abbildungs-/Tabellenverzeichnisse im Pandoc-Build

## Workflow
1. `python3 quality_gate/ihk_gate.py --build` (baut PDF + statische Prüfung)
2. Bei Bedarf: `vim dokumentation.md` editieren
3. Wiederholen bis Gate=GREEN und Score ≥ 90
4. Vor Abgabe: `bash quality_gate/freeze_release.sh` für SHA256-Freeze

## V13-Referenz nutzen
```bash
# PDFs vergleichen
pypdf/compare lokal.pdf referenz.pdf
pdftoppm -png -r 110 lokal.pdf page  # Rendern
pdftoppm -png -r 110 referenz.pdf page
# Pixel-Diff per Python (siehe tools/v13_gap_reports/PDF_COMPARISON.md)
```
