#!/usr/bin/env python3
"""Build final signed PDF from dokumentation.md + erklaerung.pdf."""
import os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))

# 1. Split dokumentation.md at declaration boundary
src = ROOT / "dokumentation.md"
tmpdir = ROOT / "quality_gate/tmp"
tmpdir.mkdir(exist_ok=True)
body_md = tmpdir / "doku_body.md"

text = src.read_text(encoding="utf-8")
idx = text.find("\\newpage\n\n\\thispagestyle{empty}")
if idx < 0:
    print("ERROR: Declaration boundary not found", file=sys.stderr)
    sys.exit(1)

body_md.write_text(text[:idx].rstrip() + "\n\n\\newpage\n", encoding="utf-8")

# 2. Build main PDF with pandoc
main_pdf = tmpdir / "doku_main.pdf"
cmd = [
    "pandoc", str(body_md),
    "-o", str(main_pdf),
    "--pdf-engine=xelatex",
    "--template=formal_template.tex",
    "--toc", "--toc-depth=2",
    "--top-level-division=section",
    "--no-highlight",
]
subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True)

# 3. Append erklaerung.pdf using pdfunite
output = ROOT / "PROJEKTARBEIT_IHK_FINAL_SIGNED.pdf"
subprocess.run(
    ["pdfunite", str(main_pdf), str(ROOT / "erklaerung.pdf"), str(output)],
    cwd=ROOT, check=True
)

print(f"BUILD OK: {output} ({output.stat().st_size} bytes)")
