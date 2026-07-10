#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

CATEGORY_MAX = {
    "formal": 15,
    "project_management": 20,
    "technical_consistency": 15,
    "evidence_traceability": 20,
    "economics": 10,
    "language_visuals": 10,
    "release_integrity": 10,
}

def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def extract_pdf_text(pdf: Path, out: Path, cwd: Path) -> str:
    if shutil.which("pdftotext"):
        run(["pdftotext", "-layout", str(pdf), str(out)], cwd)
        return out.read_text(encoding="utf-8", errors="replace")
    return ""

def pdf_pages(pdf: Path, cwd: Path) -> int | None:
    if not shutil.which("pdfinfo"):
        return None
    cp = run(["pdfinfo", str(pdf)], cwd)
    m = re.search(r"^Pages:\s+(\d+)", cp.stdout, re.M)
    return int(m.group(1)) if m else None

def find_heading_number_defects(text: str) -> list[str]:
    defects = []
    for bad in ("2.20 ", "2.21 ", "2.22 "):
        if bad in text:
            defects.append(f"Fehlerhafte Kapitelnummer gefunden: {bad.strip()}")
    return defects

def find_figure_sequence(text: str) -> list[str]:
    nums = [int(x) for x in re.findall(r"Abbildung\s+(\d+)\s*:", text)]
    if not nums:
        return ["Keine Abbildungsbeschriftungen im extrahierten Text erkannt."]
    unique = []
    for n in nums:
        if not unique or unique[-1] != n:
            unique.append(n)
    defects = []
    for a, b in zip(unique, unique[1:]):
        if b not in (a, a + 1):
            defects.append(f"Abbildungsnummern nicht fortlaufend: {a} -> {b}")
    return defects

def find_table_sequence(text: str) -> list[str]:
    nums = [int(x) for x in re.findall(r"Tabelle\s+(\d+)\s*:", text)]
    if not nums:
        return ["Keine Tabellenbeschriftungen im extrahierten Text erkannt."]
    unique = []
    for n in nums:
        if not unique or unique[-1] != n:
            unique.append(n)
    defects = []
    for a, b in zip(unique, unique[1:]):
        if b not in (a, a + 1):
            defects.append(f"Tabellennummern nicht fortlaufend: {a} -> {b}")
    return defects

def static_review(root: Path, cfg: dict[str, Any]) -> dict[str, Any]:
    src = root / cfg["source_markdown"]
    pdf = root / cfg["output_pdf"]
    report_dir = root / "quality_gate/reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    extracted = report_dir / "pdf_text.txt"

    blockers: list[str] = []
    warnings: list[str] = []
    checks: dict[str, Any] = {}

    if not src.exists():
        blockers.append(f"Markdown-Master fehlt: {src}")
        source_text = ""
    else:
        source_text = src.read_text(encoding="utf-8", errors="replace")

    if not pdf.exists():
        blockers.append(f"Final-PDF fehlt: {pdf}")
        pdf_text = ""
    else:
        pdf_text = extract_pdf_text(pdf, extracted, root)

    corpus = source_text + "\n" + pdf_text

    for term in cfg.get("canonical_stack_required", []):
        if term.lower() not in corpus.lower():
            warnings.append(f"Kanonischer Technikbegriff nicht gefunden: {term}")

    for term in cfg.get("canonical_stack_forbidden", []):
        if term.lower() in corpus.lower():
            blockers.append(f"Widersprüchlicher Technikbegriff gefunden: {term}")

    for term in cfg.get("forbidden_claims", []):
        if term.lower() in corpus.lower():
            blockers.append(f"Gesperrte Formulierung gefunden: {term}")

    required_date = cfg.get("required_document_date")
    if required_date and required_date not in corpus:
        warnings.append(f"Verbindlicher Dokumentstand nicht gefunden: {required_date}")

    for section in cfg.get("required_sections", []):
        if section.lower() not in corpus.lower():
            warnings.append(f"Pflichtbereich nicht sicher erkannt: {section}")

    checks["heading_numbering"] = find_heading_number_defects(corpus)
    blockers.extend(checks["heading_numbering"])

    checks["figure_sequence"] = find_figure_sequence(pdf_text)
    warnings.extend(checks["figure_sequence"])

    checks["table_sequence"] = find_table_sequence(pdf_text)
    warnings.extend(checks["table_sequence"])

    evidence_missing = []
    for field in cfg.get("required_evidence_fields", []):
        if field.lower() not in corpus.lower():
            evidence_missing.append(field)
    if evidence_missing:
        warnings.append("Testnachweisfelder nicht vollständig erkannt: " + ", ".join(evidence_missing))

    suspicious_patterns = {
        "70_vs_72_hours": (r"\b70\s*(?:h|Stunden)\b", r"\b72\s*(?:h|Stunden)\b"),
    }
    contradictions = []
    for name, (p1, p2) in suspicious_patterns.items():
        if re.search(p1, corpus, re.I) and re.search(p2, corpus, re.I):
            contradictions.append(name)
    if contradictions:
        blockers.append("Mögliche Widersprüche gleichzeitig vorhanden: " + ", ".join(contradictions))

    pages = pdf_pages(pdf, root) if pdf.exists() else None
    checks["pdf_pages"] = pages
    if pages is not None and pages < 20:
        blockers.append(f"PDF ungewöhnlich kurz: {pages} Seiten")
    if pages is not None and pages > 90:
        warnings.append(f"PDF ungewöhnlich lang: {pages} Seiten")

    final_pdfs = sorted(root.glob("**/*FINAL*.pdf"))
    checks["final_pdf_candidates"] = [str(p.relative_to(root)) for p in final_pdfs]
    if len(final_pdfs) > 1:
        warnings.append(f"Mehrere FINAL-PDFs gefunden ({len(final_pdfs)}). Release-Linie eindeutig einfrieren.")

    checks["source_sha256"] = sha256(src) if src.exists() else None
    checks["pdf_sha256"] = sha256(pdf) if pdf.exists() else None
    checks["git_head"] = None
    checks["git_clean"] = None
    if (root / ".git").exists() and shutil.which("git"):
        checks["git_head"] = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
        checks["git_clean"] = run(["git", "status", "--porcelain"], root).stdout.strip() == ""

    return {
        "generated_at": datetime.now().astimezone().isoformat(),
        "blockers": sorted(set(blockers)),
        "warnings": sorted(set(warnings)),
        "checks": checks,
    }

