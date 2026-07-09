# Gliederungs-Vorschlag mit Seitenbudget — IHK Projektarbeit

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Prüfling:** Daniel Massa (615951)  
**Abgabe:** 01.11.2026  
**Ziel:** ca. 75 Seiten Gesamt (Textteil 45 + Anhang 25 + Verzeichnisse 10 + Deckblatt/Erklärungen 5)

---

## Gliederungsstruktur (IHK-konform, 4 Ebenen max.)

```
DECKBLATT                                    [1 S., nicht nummeriert]
SPERRVERMERK (falls vertraulich)             [1 S., nicht nummeriert]
VORWORT                                      [I–II, römisch]
  I. Einleitung
  II. Projektumfeld
  III. Meine Tätigkeiten
  IV. Allgemeine Informationen
SPERRVERMERK-WIEDERHOLUNG (optional)         [nicht nummeriert]
INHALTSVERZEICHNIS                           [III–VI, römisch]
ABBILDUNGSVERZEICHNIS                        [VII, römisch]
TABELLENVERZEICHNIS                          [VIII, römisch]
ABKÜRZUNGSVERZEICHNIS                        [IX, römisch]

1 PROJEKTINITIIERUNG                         [Seite 1–11]
  1.1 Projektumfeld                          [2]
  1.2 Ausgangssituation                      [3]
  1.3 Ist-Analyse                            [4]
  1.4 Problemstellung                        [5]
  1.5 SWOT-Analyse                           [5]
  1.6 Soll-Konzept                           [6]
  1.7 Projektziele nach SMART                [7]
  1.8 Projektbegründung                      [8]
  1.9 Projektabgrenzung                      [9]
  1.10 Projektschnittstellen                 [10]
  1.11 Projektauftrag                        [11]

2 PROJEKTPLANUNG                             [Seite 12–23]
  2.1 Vorgehensmodell                        [13]
  2.2 Projektphasen                          [14]
  2.3 Projektstrukturplan (PSP)              [15–16]  ← A1 im Anhang
  2.4 Arbeitspakete                          [16]
  2.5 Meilensteinplanung                     [17]      ← MTA als Abb. 5/15
  2.6 Ressourcenplanung                      [18]
  2.7 Kostenplanung                          [19]
  2.8 Kommunikationsplanung                  [20]
  2.9 Risikoanalyse                          [21]
  2.10 Qualitätsplanung                      [22]
  2.11 Abweichungen vom Projektantrag        [23]

3 ANALYSE UND KONZEPTION                     [Seite 24–35]
  3.1 Anforderungsanalyse                    [25]      ← Anforderungsmatrix (Tab. 7)
  3.2 Lastenheft / Fachkonzept               [26]      ← A2 im Anhang
  3.3 Stakeholderanalyse                     [27]      ← Stakeholder-Matrix (Tab. 3)
  3.4 Make-or-Buy-Entscheidung               [28]      ← Nutzwertanalyse (Tab. 5/6)
  3.5 Wirtschaftlichkeitsanalyse             [29]
  3.6 Nutzwertanalyse                        [30]
  3.7 Zero-Trust-Konzept                     [31]      ← NIST SP 800-207 Mapping
  3.8 RBAC-Modell                            [32]      ← Rollentabelle, A5 ERD
  3.9 Datenschutz- & Sicherheitskonzept      [33]      ← DPIA, A14 Checkliste
  3.10 Lenkungsausschuss                     [33]
  3.11 Rolle des Projektleiters              [34]
  3.12 Datenschutz- und Sicherheitskonzept   [35]

4 TECHNISCHER ENTWURF                        [Seite 36–47]
  4.1 Zielplattform & Technologie-Stack      [36]
  4.2 Architekturdesign                      [36–37]    ← Schichtenarchitektur (Abb. 8)
  4.3 GitHub-Workflow-Integration            [37–38]    ← YAML, Stages (Abb. 6)
  4.4 Self-Service-Prozess                   [38–39]    ← Sequenzdiagramm (Abb. 7)
  4.5 Datenmodell                            [39–40]    ← ERD (Abb. 8), A5
  4.6 Geschäftslogik                         [40–41]    ← State Machine, Policy Engine
  4.7 Audit-Logging                          [41–42]    ← Append-Only, Hash-Chain (Abb. 9)
  4.8 Schnittstellen                         [42–43]    ← API-Endpunkte, A11
  4.9 Maßnahmen zur Qualitätssicherung       [43–44]    ← TDD, CodeQL, Coverage
  4.10 Pflichtenheft / Datenverarbeitungskonzept [44]    ← A4 im Anhang

5 UMSETZUNG                                  [Seite 48–57]
  5.1 Aufbau der Entwicklungsumgebung        [48]      ← Docker, CI/CD
  5.2 Implementierung der Datenstrukturen    [48–49]    ← Migrationen, Seed
  5.3 Implementierung des RBAC-Modells       [49–50]    ← Code-Snippets
  5.4 Implementierung der Benutzeroberfläche [50–51]    ← React/TS, A7 Wireframes
  5.5 Implementierung der GitHub-Automatisierung [51–52] ← Workflow-YAML (A3)
  5.6 Implementierung der Geschäftslogik     [52–53]    ← Policy Engine
  5.7 Implementierung der Audit-Protokollierung [53]    ← Hash-Chain, Export
  5.8 Implementierung der Qualitätssicherung [53–54]    ← Tests, Security Scans
  5.9 Entwicklerdokumentation                [54]      ← A9 im Anhang

6 TEST UND ABNAHME                           [Seite 58–67]
  6.1 Testkonzept                            [58]      ← Testpyramide, KPI-Matrix (Tab. 12)
  6.2 Funktionstests                         [59]      ← TF01–TF12 (Tab. 8)
  6.3 Integrationstests                      [60]
  6.4 Security-Tests                         [60]      ← CodeQL, Secret-Scan, TF10
  6.5 Datenschutzprüfung                     [61]      ← DPIA, Checkliste A14
  6.6 Testfallmatrix                         [61]      ← Tab. 8, A10 Konsolenausgabe
  6.7 Fehleranalyse                          [62]      ← 3 Bugs, Severity, Fix
  6.8 Soll-Ist-Vergleich                     [63]      ← Tab. 9
  6.9 Abnahme                                [64]      ← A15 Protokoll

7 EINFÜHRUNG UND DOKUMENTATION               [Seite 68–75]
  7.1 Einführungskonzept                     [68]      ← Rollout-Plan (Abb. 13)
  7.2 Pilotbetrieb                           [69]      ← 15 Nutzer, KPIs
  7.3 Schulung                               [69–70]   ← Materialien, A13
  7.4 Change Management                      [70]
  7.5 Benutzerdokumentation                  [71]      ← A13
  7.6 Betriebsdokumentation                  [71–72]   ← Deployment, Backup, Monitoring
  7.7 Übergabe                               [72]

8 PROJEKTABSCHLUSS                           [Seite 76–85]
  8.1 Projektergebnis                        [76]
  8.2 Soll-Ist-Vergleich (wirtschaftlich)    [77]      ← Tab. 13
  8.3 Wirtschaftliche Bewertung              [77–78]   ← ROI, Amortisation
  8.4 Lessons Learned                        [78–79]   ← Positiv / Optimierung
  8.5 Risiken nach Projektabschluss          [79]      ← Restrisiken
  8.6 Ausblick                               [80]      ← KI-Erweiterungen (CodeBERT, flan-t5)
  8.7 Persönliches Fazit                     [81–82]   ← Reflexion, 1–2 Seiten

LITERATURVERZEICHNIS                         [i–ii]
ABKÜRZUNGSVERZEICHNIS                        [iii]
ABBILDUNGSVERZEICHNIS                        [iv]
TABELLENVERZEICHNIS                          [v]

ANHANG                                       [vi–xx]
  A1 Detaillierte Zeitplanung (Gantt/Excel)       [vi–vii]
  A2 Lastenheft-Auszug                            [viii]
  A3 Use-Case-Diagramm                            [ix]
  A4 Pflichtenheft-Auszug                         [x]
  A5 Datenmodell (ERD)                            [xi]
  A6 EPK-Prozessbeschreibung                      [xii]
  A7 Oberflächenentwürfe (Wireframes)             [xiii–xiv]
  A8 Screenshots der Anwendung (9 Stück)          [xv–xvii]
  A9 Entwicklerdokumentation (README, API)        [xviii–xix]
  A10 Testfall-Konsolenausgabe                    [xx]
  A11 Schnittstellenübersicht (OpenAPI)           [xxi]
  A12 Klassendiagramm                             [xxii]
  A13 Benutzerdokumentation (User-Guide)          [xxiii–xxiv]
  A14 Datenschutz-Checkliste (DSGVO Art. 5, 25, 32) [xxv]
  A15 Abnahmeprotokoll (unterschrieben)           [xxvi]

EIDESSTATTLICHE ERKLÄRUNG                      [xxvii, nicht nummeriert]

---

## Seitenbudget-Detail (Ziel: ~75 Seiten)

| Bereich | Min | Soll | Max | Puffer |
|---------|-----|------|-----|--------|
| **Vorwort + Verzeichnisse** (römisch) | 8 | 10 | 12 | – |
| **Kapitel 1** (Projektinitiierung) | 9 | 11 | 13 | +2 |
| **Kapitel 2** (Projektplanung) | 10 | 12 | 14 | +2 |
| **Kapitel 3** (Analyse & Konzeption) | 11 | 12 | 14 | +2 |
| **Kapitel 4** (Technischer Entwurf) | 10 | 12 | 14 | +2 |
| **Kapitel 5** (Umsetzung) | 8 | 10 | 12 | +2 |
| **Kapitel 6** (Test & Abnahme) | 8 | 10 | 12 | +2 |
| **Kapitel 7** (Einführung) | 6 | 8 | 10 | +2 |
| **Kapitel 8** (Abschluss) | 6 | 8 | 10 | +2 |
| **Literatur + Abkürzungen** | 2 | 4 | 5 | – |
| **Textteil Summe** | **68** | **89** | **110** | **±10** |
| **Anhang A1–A15** | 15 | 20 | 25 | ±5 |
| **Eidesstattliche Erklärung** | 1 | 1 | 1 | – |
| **GESAMT** | **84** | **~75** | **136** | **Ziel: 70–85** |

> **Hinweis:** Das Ziel von ~75 Seiten bezieht sich auf das **finale PDF** (DIN A4, 12 pt, 1,5-zeilig, Ränder 2,5/2/2,5/2 cm). Markdown → PDF via Pandoc/LaTeX erzeugt typischerweise mehr Seiten als Word. **Zielkorridor: 70–85 Seiten.**

---

## Abbildungen (16 Stück, durchlaufend nummeriert)

| Nr. | Titel | Kapitel | Format | Status |
|-----|-------|---------|--------|--------|
| 1 | Projektstrukturplan (PSP) | 2.3 | Mermaid → SVG | ✅ |
| 2 | Use-Case-Diagramm | 3.3 | Mermaid → SVG | ✅ → A3 |
| 3 | Stakeholder-Matrix | 3.3 | Tabelle | ✅ |
| 4 | Risiko-Matrix | 2.9 | Tabelle | ✅ |
| 5 | Meilensteintrendanalyse (MTA) | 2.5 | Diagramm | ⚠️ **Fehlt** |
| 6 | GitHub Workflow automatisierte Rechtevergabe | 4.3 | Mermaid → SVG | ✅ |
| 7 | Self-Service-Prozess | 4.4 | Mermaid → SVG | ✅ |
| 8 | RBAC-Datenmodell (ERD) | 4.5 | Mermaid → SVG | ✅ → A5 |
| 9 | Audit-Log-Prozess | 4.7 | Mermaid → SVG | ✅ |
| 10 | Beispielhafter Testfall mit Soll-Ist | 6.6 | Diagramm | ⚠️ **Fehlt** |
| 11 | DSGVO-Checkliste Rollen/Zugriff | 3.9 | Markdown/Tabelle | ✅ → A14 |
| 12 | Vergleichsmatrix IAM-Systeme | 3.4 | Tabelle | ✅ |
| 13 | Rollout-Plan | 7.1 | Diagramm | ⚠️ **Fehlt** |
| 14 | Abnahmeprozess | 6.9 | Diagramm | ⚠️ **Fehlt** |
| 15 | Meilensteintrendanalyse (MTA) | 2.5 | Diagramm | = Abb. 5 |
| 16 | SWOT-Analyse | 1.4 | Tabelle | ✅ |

**Fehlende Diagramme (Priorität A): MTA (5/15), Testfall-Beispiel (10), Rollout-Plan (13), Abnahmeprozess (14)**

---

## Tabellen (13 Stück, durchlaufend nummeriert)

| Nr. | Titel | Kapitel | Status |
|-----|-------|---------|--------|
| 1 | Zeitplanung (Arbeitspakete) | 2.4 | ✅ |
| 2 | Kostenplanung | 2.7 | ✅ |
| 3 | Stakeholder-Matrix | 3.3 | ✅ |
| 4 | Risiko-Matrix | 2.9 | ✅ |
| 5 | Nutzwertanalyse | 3.6 | ✅ |
| 6 | Make-or-Buy-Entscheidung | 3.4 | ✅ |
| 7 | Anforderungsmatrix (Muss/Kann) | 3.2 | ✅ |
| 8 | Testfallmatrix | 6.6 | ✅ (12/12 bestanden) |
| 9 | Soll-Ist-Vergleich (funktional) | 6.8 | ✅ |
| 10 | Kommunikationsmatrix | 2.8 | ✅ |
| 11 | RACI-Matrix | 2.3 | ✅ |
| 12 | KPI-Matrix | 6.1 | ✅ |
| 13 | Amortisationsrechnung | 8.3 | ✅ |

---

## Anhang-Dateien (Export-Formate)

| Anhang | Titel | Quellformat | Export-Format | Dateiname |
|--------|-------|-------------|---------------|-----------|
| A1 | Zeitplanung | Excel / GanttProject | PDF (A4, quer) | `A1_Zeitplanung.pdf` |
| A2 | Lastenheft-Auszug | Markdown (Kap. 3.2) | PDF | `A2_Lastenheft.pdf` |
| A3 | Use-Case-Diagramm | Mermaid | SVG → PDF | `A3_UseCase.svg` / `.pdf` |
| A4 | Pflichtenheft-Auszug | Markdown (Kap. 4.10) | PDF | `A4_Pflichtenheft.pdf` |
| A5 | Datenmodell (ERD) | Mermaid | SVG → PDF | `A5_ERD.svg` / `.pdf` |
| A6 | EPK-Prozess | PlantUML | SVG → PDF | `A6_EPK.svg` / `.pdf` |
| A7 | Wireframes | Figma / Balsamiq | PNG/PDF (300 DPI) | `A7_Wireframes.pdf` |
| A8 | Screenshots (9) | Prototyp (Flameshot) | PNG (150 DPI) | `A8_Screenshot_01.png` … `09.png` |
| A9 | Entwicklerdokumentation | Markdown + OpenAPI | PDF | `A9_DevDoc.pdf` |
| A10 | Testfall-Konsole | Jest/Pytest Output | Text → PDF | `A10_TestConsole_Ausgabe.pdf` |
| A11 | Schnittstellen | OpenAPI 3.0 (YAML) | PDF / HTML | `A11_OpenAPI.pdf` |
| A12 | Klassendiagramm | PlantUML | SVG → PDF | `A12_ClassDiagram.svg` |
| A13 | Benutzerdokumentation | Markdown | PDF | `A13_UserGuide.pdf` |
| A14 | DSGVO-Checkliste | Markdown (02_anhang/14) | PDF | `A14_DSGVO_Checkliste.pdf` |
| A15 | Abnahmeprotokoll | Markdown (11_abnahme/01) | PDF (unterschrieben) | `A15_Abnahmeprotokoll.pdf` |

---

## Export-Pipeline (empfohlen)

```bash
# 1. Mermaid → SVG
cd diagrams/mermaid
for f in *.mmd; do mmdc -i "$f" -o "${f%.mmd}.svg"; done

