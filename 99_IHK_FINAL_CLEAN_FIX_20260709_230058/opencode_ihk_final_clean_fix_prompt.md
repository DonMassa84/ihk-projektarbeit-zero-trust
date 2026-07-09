# OPENCODE FINAL CLEAN FIX — PROJEKTARBEIT ZERO TRUST

## Eingabedatei
`00_input/PROJEKTARBEIT_ZERO_TRUST_ABGABE_FINAL.pdf`

## Ziel
Die aktuelle PDF ist formal NICHT abgabereif. Erstelle eine saubere Endfassung mit stabiler Nummerierung, korrektem Inhaltsverzeichnis, entschärfter Wahrheitssicherheit und prüfungstauglichem IHK-Layout.

Arbeite bevorzugt mit vorhandenen Quelldateien im Projektordner. Wenn keine Quelldatei vorhanden ist, extrahiere den PDF-Text und baue daraus eine neue Markdown-/DOCX-/PDF-Struktur.

---

## 1. KRITISCHE FORMATFEHLER BEHEBEN

### 1.1 Inhaltsverzeichnis komplett neu erzeugen
Aktuelle Fehler:
- Englisches "Contents" steht oben.
- Zusätzlich steht ein deutsches manuelles "INHALTSVERZEICHNIS" im Text.
- Nummerierung ist kaputt: "2 1 Projektinitiierung", "3 2 Projektplanung" usw.
- Kapitelnummern sind doppelt.

Ziel:
- Nur ein einziges deutsches Inhaltsverzeichnis.
- Keine Überschrift "Contents".
- Keine manuell eingefügte TOC-Textwüste.
- Kapitelnummern korrekt:
  1 Projektinitiierung
  2 Projektplanung
  3 Analyse und Konzeption
  4 Technischer Entwurf
  5 Umsetzung
  6 Test und Abnahme
  7 Einführung und Dokumentation
  8 Projektabschluss
- Vorwort, Sperrvermerk, Verzeichnisse mit römischer Nummerierung oder ohne Kapitelnummer.
- Anhang separat.

### 1.2 Doppelte Bildunterschriften entfernen
Aktuelle Fehler:
- "Abb. 16: SWOT-Analyse Abb. 16: SWOT-Analyse"
- "Abb. 1: Projektstrukturplan Abb. 1: Projektstrukturplan"
- ähnliche Dopplungen im gesamten Dokument.

Ziel:
- Jede Abbildung nur einmal beschriften.
- Format: `Abbildung X: Titel (eigene Darstellung / Screenshot aus Testumgebung / Mockup / schematische Darstellung)`
- Keine doppelte Caption.

### 1.3 Nicht gerenderte Bilder kennzeichnen oder entfernen
Wenn Diagramme/Bilder nicht wirklich sichtbar sind und nur Text wie "Projektstrukturplan" steht:
- entweder sauber als gerendertes Diagramm neu erzeugen,
- oder aus dem Hauptteil entfernen und im Anhang als Platzhalter kennzeichnen.
Keine leeren Bildstellen.

---

## 2. WAHRHEITSSICHERHEIT KORRIGIEREN

### 2.1 Eidesstattliche Erklärung ersetzen
Aktuelle riskante Stelle:
"Die in der Arbeit beschriebenen Projektergebnisse, Messwerte, Testergebnisse und Screenshots stammen aus der tatsächlichen Projektbearbeitung."

Diese Formulierung komplett ersetzen durch:

"Ich versichere, dass ich die vorliegende Projektarbeit selbstständig erstellt und keine anderen als die angegebenen Quellen und Hilfsmittel verwendet habe. Konzepte, Prototypen, Testfälle, Auswertungen, Screenshots und Abbildungen, die auf einer Testumgebung, Simulation, synthetischen Daten oder Mockups beruhen, sind entsprechend gekennzeichnet. Betriebliche Daten wurden nur verwendet, soweit sie für die Projektdokumentation zulässig und anonymisiert darstellbar sind."

### 2.2 100-%-F1-Score entfernen
Aktuelle riskante Stelle im Ausblick:
"CodeBERT-basierter Anomalie-Detektor mit 100 % F1-Score ..."

Komplett entfernen und ersetzen durch:

"Als möglicher Folgeausbau kann eine KI-gestützte Anomalieerkennung für Rollenänderungen prototypisch geprüft werden. Diese Erweiterung ist nicht Bestandteil der Projektabnahme und wurde im Rahmen der Projektarbeit nicht produktiv bewertet."

