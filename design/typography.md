# Typografie & Layout-Regeln — IHK Projektarbeit

**Version:** 1.0  
**Datum:** 09.07.2026

---

## Schriftarten

### Primär (Lateinisch, Westeuropäisch)
| Einsatz | Schrift | Fallback | Begründung |
|---------|---------|----------|------------|
| **Überschriften (H1–H3)** | Liberation Sans / DejaVu Sans | Arial, Helvetica, sans-serif | Klare Lesbarkeit, professionell, Open Source |
| **Fließtext** | Liberation Serif / DejaVu Serif | Times New Roman, Georgia, serif | Bessere Lesbarkeit bei langen Texten, IHK-üblich |
| **Tabellen, Bildunterschriften, Fußnoten** | Liberation Sans / DejaVu Sans | Arial, Helvetica, sans-serif | Einheitlich mit Überschriften, gut lesbar in klein |
| **Code, Monospace** | Liberation Mono / DejaVu Sans Mono | Courier New, Consolas, monospace | Fixbreite für Code, YAML, JSON, SQL |

### Schriftgrößen & Zeilenabstände

| Element | Größe | Zeilenabstand (leading) | Abstand oben | Abstand unten |
|---------|-------|------------------------|--------------|---------------|
| **Deckblatt Titel** | 28 pt | 1.2 | 0 | 12 pt |
| **Deckblatt Untertitel** | 16 pt | 1.3 | 6 pt | 24 pt |
| **H1 (Kapitel)** | 18 pt | 1.3 | 24 pt | 12 pt |
| **H2 (Abschnitt)** | 15 pt | 1.3 | 18 pt | 8 pt |
| **H3 (Unterabschnitt)** | 13 pt | 1.3 | 12 pt | 6 pt |
| **Fließtext** | 11 pt | 1.5 | 0 | 6 pt |
| **Tabellen-Header** | 10 pt | 1.2 | 4 pt | 4 pt |
| **Tabellen-Inhalt** | 10 pt | 1.2 | 4 pt | 4 pt |
| **Abbildungsbeschriftung** | 10 pt | 1.2 | 6 pt | 12 pt |
| **Tabellenbeschriftung** | 10 pt | 1.2 | 12 pt | 6 pt |
| **Fußnoten** | 9 pt | 1.2 | 3 pt | 3 pt |
| **Code-Blöcke** | 10 pt | 1.3 | 6 pt | 6 pt |
| **Inline-Code** | 10 pt | 1.5 | – | – |
| **Kopfzeile** | 9 pt | 1.0 | 4 pt | 4 pt |
| **Fußzeile** | 9 pt | 1.0 | 4 pt | 4 pt |

---

## Layout & Seitenformat

### Seitenränder (DIN A4)
| Rand | Wert | Hinweis |
|------|------|---------|
| **Oben** | 25 mm | Platz für Kopfzeile |
| **Unten** | 25 mm | Platz für Fußzeile |
| **Links** | 30 mm | Bindekorrektur (6 mm) + 24 mm |
| **Rechts** | 20 mm | |

### Spalten
- **Einspaltig** durchgehend
- Keine Mehrspaltigkeit

### Kopfzeile (ab Kapitel 1)
| Position | Inhalt |
|----------|--------|
| **Links** | "Zero-Trust-Sicherheitskonzept mit GitHub-Integration" |
| **Rechts** | "Kapitel X: Kapitelname" (automatisch) |
| **Trennlinie** | 0.5 pt, Neutral 300, 4 pt unter Kopfzeile |

### Fußzeile (ab Kapitel 1)
| Position | Inhalt |
|----------|--------|
| **Außen (links/rechts)** | "Daniel Massa | Prüflingsnr. 615951 | IHK Stuttgart" |
| **Zentriert** | Seitenzahl (arabisch) |
| **Trennlinie** | 0.5 pt, Neutral 300, 4 pt über Fußzeile |

