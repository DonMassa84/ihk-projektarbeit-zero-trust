#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final"
cd "$ROOT"

echo "=== 1. LaTeX-Header reparieren ==="
cat > 09_export/build_scripts/pdf-header.tex << 'EOF'
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
EOF

echo "✅ Header geschrieben"

echo "=== 2. Makefile anpassen (pdf Target auf Markdown-Build) ==="
# Backup
cp Makefile Makefile.backup.$(date +%Y%m%d_%H%M%S)

# Ersetze pdf Target
sed -i '/^pdf:.*/,/^$/{
  /^pdf:.*/!d
}' Makefile

# Einfacher: komplettes pdf Target ersetzen
cat > /tmp/makefile_pdf.patch << 'PATCH'
--- Makefile
+++ Makefile
@@ -19,28 +19,26 @@
 
 # ─── PDF ───────────────────────────────────────────────────────────
 # IHK-konform: Markdown → Eisvogel → XeLaTeX
 
-pdf: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf
-
-$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf: /home/schattenmacher/Downloads/PROJEKTARBEIT_ZERO_TRUST_IHK_FINAL_OPTIMIERT.pdf
-	@echo "=== PDF übernehmen (optimierte 54-Seiten-Fassung) ==="
-	cp "$<" "$@"
-	@echo "✓ $@ ($(shell du -h $@ | cut -f1))"
+pdf: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf
 
-# Alternativ: PDF aus Master-Markdown bauen (IHK-konform: Arial/LiberationSans 12pt, 1,5-zeilig, Ränder 1,5/4,5 cm)
-pdf-from-markdown: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf
-
-$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf: $(MASTER)
-	@echo "=== PDF aus Markdown bauen (IHK-Format: Liberation Sans 12pt, 1,5-zeilig) ==="
-	sed 's/✅/X/g; s/⚠/!/g; s/🎯/O/g; s/️//g; s/✓/[x]/g; s/☐/[ ]/g; s/→/->/g; s/−/-/g' "$(MASTER)" > /tmp/projektarbeit_no_emoji.md
-	pandoc /tmp/projektarbeit_no_emoji.md -f markdown -o "$@" \
-		--resource-path=. \
-		--template=eisvogel \
-		--pdf-engine=xelatex \
-		-V colorlinks=true \
-		-V toc=true \
-		-V titlepage=true \
-		-V title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
-		-V author="Daniel Massa" \
-		-V date="01.11.2026" \
-		-V papersize=a4 \
-		-V mainfont="Liberation Sans" \
-		-V sansfont="Liberation Sans" \
-		-V monofont="Liberation Mono" \
-		-V fontsize=12pt \
-		-V geometry:left=1.5cm,right=4.5cm,top=2.5cm,bottom=2.5cm \
-	-H 09_export/build_scripts/pdf-header.tex
-	@echo "✓ $@"
+$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf: $(MASTER)
+	@echo "=== PDF bauen (IHK-Format: Liberation Sans 12pt, 1,5-zeilig, Ränder 1,5/4,5 cm) ==="
+	sed 's/✅/X/g; s/⚠/!/g; s/🎯/O/g; s/️//g; s/✓/[x]/g; s/☐/[ ]/g; s/→/->/g; s/−/-/g' "$(MASTER)" > /tmp/projektarbeit_no_emoji.md
+	pandoc /tmp/projektarbeit_no_emoji.md -f markdown -o "$@" \
+		--resource-path=. \
+		--template=eisvogel \
+		--pdf-engine=xelatex \
+		-V colorlinks=true \
+		-V toc=true \
+		-V titlepage=true \
+		-V title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
+		-V author="Daniel Massa" \
+		-V date="01.11.2026" \
+		-V papersize=a4 \
+		-V mainfont="Liberation Sans" \
+		-V sansfont="Liberation Sans" \
+		-V monofont="Liberation Mono" \
+		-V fontsize=12pt \
+		-V geometry:left=1.5cm,right=4.5cm,top=2.5cm,bottom=2.5cm \
+	-H 09_export/build_scripts/pdf-header.tex
+	@echo "✓ $@"
PATCH

