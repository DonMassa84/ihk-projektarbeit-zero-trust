# Design System — IHK Projektarbeit "Zero-Trust-Sicherheitskonzept mit GitHub-Integration"

**Version:** 1.0  
**Datum:** 09.07.2026  
**Autor:** Daniel Massa  
**Ziel:** Einheitliches, prüfungstaugliches Erscheinungsbild für die gesamte Projektdokumentation

---

## 1. Design-Prinzipien

| Prinzip | Beschreibung |
|---------|--------------|
| **Sachlichkeit** | Keine Marketing-Sprache, keine überladenen Grafiken. Fokus auf Inhalt. |
| **Konsistenz** | Einheitliche Schrift, Farben, Abstände, Nummerierung über alle Kapitel. |
| **Prüfungstauglichkeit** | IHK-Vorgaben erfüllen: DIN A4, Ränder, Schriftgröße, Verzeichnisse, Quellen. |
| **Nachvollziehbarkeit** | Jedes visuelle Element hat eine inhaltliche Begründung. |
| **Prototyp-Charakter** | Keine Produktiv-Nachweise vortäuschen. Simulationsplatzhalter kennzeichnen. |

---

## 2. Farbpalette

| Rolle | Hex | RGB | Verwendung |
|-------|-----|-----|------------|
| **Primary Dark** | `#1B1F24` | 27, 31, 36 | Überschriften, Rahmen, Footer |
| **Primary Blue** | `#2E5C8A` | 46, 92, 138 | Akzente, Links, Diagrammelemente |
| **Secondary Blue** | `#4A8FC7` | 74, 143, 199 | Hover, Sekundäre Akzente |
| **Success Green** | `#2D7D32` | 45, 125, 50 | Bestanden, Positiv, Abgeschlossen |
| **Warning Orange** | `#E67E22` | 230, 126, 34 | Warnungen, Teilweise, Offen |
| **Danger Red** | `#C62828` | 198, 40, 40 | Kritisch, Nicht bestanden, Mängel |
| **Neutral Gray** | `#6B7280` | 107, 114, 128 | Hilfetexte, Metadaten, Fußnoten |
| **Background** | `#FFFFFF` | 255, 255, 255 | Seitenhintergrund |
| **Alt Background** | `#F8F9FA` | 248, 249, 250 | Tabellenzeilen (alternierend), Code-Blöcke |
| **Border** | `#DEE2E6` | 222, 226, 230 | Tabellenrahmen, Abbildungsrahmen |

**Barrierefreiheit:** Kontrastverhältnis ≥ 4.5:1 für Text auf Hintergrund.

---

## 3. Typografie

| Element | Schrift | Größe | Zeilenabstand | Gewicht | Farbe |
|---------|---------|-------|---------------|---------|-------|
| **Deckblatt-Titel** | Liberation Sans | 28 pt | 1.2 | Bold | Primary Dark |
| **Deckblatt-Untertitel** | Liberation Sans | 16 pt | 1.3 | Regular | Primary Blue |
| **Kapitel-Überschrift (H1)** | Liberation Sans | 18 pt | 1.3 | Bold | Primary Dark |
| **Abschnitt (H2)** | Liberation Sans | 15 pt | 1.3 | Bold | Primary Dark |
| **Unterabschnitt (H3)** | Liberation Sans | 13 pt | 1.3 | Semi-Bold | Primary Dark |
| **Fliesstext** | Liberation Sans | 11 pt | 1.5 | Regular | Primary Dark |
| **Tabellen-Header** | Liberation Sans | 10 pt | 1.2 | Bold | Primary Dark |
| **Tabellen-Inhalt** | Liberation Sans | 10 pt | 1.2 | Regular | Primary Dark |
| **Abbildungsbeschriftung** | Liberation Sans | 10 pt | 1.2 | Italic | Neutral Gray |
| **Tabellenbeschriftung** | Liberation Sans | 10 pt | 1.2 | Italic | Neutral Gray |
| **Fußnoten** | Liberation Sans | 9 pt | 1.2 | Regular | Neutral Gray |
| **Code / Monospace** | Liberation Mono | 10 pt | 1.3 | Regular | Primary Dark |
| **Kopfzeile** | Liberation Sans | 9 pt | 1.0 | Regular | Neutral Gray |
| **Fußzeile** | Liberation Sans | 9 pt | 1.0 | Regular | Neutral Gray |

**Fallback-Schriften (falls Liberation nicht verfügbar):**
1. DejaVu Sans / DejaVu Sans Mono
2. Arial / Courier New
3. Times New Roman (nur für Fliesstext, wenn Sans-Serif nicht möglich)

---

## 4. Layout-Regeln

### Seitenformat
- **Format:** DIN A4 (210 × 297 mm)
- **Ränder:** oben 25 mm, unten 25 mm, links 30 mm (Bindekorrektur), rechts 20 mm
- **Spalten:** einspaltig

