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

# ─── PDF (IHK-formatiert) ──────────────────────────────────────────

pdf: $(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf

$(OUTDIR)/PROJEKTARBEIT_IHK_FINAL.pdf: $(MASTER) $(TEMPLATE)
	@echo "=== PDF exportieren ==="
	pandoc "$(MASTER)" -f markdown -t html5 \
		--template="$(TEMPLATE)" \
		--metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
		-o "$(OUTDIR)/PROJEKTARBEIT.html"
	google-chrome --headless=new --disable-gpu --no-sandbox \
		--print-to-pdf-no-header \
		--print-to-pdf="$@" \
		"file://$(OUTDIR)/PROJEKTARBEIT.html"
	@echo "✓ $@"
	@python3 -c "import subprocess; r=subprocess.run(['strings','$@'],capture_output=True,text=True); print(f'  Seiten: {r.stdout.count(\"/Type /Page\")}')" 2>/dev/null

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

MERMAID_SRC := $(wildcard 04_diagramme_mermaid/*.mmd)
MERMAID_PNG := $(patsubst 04_diagramme_mermaid/%.mmd, 04_diagramme_mermaid/png/%.png, $(MERMAID_SRC))

diagrams: $(MERMAID_PNG)

04_diagramme_mermaid/png/%.png: 04_diagramme_mermaid/%.mmd
	@echo "=== Diagramm: $@ ==="
	npx -p @mermaid-js/mermaid-cli mmdc -i "$<" -o "$@" -w 800 -H 600 -b white 2>/dev/null || \
	echo "  ⚠ mermaid-cli nicht verfügbar, installiere mit: npm install -g @mermaid-js/mermaid-cli"

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

SCREENSHOT_HTML := $(wildcard $(SCR_DIR)/*.html)
SCREENSHOT_PNG  := $(patsubst $(SCR_DIR)/%.html, $(SCR_DIR)/%.png, $(SCREENSHOT_HTML))

screenshots: $(SCREENSHOT_PNG)

$(SCR_DIR)/%.png: $(SCR_DIR)/%.html
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