# Apply patch - simpler approach: rewrite the relevant section
cat > /tmp/new_makefile_section << 'MAKEEOF'

# ─── PDF ───────────────────────────────────────────────────────────
# IHK-konform: Markdown → Eisvogel → XeLaTeX

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
MAKEEOF

# Replace the pdf section in Makefile
awk '
/^# ─── PDF / { in_pdf=1; print; next }
in_pdf && /^# ─── / && !/^# ─── PDF / { in_pdf=0 }
!in_pdf { print }
in_pdf && /^MAKE_SECTION/ { system("cat /tmp/new_makefile_section"); in_pdf=0 }
' Makefile > Makefile.new && mv Makefile.new Makefile

# Better approach: use sed to replace between markers
sed -i '/^# ─── PDF ───────────────────────────────────────────────────────────$/,/^# ─── DOCX ──────────────────────────────────────────────────────────$/{
  /^# ─── PDF ───────────────────────────────────────────────────────────$/!{
    /^# ─── DOCX ──────────────────────────────────────────────────────────$/!d
  }
}' Makefile

# Simpler: just recreate the whole Makefile with the correct pdf section
cat > Makefile << 'MAKEEOF'
# Makefile – IHK Zero-Trust Projektarbeit
# Reproduzierbarer Build-Workflow für alle Artefakte
# Usage: make [target]
#   make all        – Kompletten Build (Standard)
#   make pdf        – Nur PDF exportieren (IHK-konform: Markdown → Eisvogel → XeLaTeX)
#   make diagrams   – Nur Diagramme rendern
#   make screenshots – Nur Screenshots rendern
#   make clean      – Alle generierten Artefakte löschen (finale PDF bleibt)

MASTER   := 09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md
OUTDIR   := 09_export
TEMPLATE := 09_export/build_scripts/ihk_template.html
EPK_DIR  := 04_diagramme_mermaid/epk
SCR_DIR  := 10_screenshots

.PHONY: all pdf docx html diagrams screenshots epk clean lint

all: diagrams screenshots epk pdf docx html lint

# ─── PDF ───────────────────────────────────────────────────────────
# IHK-konform: Markdown → Eisvogel → XeLaTeX

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

# ─── DOCX ──────────────────────────────────────────────────────────

docx: $(OUTDIR)/PROJEKTARBEIT.docx

$(OUTDIR)/PROJEKTARBEIT.docx: $(MASTER)
	@echo "=== DOCX exportieren ==="
	pandoc "$(MASTER)" -f markdown -o "$@" --reference-doc=$(OUTDIR)/build_scripts/reference.docx 2>/dev/null || \
	pandoc "$(MASTER)" -f markdown -o "$@"
	@echo "✓ $@"

# ─── HTML ──────────────────────────────────────────────────────────

html: $(OUTDIR)/PROJEKTARBEIT.html

$(OUTDIR)/PROJEKTARBEIT.html: $(MASTER) $(TEMPLATE)
	@echo "=== HTML exportieren ==="
	pandoc "$(MASTER)" -f markdown -t html5 \
		--template="$(TEMPLATE)" \
		--metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
		-o "$@"
	@echo "✓ $@"

