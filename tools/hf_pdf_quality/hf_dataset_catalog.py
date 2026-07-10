#!/usr/bin/env python3
"""
HF Dataset Catalog — Recherche-/Dokumentationsstruktur für Dataset-Kandidaten.
Modi: static, online-search, sample
"""
import argparse, os, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORTS = ROOT / "reports"

DATASETS = [
    {"name": "darkknight25/Advanced_SIEM_Dataset", "task": "SIEM, Anomaly Detection, Threat Classification", "relevance": "Hoch", "risk": "synthetisch / Lizenz prüfen"},
    {"name": "DanCip/github-issues-vulnerability-detection", "task": "GitHub Issues mit CVE-Bezug", "relevance": "Sehr hoch", "risk": "Lizenz prüfen"},
    {"name": "kholil-lil/wazuh-alerts", "task": "Wazuh Alerts, SIEM-Regelvalidierung", "relevance": "Hoch", "risk": "Personenbezug prüfen"},
    {"name": "google/code_x_glue_cc_defect_detection", "task": "Code Defect / Vulnerability Detection", "relevance": "Hoch", "risk": "nur Code-Klassifikation"},
    {"name": "arag0rn/SecVulEval", "task": "C/C++ Vulnerability Samples", "relevance": "Mittel", "risk": "Stack passt ggf. nicht"},
    {"name": "ukcli/Cybersecurity-Dataset-Heimdall-v1.1", "task": "Credential-Store-/Endpoint-Anomalien", "relevance": "Mittel", "risk": "Lizenz prüfen"},
    {"name": "Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset", "task": "Cybersecurity Instruction Tuning", "relevance": "Mittel", "risk": "nicht als Faktenquelle"},
]

def write_static_report(outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    lines = ["# DATASET_CATALOG_REPORT.md\n"]
    lines.append(f"Erstellt: {datetime.now().isoformat()}\n")
    lines.append("| Dataset | Task | Relevanz | Risiko | Erlaubt in PDF |")
    lines.append("|---|---|---|---|---|")
    for ds in DATASETS:
        lines.append(f"| {ds['name']} | {ds['task']} | {ds['relevance']} | {ds['risk']} | NO |")
    lines.append("\n## Empfehlung")
    lines.append("Nur als Repo-Artefakt. Keine Produktivbehauptung.")
    (outdir / "DATASET_CATALOG_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {outdir / 'DATASET_CATALOG_REPORT.md'}")

def main():
    parser = argparse.ArgumentParser(description="HF Dataset Catalog")
    parser.add_argument("--mode", choices=["static", "online-search", "sample"], default="static")
    parser.add_argument("--allow-online", action="store_true")
    parser.add_argument("--dataset", type=str, default=None)
    parser.add_argument("--max-rows", type=int, default=3)
    args = parser.parse_args()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = REPORTS / f"hf_dataset_catalog_{ts}"

    if args.mode == "static":
        write_static_report(outdir)
    elif args.mode in ("online-search", "sample"):
        if not args.allow_online:
            print("FEHLER: --allow-online erforderlich für Online-Modus.")
            sys.exit(1)
        print(f"Modus {args.mode}: Noch nicht implementiert. Nur static verfügbar.")
        write_static_report(outdir)

if __name__ == "__main__":
    main()
