#!/usr/bin/env python3
"""
HF Dataset Scout — Recherche-/Dokumentationsstruktur für mögliche spätere Nutzung.
Kein großer Download. Nur Kandidatenliste und Lizenzprüfung.
"""
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORTS = ROOT / "reports"

DATASETS = [
    {
        "name": "SIEM/Security Logs",
        "suchbegriffe": ["wazuh alerts", "siem logs", "security event", "intrusion detection"],
        "zweck": "Training für Anomalieerkennung in Security-Events",
        "lizenz": "Prüfung erforderlich (CC-BY, MIT, proprietär)",
        "risiko": "Kann personenbezogene IPs/Hostnames enthalten",
    },
    {
        "name": "Wazuh Alerts",
        "suchbegriffe": ["wazuh", "ossec", "alert classification"],
        "zweck": "Klassifikation von Sicherheitsalerts",
        "lizenz": "Apache 2.0 (Wazuh selbst), Datasets variieren",
        "risiko": "Echte Alert-Daten können sensibel sein",
    },
    {
        "name": "GitHub Issues mit CVE-Bezug",
        "suchbegriffe": ["github issues CVE", "vulnerability disclosure", "security advisory"],
        "zweck": "Analyse von Schwachstellen-Meldungen",
        "lizenz": "GitHub Terms, Open Data",
        "risiko": "Niedrig — öffentliche Daten",
    },
    {
        "name": "Code Vulnerability Detection",
        "suchbegriffe": ["code vulnerability", "SAST dataset", "security code review"],
        "zweck": "Training für automatische Code-Schwachstellen-Erkennung",
        "lizenz": "Variiert — Einzelfallprüfung",
        "risiko": "Möglicherweise urheberrechtlich geschützter Code",
    },
    {
        "name": "Security Event Classification",
        "suchbegriffe": ["security event classification", "MITRE ATT&CK dataset", "threat intelligence"],
        "zweck": "Klassifikation nach MITRE ATT&CK Framework",
        "lizenz": "MITRE ATT&CK ist öffentlich",
        "risiko": "Niedrig",
    },
    {
        "name": "Audit Log Anomaly Detection",
        "suchbegriffe": ["audit log anomaly", "log analysis dataset", "anomaly detection logs"],
        "zweck": "Erkennung von Anomalien in Audit-Logs",
        "lizenz": "Prüfung erforderlich",
        "risiko": "Kann echte Benutzeraktivitäten enthalten",
    },
]

def main():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = REPORTS / f"hf_pdf_quality_{ts}"
    outdir.mkdir(parents=True, exist_ok=True)

    lines = ["# DATASET_SCOUT.md\n"]
    lines.append("## Zweck")
    lines.append("Recherche-Dokumentation für mögliche spätere ML-Nutzung.")
    lines.append("Nicht Teil des finalen IHK-Prototyps.\n")
    lines.append("## Regeln")
    lines.append("- Keine personenbezogenen Echtdaten verwenden")
    lines.append("- Keine neuen Behauptungen in finale PDF übernehmen")
    lines.append("- Lizenzprüfung erforderlich vor Nutzung")
    lines.append("- Kein automatischer Download\n")
    lines.append("## Kandidaten\n")

    for ds in DATASETS:
        lines.append(f"### {ds['name']}")
        lines.append(f"- **Zweck:** {ds['zweck']}")
        lines.append(f"- **Suchbegriffe:** {', '.join(ds['suchbegriffe'])}")
        lines.append(f"- **Lizenz:** {ds['lizenz']}")
        lines.append(f"- **Risiko:** {ds['risiko']}\n")

    lines.append("## Empfehlung")
    lines.append("Für die vorliegende Projektarbeit: Keine produktive ML-Integration.")
    lines.append("HF dient nur als Recherche-Plattform für mögliche Erweiterungen.\n")
    lines.append("## Nächste Schritte")
    lines.append("1. Lizenz jedes Datensatzes einzeln prüfen")
    lines.append("2. Anonymisierung vor任何 Training")
    lines.append("3. Keine echten Produktionsdaten verwenden")

    (outdir / "DATASET_SCOUT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"DATASET_SCOUT.md: {outdir / 'DATASET_SCOUT.md'}")

if __name__ == "__main__":
    main()