### Vorwort / Verzeichnisse (Seiten I–X)
- **Keine Kopfzeile**
- **Fußzeile:** nur Seitenzahl (römisch), zentriert

---

## Nummerierung

### Kapitel / Abschnitte
```
1 Kapitelname
1.1 Abschnitt
1.1.1 Unterabschnitt
1.1.1.1 (nicht empfohlen, max. 3 Ebenen)
```

### Abbildungen (durchlaufend, gesamt)
```
Abb. 1: Projektstrukturplan (PSP)
Abb. 2: Use-Case-Diagramm
...
Abb. 16: SWOT-Analyse
```

### Tabellen (durchlaufend, gesamt)
```
Tab. 1: Zeitplanung (Arbeitspakete)
Tab. 2: Kostenplanung
...
Tab. 13: Amortisationsrechnung
```

### Gleichungen
```
(1)  ROI = (Nutzen – Kosten) / Kosten × 100 %
(2)  Amortisation = Investition / Jährliche Ersparnis
```

### Listennummerierung
- **Ebene 1:** 1. / 2. / 3.
- **Ebene 2:** a) / b) / c)  — oder • / – (ungordnet)
- **Ebene 3:** i) / ii) / iii)

---

## Absatz- & Zeichenformate

### Fließtext
- **Blocksatz** mit Silbentrennung (deutsch)
- **Erste Zeile** nicht einrücken (Absatzabstand 6 pt)
- **Keine** Witwen/Waisen (min. 2 Zeilen zusammen)

### Hervorhebungen
| Art | Format | Beispiel |
|-----|--------|----------|
| **Fachbegriff (1. Nennung)** | *Kursiv* | *Zero Trust* |
| **Abkürzung (1. Nennung)** | *Kursiv* | *Role-Based Access Control (RBAC)* |
| **Wichtige Betonung** | **Fett** | **Muss-Kriterium** |
| **Datei, Code, Befehl** | `Monospace` | `role-request.yml` |
| **UI-Element** | `Monospace` | "Klicken Sie auf `Speichern`" |
| **Zitat > 3 Zeilen** | Blockzitat, eingerückt 1 cm, 10 pt, Kursiv | — |

---

## Tabellen

### Aufbau
| Bereich | Formatierung |
|---------|--------------|
| **Header-Zeile** | Fett, Hintergrund Primary Blue 10%, Text Primary Dark, zentriert (außer 1. Spalte links) |
| **Datenzeilen** | Alternierend: Weiß / Neutral 100 |
| **Rahmen** | 0.5 pt, Neutral 300, außen komplett, innen nur horizontale Linien |
| **Ausrichtung** | Text: links | Zahlen: rechts | Status/Boolean: zentriert |
| **Breite** | Automatisch, max. Textbreite (16 cm) |
| **Umbrüche** | Keine Seitenumbrüche innerhalb einer Zeile (keep-together) |

### Beschriftung
```
Tab. 5: Nutzwertanalyse (1–5)
Quelle: Eigene Darstellung
```
- **Über** der Tabelle
- **Fett** für "Tab. X:", normal für Titel
- **Kursiv, 9 pt** für Quelle/Hinweis darunter

---

## Abbildungen

### Technische Anforderungen
| Format | Vektor (SVG/PDF) | Raster (PNG) |
|--------|------------------|--------------|
| **Diagramme** | Bevorzugt (Mermaid/PlantUML Export) | 300 DPI, falls Vektor nicht möglich |
| **Screenshots** | – | 150–300 DPI, PNG verlustfrei |
| **Fotos** | – | 300 DPI, JPEG 85% |
| **Max. Breite** | 16 cm (Textbreite) | 16 cm |
| **Max. Höhe** | 20 cm | 20 cm |

### Beschriftung
```
Abb. 6: GitHub Workflow für automatisierte Rechtevergabe
Quelle: Eigene Darstellung (Mermaid, gerendert via mmdc)
```
- **Unter** der Abbildung
- **Fett** für "Abb. X:", normal für Titel
- **Kursiv, 9 pt** für Quelle/Hinweis darunter

