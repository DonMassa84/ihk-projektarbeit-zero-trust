# Gap-Analyse: IHK-Projektarbeit "Zero-Trust-Sicherheitskonzept mit GitHub-Integration"

**Datum:** 09.07.2026  
**Prüfling:** Daniel Massa (615951)  
**Abgabefrist:** 01.11.2026 (in 115 Tagen)  
**Status:** 🟡 **GELB – Überarbeitung erforderlich vor Abgabe**

---

## 1. Zusammenfassung (Executive Summary)

| Dimension | Status | Begründung |
|-----------|--------|------------|
| **Inhaltliche Vollständigkeit** | 🟢 GRÜN | Alle 8 Pflichtkapitel + Anhang vorhanden, Inhalte substanziell |
| **Formale Einhaltung** | 🟡 GELB | Verzeichnisse vorhanden, aber Seitenzahlen fehlen; Abbildungs-/Tabellenbeschriftungen teilweise inkonsistent |
| **Nachweisbarkeit** | 🟡 GELB | Screenshots als "Simulation" markiert, Anhang A2–A15 nur als Platzhalter |
| **Prototyp-Charakter** | 🟢 GRÜN | Durchgängig als Prototyp/Machbarkeitsnachweis gekennzeichnet |
| **IHK-Formale Vorgaben** | 🟡 GELB | Sperrvermerk, Eidesstattliche Erklärung, Abgabedatum OK; Unterschriften fehlen |
| **Export-Qualität** | 🟡 GELB | DOCX/HTML vorhanden, PDF nur via weasyprint (kein LaTeX/Typst) |

**Gesamtbewertung:** **75 % abgabereif** – fehlende 25 % sind formaler Natur (Anhänge befüllen, Screenshots echt, Signaturen, PDF/LaTeX-Export).

---

## 2. Detaillierte Gap-Analyse nach IHK-Kriterien

### 2.1 Formale Vorgaben (Rahmenprüfungsordnung IHK)

| Kriterium | Soll | Ist | Gap | Priorität |
|-----------|------|-----|-----|-----------|
| Deckblatt | Vollständig | ✅ Vollständig | – | – |
| Sperrvermerk | Vorhanden | ✅ Vorhanden | – | – |
| Inhaltsverzeichnis | 3 Ebenen, seitenrichtig | ✅ Struktur OK, **Seitenzahlen fehlen** | **Hoch** | A1 |
| Abbildungsverzeichnis | Nummeriert, Titel, Seite | ✅ 16 Einträge, **Seiten fehlen** | **Hoch** | A1 |
| Tabellenverzeichnis | Nummeriert, Titel, Seite | ✅ 13 Einträge, **Seiten fehlen** | **Hoch** | A1 |
| Abkürzungsverzeichnis | Alphabetisch, vollständig | ✅ 43 Einträge | – | – |
| Literaturverzeichnis | Einheitlich, DOI/URL + Abrufdatum | ✅ 16 Quellen, konsistent | – | – |
| Eidesstattliche Erklärung | Unterschrieben, datiert | ⚠️ Text OK, **Unterschrift & Datum fehlen** | **Kritisch** | A1 |
| Seitenzahlung | Römisch (Vorwort/Verzeichnisse), Arabisch (Kapitel) | ⚠️ **Nicht im Markdown umgesetzt** | **Hoch** | A1 |
| Dateigröße | < 50 MB | ✅ ~12 MB (DOCX), PDF ~0.6 MB | – | – |
| Abgabedatum | 01.11.2026 | ✅ Konsistent überall | – | – |

### 2.2 Inhaltliche Kapitel (RFO-konform)

| Kapitel | Titel | Seitenbudget (ca.) | Ist-Status | Gap |
|---------|-------|-------------------|------------|-----|
| 1 | Projektinitiierung | 10–12 | ✅ Vollständig, SMART-Ziele konkret | – |
| 2 | Projektplanung | 10–12 | ✅ PSP, Meilensteine, Kosten, Risiken | – |
| 3 | Analyse & Konzeption | 12–15 | ✅ Make-or-Buy, Nutzwert, RBAC, Zero Trust | – |
| 4 | Technischer Entwurf | 10–12 | ✅ Architektur, Workflow, Datenmodell | – |
| 5 | Umsetzung | 8–10 | ✅ Code-Beispiele, YAML, ML-Eval erwähnt | – |
| 6 | Test & Abnahme | 8–10 | ✅ 12 Testfälle alle bestanden | – |
| 7 | Einführung & Doku | 6–8 | ✅ Pilot, Schulung, Change Mgmt | – |
| 8 | Projektabschluss | 6–8 | ✅ Lessons Learned, Wirtschaftlichkeit | – |
| **Gesamt Textteil** | | **70–85** | **ca. 40 Seiten (Markdown → PDF)** | **Seitenbudget prüfen** |