### Kopf-/Fußzeile
- **Kopfzeile (ab Kapitel 1):** Links: "Zero-Trust-Sicherheitskonzept mit GitHub-Integration", Rechts: Kapitelnummer + Kapitelname
- **Fußzeile:** Zentriert: Seitenzahl (arabisch, ab Kapitel 1), außen: "Daniel Massa | Prüflingsnr. 615951 | IHK Stuttgart"
- **Deckblatt / Vorwort / Verzeichnisse:** keine Kopfzeile, Fußzeile nur Seitenzahl (römisch)

### Nummerierung
- **Kapitel:** 1, 2, 3, ...
- **Abschnitte:** 1.1, 1.2, ...
- **Unterabschnitte:** 1.1.1, 1.1.2, ...
- **Abbildungen:** Abb. 1, Abb. 2, ... (kapitelübergreifend durchlaufend)
- **Tabellen:** Tab. 1, Tab. 2, ... (kapitelübergreifend durchlaufend)
- **Gleichungen:** (1), (2), ... (kapitelübergreifend)
- **Seiten:** römisch (I, II, ...) für Vorwort/Verzeichnisse, arabisch (1, 2, ...) ab Kapitel 1

### Abstände
- **Absatzabstand:** 6 pt (0.21 cm)
- **Überschrift zu Text:** 12 pt oben, 6 pt unten
- **Abbildung/Tabelle zu Text:** 12 pt oben/unten
- **Listen:** 3 pt zwischen Items, 6 pt zu umgebendem Text

---

## 5. Tabellen-Design

| Eigenschaft | Wert |
|-------------|------|
| **Rahmen** | 0.5 pt, Border-Farbe |
| **Header-Hintergrund** | Primary Blue (10 % Deckkraft) |
| **Zeilen alternierend** | Weiß / Alt Background |
| **Schrift** | Liberation Sans 10 pt |
| **Ausrichtung** | Links (Text), Rechts (Zahlen), Zentriert (Status/Checkboxen) |
| **Beschriftung** | **Tab. X:** Titel (fett), darunter Quelle/Hinweis in 9 pt Italic |
| **Breite** | Max. Textbreite (16 cm), nicht über Seitenrand |

---

## 6. Abbildungen-Design

| Eigenschaft | Wert |
|-------------|------|
| **Rahmen** | 0.5 pt, Border-Farbe |
| **Hintergrund** | Weiß |
| **Beschriftung** | **Abb. X:** Titel (fett), darunter Quelle/Hinweis in 9 pt Italic |
| **Diagramme (Mermaid/PlantUML)** | Export als SVG (vektoriell) bevorzugt, sonst PNG 300 DPI |
| **Screenshots** | PNG, max. 16 cm Breite, 150–300 DPI |
| **KI-generierte Bilder** | Kennzeichnung: "[KI-generiert: Modell, Prompt-Ref]" in Bildunterschrift |

---

## 7. Code-Blöcke

| Eigenschaft | Wert |
|-------------|------|
| **Hintergrund** | Alt Background |
| **Rahmen** | 1 pt links, Primary Blue |
| **Schrift** | Liberation Mono 10 pt |
| **Zeilennummern** | Optional, bei > 15 Zeilen |
| **Syntax-Highlighting** | Ja (Pandoc/LaTeX/Typst Standard) |

---

## 8. Verzeichnisse

| Verzeichnis | Format |
|-------------|--------|
| **Inhaltsverzeichnis** | 3 Ebenen (Kapitel, Abschnitt, Unterabschnitt), Punktrührer |
| **Abbildungsverzeichnis** | Nr., Titel, Seite |
| **Tabellenverzeichnis** | Nr., Titel, Seite |
| **Abkürzungsverzeichnis** | Abkürzung | Bedeutung, alphabetisch |
| **Literaturverzeichnis** | Numerisch [1], [2]... im Text, vollständige Angabe im Verzeichnis (APA-ähnlich) |

---

## 9. PDF/Export-Spezifika

| Parameter | Wert |
|-----------|------|
| **PDF-Version** | 1.7 (PDF/A-1b konform wenn möglich) |
| **Schriften einbetten** | Ja (alle verwendeten) |
| **Bildkompression** | JPEG 85 % für Fotos, verlustfrei für Diagramme |
| **Metadaten** | Titel, Autor, Betreff, Schlüsselwörter, Erstellungsdatum |
| **Dateigröße** | < 50 MB (IHK-Vorgabe) |

---

## 10. Checkliste für finale Prüfung

- [ ] Alle Überschriften korrekt nummeriert
- [ ] Alle Abbildungen/Tabellen beschriftet und im Text referenziert
- [ ] Verzeichnisse vollständig und seitenrichtig
- [ ] Quellen im Text ([1]) und Literaturverzeichnis konsistent
- [ ] Keine "TODO_", "Platzhalter", "Simulation" im finalen Text (außer gekennzeichnet)
- [ ] Farbkontraste eingehalten
- [ ] Schriftarten eingebettet
- [ ] Seitenzahlen korrekt (römisch/arabisch)
- [ ] Dateigröße < 50 MB
- [ ] PDF/A-1b validiert (optional, aber empfohlen)

---

*Ende Design System. Dieses Dokument ist Referenz für alle weiteren Design-Entscheidungen.*