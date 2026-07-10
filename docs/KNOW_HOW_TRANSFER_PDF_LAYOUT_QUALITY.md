# Know-how-Transfer: PDF-Layout-Qualität

## 1. Ausgangsproblem
- Doppelte Abbildungs- und Tabellenbeschriftungen (`Abbildung 1: Abbildung 1:`)
- Unicode-Ersatzzeichen (`�` für Pfeile `→`, `↔`)
- Seitenzahl von 46 (mit Duplikaten) auf 32 (bereinigt) nach `extract_section`-Fix
- Extern erzeugte Referenz-PDF (V1_3_FLATTENED, 44 S., ReportLab) nicht durchsuchbar

## 2. Root Causes

| Symptom | Technische Ursache | Quelldatei | Korrektur |
|---------|-------------------|------------|-----------|
| `Abbildung X: Abbildung X:` | `\renewcommand{\figurename}{Abbildung}` + manuelle `Abbildung X:` in Caption | `build_formal_final.py:fig_md()`, `formal_template_final.tex` | Fig_md: "Abbildung X:" aus Alt-Text entfernen; LaTeX nummeriert automatisch |
| `→` als `�` | Unicode-Pfeil (U+2192) ohne Font-Glyph-Unterstützung in PDF-Viewer | `docs/projektdokumentation.md` | `full_md.replace('\u2192', '-->')` im Build-Script |
| `↔` als `�` | Unicode-Pfeil (U+2194) ohne Font-Glyph-Unterstützung | `docs/projektdokumentation.md` | `full_md.replace('\u2194', '<->')` im Build-Script |
| Seitenzahl 32 vs 44 | `extract_section` stoppte bei `##` statt `###` → Duplikate | `build_formal_final.py:extract_section()` | Level-aware `^(### \|## )` |
| `Contents` statt Inhaltsverzeichnis | LaTeX-Default-Wert | `formal_template_final.tex` | `\renewcommand{\contentsname}{Inhaltsverzeichnis}` |

## 3. Standardprozess für PDF-Builds
1. Quelle ändern (`docs/projektdokumentation.md` oder `build_formal_final.py`)
2. PDF bauen: `tools/build_ihk_final.sh`
3. Text prüfen: `pdftotext` → 5000+ Wörter erwartet
4. Fonts prüfen: `pdffonts` → alle Fonts eingebettet
5. Unicode prüfen: grep nach `�` → 0 Treffer
6. Captions prüfen: grep nach `Abbildung X: Abbildung` → 0 Treffer
7. Metadaten prüfen: grep nach `TODO|FIXME|DRAFT` → 0 Treffer
8. SHA256 bilden
9. Freeze erstellen
10. Keine nachträgliche PDF-Manipulation

## 4. Vermeidungsregeln
- Keine direkten PDF-Overlays oder manuelle PDF-Bearbeitung
- Keine mehrfachen Captions (entweder LaTeX-auto oder manuell, nie beides)
- Keine Unicode-Sonderzeichen ohne Font-Prüfung
- Keine festen Tabellenhöhen in LaTeX
- Keine Freeze-Datei als Arbeitsdatei
- Keine Freigabe ohne vollständigen Seitenreview
- Keine finalen PDFs per Python/PyPDF/ReportLab erzeugen (nicht durchsuchbar)

## 5. Wiederverwendbare Checkliste
- [ ] Git-Status dokumentiert
- [ ] Masterquelle identifiziert (`docs/projektdokumentation.md`)
- [ ] Build reproduzierbar (`tools/build_ihk_final.sh`)
- [ ] PDF durchsuchbar (pdftotext > 0 Wörter)
- [ ] Fonts eingebettet (pdffonts: alle "yes")
- [ ] Keine Unicode-Fehler (`grep �` = 0)
- [ ] Keine doppelten Captions
- [ ] Inhaltsverzeichnis korrekt
- [ ] Alle Seiten gerendert (pdftoppm)
- [ ] Alle Seiten visuell geprüft
- [ ] SHA256 erstellt
- [ ] Freeze-Verzeichnis erstellt
- [ ] Kein Push erfolgt

## 6. Build-Kommandos
```bash
# Kompletter Build
bash tools/build_ihk_final.sh

# Nur Unicode-Ersatz prüfen
grep -nE '�|Figure.*Abbildung|Tabelle.*Tabelle' <(pdftotext output.pdf -)

# Nur Fonts prüfen
pdffonts output.pdf

# Nur Metadaten prüfen
grep -nE 'TODO|FIXME|DRAFT|ACCEPTED_CHANGES' <(pdftotext output.pdf -)

# Flattened-Version erzeugen (Viewer-kompatibel)
mutool convert -o flattened.pdf searchable.pdf
```
