# Layout-Regeln — IHK Projektarbeit

**Version:** 1.0  
**Datum:** 09.07.2026

---

## Seitengeometrie (DIN A4, 210 × 297 mm)

| Parameter | Wert | Einheit | Hinweis |
|-----------|------|---------|---------|
| **Papierformat** | A4 | – | 210 × 297 mm |
| **Rand oben** | 25 | mm | Kopfzeilenbereich |
| **Rand unten** | 25 | mm | Fußzeilenbereich |
| **Rand links (Bund)** | 30 | mm | 24 mm Text + 6 mm Bindekorrektur |
| **Rand rechts** | 20 | mm | |
| **Textbreite** | 160 | mm | 16 cm nutzbare Breite |
| **Texthöhe** | 247 | mm | 24,7 cm nutzbare Höhe |
| **Kopfzeilenhöhe** | 12 | mm | inkl. Trennlinie |
| **Fußzeilenhöhe** | 12 | mm | inkl. Trennlinie |
| **Spaltenabstand** | – | – | einspaltig |

---

## Raster & Ausrichtung

### Grundraster
- **Baseline-Grid:** 4 pt (≈ 1,41 mm)
- **Alle Abstände** Vielfache von 4 pt (6 pt, 8 pt, 12 pt, 16 pt, 24 pt)
- **Schriftgrößen** auf Baseline-Grid ausgerichtet

### Textblock
- **Blocksatz** mit Silbentrennung (DE-DE-1996)
- **Letzte Zeile** eines Absatzes: keine Erzwingung der Ausdehnung
- **Hängende Interpunktion** aktiviert (optischer Randausgleich)

---

## Typografische Hierarchie (visuelle Gewichtung)

| Ebene | Relatives Gewicht | Visueller Kontrast |
|-------|-------------------|-------------------|
| H1 (Kapitel) | 100 % | Schriftgröße + Bold + 24 pt oben |
| H2 (Abschnitt) | 83 % | Schriftgröße + Bold + 18 pt oben |
| H3 (Unterabschnitt) | 72 % | Schriftgröße + Semi-Bold + 12 pt oben |
| Fließtext | 61 % | Regular, 1,5-zeilig |
| Tabellen-Header | 55 % | Bold, kleiner, farbiger Hintergrund |
| Bildunterschrift | 55 % | Normal, 10 pt, kursiv für Quelle |
| Fußnote | 45 % | 9 pt, enger Zeilenabstand |

---

## Weißraum-Regeln (Vertical Rhythm)

| Situation | Abstand oben | Abstand unten |
|-----------|--------------|---------------|
| H1 → H2 | 24 pt | 12 pt |
| H2 → H3 | 18 pt | 8 pt |
| H3 → Fließtext | 12 pt | 6 pt |
| Fließtext → Fließtext | 0 | 6 pt |
| Fließtext → Liste | 6 pt | 6 pt |
| Liste → Fließtext | 6 pt | 6 pt |
| Fließtext → Tabelle | 12 pt | 6 pt |
| Tabelle → Fließtext | 6 pt | 12 pt |
| Fließtext → Abbildung | 12 pt | 6 pt |
| Abbildung → Bildunterschrift | 6 pt | 12 pt |
| Bildunterschrift → Fließtext | 12 pt | 6 pt |
| Code-Block → Fließtext | 6 pt | 6 pt |
| Horizontal Rule (HR) | 12 pt | 12 pt |

---

## Horizontale Ausrichtung

### Fließtext
- **Blocksatz** mit Silbentrennung
- **Letzte Zeile** nicht gestreckt
- **Hängende Interpunktion** für Anführungszeichen, Klammern

### Tabellen
| Spaltentyp | Ausrichtung |
|------------|-------------|
| Text (Bezeichnungen) | Links |
| Zahlen (Beträge, Mengen, %) | Rechts (dezimalbündig) |
| Datum / Uhrzeit | Zentriert |
| Boolean / Status (Ja/Nein, ✓/✗) | Zentriert |
| ID / Schlüssel | Zentriert oder Monospace-links |

### Abbildungen
- **Zentriert** auf Textbreite (max. 160 mm)
- **Keine** Randausdehnung über Textbreite hinaus
- **Gruppierte** Abbildungen (a, b, c) nebeneinander mit 4 mm Abstand

### Listen
- **Ebene 1:** Hängend 8 mm, Bullet/Nummer bei 0 mm
- **Ebene 2:** Hängend 16 mm, Bullet/Nummer bei 8 mm
- **Abstand** Liste → Text: 6 pt

---

## Kopf- & Fußzeilen

### Kopfzeile (ab Kapitel 1)
| Zone | Inhalt | Ausrichtung | Schrift |
|------|--------|-------------|---------|
| **Links** | "Zero-Trust-Sicherheitskonzept mit GitHub-Integration" | Links | 9 pt, Neutral 700 |
| **Rechts** | "Kapitel X: Kapitelname" (automatisch) | Rechts | 9 pt, Neutral 700 |
| **Trennlinie** | 0,5 pt, Neutral 300 | Vollbreite | – |

### Fußzeile (ab Kapitel 1)
| Zone | Inhalt | Ausrichtung | Schrift |
|------|--------|-------------|---------|
| **Links (ungerade) / Rechts (gerade)** | "Daniel Massa | Prüflingsnr. 615951 | IHK Stuttgart" | Außen | 9 pt, Neutral 700 |
| **Zentriert** | Seitenzahl (arabisch) | Zentriert | 9 pt, Neutral 700 |
| **Trennlinie** | 0,5 pt, Neutral 300 | Vollbreite | – |

