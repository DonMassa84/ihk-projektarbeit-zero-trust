# Hugging Face Dataset Candidates – Zero-Trust / GitHub-Security

## Entscheidung

Diese Datensätze sind nur Kandidaten für Recherche, Ausblick und spätere ML-Evaluation. Sie sind nicht automatisch Bestandteil der finalen IHK-PDF.

Vor Nutzung prüfen:

- Lizenz
- Datenqualität
- Personenbezug
- synthetisch vs. real
- Format
- Größe
- Zweckbindung
- Reproduzierbarkeit
- keine ungeprüften Leistungsbehauptungen

## Kandidatenliste

| Dataset | Quelle | Zweck | Relevanz | Risiko |
|---|---|---|---|---|
| darkknight25/Advanced_SIEM_Dataset | https://huggingface.co/datasets/darkknight25/Advanced_SIEM_Dataset | SIEM, Anomaly Detection, Threat Classification, UEBA | Hoch für Security-Event-Ausblick | synthetisch / Lizenz prüfen |
| DanCip/github-issues-vulnerability-detection | https://huggingface.co/datasets/DanCip/github-issues-vulnerability-detection | GitHub Issues mit CVE-Bezug | Sehr hoch für GitHub-Security-Kontext | Lizenz und Datenherkunft prüfen |
| kholil-lil/wazuh-alerts | https://huggingface.co/datasets/kholil-lil/wazuh-alerts | Wazuh Alerts, SIEM-Regelvalidierung, SOC-Dashboard | Hoch für SOC-/Audit-Ausblick | Felder auf Personenbezug prüfen |
| google/code_x_glue_cc_defect_detection | https://huggingface.co/datasets/google/code_x_glue_cc_defect_detection | Code Defect / Vulnerability Detection | Hoch für Code-Security-Review | nur Code-Klassifikation, nicht RBAC |
| arag0rn/SecVulEval | https://huggingface.co/datasets/arag0rn/SecVulEval | C/C++ Vulnerability Samples mit CVE/CWE-Metadaten | Mittel bis hoch für Vulnerability-Ausblick | Sprache/Stack passt ggf. nicht direkt |
| ukcli/Cybersecurity-Dataset-Heimdall-v1.1 | https://huggingface.co/datasets/ukcli/Cybersecurity-Dataset-Heimdall-v1.1 | Credential-Store-/Endpoint-Anomalien | Mittel für Zero-Trust-Ausblick | Lizenz/Struktur prüfen |
| Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset | https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset | Cybersecurity Instruction Tuning | Mittel für Q&A/Trainingsdaten | nicht als Faktenquelle verwenden |

## Empfohlene Nutzung im Projekt

Nur als Repo-Artefakt:

- Dataset-Scout
- Ausblick
- technische Bewertungsgrundlage
- keine Produktivbehauptung

## Nicht erlaubte Nutzung

- Keine echten personenbezogenen Daten trainieren.
- Keine vertraulichen Projektdaten hochladen.
- Keine finalen IHK-Behauptungen aus Dataset-Kandidaten ableiten.
- Keine Aussage „ML-Modell produktiv validiert", wenn nur Recherche erfolgt ist.