# 2. PlantUML → SVG
cd diagrams/plantuml
for f in *.puml; do plantuml -tsvg "$f"; done

# 3. Markdown → PDF (via Pandoc + XeLaTeX)
pandoc 09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md \
  --pdf-engine=xelatex \
  -V geometry:"top=2.5cm,bottom=2.5cm,left=3cm,right=2cm" \
  -V fontsize=12pt \
  -V linestretch=1.5 \
  -V fontfamily=libertine \
  -V lang=de-DE \
  --toc --toc-depth=3 \
  --number-sections \
  -o export/PROJEKTARBEIT_ZERO_TRUST_FINAL.pdf

# 4. Anhang-Dateien einzeln konvertieren & zusammenfügen
# (pdfunite / Ghostscript)
```

---

## Qualitäts-Checkliste vor Abgabe

| Kriterium | Check |
|-----------|-------|
| [ ] Alle 16 Abbildungen als SVG/PNG im Anhang referenziert | |
| [ ] Alle 13 Tabellen im Text referenziert ("vgl. Tab. 5") | |
| [ ] Seitenzahlen in Verzeichnissen stimmen (PDF prüfen) | |
| [ ] Eidesstattliche Erklärung unterschrieben + Datum | |
| [ ] Abnahmeprotokoll (A15) unterschrieben (Auftraggeber + PL) | |
| [ ] Sperrvermerk korrekt (VFB, IHK Stuttgart) | |
| [ ] Deckblatt: Prüflingsnummer, IHK, Betreuer, Datum | |
| [ ] Seitenzahlung: römisch (I–X) → arabisch (1–Ende) | |
| [ ] Keine "TODO_", "Simulation", "Platzhalter" im finalen Text | |
| [ ] Alle Screenshots echt (nicht HTML-Simulation) | |
| [ ] Dateigröße PDF < 50 MB | |
| [ ] 3 Exemplare gebunden + 1 PDF/A für IHK-Portal | |

---

*Stand: 09.07.2026 | Nächste Aktualisierung nach Screenshot-Erstellung (KW 28)*