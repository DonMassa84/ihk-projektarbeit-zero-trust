#!/usr/bin/env python3
"""
Hugging-Face-gestützter Bachelor-/IHK-PDF-Quality-Engine
Lokaler Qualitätsprozess — HF nur als optionaler Review-/Research-Baustein.

 Modi:
   local     — keine externe Verbindung, nur Regex/Heuristik
   hf-local  — lokale Transformers-Modelle (falls installiert)
   hf-api    — nur vorbereitet, explizit bestätigen
"""
import argparse, hashlib, os, re, subprocess, sys, textwrap
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REPORTS = ROOT / "reports"
TOOLS = ROOT / "tools" / "hf_pdf_quality"

# ── PDF finden ────────────────────────────────────────────────────
def find_pdf():
    candidates = [
        ROOT / "99_IHK_FINAL_EXPORT_20260710" / "PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf",
        ROOT / "99_ABGABE_FREEZE_20260710_013218" / "PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL_ABGABE.pdf",
    ]
    for c in candidates:
        if c.exists():
            return c
    # fallback: search
    for p in ROOT.rglob("*.pdf"):
        name = p.name.lower()
        if any(k in name for k in ["projektarbeit", "zero", "trust", "ihk", "final"]):
            return p
    return None

# ── Text extrahieren ──────────────────────────────────────────────
def extract_text(pdf_path):
    try:
        r = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"],
                           capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    except Exception:
        pass
    # Fallback: pypdf
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except ImportError:
        pass
    return ""

# ── Risiko-Checks ─────────────────────────────────────────────────
def risk_checks(text):
    findings = []

    # Platzhalter
    for pat in [r'\bTODO\b', r'\bFIXME\b', r'\bLorem\b', r'\bPlatzhalter\b',
                r'\bMustertext\b', r'\bdraft\b',
                r'\bnoch einfügen\b', r'\bXXX\b']:
        hits = [(i+1, ln) for i, ln in enumerate(text.splitlines()) if re.search(pat, ln, re.I)]
        if hits:
            findings.append(("PLATZHALTER", pat, hits[:5]))

    # Offene Checkboxen
    hits = [(i+1, ln) for i, ln in enumerate(text.splitlines()) if '☐' in ln]
    if hits:
        findings.append(("CHECKBOX_OFFEN", "☐", hits[:5]))

    # Offene Unterschriften
    hits = [(i+1, ln) for i, ln in enumerate(text.splitlines())
            if re.search(r'Unterschrift\s*[:\.]?\s*_{3,}', ln)]
    if hits:
        findings.append(("UNTERSCHRIFT_OFFEN", "pattern", hits[:5]))

    # Doppeltes IV
    iv_hits = [(i+1, ln) for i, ln in enumerate(text.splitlines())
               if re.search(r'Inhaltsverzeichnis', ln, re.I)]
    if len(iv_hits) > 2:
        findings.append(("DOPPELTES_IV", f"{len(iv_hits)} Treffer", iv_hits[:5]))

    # Kritische Formulierungen
    critical = [
        r'tatsächliche Projektbearbeitung',
        r'vollständig produktiv',
        r'nachweislich',
    ]
    for pat in critical:
        hits = [(i+1, ln) for i, ln in enumerate(text.splitlines()) if re.search(pat, ln, re.I)]
        if hits:
            findings.append(("KRITISCHE_FORMULIERUNG", pat, hits[:5]))

    # Widersprüchliche Datumsangaben
    dates = re.findall(r'\d{1,2}\.\d{1,2}\.\d{4}', text)
    unique_dates = set(dates)
    if len(unique_dates) > 3:
        findings.append(("VIELE_DATUMSBINDUNGEN", f"{len(unique_dates)} verschiedene Daten", []))

    return findings

# ── Kapitelstruktur bewerten ──────────────────────────────────────
def chapter_review(text):
    required = [
        ("Projektinitiierung", [r'Ausgangssituation', r'Soll-Zustand', r'Projektziel']),
        ("Planung", [r'Zeitplan', r'Gantt', r'Meilenstein', r'Ressourcen']),
        ("Analyse/Konzeption", [r'Stakeholder', r'Anforderung', r'Analyse']),
        ("Technischer Entwurf", [r'Architektur', r'Schnittstelle', r'Datenmodell']),
        ("Umsetzung", [r'Implementierung', r'Konfiguration', r'Deployment']),
        ("Test/Abnahme", [r'Test', r'Abnahme', r'Validation']),
        ("Dokumentation", [r'Dokumentation', r'Betrieb', r'Einführung']),
        ("Projektabschluss", [r'Lessons Learned', r'Abschluss', r'Fazit']),
        ("Literatur", [r'Literatur', r'Quellen', r'Referenzen']),
        ("Eidesstattliche Erklärung", [r'Eidesstattlich', r'versichere']),
    ]
    results = []
    for chapter, patterns in required:
        found = any(re.search(p, text, re.I) for p in patterns)
        results.append((chapter, found))
    return results