### KI-generierte Bilder
```
Abb. 17: Abstrakte Zero-Trust-Architektur
[KI-generiert: Stable Diffusion XL, Prompt: "abstract zero trust architecture diagram, clean lines, corporate style"]
Quelle: Eigene Generierung
```

---

## Code-Blöcke

### Formatierung
```
```yaml
# .github/workflows/role-request.yml
name: Role Request Workflow
on:
  issues:
    types: [opened, edited]
```
```

### Regeln
- **Sprache angeben** (yaml, bash, python, json, sql, dockerfile, …)
- **Zeilennummern** bei > 15 Zeilen (Pandoc: `numberLines`)
- **Keine echten Secrets** — Platzhalter: `${{ secrets.GITHUB_TOKEN }}`
- **Einrückung** konsistent (2 Spaces für YAML, 4 für Python)
- **Kommentare** für Erklärungen im Code

---

## Verzeichnisse

### Inhaltsverzeichnis
- **Ebenen:** 3 (Kapitel, Abschnitt, Unterabschnitt)
- **Punktrührer** (Leader dots) bis Seitenzahl
- **Seitenzahlen** rechtsbündig

### Abbildungsverzeichnis
```
Abb. 1  Projektstrukturplan (PSP) ........................ 15
Abb. 2  Use-Case-Diagramm ................................ 25
...
Abb. 16 SWOT-Analyse ..................................... 9
```

### Tabellenverzeichnis
```
Tab. 1  Zeitplanung (Arbeitspakete) ...................... 16
Tab. 2  Kostenplanung .................................... 19
...
Tab. 13 Amortisationsrechnung ............................ 76
```

### Abkürzungsverzeichnis
| Abkürzung | Bedeutung |
|-----------|-----------|
| RBAC | Role-Based Access Control |
| ZT | Zero Trust |
| ... | ... |
- **Alphabetisch** sortiert
- **Zweispaltig** (Abkürzung | Bedeutung)

### Literaturverzeichnis
- **Numerisch** [1], [2]... im Text
- **APA-ähnlich** im Verzeichnis
- **DOI/URL + Abrufdatum** bei Online-Quellen

---

## PDF/Export-spezifisch

| Parameter | Wert |
|-----------|------|
| **PDF-Version** | 1.7 (PDF/A-1b konform empfohlen) |
| **Schrift-Einbettung** | Vollständig (alle verwendeten Glyphen) |
| **Bild-Kompression** | JPEG 85% (Fotos), Flate/Zip (Diagramme, Screenshots) |
| **Metadaten** | Titel, Autor, Betreff, Keywords, Erstelldatum, PDF/A-Identifier |
| **Dateigröße** | < 50 MB (IHK-Vorgabe) |
| **Lesezeichen** | Entsprechend Inhaltsverzeichnis (alle 3 Ebenen) |
| **Strukturbaum** | Tags für Barrierefreiheit (H1–H3, Figure, Table, List) |

---

## Checkliste vor Export

- [ ] Alle Überschriften korrekt nummeriert (max. 3 Ebenen)
- [ ] Alle Abbildungen/Tabellen beschriftet, nummeriert, im Text referenziert
- [ ] Verzeichnisse vollständig, seitenrichtig
- [ ] Quellen im Text ([1]) ↔ Literaturverzeichnis konsistent
- [ ] Keine `TODO_`, `Platzhalter`, `Simulation` im finalen Text
- [ ] Farbkontraste geprüft (WCAG AA)
- [ ] Schriften eingebettet
- [ ] Seitenzahlen: römisch (Vorwort/Verzeichnisse) / arabisch (Kapitel 1–)
- [ ] Dateigröße < 50 MB
- [ ] PDF/A-1b validiert (optional: `veraPDF`)

---

*Ende Typografie & Layout-Regeln. Bindend für alle Exporte (DOCX, PDF, HTML).*