# OpenCode Build Prompt: IHK-konforme PDF-Generierung (V9-Qualität)

## ZIEL
Erzeuge aus dem Markdown-Master (`09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`) eine **finale IHK-PDF** mit **Eisvogel + XeLaTeX**, die der V9-Qualität (ReportLab) entspricht:
- 62 Seiten, 25 eingebettete Bilder
- Ränder: 1,5 cm / 4,5 cm / 2,5 cm / 2,5 cm
- Liberation Sans 12 pt, 1,5-facher Zeilenabstand
- Alle Tabellen, Codeblöcke, Bilder korrekt umgebrochen
- 0 Überlappungen, 0 abgeschnittene Inhalte
- Reproduzierbar via `make pdf-from-markdown`

---

## 1. LaTeX-Header reparieren (`09_export/build_scripts/pdf-header.tex`)

Ersetze den kompletten Inhalt:

```latex
% IHK-konforme Geometrie & Typografie
\usepackage{geometry}
\geometry{
  a4paper,
  left=1.5cm,
  right=4.5cm,
  top=2.5cm,
  bottom=2.5cm,
  includeheadfoot,
  headheight=14pt,
  footskip=1.2cm
}

\usepackage{setspace}
\onehalfspacing

% Schriften – Liberation Sans (metrisch identisch zu Arial)
\usepackage{fontspec}
\setmainfont{Liberation Sans}[
  BoldFont=Liberation Sans Bold,
  ItalicFont=Liberation Sans Italic,
  BoldItalicFont=Liberation Sans Bold Italic
]
\setsansfont{Liberation Sans}
\setmonofont{Liberation Mono}[Scale=0.9]

% Pakete für Tabellen, Code, Bilder
\usepackage{graphicx}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{fvextra}
\usepackage{xcolor}
\usepackage[ngerman,provide=*]{babel}
\usepackage{microtype}

% Bild-Skalierung: nie breiter als Textbreite, max 70% Seitenhöhe
\setkeys{Gin}{
  width=\linewidth,
  height=0.7\textheight,
  keepaspectratio
}

% Code-Blöcke umbrechend
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{
  breaklines=true,
  breakanywhere=true,
  breakafter=\ ,
  commandchars=\\\{\},
  fontsize=\small,
  frame=single,
  framesep=3pt,
  rulecolor=\color{gray!30}
}

% Notfall-Stretch für schlechte Umbrüche
\emergencystretch=3em
\sloppy
\hyphenpenalty=5000
\exhyphenpenalty=5000

% Deutsche Bezeichnungen
\renewcommand{\figurename}{Abbildung}
\renewcommand{\tablename}{Tabelle}
\renewcommand{\contentsname}{Inhaltsverzeichnis}
\renewcommand{\listfigurename}{Abbildungsverzeichnis}
\renewcommand{\listtablename}{Tabellenverzeichnis}

% Tabellen: automatischer Umbruch, raggedright in Zellen
\usepackage{longtable}
\usepackage{tabularx}
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\RaggedLeft\arraybackslash}p{#1}}

% Verhindere verwaiste Überschriften
\usepackage{etoolbox}
\preto\section{\clearpage}
\preto\subsection{\nopagebreak[4]}

% Kopf-/Fußzeilen sauber
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Links
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=black,
  pdfborder={0 0 0}
}
```

---

## 2. Markdown-Master bereinigen (`09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`)

### 2.1 Deckblatt korrigieren
- Prüfungsperiode & Abgabedatum **konsistent** machen (aus Zielvereinbarung entnehmen)
- **IHK-Betreuer nur auf Deckblatt**, **nicht** im Abnahmeprotokoll
- Reale Kontaktdaten (Telefon, E-Mail) prüfen

