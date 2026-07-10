#!/usr/bin/env python3
"""
HF Privacy Guard — Blockiert Text mit personenbezogenen/vertraulichen Inhalten.
"""
import re, sys

PATTERNS = [
    (r'(?i)prüflingsnummer', "PRUEFLINGSNUMMER"),
    (r'(?i)hackstraße|hackstrasse', "ADRESSE"),
    (r'(?i)\bstraße\b|\bstrasse\b', "ADRESSE_POSSIBLE"),
    (r'(?i)telefon|tel\.|mobile|handy', "TELEFON"),
    (r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', "EMAIL"),
    (r'(?i)token|secret|api[_-]?key|password|passwd|bearer', "SECRET_POSSIBLE"),
    (r'github_pat_[A-Za-z0-9_]+', "GITHUB_PAT"),
    (r'ghp_[A-Za-z0-9_]+', "GITHUB_PAT_LEGACY"),
    (r'[A-Z]{2}\d{2}[A-Z0-9]{11,30}', "IBAN"),
    (r'(?i)eidesstattlich', "EIDESSTATTLICH"),
    (r'(?i)unterschrift\s*[:\.]?\s*_{3,}', "UNTERSCHRIFTFELD"),
]

def scan_text(text):
    findings = []
    for pat, label in PATTERNS:
        for match in re.finditer(pat, text):
            findings.append((label, match.start(), match.group()[:60]))
    return findings

def main():
    import argparse
    parser = argparse.ArgumentParser(description="HF Privacy Guard")
    parser.add_argument("--text", type=str, default=None, help="Text to scan")
    parser.add_argument("--file", type=str, default=None, help="File to scan")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()

    findings = scan_text(text)

    print("=== HF PRIVACY GUARD ===")
    if findings:
        print(f"BLOCKED_BY_PRIVACY_GUARD")
        for label, pos, snippet in findings[:20]:
            print(f"  Reason: {label} at {pos}: {snippet}")
        print(f"\nAction: use local-only heuristic review")
        sys.exit(1)
    else:
        print("CLEAN — no privacy risks detected")
        sys.exit(0)

if __name__ == "__main__":
    main()