### Vorwort / Verzeichnisse (Seiten I–X)
- **Kopfzeile:** Keine
- **Fußzeile:** Nur Seitenzahl (römisch), zentriert, 9 pt

### Deckblatt / Sperrvermerk / Eidesstattliche Erklärung
- **Keine** Kopf-/Fußzeilen
- **Seitenzahl** nicht gezählt (oder römisch fortlaufend)

---

## Besondere Layout-Situationen

### Lange Tabellen (Seitenumbruch)
| Regel | Umsetzung |
|-------|-----------|
| **Header-Wiederholung** | Auf jeder neuen Seite |
| **Kein Zeilenumbruch** | Innerhalb einer Zeile (`keep-together`) |
| **Fortsetzungshinweis** | "(Fortsetzung)" in Klammern unter Tabelle |
| **Fußnoten in Tabellen** | Buchstaben (a, b, c), unter Tabelle, vor Quelle |

### Lange Abbildungen (Hochformat)
- **Querformat** vermeiden (Druckproblem)
- Falls nötig: **90° gedreht**, Beschriftung mitgedreht
- **Querformat-Seite** eigene Seitengeometrie (Ränder getauscht)

### Fußnoten
- **Nummerierung** pro Kapitel neu (1, 2, 3…)
- **Position** am Seitenende, vor Fußzeile
- **Trennlinie** 5 cm, 0,5 pt, Neutral 300
- **Schrift** 9 pt, 1,2-zeilig, Einzug 5 mm (Hängend)

### Querverweise
- **Format:** "Abb. 3", "Tab. 5", "Kap. 3.8", "Gleichung (2)"
- **Hyperlinks** im PDF (intern)
- **Keine** "oben/unten", "vorherige/nächste Seite"

---

## Farbanwendung im Layout

| Element | Farbe |
|---------|-------|
| **Text (Fließtext, Überschriften)** | Primary Dark (`#1B1F24`) |
| **Tabellen-Header Hintergrund** | Primary Blue 10% (`#E8F0F8`) |
| **Tabellen-Zeilen (alternierend)** | Neutral 100 (`#F3F4F6`) |
| **Tabellen-Rahmen** | Neutral 300 (`#D1D5DB`) |
| **Abbildungsrahmen** | Neutral 300 (`#D1D5DB`), 0,5 pt |
| **Code-Block Hintergrund** | Neutral 50 (`#F9FAFB`) |
| **Code-Block Rahmen** | Neutral 300 (`#D1D5DB`), 0,5 pt |
| **Link (PDF)** | Primary Blue (`#2E5C8A`), Unterstrichen |
| **Link besucht** | Primary Blue 70% |
| **Kopfzeilen-Text** | Neutral 700 (`#4B5563`) |
| **Fußzeilen-Text** | Neutral 700 (`#4B5563`) |
| **Trennlinien (Kopf/Fuß)** | Neutral 300 (`#D1D5DB`) |

---

## Druck- & PDF-Export

### Druckdaten
| Parameter | Wert |
|-----------|-------|
| **Beschnitt** | 3 mm ringsum (wenn vollflächige Elemente) |
| **Farbraum** | CMYK (Prozessfarben), Spotfarben vermeiden |
| **Schwarz** | 100% K (nicht Rich Black) für Text |
| **Überdrucken** | Schwarzer Text auf farbigem Hintergrund: Überdrucken an |
| **Auflösung Bilder** | 300 DPI (effektiv im Endformat) |
| **Schriften** | Vollständig einbetten (Subsetting erlaubt) |

### PDF-Export (PDF/A-1b empfohlen)
| Einstellung | Wert |
|-------------|------|
| **PDF-Version** | 1.7 |
| **Konformität** | PDF/A-1b (ISO 19005-1) |
| **Schrift-Einbettung** | Vollständig (Subsetting ok) |
| **Bild-Kompression** | JPEG 85% (Fotos), Flate/Zip (Diagramme, Screenshots) |
| **Downsampling** | 300 DPI → 300 DPI (kein Downsampling) |
| **Metadaten** | Titel, Autor, Betreff, Keywords, Erstelldatum, PDF/A-Identifier |
| **Lesezeichen** | Entsprechend Inhaltsverzeichnis (3 Ebenen) |
| **Strukturbaum** | Tags aktivieren (H1–H3, Figure, Table, List, TOC) |
| **Dateigröße** | < 50 MB (IHK-Vorgabe) |
| **Validierung** | `veraPDF` (optional, aber empfohlen) |

---

## Export-Formate & Vorlagen

| Format | Vorlage | Tool | Zweck |
|--------|---------|------|-------|
| **DOCX** | `templates/ihk_project_doc_template.docx` | LibreOffice / Word | Bearbeitung, Prüfung |
| **PDF** | `templates/latex_template.tex` / `typst_template.typ` | Pandoc + XeLaTeX / Typst | Finale Abgabe |
| **HTML** | `templates/html_template.html` | Pandoc | Web-Preview, Barrierefreiheit |
| **Markdown** | Master-Datei (`PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`) | – | Quelle, Versionierung |

---

## Versionierung der Layout-Regeln

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | 09.07.2026 | Erstfassung | Daniel Massa |

---

*Ende Layout-Regeln. Diese Regeln sind verbindlich für alle Exporte (DOCX, PDF, HTML).*