**Bewertung:** Inhaltlich **sehr gut**, aber **Seitenzahl im PDF muss geprüft werden** (IHK erwartet ca. 40–60 Seiten Textteil + Anhang).

### 2.3 Anhang (A1–A15) – **Haupt-Gap**

| Anhang | Titel | Status | Handlung |
|--------|-------|--------|----------|
| A1 | Detaillierte Zeitplanung | ✅ Verweis auf Tabelle 1/2.3 | OK |
| A2 | Lastenheft-Auszug | ❌ **Nur Platzhalter** | **Inhalt erstellen** |
| A3 | Use-Case-Diagramm | ❌ **Nur Platzhalter** | **Diagramm exportieren** |
| A4 | Pflichtenheft-Auszug | ❌ **Nur Platzhalter** | **Inhalt erstellen** |
| A5 | Datenmodell (ERD) | ❌ **Nur Platzhalter** | **ERD als SVG/PNG exportieren** |
| A6 | EPK-Prozessbeschreibung | ❌ **Nur Platzhalter** | **EPK erstellen** |
| A7 | Oberflächenentwürfe | ❌ **Nur Platzhalter** | **Wireframes exportieren** |
| A8 | Screenshots der Anwendung | ⚠️ **9 Simulations-Platzhalter** | **Echte Screenshots erstellen** |
| A9 | Entwicklerdokumentation | ❌ **Nur Platzhalter** | **README/API-Doc exportieren** |
| A10 | Testfall Konsole | ❌ **Nur Platzhalter** | **Test-Logs exportieren** |
| A11 | Schnittstellenübersicht | ❌ **Nur Platzhalter** | **OpenAPI/Swagger exportieren** |
| A12 | Klassendiagramm | ❌ **Nur Platzhalter** | **PlantUML → SVG exportieren** |
| A13 | Benutzerdokumentation | ❌ **Nur Platzhalter** | **User-Guide als PDF erstellen** |
| A14 | Datenschutz-Checkliste | ✅ **Erstellt** (02_anhang/14) | **In Master einbinden** |
| A15 | Abnahmeprotokoll | ✅ **Erstellt** (11_abnahme/01) | **In Master einbinden** |

**→ 12 von 15 Anhängen sind leer!** Das ist der **größte formale Mangel**.

### 2.4 Diagramme & Visualisierung

| Diagramm | Format | Status | Gap |
|----------|--------|--------|-----|
| PSP (Abb. 1) | Mermaid | ✅ In 04_diagramme_mermaid/ | Export prüfen |
| Use-Case (Abb. 2) | Mermaid | ✅ Vorhanden | **Nicht als Bild im Anhang A3** |
| Stakeholder-Matrix (Abb. 3) | Tabelle | ✅ In Kapitel 3.3 | – |
| Risiko-Matrix (Abb. 4) | Tabelle | ✅ In Kapitel 2.9 | – |
| Meilensteintrend (Abb. 5/15) | Text | ⚠️ Nur Beschreibung | **Diagramm fehlt** |
| GitHub Workflow (Abb. 6) | Mermaid | ✅ Vorhanden | Export prüfen |
| Self-Service (Abb. 7) | Mermaid | ✅ Vorhanden | Export prüfen |
| RBAC-ERD (Abb. 8) | Mermaid | ✅ Vorhanden | **Nicht als A5 exportiert** |
| Audit-Log (Abb. 9) | Mermaid | ✅ Vorhanden | Export prüfen |
| Testfall (Abb. 10) | Text | ⚠️ Nur Tabelle | **Visualisierung fehlt** |
| DSGVO-Checkliste (Abb. 11) | Markdown | ✅ In 02_anhang/14 | **Nicht als Bild** |
| Make-or-Buy (Abb. 12) | Tabelle | ✅ In Kapitel 3.4 | – |
| Rollout-Plan (Abb. 13) | Text | ⚠️ Nur Beschreibung | **Diagramm fehlt** |
| Abnahmeprozess (Abb. 14) | Text | ⚠️ Nur Beschreibung | **Diagramm fehlt** |
| SWOT (Abb. 16) | Tabelle | ✅ In Kapitel 1.4 | – |

### 2.5 Screenshots (A8) – Kritisch

