# IHK-PDF Quality Engine

Lokaler Qualitätsprozess für IHK-/Bachelor-Projektdokumentation.
Hugging Face nur als optionaler Review-/Research-Baustein.

## Sicherheitsgrenzen

- **Keine automatische externe Übertragung**
- **Keine Secrets/Token/personenbezogenen Daten an externe APIs**
- **Finale PDF bleibt lokal und reproduzierbar**
- **HF nur optional**

## Verzeichnisstruktur

```
tools/hf_pdf_quality/
├── README.md
├── hf_pdf_quality_check.py      # Hauptscript
├── hf_dataset_scout.py          # Datensatz-Recherche
├── prompts/                     # Prompt-Templates
│   ├── bachelor_chapter_review.prompt.md
│   ├── ihk_formal_review.prompt.md
│   ├── examiner_questions.prompt.md
│   └── prototype_claims_review.prompt.md
├── config/
│   └── review_config.yaml
└── requirements.txt
```

## Modi

```bash
# Lokaler Check (keine externe Verbindung)
python3 tools/hf_pdf_quality/hf_pdf_quality_check.py --mode local

# Mit lokalen HF-Modellen (falls installiert)
python3 tools/hf_pdf_quality/hf_pdf_quality_check.py --mode hf-local

# HF-API (nur vorbereitet, nicht aktiviert)
python3 tools/hf_pdf_quality/hf_pdf_quality_check.py --mode hf-api
```

## Final Gate

```bash
bash tools/hf_pdf_quality/run_final_quality_gate.sh
```

Erstellt:
- `reports/final_gate_<timestamp>/`
  - `PDFINFO.txt`
  - `QPDF_CHECK.txt`
  - `fulltext.txt`
  - `RISIKO_CHECK.txt`
  - `CHAPTER_REVIEW.md`
  - `FORMAL_RISK_REVIEW.md`
  - `PROTOTYPE_CLAIMS_REVIEW.md`
  - `EXAMINER_QUESTIONS.md`
  - `FINAL_RECOMMENDATION.md`
  - `SHA256SUMS.txt`

## Gate-Ampel

| Status | Bedeutung |
|--------|-----------|
| 🟢 GREEN | Keine harten Risiken. PDF einfrieren. |
| 🟡 YELLOW | Formale Hinweise. Manuell prüfen. |
| 🔴 RED | Platzhalter/offene Checkboxen. Korrigieren. |

## Abhängigkeiten

Minimal:
- `pdftotext` (poppler-utils)
- Python 3.8+

Optional:
- `qpdf` (PDF-Validierung)
- `pypdf` (Fallback Textextraktion)
- `pyyaml` (Config)
- `rich` (Formatierung)
- `transformers` (HF-Review)

## Empfehlung

1. Gate ausführen
2. Bei GREEN: PDF einfrieren
3. Bei YELLOW: Manuell prüfen, dann einfrieren
4. Bei RED: Korrigieren, neu bauen, Gate wiederholen