# ── IHK/Bachelor-Niveau ──────────────────────────────────────────
def niveau_check(text):
    criteria = [
        ("Klare Ausgangssituation", [r'Ausgangssituation', r'Ist-Zustand', r'Problemstellung']),
        ("SMART-Ziele", [r'SMART', r'messbar', r'zeitgebunden', r'realistisch']),
        ("Stakeholderanalyse", [r'Stakeholder', r'Beteiligte', r'Interessent']),
        ("Make-or-Buy / Alternativen", [r'Make.or.Buy', r'Alternativ', r'Vergleich']),
        ("Wirtschaftlichkeit", [r'Wirtschaftlich', r'Kosten', r'ROI', r'Amortisation']),
        ("Risikoanalyse", [r'Risiko', r'Bedrohung', r'Wahrscheinlichkeit']),
        ("Datenschutz / rechtliche Risiken", [r'Datenschutz', r'DSGVO', r'GDPR', r'Recht']),
        ("Qualitätssicherung", [r'Qualität', r'QS', r'Prüf']),
        ("Soll-Ist-Vergleich", [r'Soll.*Ist', r'Vergleich', r'Abweichung']),
        ("Abnahme", [r'Abnahme', r'Abnahmeprotokoll', r'Freigabe']),
        ("Lessons Learned", [r'Lessons.Learned', r'Erkenntnis', r'Mitnahme']),
    ]
    results = []
    for criterion, patterns in criteria:
        found = any(re.search(p, text, re.I) for p in patterns)
        results.append((criterion, found))
    return results

# ── Bachelor-/IHK-Struktur (erweitert) ───────────────────────────
def bachelor_structure_check(text):
    required = [
        "Projektinitiierung", "Ausgangssituation", "Ist-Analyse",
        "Soll-Konzept", "SMART", "Projektabgrenzung", "Stakeholderanalyse",
        "Make-or-Buy", "Machbarkeitsanalyse", "Wirtschaftlichkeitsanalyse",
        "Nutzwertanalyse", "Risikoanalyse", "Qualitätsplanung",
        "Projektstrukturplan", "Arbeitspakete", "Meilensteinplanung",
        "Kostenplanung", "Kommunikationsplanung", "Testkonzept",
        "Testfallmatrix", "Soll-Ist-Vergleich", "Abnahme",
        "Einführung", "Schulung", "Übergabe", "Projektabschluss",
        "Lessons Learned", "Literaturverzeichnis", "Eidesstattliche Erklärung", "Anhang",
    ]
    results = []
    for item in required:
        found = bool(re.search(re.escape(item), text, re.I))
        results.append((item, found))
    return results

# ── ML-/HF-Risiken ──────────────────────────────────────────────
def ml_risk_check(text):
    patterns = [
        (r'Hugging Face produktiv', "HF produktiv-Claim"),
        (r'Inference Endpoint produktiv', "Inference produktiv"),
        (r'automatisch trainiert', "Auto-Training-Claim"),
        (r'100\s*%\s*F1', "100% F1-Claim"),
        (r'CodeBERT Anomalie-Detektor', "CodeBERT produktiv"),
        (r'flan-t5 Policy-Generator', "flan-t5 produktiv"),
        (r'synthetische Daten.*produktiv', "synthetisch produktiv"),
        (r'Datensatz produktiv genutzt', "Dataset produktiv"),
        (r'echte Projektdaten trainiert', "Echtdaten-Training"),
    ]
    findings = []
    for pat, label in patterns:
        hits = [(i+1, ln) for i, ln in enumerate(text.splitlines()) if re.search(pat, ln, re.I)]
        if hits:
            findings.append((label, hits[:3]))
    return findings

# ── HF-Review (optional) ─────────────────────────────────────────
def hf_review_local(text, prompts_dir):
    """Lokales HF-Review mit Transformers (falls installiert)."""
    try:
        from transformers import pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        # Nur erste 3000 Zeichen für lokale Verarbeitung
        chunk = text[:3000]
        summary = summarizer(chunk, max_length=500, min_length=100)
        return summary[0]['summary_text']
    except ImportError:
        return "HF-Review nicht verfügbar: transformers nicht installiert"
    except Exception as e:
        return f"HF-Review Fehler: {e}"