def validate_manual(root: Path, cfg: dict[str, Any]) -> dict[str, Any]:
    path = root / "quality_gate/manual_review.json"
    data = load_json(path)
    errors = []
    total = 0
    per_category = {}
    mins = cfg["minimum_category_scores"]

    for name, max_score in CATEGORY_MAX.items():
        entry = data.get(name)
        if not isinstance(entry, dict):
            errors.append(f"Kategorie fehlt: {name}")
            continue
        score = entry.get("score")
        if not isinstance(score, int) or not 0 <= score <= max_score:
            errors.append(f"Ungültiger Score {name}: {score}")
            continue
        evidence = entry.get("evidence", [])
        findings = entry.get("open_findings", [])
        if score > 0 and not evidence:
            errors.append(f"{name}: Score ohne Belegliste")
        if score >= mins[name] and findings:
            errors.append(f"{name}: Mindestscore erreicht, aber offene Befunde vorhanden")
        total += score
        per_category[name] = {
            "score": score,
            "max": max_score,
            "minimum": mins[name],
            "evidence_count": len(evidence),
            "open_findings": findings,
        }

    return {"errors": errors, "total": total, "categories": per_category}

def write_markdown(result: dict[str, Any], path: Path) -> None:
    s = result["static"]
    m = result["manual"]
    lines = [
        "# IHK Quality Gate",
        "",
        f"- Zeitpunkt: {s['generated_at']}",
        f"- Interner Score: **{result['score']} / 100**",
        f"- Gate: **{'GREEN' if result['passed'] else 'RED'}**",
        "",
        "## Hard Blocker",
    ]
    lines += [f"- {x}" for x in s["blockers"]] or ["- Keine"]
    lines += ["", "## Warnungen"]
    lines += [f"- {x}" for x in s["warnings"]] or ["- Keine"]
    lines += ["", "## Kategorien"]
    for name, d in m["categories"].items():
        lines.append(f"- {name}: {d['score']}/{d['max']} (Minimum {d['minimum']})")
    lines += ["", "## Validierungsfehler"]
    lines += [f"- {x}" for x in m["errors"]] or ["- Keine"]
    lines += ["", "## Release-Identität"]
    for key in ("source_sha256", "pdf_sha256", "git_head", "git_clean", "pdf_pages"):
        lines.append(f"- {key}: `{s['checks'].get(key)}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--build", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    cfg = load_json(root / "quality_gate/config/gate.json")

    if args.build:
        cp = subprocess.run(cfg["build_command"], cwd=root, shell=True)
        if cp.returncode != 0:
            print("BUILD FAILED", file=sys.stderr)
            return cp.returncode

    static = static_review(root, cfg)
    manual = validate_manual(root, cfg)
    score = manual["total"]

    category_failed = any(
        d["score"] < d["minimum"] for d in manual["categories"].values()
    )
    passed = (
        score >= cfg["minimum_total_score"]
        and not static["blockers"]
        and not manual["errors"]
        and not category_failed
    )

    if static["blockers"]:
        score = min(score, 69)
        passed = False

    result = {
        "score": score,
        "passed": passed,
        "static": static,
        "manual": manual,
    }

    report_dir = root / "quality_gate/reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "gate.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, report_dir / "gate.md")

    print(f"IHK_GATE={'GREEN' if passed else 'RED'} SCORE={score}/100")
    print(f"REPORT={report_dir / 'gate.md'}")
    return 0 if passed else 2

if __name__ == "__main__":
    raise SystemExit(main())