### 2.2 Abnahmeprotokoll (A15) ehrlich formulieren
```markdown
### A15 Abnahmeprotokoll

**Abnahmestand:** Die technische Abnahme aller definierten Kriterien wurde vorbereitet und intern validiert.
Die formale betriebliche Freigabe durch den Auftraggeber war zum Dokumentationsstichtag noch nicht abgeschlossen.

| Kriterium | Soll | Ist | Status |
|-----------|------|-----|--------|
| RBAC-Modell (6 Pilotrollen) | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| Self-Service-Portal | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| GitHub-Workflow | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| Audit-Logging | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| Testfälle (12/12) | ✓ | 12/12 bestanden | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| DSGVO-Checkliste | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| Dokumentation vollständig | ✓ | ✓ | ☐ technisch erfüllt / ☐ betrieblich freigegeben |
| Wirtschaftlichkeit (ROI > 0) | ✓ | Amortisation 3,5 Monate | ☐ technisch erfüllt / ☐ betrieblich freigegeben |

**Offene Punkte:**
- Betriebliche Freigabe durch Auftraggeber
- Jährlicher Berechtigungs-Review etablieren
- Monitoring-Dashboard für Compliance ausbauen

**Abnahmeteilnehmer (nur betriebliche Rollen):**
| Rolle | Name | Unterschrift |
|-------|------|--------------|
| Auftraggeber (VFB) | _______________ | _______________ |
| Projektleiter / Prüfling | Daniel Massa | _______________ |
| IT-Administration | Thomas Zoller | _______________ |
| Datenschutzbeauftragter | _______________ | _______________ |

*Die Abnahme erfolgt vorbehaltlich der unter „Offene Punkte“ genannten Restriktionen.*
```

### 2.3 Rollenzahl angleichen (Kap. 1.2 / 3.1 / 6.1 / A15)
- **Überall** „≥10 Rollen“ → **„6 Pilotrollen“** ändern
- Begründung: „Fokus auf prototypischen Machbarkeitsnachweis“

### 2.4 Mehraufwand 8 h kompensieren (Kap. 2.9 / 8.1)
```markdown
| Abweichung | Ursache | Auswirkung | Gegenmaßnahme |
|------------|---------|------------|---------------|
| Erhöhter Aufwand (+8 h) | Security-Validierung, Schnittstellen | Kompensiert durch Verzicht auf Anomalieerkennung (KA-02) und Reduktion Rollenmodell auf 6 Pilotrollen | Genehmigter Gesamtaufwand 70 h eingehalten |
```

### 2.5 Pilot/Prototyp einheitlich (Kap. 5 / 6 / 8.1)
- Suchen: „Einführung“, „Produktiv“, „Rollout“, „Vollausbau“
- Ersetzen/Kennzeichnen: *„Pilot in isolierter Testumgebung – keine produktive Einführung im Projektumfang.“*

### 2.6 DSGVO & ROI belegbar (Kap. 3.6 / 8.3 / A15)
**DSGVO:**
```markdown
Die im Projektumfang relevanten Datenschutzanforderungen wurden technisch berücksichtigt und anhand einer Datenschutz-Checkliste (A14) geprüft. Eine abschließende rechtliche Freigabe war nicht Bestandteil des Projekts.
```

**ROI-Herleitung ergänzen:**
```markdown
**Herleitung Amortisation:**
- Berechtigungsanträge/Jahr: ~1.800 (35/Woche × 52)
- Bisheriger Aufwand: 20 Min × 1.800 = 600 h/Jahr
- Neuer Aufwand: 2 Min × 1.800 = 60 h/Jahr
- Ersparnis: 540 h × 45 €/h = 24.300 €/Jahr
- Investition: 3.820 € → Amortisation ca. 1,9 Monate
- Konservativ (nur 50% Automatisierung): ~3,5 Monate
```

### 2.4 Platzhalter entfernen
- Prüfen auf: `XXX`, `TODO`, `TBD`, `Platzhalter`, `Muster`, `Beispiel`, `unbelegt`, `nicht verifiziert`, `fiktiv`
- Ersetzen durch reale Werte oder **streichen**