# ── Report schreiben ──────────────────────────────────────────────
def write_report(outdir, pdf_path, text, risks, chapters, niveau, bachelor=None, ml_risks=None, hf_text=None):
    outdir.mkdir(parents=True, exist_ok=True)

    # PDF_TEXT_EXTRACT.txt
    (outdir / "PDF_TEXT_EXTRACT.txt").write_text(text, encoding="utf-8")

    # CHAPTER_REVIEW.md
    chap_lines = ["# Kapitelstruktur-Review\n"]
    for ch, ok in chapters:
        status = "✅" if ok else "❌"
        chap_lines.append(f"- {status} {ch}")
    (outdir / "CHAPTER_REVIEW.md").write_text("\n".join(chap_lines), encoding="utf-8")

    # FORMAL_RISK_REVIEW.md
    risk_lines = ["# Formale Risiko-Prüfung\n"]
    if not risks:
        risk_lines.append("Keine Risiken gefunden.\n")
    else:
        for rtype, pattern, hits in risks:
            risk_lines.append(f"\n## {rtype}\nPattern: `{pattern}`\n")
            for lno, ln in hits:
                risk_lines.append(f"  Z{lno}: {ln.strip()[:120]}")
    (outdir / "FORMAL_RISK_REVIEW.md").write_text("\n".join(risk_lines), encoding="utf-8")

    # PROTOTYPE_CLAIMS_REVIEW.md
    claim_lines = ["# Prototyp-Claims-Review\n"]
    claim_patterns = [
        (r'100\s*%', "100%-Aussage"),
        (r'vollständig produktiv', "Produktiv-Claim"),
        (r'nachweislich', "Nachweis-Claim"),
        (r'tatsächliche Projektbearbeitung', "Tatsächlich-Claim"),
    ]
    for pat, label in claim_patterns:
        hits = [(i+1, ln) for i, ln in enumerate(text.splitlines()) if re.search(pat, ln, re.I)]
        if hits:
            claim_lines.append(f"\n## {label}\n")
            for lno, ln in hits:
                claim_lines.append(f"  Z{lno}: {ln.strip()[:120]}")
    if len(claim_lines) == 1:
        claim_lines.append("Keine kritischen Prototyp-Claims gefunden.\n")
    (outdir / "PROTOTYPE_CLAIMS_REVIEW.md").write_text("\n".join(claim_lines), encoding="utf-8")

    # EXAMINER_QUESTIONS.md
    examiner_lines = ["# Mögliche Prüferfragen\n"]
    missing_niveau = [c for c, ok in niveau if not ok]
    missing_chapters = [c for c, ok in chapters if not ok]
    if missing_niveau:
        examiner_lines.append("\n## Fehlende Niveau-Kriterien\n")
        for c in missing_niveau:
            examiner_lines.append(f"- {c}")
    if missing_chapters:
        examiner_lines.append("\n## Fehlende Kapitel\n")
        for c in missing_chapters:
            examiner_lines.append(f"- {c}")
    examiner_lines.append("\n## Typische Prüferfragen\n")
    examiner_lines.append("- Wie haben Sie die Anforderungen erhoben?")
    examiner_lines.append("- Welche Alternativen haben Sie bewertet?")
    examiner_lines.append("- Woran messen Sie den Erfolg?")
    examiner_lines.append("- Welche Risiken haben Sie identifiziert und wie adressiert?")
    examiner_lines.append("- Was war der größte Lesson Learned?")
    (outdir / "EXAMINER_QUESTIONS.md").write_text("\n".join(examiner_lines), encoding="utf-8")

    # FINAL_RECOMMENDATION.md
    rec_lines = ["# Final Recommendation\n"]
    hard_risks = [r for r in risks if r[0] in ("PLATZHALTER", "CHECKBOX_OFFEN", "UNTERSCHRIFT_OFFEN", "DOPPELTES_IV")]
    if hard_risks:
        rec_lines.append("\n## Status: 🔴 RED\n")
        rec_lines.append("Harte Risiken gefunden. PDF muss vor Abgabe korrigiert werden.\n")
    elif risks:
        rec_lines.append("\n## Status: 🟡 YELLOW\n")
        rec_lines.append("Formale Hinweise gefunden. Manuell prüfen.\n")
    else:
        rec_lines.append("\n## Status: 🟢 GREEN\n")
        rec_lines.append("Keine harten Risiken. PDF kann eingefroren werden.\n")

    rec_lines.append("\n## Formulierungen für Prüfung\n")
    rec_lines.append("### Hugging Face\n")
    rec_lines.append(textwrap.dedent("""\
        „Hugging Face wurde im Projektkontext als Recherche- und Bewertungsplattform
        für mögliche spätere ML-Erweiterungen betrachtet. Eine produktive Integration
        in den finalen IHK-Prototyp war nicht Bestandteil des Projektumfangs. Die finale
        Projektdokumentation wurde lokal reproduzierbar erzeugt und durch formale
        Prüfskripte validiert."\n"""))
    rec_lines.append("### ML-Ausblick\n")
    rec_lines.append(textwrap.dedent("""\
        „Für eine spätere Ausbaustufe wurden öffentlich verfügbare Security- und
        Vulnerability-Datensätze recherchiert. Ziel ist die Bewertung, ob Security-Events,
        GitHub-Issues oder Code-Schwachstellen perspektivisch für eine ML-basierte
        Anomalieerkennung genutzt werden können. Im Rahmen der vorliegenden Projektarbeit
        wurde diese Erweiterung nicht produktiv umgesetzt."\n"""))
    rec_lines.append("### Prototyp\n")
    rec_lines.append(textwrap.dedent("""\
        „Die Umsetzung erfolgte als prototypischer Machbarkeitsnachweis. Produktive
        Rollout-, Betriebs- und Skalierungsmaßnahmen wurden konzeptionell vorbereitet,
        waren jedoch nicht Bestandteil des genehmigten Projektumfangs."\n"""))
    (outdir / "FINAL_RECOMMENDATION.md").write_text("\n".join(rec_lines), encoding="utf-8")

    # BACHELOR_STRUCTURE.md
    if bachelor is not None:
        bach_lines = ["# Bachelor-/IHK-Struktur-Check\n"]
        found_count = sum(1 for _, ok in bachelor if ok)
        bach_lines.append(f"Ergebnis: {found_count}/{len(bachelor)} Kriterien gefunden\n")
        for item, ok in bachelor:
            status = "✅" if ok else "❌"
            bach_lines.append(f"- {status} {item}")
        (outdir / "BACHELOR_STRUCTURE.md").write_text("\n".join(bach_lines), encoding="utf-8")

    # ML_RISK_REVIEW.md
    if ml_risks is not None:
        ml_lines = ["# ML-/HF-Risiko-Prüfung\n"]
        if not ml_risks:
            ml_lines.append("Keine ML/HF-Risiken gefunden.\n")
        else:
            for label, hits in ml_risks:
                ml_lines.append(f"\n## {label}\n")
                for lno, ln in hits:
                    ml_lines.append(f"  Z{lno}: {ln.strip()[:120]}")
        (outdir / "ML_RISK_REVIEW.md").write_text("\n".join(ml_lines), encoding="utf-8")

    # SHA256SUMS.txt
    sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    (outdir / "SHA256SUMS.txt").write_text(f"{sha}  {pdf_path.name}\n", encoding="utf-8")

    # HF Review (optional)
    if hf_text:
        (outdir / "HF_REVIEW_SUMMARY.md").write_text(f"# HF Review Summary\n\n{hf_text}\n", encoding="utf-8")

