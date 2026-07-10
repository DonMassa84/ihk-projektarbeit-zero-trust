# Makefile – IHK Zero-Trust Projektarbeit
# Reproduzierbarer Build-Workflow für alle Artefakte
# Usage: make [target]
#   make all        – Kompletten Build (Standard)
#   make pdf        – Nur PDF exportieren
#   make diagrams   – Nur Diagramme rendern
#   make clean      – Alle generierten Artefakte löschen

MASTER   := 09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md
OUTDIR   := 09_export
TEMPLATE := 09_export/build_scripts/ihk_template.html
EPK_DIR  := 04_diagramme_mermaid/epk
SCR_DIR  := 10_screenshots

.PHONY: all pdf docx html diagrams screenshots clean lint

all: diagrams screenshots pdf docx html lint

# ─── PDF ───────────────────────────────────────────────────────────
# Optimierte 54-Seiten-Fassung (ReportLab, aus externer Konsolidierung)
# Der alte Markdown-Build bleibt als "pdf-from-markdown" erhalten.

pdf: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf

$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf: /home/schattenmacher/Downloads/PROJEKTARBEIT_ZERO_TRUST_IHK_FINAL_OPTIMIERT.pdf
	@echo "=== PDF übernehmen (optimierte 54-Seiten-Fassung) ==="
	cp "$<" "$@"
	@echo "✓ $@ ($(shell du -h $@ | cut -f1))"

# Alternativ: PDF aus Master-Markdown bauen (IHK-konform: Arial/LiberationSans 12pt, 1,5-zeilig, Ränder 1,5/4,5 cm)
pdf-from-markdown: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf

$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL_MARKDOWN.pdf: $(MASTER)
	@echo "=== PDF aus Markdown bauen (IHK-Format: Liberation Sans 12pt, 1,5-zeilig) ==="
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
	rm -f $(OUTDIR)/PROJEKTARBEIT*.pdf
	rm -f $(EPK_DIR)/*.png
	rm -f 04_diagramme_mermaid/png/*.png
	rm -f $(SCR_DIR)/*.png
	@echo "✓ Alle generierten Artefakte gelöscht"
	@echo "  (Master-Dokument und Quellen bleiben erhalten)"