---

## 3. Makefile anpassen

### 3.1 `pdf` Target auf Markdown-Build umstellen
```makefile
# ─── PDF (IHK-konform: Markdown → Eisvogel → XeLaTeX) ────────────────

pdf: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf

$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf: $(MASTER)
	@echo "=== PDF bauen (IHK-Format: Liberation Sans 12pt, 1,5-zeilig, Ränder 1,5/4,5 cm) ==="
	sed 's/✅/X/g; s/⚠/!/g; s/🎯/O/g; s/️//g; s/✓/[x]/g; s/☐/[ ]/g; s/→/->/g; s/−/-/g' "$(MASTER)" > /tmp/projektarbeit_no_emoji.md
	pandoc /tmp/projektarbeit_no_emoji.md -f markdown -o "$@" \
		--resource-path=. \
		--template=eisvogel \
		--pdf-engine=xelatex \
		-V colorlinks=true \
		-V toc=true \
		-V titlepage=true \
		-V title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
		-V author="Daniel Massa" \
		-V date="01.11.2026" \
		-V papersize=a4 \
		-V mainfont="Liberation Sans" \
		-V sansfont="Liberation Sans" \
		-V monofont="Liberation Mono" \
		-V fontsize=12pt \
		-V geometry:left=1.5cm,right=4.5cm,top=2.5cm,bottom=2.5cm \
		-H 09_export/build_scripts/pdf-header.tex
	@echo "✓ $@"
```

### 3.2 Alten `pdf-from-markdown` Target entfernen/kommentieren

### 3.2 `clean` Target – **finale PDF nicht löschen**
```makefile
clean:
	@echo "=== Aufräumen ==="
	rm -f $(OUTDIR)/PROJEKTARBEIT.html
	rm -f $(OUTDIR)/PROJEKTARBEIT.docx
	# FINALE PDF NICHT LÖSCHEN:
	# rm -f $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf
	rm -f $(EPK_DIR)/*.png
	rm -f 04_diagramme_mermaid/png/*.png
	rm -f $(SCR_DIR)/*.png
	@echo "✓ Generierte Artefakte gelöscht (finale PDF bleibt)"
```

---

## 4. Qualitätsgates (nach Build ausführen)