| # | Name | Status | Quelle |
|---|------|--------|--------|
| 1 | GitHub Repo Übersicht | ⚠️ **Simulation** (HTML → Chrome Headless) | 10_screenshots/sources/ |
| 2 | GitHub Actions Workflow | ⚠️ **Simulation** | dito |
| 3 | YAML Workflow-Datei | ⚠️ **Simulation** | dito |
| 4 | Testlauf Actions | ⚠️ **Simulation** | dito |
| 5 | Secret-Scanning | ⚠️ **Simulation** | dito |
| 6 | Rollen-/Teamstruktur | ⚠️ **Simulation** | dito |
| 7 | Audit-Log-Auszug | ⚠️ **Simulation** | dito |
| 8 | Self-Service-Formular | ⚠️ **Simulation** | dito |
| 9 | Terminal-Testausgabe | ⚠️ **Simulation** | dito |

**IHK-Regel:** "Screenshots müssen aus der realen Anwendung stammen. Simulierte Platzhalter sind nicht prüfungsrelevant." → **Alle 9 müssen durch echte Prototyp-Screenshots ersetzt werden.**

### 2.6 Nachweisbarkeit & Prototyp-Charakter

| Aspekt | Status | Bewertung |
|--------|--------|-----------|
| Code-Referenzen | ✅ YAML-Beispiel, API-Endpunkte | OK |
| Testprotokolle | ✅ 12 Testfälle mit Status | OK |
| ML-Evaluation | ⚠️ Erwähnt (CodeBERT F1=1.0, flan-t5), **kein Beleg** | **Gap** |
| DPIA | ✅ Erwähnt, Checkliste in A14 | OK |
| Abnahmeprotokoll | ✅ Erstellt (11_abnahme/01) | **Nicht in Master eingebunden** |
| Eigenleistung-Abgrenzung | ✅ Kapitel 3.11, 8.7 | OK |
| Prototyp-Kennzeichnung | ✅ Durchgängig "prototypisch", "Simulation" | **Sehr gut** |

---

## 3. Priorisierte To-Do-Liste (Critical Path)

### 🔴 PRIORITÄT A – Kritisch (Blockiert Abgabe)

| # | Aufgabe | Aufwand | Deadline | Verantwortlich |
|---|---------|---------|----------|----------------|
| A1 | **Echte Screenshots** aus laufendem Prototyp erstellen (9 Stück) | 4–6 h | **Woche 1** | Daniel |
| A2 | **Alle Anhang-Inhalte** (A2–A13) befüllen & als PDF/SVG exportieren | 8–12 h | **Woche 1–2** | Daniel |
| A3 | **Eidesstattliche Erklärung** unterschreiben (Datum, Signatur) | 5 min | **Woche 1** | Daniel |
| A4 | **Abnahmeprotokoll** (A15) & **DSGVO-Checkliste** (A14) in Master einbinden | 1 h | **Woche 1** | Daniel |
| A5 | **PDF-Export via LaTeX/Typst** (seitenrichtig, Verzeichnisse mit Seitenzahlen) | 2–4 h | **Woche 2** | Daniel |
| A6 | **Seitenzahlen & Verzeichnisse** im finalen PDF prüfen | 1 h | **Woche 2** | Daniel |

### 🟠 PRIORITÄT B – Wichtig (Qualität)

| # | Aufgabe | Aufwand | Deadline |
|---|---------|---------|----------|
| B1 | Meilensteintrendanalyse (MTA) als Diagramm (Abb. 5/15) | 2 h | Woche 2 |
| B2 | Rollout-Plan (Abb. 13) & Abnahmeprozess (Abb. 14) visualisieren | 2 h | Woche 2 |
| B3 | ML-Evaluation (CodeBERT, flan-t5) mit Logs/Artifacts belegen | 2 h | Woche 2 |
| B4 | Alle Mermaid-Diagramme als SVG exportieren & in Anhang einbinden | 1 h | Woche 2 |
| B5 | Prüferfragen-Katalog (50+) finalisieren & Antworten vorbereiten | 4 h | Woche 3 |

### 🟢 PRIORITÄT C – Nice-to-have

| # | Aufgabe | Aufwand |
|---|---------|---------|
| C1 | Cover-Grafik professionell gestalten | 1 h |
| C2 | Icon-Set für Diagramme einheitlich | 1 h |
| C3 | Präsentationsfolien (15 Min) ausbauen | 3 h |
| C4 | Zweit-Korrektur (Rechtschreibung, LanguageTool) | 2 h |

---

## 4. Seitenbudget-Planung (PDF-Ziel)

| Bereich | Zielseiten | Puffer |
|---------|------------|--------|
| Deckblatt, Sperrvermerk, Vorwort, Verzeichnisse | 8–10 (römisch) | – |
| Kapitel 1–8 (Textteil) | 40–50 | ±5 |
| Literatur, Abkürzungen | 3–4 | – |
| Anhang A1–A15 | 15–25 | ±5 |
| Eidesstattliche Erklärung | 1 | – |
| **Gesamt** | **67–90** | **Ziel: ~75** |

