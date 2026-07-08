# Zero-Trust-Sicherheitskonzept mit GitHub-Integration

**IHK-Projektarbeit – Certified IT Business Manager (IHK)**  
Prüfling: Daniel Massa | Prüflingsnummer: 615951 | Abgabe: 01.11.2026

## Projektbeschreibung

Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe (RBAC) und GitHub-basierter Workflow-Integration beim Verein zur Förderung der Berufsbildung e.V. (VFB), Ludwigsburg.

## Repository-Struktur

```
ihk_zero_trust_projektarbeit_final/
├── 00_master/                  # Ursprüngliche Master-Dokumente
├── 01_kapitel/                 # Einzelkapitel
├── 02_anhang/                  # Anhänge A1–A15
├── 03_tabellen/                # Tabellen
├── 04_diagramme_mermaid/       # Diagramme (Mermaid + EPK)
│   ├── mermaid/                # Mermaid-Quellen (.mmd)
│   ├── png/                    # Gerenderte Mermaid-PNGs
│   └── epk/                    # EPK-Diagramme (HTML + PNG)
├── 05_praesentation/           # Präsentationsfolien + Sprechtext
├── 06_prueferfragen/           # Prüferfragen-Katalog
├── 07_quellen/                  # Quellenverzeichnis
├── 08_reports/                 # Qualitätsberichte
├── 09_export/                  # Exportierte Artefakte
│   ├── final/                  # Master-Dokument (Markdown)
│   └── build_scripts/          # Build-Tools + Vorlagen
├── 10_screenshots/             # Screenshots
├── 11_abnahme/                 # Abnahmeprotokoll
├── Makefile                    # Reproduzierbarer Build
├── .gitignore
└── README.md
```

## Quickstart

### Voraussetzungen

- `pandoc` (Dokumentkonvertierung)
- `google-chrome` (PDF-Export, Diagramm-Rendering)
- `make` (Build-Automation)
- Optional: `mermaid-cli` (Mermaid-Diagramme)

### Build

```bash
make all        # Vollständiger Build (Diagramme + Screenshots + PDF + DOCX)
make pdf        # Nur PDF exportieren
make diagrams   # Nur Diagramme rendern
make clean      # Generierte Artefakte löschen
```

### Ausgabe

| Format | Pfad |
|--------|------|
| PDF (IHK-formatiert) | `09_export/PROJEKTARBEIT_IHK_FINAL.pdf` |
| DOCX | `09_export/PROJEKTARBEIT.docx` |
| HTML | `09_export/PROJEKTARBEIT.html` |
| Master (Markdown) | `09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md` |

## Workflow zur Reproduktion

1. **Clone**: `git clone <repo-url>`
2. **Build**: `cd ihk_zero_trust_projektarbeit_final && make all`
3. Das Makefile führt automatisch aus:
   - Rendering aller Mermaid-Diagramme → PNG
   - Rendering aller EPK-Diagramme → PNG
   - Generierung aller Screenshots → PNG
   - Export als PDF (Arial 12pt, 1,5zeilig, Korrekturrand)
   - Export als DOCX und HTML
   - Lint-Prüfung

## Abhängigkeiten

```bash
# Ubuntu/Debian
sudo apt-get install pandoc texlive-xelatex
# Chrome-Headless (für PDF/PNG)
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update && sudo apt-get install google-chrome-stable
# Mermaid CLI (optional)
npm install -g @mermaid-js/mermaid-cli
```

## Lizenz

© 2026 Daniel Massa. Alle Rechte vorbehalten. Diese Projektarbeit unterliegt dem Sperrvermerk und darf nur im Rahmen des IHK-Prüfungsprozesses eingesehen werden.