# ── Main ──────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="IHK-PDF Quality Check")
    parser.add_argument("--mode", choices=["local", "hf-local", "hf-api"], default="local")
    parser.add_argument("--pdf", type=str, default=None)
    parser.add_argument("--outdir", type=str, default=None)
    args = parser.parse_args()

    pdf_path = Path(args.pdf) if args.pdf else find_pdf()
    if not pdf_path or not pdf_path.exists():
        print("FEHLER: Keine PDF gefunden.", file=sys.stderr)
        sys.exit(1)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = Path(args.outdir) if args.outdir else REPORTS / f"hf_pdf_quality_{ts}"

    print(f"PDF: {pdf_path}")
    print(f"Modus: {args.mode}")
    print(f"Output: {outdir}")

    text = extract_text(pdf_path)
    if not text.strip():
        print("FEHLER: Kein Text extrahiert.", file=sys.stderr)
        sys.exit(1)

    risks = risk_checks(text)
    chapters = chapter_review(text)
    niveau = niveau_check(text)
    bachelor = bachelor_structure_check(text)
    ml_risks = ml_risk_check(text)

    hf_text = None
    if args.mode == "hf-local":
        hf_text = hf_review_local(text, TOOLS / "prompts")
    elif args.mode == "hf-api":
        print("HF-API-Modus: Noch nicht implementiert. Bitte --mode local oder --mode hf-local verwenden.")
        return

    write_report(outdir, pdf_path, text, risks, chapters, niveau, bachelor, ml_risks, hf_text)

    # Ampel
    hard = [r for r in risks if r[0] in ("PLATZHALTER", "CHECKBOX_OFFEN", "UNTERSCHRIFT_OFFEN", "DOPPELTES_IV")]
    if hard:
        gate = "RED"
    elif risks or ml_risks:
        gate = "YELLOW"
    else:
        gate = "GREEN"

    print(f"\n=== GATE: {gate} ===")
    print(f"Risiken: {len(risks)}")
    print(f"Kapitel: {sum(1 for _,ok in chapters if ok)}/{len(chapters)}")
    print(f"Niveau:  {sum(1 for _,ok in niveau if ok)}/{len(niveau)}")
    print(f"Reports: {outdir}")

if __name__ == "__main__":
    main()
