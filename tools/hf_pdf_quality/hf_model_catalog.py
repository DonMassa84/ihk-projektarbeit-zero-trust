#!/usr/bin/env python3
"""
HF Model Catalog — Modell-Kandidaten für Review/Security/Semantic Search.
Modi: static, local-check, online-metadata
"""
import argparse, os, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORTS = ROOT / "reports"

MODELS = [
    {"name": "microsoft/codebert-base", "task": "Code + NL, Feature Extraction", "local": "Mittel", "role": "Code-/Security-Ausblick"},
    {"name": "microsoft/graphcodebert-base", "task": "Code mit Datenfluss", "local": "Schwer", "role": "optionaler Code-Ausblick"},
    {"name": "google/flan-t5-small", "task": "Instruction/Text2Text", "local": "Gut", "role": "Review-Hinweise"},
    {"name": "google-t5/t5-small", "task": "Text2Text, 60M", "local": "Gut", "role": "Testmodell"},
    {"name": "sentence-transformers/all-MiniLM-L6-v2", "task": "Embeddings, Semantic Search", "local": "Sehr gut", "role": "Kapitelähnlichkeit"},
    {"name": "sshleifer/distilbart-cnn-12-6", "task": "Summarization", "local": "Mittel", "role": "Kapitelzusammenfassungen"},
]

def write_static_report(outdir):
    outdir.mkdir(parents=True, exist_ok=True)
    lines = ["# MODEL_CATALOG_REPORT.md\n"]
    lines.append(f"Erstellt: {datetime.now().isoformat()}\n")
    lines.append("| Modell | Task | Lokale Eignung | Projektrolle |")
    lines.append("|---|---|---|---|")
    for m in MODELS:
        lines.append(f"| {m['name']} | {m['task']} | {m['local']} | {m['role']} |")
    lines.append("\n## Empfehlung")
    lines.append("Nur lokaler Cache. Kein Download ohne --allow-online.")
    (outdir / "MODEL_CATALOG_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {outdir / 'MODEL_CATALOG_REPORT.md'}")

def check_local_cache():
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    print("=== LOCAL HF CACHE CHECK ===")
    if cache_dir.exists():
        models = list(cache_dir.glob("models--*"))
        print(f"Cache-Verzeichnis: {cache_dir}")
        print(f"Gecachte Modelle: {len(models)}")
        for m in models[:10]:
            print(f"  - {m.name}")
    else:
        print("Kein HF-Cache gefunden.")

def main():
    parser = argparse.ArgumentParser(description="HF Model Catalog")
    parser.add_argument("--mode", choices=["static", "local-check", "online-metadata"], default="static")
    parser.add_argument("--allow-online", action="store_true")
    args = parser.parse_args()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = REPORTS / f"hf_model_catalog_{ts}"

    if args.mode == "static":
        write_static_report(outdir)
    elif args.mode == "local-check":
        check_local_cache()
        write_static_report(outdir)
    elif args.mode == "online-metadata":
        if not args.allow_online:
            print("FEHLER: --allow-online erforderlich.")
            sys.exit(1)
        print("Online-Modus: Noch nicht implementiert.")
        write_static_report(outdir)

if __name__ == "__main__":
    main()