**IHK-Erfahrung:** 60–80 Seiten ist der Sweet Spot. >100 wirkt "aufgebläht", <50 "zu dünn".

---

## 5. Prüferfragen-Vorbereitung (Top 20 aus 06_prueferfragen/)

Die Datei `06_prueferfragen/01_prueferfragen_katalog.md` enthält **53 Fragen** in 6 Kategorien (A–F). **Vollständig und gut beantwortet.** Kein Handlungsbedarf außer: **Antworten mündlich trainieren** (Zeitlimit 20 Min Vortrag + 20 Min Fachgespräch).

---

## 6. Bauplan für die letzten 4 Wochen

| Woche | Fokus | Meilenstein |
|-------|-------|-------------|
| **KW 28 (07–11.07)** | **Screenshots + Anhang-Inhalte** | A1–A4 erledigt, Prototyp läuft |
| **KW 29 (14–18.07)** | **Export-Pipeline + PDF-Qualität** | A5–A6, B1–B4, PDF seitenrichtig |
| **KW 30 (21–25.07)** | **Feinschliff + Prüferfragen** | B5, C1–C4, Generalprobe Vortrag |
| **KW 31 (28.07–01.08)** | **Puffer / Korrektur** | Letzte Korrekturen, Unterschriften, finale PDF |
| **Puffer bis 01.11.** | **3 Monate Reserve** für unvorhergesehenes | – |

---

## 7. Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Prototyp nicht stabil für Screenshots | Mittel | Hoch | Docker-Compose fixieren, Testdaten seed-en |
| LaTeX/Typst-Export bricht | Mittel | Hoch | Fallback: weasyprint + manuelle Nachbearbeitung |
| Betreuer nicht verfügbar für Abnahme | Niedrig | Hoch | Stellvertreter benennen, Termin früh fixieren |
| IHK formale Beanstandung (Seitenzahlen, Signaturen) | Mittel | Hoch | Checkliste A1–A6 strikt abarbeiten |
| Dateigröße > 50 MB durch Bilder | Niedrig | Mittel | Bilder komprimieren (PNG 150 DPI, JPEG 85%) |

---

## 8. Nächste konkrete Aktionen (Heute/Morgen)

```bash
# 1. Prototyp starten & Screenshots machen
cd ~/openclaw-workspace/ihk_zero_trust_projektarbeit_final/12_prototype_zero_trust
docker-compose up -d
# Screenshots mit Flameshot / GNOME Screenshot machen → 10_screenshots/

# 2. Anhang-Inhalte generieren
# A2: Lastenheft-Auszug aus Kapitel 3.2 → PDF
# A3: Use-Case aus Mermaid → SVG → PDF
# A4: Pflichtenheft aus 4.10 → PDF
# A5: ERD aus Mermaid → SVG → PDF
# A6: EPK aus PlantUML → SVG → PDF
# A7: Wireframes (Figma/Balsamiq Export) → PDF
# A9: README.md + OpenAPI Spec → PDF
# A10: Jest/Pytest Output → Text → PDF
# A11: OpenAPI Spec → PDF
# A12: PlantUML Klassendiagramm → SVG → PDF
# A13: User-Guide (Markdown) → PDF

# 3. Master-Markdown aktualisieren (Anhang-Verweise auf echte Dateien)

# 4. PDF bauen (Pandoc + LaTeX/Typst)
bash 09_export/build_scripts/export_docx_pdf.sh
```

---

## 9. Fazit

**Die inhaltliche Arbeit ist exzellent.** Konzept, Methodik, technische Umsetzung und Dokumentation entsprechen **hohem IHK-Niveau**. Der **einzige Blocker** sind formale Lücken im Anhang (12/15 leer), simulierte Screenshots und der fehlende seitenrichtige PDF-Export.

**Bei konsequenter Abarbeitung der Priorität-A-Liste in den nächsten 2 Wochen ist die Arbeit "prüfungsnah finalisierbar" (GRÜN).**

---

*Erstellt auf Basis von:*
- `PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md` (Master, 1211 Zeilen)
- `AI_HANDOFF.md` (Projektsteuerung)
- `00_master/08_todo_liste_realdaten.md` (Offene TODOs)
- `03_tabellen/`, `04_diagramme_mermaid/`, `10_screenshots/`, `11_abnahme/`, `07_quellen/`, `06_prueferfragen/`
- `design/` (Design System, Farbpalette, Typografie, Layout-Regeln – heute erstellt)