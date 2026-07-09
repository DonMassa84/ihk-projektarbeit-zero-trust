---
language: de
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: microsoft/codebert-base
tags:
  - zero-trust
  - anomaly-detection
  - security
  - audit-logs
  - ihk-project
---

# Zero-Trust Anomaly Detector

## Model Description

Ein feinetuniertes **CodeBERT**-Modell zur Erkennung von Anomalien in Audit-Logs eines Zero-Trust-Sicherheitssystems. Entwickelt im Rahmen der IHK-Projektarbeit "Zero-Trust-Sicherheitskonzept mit GitHub-Integration".

## Intended Use

- **Klassifikation** von Audit-Log-Einträgen als normal oder anomal
- **Echtzeit-Überwachung** von Rollen- und Berechtigungsänderungen
- **Security Incident Detection** bei verdächtigen Aktivitäten

## Training Data

- Synthetische Audit-Logs basierend auf RBAC-Workflow-Mustern
- Reale GitHub-Action-Logs aus CI/CD-Pipelines
- DSGVO-konform: Keine personenbezogenen Daten im Training

## Performance (experimentell, auf synthetischen Testdaten)

| Metrik | Wert |
|--------|------|
| Accuracy | ~85% |
| Precision | ~83% |
| Recall | ~82% |
| F1-Score | ~82% |
| AUC-ROC | ~0.89 |

> **Wichtiger Hinweis:** Diese Werte wurden auf einem kleinen, synthetischen Datensatz ermittelt. Das Modell ist ein experimenteller Machbarkeitsnachweis und **nicht für den Produktiveinsatz bestimmt**. Reale Performance kann erheblich abweichen.

## Usage (Demo)

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="DonMassa84/zero-trust-anomaly-detector",
)

result = classifier("ROLE_ESCALATION by admin on super-admin-role")
print(result)
# [{'label': 'ANOMALY', 'score': 0.89}]
```

## Limitations

- **Experimenteller Status:** Das Modell ist ein Proof-of-Concept, kein produktives System
- Trainiert auf synthetischen Daten → reale Performance kann abweichen
- Erkennt nur Muster aus Trainingsdaten → neue Angriffsmuster können übersehen werden
- Sprachmodell ist Deutsch/Englisch, Code-Mixing kann die Performance beeinträchtigen
- Keine Zertifizierung für sicherheitskritische Anwendungen

## Ethical Considerations

- **Privacy:** Das Modell speichert keine Log-Daten. Inference läuft lokal.
- **False Positives:** Bei kritischen Systemen immer menschliche Überprüfung erforderlich.
- **Bias:** Keine demografischen Merkmale in den Trainingsdaten enthalten.

## Citation

```bibtex
@misc{massa2025zerotrust,
  author = {Massa, Daniel-Alfonsin},
  title = {Zero-Trust Security Concept with GitHub Integration},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/DonMassa84/zero-trust-github-integration}
}
```