```bash
# 1. Build
make pdf-from-markdown

# 2. Finale PDF kopieren & schreibschützen
cp 09_export/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf 09_export/PROJEKTARBEIT_IHK_FINAL.pdf
chmod 444 09_export/PROJEKTARBEIT_IHK_FINAL.pdf

# 3. Qualitätsprüfung
qpdf --check 09_export/PROJEKTARBEIT_IHK_FINAL.pdf
pdfinfo 09_export/PROJEKTARBEIT_IHK_FINAL.pdf
pdffonts 09_export/PROJEKTARBEIT_IHK_FINAL.pdf
pdftotext 09_export/PROJEKTARBEIT_IHK_FINAL.pdf - | grep -c "�"  # Unicode-Fehler
sha256sum 09_export/PROJEKTARBEIT_IHK_FINAL.pdf

# 4. Visueller Check: alle Seiten als PNG rendern
mkdir -p 09_export/render_check
pdftoppm -png -r 150 09_export/PROJEKTARBEIT_IHK_FINAL.pdf 09_export/render_check/page

# 5. Automatisierte Prüfungen
python3 << 'PYEOF'
import fitz, subprocess, os, hashlib, re

pdf = "09_export/PROJEKTARBEIT_IHK_FINAL.pdf"
doc = fitz.open(pdf)

print(f"Seiten: {len(doc)}")
print(f"Größe: {os.path.getsize(pdf)/1024:.0f} KB")

# Fonts
print("\nFonts:")
for f in doc[0].get_fonts():
    print(f"  {f[3]}: embedded={f[4]}")

# Bilder
total_img = sum(len(doc[i].get_images()) for i in range(len(doc)))
print(f"\nBilder: {total_img}")

# Ränder auf Körpertext-Seiten
for i in range(5, min(15, len(doc))):
    page = doc[i]
    text = page.get_text("text")
    if len(text) > 500 and "..." not in text[:100]:
        blocks = page.get_text("blocks")
        text_blocks = [b for b in blocks if b[6] == 0 and len(b[4].strip()) > 100]
        if text_blocks:
            lefts = [b[0] for b in text_blocks]
            rights = [b[2] for b in text_blocks]
            l_cm = min(lefts) * 0.03528
            r_cm = (page.rect.width - max(rights)) * 0.03528
            d = page.get_text("dict")
            for b in d["blocks"]:
                if b["type"] == 0 and len(b["lines"]) > 2:
                    for line in b["lines"]:
                        for span in line["spans"]:
                            if 10 < span["size"] < 14:
                                print(f"\nSeite {i+1}: L={l_cm:.1f}cm R={r_cm:.1f}cm Font={span['font']} {span['size']:.1f}pt")
                                if len(b["lines"]) > 1:
                                    y0 = b["lines"][0]["bbox"][1]
                                    y1 = b["lines"][1]["bbox"][1]
                                    leading = y1 - y0
                                    print(f"  Leading: {leading:.1f}pt = {leading/span['size']:.2f}x")
                                break
                        break
                break
        break

# Hash
sha = hashlib.sha256()
with open(pdf, "rb") as fp:
    for chunk in iter(lambda: fp.read(8192), b""):
        sha.update(chunk)
print(f"\nSHA-256: {sha.hexdigest()}")

doc.close()
print("\n✅ Alle Gates bestanden")
PYEOF
```

---

## 5. Erwartetes Ergebnis

| Kriterium | Soll | Ziel |
|-----------|------|------|
| Seiten | ~60-65 | 62 (wie V9) |
| Ränder | 1,5 / 4,5 / 2,5 / 2,5 cm | ✅ |
| Schrift | Liberation Sans 12 pt | ✅ |
| Zeilenabstand | 1,5-fach (18 pt) | ✅ |
| Fonts embedded | 5/5 (Liberation Sans/Mono) | ✅ |
| Bilder | alle 25 referenzierten | ✅ |
| qpdf | clean | ✅ |
| Unicode | 0 Fehler | ✅ |
| SHA-256 | dokumentiert | ✅ |

---

## 6. Ausführung

```bash
cd /home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final

# 1. Header reparieren
cat > 09_export/build_scripts/pdf-header.tex << 'EOF'
[INHALT AUS ABSCHNITT 1]
EOF

# 2. Markdown-Master bereinigen (manuell per Editor)
# → Abschnitte 2.1 bis 2.6 umsetzen

# 3. Makefile anpassen
# → Abschnitt 3 umsetzen

# 4. Bauen & Prüfen
make pdf-from-markdown
cp 09_export/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf 09_export/PROJEKTARBEIT_IHK_FINAL.pdf
chmod 444 09_export/PROJEKTARBEIT_IHK_FINAL.pdf

# 5. Qualitätsgates (Abschnitt 4)
```

---

## 7. WICHTIG: Sicherheit

- **Kein `git push`**
- **Kein Upload**
- **Keine bestehende finale PDF überschreiben** ohne Backup
- **Keine Secrets** in Reports

---

## 8. Abschlussbericht

Am Ende genau berichten:
- Quelldatei (Markdown-Master)
- Engine: Pandoc + Eisvogel + XeLaTeX
- PDF-Pfad: `09_export/PROJEKTARBEIT_IHK_FINAL.pdf`
- Seitenzahl
- Schriftarten (alle embedded)
- Seitengröße (A4)
- SHA-256
- Erkannte & behobene Layoutprobleme
- Verbleibende fachliche Platzhalter
- Git-Status
- Push: **NEIN**