Auch entfernen:
- eval_f1=1.0
- 2000 synthetische GitHub-Events als harte Leistungsbehauptung
- Memorization-Fallback
- produktionsreife KI-Formulierungen

### 2.3 Abnahme entschärfen
Aktuelle riskante Stelle:
"Das Abnahmeprotokoll wurde unterzeichnet und ist im Anhang hinterlegt."

Wenn keine echte Unterschrift vorhanden ist, ersetzen durch:

"Für den Prototyp wurde eine fachliche Abnahmeempfehlung anhand definierter Muss-Kriterien vorbereitet. Das Abnahmeprotokoll im Anhang dient als Vorlage zur formalen Abnahme durch Auftraggeber und IT-Verantwortliche."

Im Anhang:
- "IHK-Betreuer" als Abnahmeteilnehmer entfernen.
- Keine Aussage, dass alle Personen unterschrieben haben.
- Leere Unterschriftenfelder als "Vorlage" kennzeichnen.

---

## 3. ZAHLEN PLAUSIBILISIEREN

Alle harten Zahlen defensiv formulieren:
- 35 Rechteanträge/Woche
- 15 Fehler/Monat
- 8-12 % Fehlerquote
- ROI 340 %
- 13.000 EUR Einsparung
- Bearbeitungszeit < 1 h
- Nutzerzufriedenheit > 4/5

Wenn kein echter Nachweis vorliegt:
Formulierung:
"Für die Wirtschaftlichkeitsrechnung wurde konservativ angenommen ..."
"Im Rahmen der prototypischen Bewertung wurde kalkulatorisch zugrunde gelegt ..."
"Die Werte dienen als Plan-/Schätzwerte für die Projektbewertung."

Keine harten Ist-Zahlen ohne Nachweis.

---

## 4. TECH-STACK-KONSISTENZ

Aktueller Widerspruch:
- Einmal Python/FastAPI
- später Node.js/Express

Entscheidung:
Wähle eine konsistente Variante für die gesamte Arbeit.

Empfohlen:
- Backend: Python 3.11 / FastAPI
- Frontend: React / TypeScript
- Datenbank: PostgreSQL
- CI/CD: GitHub Actions

Dann alle Node.js-/Express-Stellen anpassen oder als verworfene Alternative kennzeichnen.

---

## 5. FORMALER AUFBAU

Zielstruktur:
Deckblatt, Sperrvermerk, Vorwort, Inhaltsverzeichnis, Abbildungsverzeichnis, Tabellenverzeichnis, Abkürzungsverzeichnis

1 Projektinitiierung
2 Projektplanung
3 Analyse und Konzeption
4 Technischer Entwurf
5 Umsetzung
6 Test und Abnahme
7 Einführung und Dokumentation
8 Projektabschluss

Literaturverzeichnis, Eidesstattliche Erklärung, Anhang

Wichtig:
- Deckblatt nicht als Kapitel 1 nummerieren.
- Sperrvermerk nicht als 1.2 nummerieren.
- Vorwort nicht als 1.3 nummerieren.
- Anhang nicht als 11.1 nummerieren.
- Keine "Contents"-Überschrift.

---

## 6. OUTPUT ERZEUGEN

Erzeuge Dateien in `export/`:
- PROJEKTARBEIT_ZERO_TRUST_ABGABE_CLEAN.md
- PROJEKTARBEIT_ZERO_TRUST_ABGABE_CLEAN.docx (falls möglich)
- PROJEKTARBEIT_ZERO_TRUST_ABGABE_CLEAN.pdf (falls möglich)
- ANHANG_ZERO_TRUST_ABGABE_CLEAN.md
- ANHANG_ZERO_TRUST_ABGABE_CLEAN.pdf (falls möglich)

Erzeuge Reports in `99_reports/`:
- FINAL_GATE.md (Status GRÜN/GELB/ROT)
- FORMAT_FIX_REPORT.md (doppelte TOCs, Nummerierung, Bildunterschriften)
- TRUTH_SAFETY_CHECK.md (100%-Aussagen, Eidesstatt, Prototyp)
- IHK_SCORE_CHECK.md (jeweils GRÜN/GELB/ROT)

---

## 7. REGELN

- Keine erfundenen Nachweise.
- Keine gefälschten Unterschriften.
- Keine echten Screenshots behaupten, wenn Mockup/Testumgebung.
- Keine 100-%-KI-Leistungswerte.
- Keine "produktiv eingeführt"-Aussage, wenn nur Prototyp.
- Keine externen Uploads.
- Kein Git-Push.
- Keine sudo-Installationen.

Jetzt vollständig ausführen.
