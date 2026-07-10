#!/usr/bin/env python3
"""
HF Reference Export — Exportiert Referenz-Links für Dataset-/Modell-Kandidaten.
"""
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORTS = ROOT / "reports"

REFERENCES = [
    ("Hugging Face Docs", "https://huggingface.co/docs"),
    ("HfApi", "https://huggingface.co/docs/huggingface_hub/en/package_reference/hf_api"),
    ("Datasets Loading", "https://huggingface.co/docs/datasets/loading"),
    ("Datasets Streaming", "https://huggingface.co/docs/datasets/stream"),
    ("Transformers Pipelines", "https://huggingface.co/docs/transformers/main_classes/pipelines"),
    ("Hub Environment Variables", "https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables"),
    ("Advanced_SIEM_Dataset", "https://huggingface.co/datasets/darkknight25/Advanced_SIEM_Dataset"),
    ("github-issues-vulnerability", "https://huggingface.co/datasets/DanCip/github-issues-vulnerability-detection"),
    ("wazuh-alerts", "https://huggingface.co/datasets/kholil-lil/wazuh-alerts"),
    ("code_x_glue_cc_defect", "https://huggingface.co/datasets/google/code_x_glue_cc_defect_detection"),
    ("SecVulEval", "https://huggingface.co/datasets/arag0rn/SecVulEval"),
    ("Cybersecurity-Heimdall", "https://huggingface.co/datasets/ukcli/Cybersecurity-Dataset-Heimdall-v1.1"),
    ("Trendyol-Cybersecurity", "https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset"),
    ("CodeBERT", "https://huggingface.co/microsoft/codebert-base"),
    ("GraphCodeBERT", "https://huggingface.co/microsoft/graphcodebert-base"),
    ("flan-t5-small", "https://huggingface.co/google/flan-t5-small"),
    ("all-MiniLM-L6-v2", "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2"),
    ("distilbart-cnn-12-6", "https://huggingface.co/sshleifer/distilbart-cnn-12-6"),
]

def main():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = REPORTS / f"hf_reference_export_{ts}"
    outdir.mkdir(parents=True, exist_ok=True)

    lines = ["# HF Reference Export\n"]
    lines.append(f"Erstellt: {datetime.now().isoformat()}\n")
    lines.append("| Name | URL |")
    lines.append("|---|---|")
    for name, url in REFERENCES:
        lines.append(f"| {name} | {url} |")

    (outdir / "HF_REFERENCES.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {outdir / 'HF_REFERENCES.md'}")

if __name__ == "__main__":
    main()