# ─── Mermaid-Diagramme ─────────────────────────────────────────────
# Quellen sind *.md (nicht *.mmd), exportierte PNGs liegen in exported_png/
diagrams:
	@echo "=== Mermaid-Diagramme (bereits in exported_png/ vorhanden) ==="
	@ls 04_diagramme_mermaid/exported_png/*.png 2>/dev/null | wc -l | xargs echo "  PNGs verfügbar:"

# ─── EPK-Diagramme (HTML→PNG) ──────────────────────────────────────

EPK_HTML := $(wildcard $(EPK_DIR)/*.html)
EPK_PNG  := $(patsubst $(EPK_DIR)/%.html, $(EPK_DIR)/%.png, $(EPK_HTML))

epk: $(EPK_PNG)

$(EPK_DIR)/%.png: $(EPK_DIR)/%.html
	@echo "=== EPK: $@ ==="
	google-chrome --headless=new --disable-gpu --no-sandbox \
		--window-size=800,1000 \
		--screenshot="$@" "file://$$(realpath $<)" 2>/dev/null || \
	echo "  ⚠ Chrome-Headless nicht verfügbar"

# ─── Screenshots ───────────────────────────────────────────────────
# HTML-Quellen in 10_screenshots/sources/ → PNG in 10_screenshots/
# Zusätzlich Aliase für vom Markdown referenzierte Dateinamen

SCREENSHOT_SRC := $(wildcard $(SCR_DIR)/sources/*.html)
SCREENSHOT_PNG := $(patsubst $(SCR_DIR)/sources/%.html, $(SCR_DIR)/%.png, $(SCREENSHOT_SRC))

screenshots: $(SCREENSHOT_PNG)
	@echo "=== Screenshot-Aliase ==="
	@if [ -f $(SCR_DIR)/01_github_repo.png ]; then \
		cp -n $(SCR_DIR)/01_github_repo.png $(SCR_DIR)/01_github_repo_uebersicht.png 2>/dev/null; \
		cp -n $(SCR_DIR)/02_github_actions.png $(SCR_DIR)/02_github_actions_workflow.png 2>/dev/null; \
		cp -n $(SCR_DIR)/03_yaml_workflow.png $(SCR_DIR)/03_yaml_workflow_datei.png 2>/dev/null; \
		echo "  ✓ Aliase erstellt"; \
	fi

$(SCR_DIR)/%.png: $(SCR_DIR)/sources/%.html
	@echo "=== Screenshot: $@ ==="
	google-chrome --headless=new --disable-gpu --no-sandbox \
		--window-size=1280,800 \
		--screenshot="$@" "file://$$(realpath $<)" 2>/dev/null || \
	echo "  ⚠ Chrome-Headless nicht verfügbar"

# ─── Lint / Qualitätssicherung ─────────────────────────────────────

lint:
	@echo "=== Rechtschreibprüfung ==="
	-which aspell 2>/dev/null && aspell check $(MASTER) 2>/dev/null; \
	echo "  (cspell/aspell für Markdown empfohlen)"
	@echo "=== Zeilenanzahl ==="
	@wc -l $(MASTER)
	@echo "=== Verzeichnisstruktur ==="
	@find . -type f -not -path './.git/*' -not -path '*/node_modules/*' -not -name '*.png' -not -name '*.pdf' | sort

# ─── Clean ─────────────────────────────────────────────────────────

clean:
	@echo "=== Aufräumen ==="
	rm -f $(OUTDIR)/PROJEKTARBEIT.html
	rm -f $(OUTDIR)/PROJEKTARBEIT.docx
	# FINALE PDF NICHT LÖSCHEN:
	# rm -f $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf
	rm -f $(EPK_DIR)/*.png
	rm -f 04_diagramme_mermaid/png/*.png
	rm -f $(SCR_DIR)/*.png
	@echo "✓ Alle generierten Artefakte gelöscht (finale PDF bleibt)"
	@echo "  (Master-Dokument und Quellen bleiben erhalten)"
MAKEEOF

echo "✅ Makefile aktualisiert"

echo ""
echo "=== NÄCHSTE SCHRITTE (manuell) ==="
echo "1. Markdown-Master bereinigen (OPENCODE_BUILD_PROMPT.md Abschnitt 2)"
echo "   - Deckblatt: Prüfungsperiode & Abgabedatum konsistent"
echo "   - IHK-Betreuer nur auf Deckblatt, nicht in Abnahmeprotokoll"
echo "   - Abnahmeprotokoll ehrlich formulieren (technisch erfüllt / betrieblich offen)"
echo "   - Rollenzahl: überall 6 Pilotrollen statt ≥10"
echo "   - Mehraufwand 8h kompensiert (Verzicht KA-02, Rollenreduktion)"
echo "   - Pilot/Prototyp einheitlich formulieren"
echo "   - DSGVO & ROI belegbar formulieren"
echo "   - Platzhalter entfernen"
echo ""
echo "2. Dann bauen:"
echo "   make pdf"
echo ""
echo "3. Qualitätsgates prüfen (qpdf, pdfinfo, pdffonts, SHA-256)"
echo ""
echo "✅ Build-Pipeline bereit"