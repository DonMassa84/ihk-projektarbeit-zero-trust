# Finalisierungs-Plan — Letzte 4 Wochen vor IHK-Abgabe (01.11.2026)

**Status Stand 09.07.2026:** 🟡 GELB — Inhalte top, Formales & Anhang unvollständig  
**Ziel:** 🟢 GRÜN — "Prüfungsnah finalisierbar" bis Mitte August, Puffer bis November

---

## WOCHENPLAN (Critical Path)

### 🔴 WOCHE 1: KW 28 (07.–11.07.2026) — **Screenshots & Anhang-Inhalte**
**Fokus:** "Echte Beweise" erzeugen — alles andere wartet darauf

| Tag | Aufgabe | Dauer | Output | Done? |
|-----|---------|-------|--------|-------|
| Mo | **Prototyp starten & stabilisieren** (Docker Compose, Testdaten seed-en) | 2 h | `docker-compose up -d` läuft, 15 Testnutzer angelegt | ☐ |
| Mo | **9 echte Screenshots** erstellen (Flameshot/GNOME) | 2 h | `10_screenshots/01_github_repo_uebersicht.png` … `09_terminal_testausgabe.png` (150 DPI, PNG) | ☐ |
| Di | **A2 Lastenheft** aus Kap. 3.2 → PDF | 1 h | `A2_Lastenheft.pdf` | ☐ |
| Di | **A3 Use-Case** Mermaid → SVG → PDF | 30 min | `A3_UseCase.svg`, `A3_UseCase.pdf` | ☐ |
| Mi | **A4 Pflichtenheft** aus Kap. 4.10 → PDF | 1 h | `A4_Pflichtenheft.pdf` | ☐ |
| Mi | **A5 ERD** Mermaid → SVG → PDF + SQL-DDL | 1 h | `A5_ERD.svg`, `A5_ERD.pdf`, `A5_schema.sql` | ☐ |
| Do | **A6 EPK** PlantUML → SVG → PDF | 1 h | `A6_EPK.svg`, `A6_EPK.pdf` | ☐ |
| Do | **A7 Wireframes** (Figma/Balsamiq/Handskizze gescannt) → PDF | 1 h | `A7_Wireframes.pdf` (300 DPI) | ☐ |
| Fr | **A9 DevDoc** README + OpenAPI + Deploy-Guide → PDF | 1 h | `A9_DevDoc.pdf` | ☐ |
| Fr | **A10 Test-Konsole** Jest/Pytest Output → PDF | 30 min | `A10_TestConsole.pdf` | ☐ |
| Sa | **A11 OpenAPI** Spec → PDF/HTML | 30 min | `A11_OpenAPI.pdf` | ☐ |
| Sa | **A12 Klassendiagramm** PlantUML → SVG → PDF | 30 min | `A12_ClassDiagram.svg/pdf` | ☐ |
| So | **A13 User-Guide** Markdown → PDF | 1 h | `A13_UserGuide.pdf` | ☐ |
| So | **A14 DSGVO-Checkliste** → PDF (bereits in 02_anhang/14) | 15 min | `A14_DSGVO_Checkliste.pdf` | ☐ |
| So | **A15 Abnahmeprotokoll** → PDF + **Unterschriften organisieren** | 2 h | `A15_Abnahmeprotokoll.pdf` (unterschrieben: AG, PL, IT-Admin, DSB, IHK-Betreuerin) | ☐ |

**Wochen-Ziel:** Alle 15 Anhänge als **PDF/Dateien** im Ordner `export/ANHANG/` — bereit zum Einbinden.

---

### 🟠 WOCHE 2: KW 29 (14.–18.07.2026) — **Export-Pipeline & PDF-Qualität**
**Fokus:** Masterdatei finalisieren, seitenrichtigen PDF-Export, formale Korrektheit

| Tag | Aufgabe | Dauer | Output | Done? |
|-----|---------|-------|--------|-------|
| Mo | **Master-MD final prüfen**: `grep -n "TODO_\|Simulation\|Platzhalter"` → 0 Treffer | 1 h | Saubere `09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md` | ☐ |
| Mo | **Verzeichnisse aktualisieren**: Seitenzahlen in Inhalts-, Abbildungs-, Tabellenverzeichnis (manuell im MD oder via Pandoc-Lua-Filter) | 1 h | Korrekte Seitenzahlen | ☐ |
| Di | **LaTeX/Typst installieren**: `sudo apt install texlive-xetex texlive-lang-german` | 15 min | Build-Umgebung ready | ☐ |
| Di | **Pandoc Export testen**: `bash 09_export/build_scripts/export_docx_pdf.sh` | 30 min | `PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.pdf` | ☐ |
| Mi | **PDF prüfen**: `pdfinfo`, `pdftotext` → Seitenzahlen, Verzeichnisse, Lesezeichen, Metadaten, < 50 MB | 1 h | Validiertes PDF | ☐ |
| Mi | **PDF/A-1b validieren**: `veraPDF PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.pdf` | 30 min | GRÜN (keine Fehler) | ☐ |
| Do | **Diagramme als SVG einbinden**: Alle 16 Mermaid/PlantUML → SVG → in Master referenzieren | 1 h | Vektorgrafiken im PDF | ☐ |
| Do | **Anhang-Dateien einbinden**: `pdfunite` oder Ghostscript — Master + 15 Anhänge → **ein PDF** | 30 min | `PROJEKTARBEIT_ZERO_TRUST_KOMPLETT.pdf` | ☐ |
| Fr | **Formale Checkliste** (siehe unten) Punkt für Punkt abarbeiten | 2 h | Checkliste 100 % | ☐ |
| Fr | **Eidesstattliche Erklärung** unterschreiben (Datum 01.11.2026), scannen, in PDF einbinden | 15 min | Unterschriebene Erklärung | ☐ |
| Sa | **Dateigröße prüfen** (< 50 MB), notfalls Bilder komprimieren (`pngquant`, `jpegoptim`) | 30 min | Finale Datei | ☐ |
| So | **Backup**: Git commit + Tag `v1.0-submission-ready` + USB-Stick + Cloud | 15 min | Versioniert & gesichert | ☐ |

**Wochen-Ziel:** **Ein einziges, formale perfektes PDF** (Master + Anhang, ~75 Seiten, < 50 MB, PDF/A-1b).

---

### 🟡 WOCHE 3: KW 30 (21.–25.07.2026) — **Präsentation & Prüferfragen**
**Fokus:** Mündliche Prüfung vorbereiten (20 Min Vortrag + 20 Min Fachgespräch)

| Tag | Aufgabe | Dauer | Output | Done? |
|-----|---------|-------|--------|-------|
| Mo | **15-Min-Präsentation** Folien erstellen (PowerPoint/LibreOffice/Markdown→Reveal.js) | 3 h | `Praesentation_15min.pdf` | ☐ |
| Di | **Sprechtext** für jede Folie schreiben (Notizen-Sektion) | 2 h | `Sprechtext.md` | ☐ |
| Mi | **Prüferfragen-Katalog** (53 Fragen) **mündlich durchsprechen** — Timer: 20 Min Fachgespräch simulieren | 2 h | Sichere Antworten | ☐ |
| Do | **Eigenleistung-Schärfung**: "Was habe ICH gemacht?" — 3-Satz-Elevator-Pitch + 5 Detailbeispiele | 1 h | Sichere Formulierungen | ☐ |
| Fr | **Generalprobe**: Vortrag + Fachgespräch mit Sparring-Partner (Kollege/Betreuer) | 2 h | Feedback, Zeitmessung | ☐ |
| Sa | **Korrekturlesen** final (LanguageTool, DeepL Write, 4-Augen) | 2 h | Rechtschreibfehler 0 | ☐ |
| So | **Ruhe / Puffer** | – | Erholung | ☐ |

**Wochen-Ziel:** Vortrag sitzt (15:00 ± 0:30), alle 53 Fragen flüssig beantwortbar, Eigenleistung glaubwürdig darstellbar.

---

### 🟢 WOCHE 4: KW 31 (28.07.–01.08.2026) — **Puffer & Finale Abgabevorbereitung**
**Fokus:** Letzte Korrekturen, physische Exemplare, Abgabe-Logistik

| Tag | Aufgabe | Dauer | Output | Done? |
|-----|---------|-------|--------|-------|
| Mo | **Letztes PDF-Review** (gesamt, Seite für Seite) | 1 h | Keine Überraschungen | ☐ |
| Di | **3 Exemplare drucken & binden** (Druckerei/Unibind/Spulenbindung, Deckblatt Karton) | 2 h | 3 gebundene Exemplare | ☐ |
| Mi | **1 PDF/A auf USB-Stick** (IHK-Portal/Post) + 1 Backup-Stick | 15 min | Abgabefertig | ☐ |
| Do | **Abgabe-Logistik**: Post/Einschreiben an IHK Stuttgart (Adresse lt. Bescheid), Tracking-Nummer notieren | 1 h | Einlieferungsbeleg | ☐ |
| Fr | **Dokumentation der Abgabe**: Foto der Sendung, Tracking, Empfangsbestätigung IHK abwarten | 30 min | Nachweis | ☐ |
| Sa/So | **FREI** — Projektarbeit ABGEGEBEN! 🎉 | – | – | ☐ |

---

## 📋 FORMALE CHECKLISTE (Punkt für Punkt vor PDF-Final)

| # | Kriterium | Prüfung | OK? |
|---|-----------|---------|-----|
| 1 | **Deckblatt**: Titel, Untertitel, Prüfungsfach, Prüfling (Name, Nr., Adresse), Betrieb, Betreuer, IHK, Datum, Erklärung, Unterschriftszeile | Sichtprüfung | ☐ |
| 2 | **Sperrvermerk**: VFB, IHK Stuttgart, Vertraulichkeit, Prüfungszweck | Sichtprüfung | ☐ |
| 3 | **Inhaltsverzeichnis**: 3 Ebenen, seitenrichtig, Punktrührer | `pdftotext` prüfen | ☐ |
| 4 | **Abbildungsverzeichnis**: 16 Einträge, Nr., Titel, Seite | `pdftotext` prüfen | ☐ |
| 5 | **Tabellenverzeichnis**: 13 Einträge, Nr., Titel, Seite | `pdftotext` prüfen | ☐ |
| 6 | **Abkürzungsverzeichnis**: 43 Einträge, alphabetisch | Sichtprüfung | ☐ |
| 7 | **Literaturverzeichnis**: 25 Quellen, numerisch [1]–[25], DOI/URL + Abrufdatum 01.10.2026 | Konsistenzprüfung | ☐ |
| 8 | **Eidesstattliche Erklärung**: Text exakt, **Unterschrift + Datum 01.11.2026**, **nicht nummeriert**, am Ende | Original unterschrieben | ☐ |
| 9 | **Seitenzahlung**: römisch (I–X) für Vorwort/Verzeichnisse, arabisch (1–Ende) ab Kap. 1 | `pdfinfo` | ☐ |
| 10 | **Keine TODO/Simulation/Platzhalter** im finalen Text | `grep -i "TODO_\|Simulation\|Platzhalter"` | ☐ |
| 11 | **Alle 16 Abbildungen** als SVG/PNG eingebunden, beschriftet ("Abb. X: Titel"), Quelle angegeben | PDF-Check | ☐ |
| 12 | **Alle 13 Tabellen** im Text referenziert ("vgl. Tab. 5"), beschriftet ("Tab. X: Titel"), Quelle | PDF-Check | ☐ |
| 13 | **Alle 15 Anhänge** (A1–A15) als PDF/SVG eingebunden/referenziert | Ordner `export/ANHANG/` | ☐ |
| 14 | **Echte Screenshots** (9 Stück, keine HTML-Simulation) | `10_screenshots/*.png` | ☐ |
| 15 | **Abnahmeprotokoll (A15)** unterschrieben (AG, PL, IT-Admin, DSB, IHK-Betreuerin) | Scan im Anhang | ☐ |
| 16 | **Dateigröße** < 50 MB | `ls -lh` | ☐ |
| 16 | **PDF/A-1b** validiert (`veraPDF` = GRÜN) | `veraPDF` | ☐ |
| 17 | **3 Exemplare** gebunden + **1 USB-Stick** (PDF/A) | Physisch | ☐ |
| 18 | **Abgabe fristgerecht** bis 01.11.2026 (Poststempel / IHK-Portal) | Einlieferungsbeleg | ☐ |

---

## 🚨 RISIKO-PUFFER (Was schiefgehen kann & Plan B)

| Risiko | Wahrscheinlichkeit | Plan B |
|--------|-------------------|-------------------|
| **Prototyp stürzt ab / Screenshots unmöglich** | Mittel | **Plan B:** Docker-Image fixieren (`docker commit`), auf zweitem Rechner testen, notfalls alte Screenshots als "Simulationsplatzhalter" **deutlich kennzeichnen** + Erklärung im Text |
| **LaTeX-Export bricht** (fehlende Fonts, UTF-8) | Mittel | **Plan B:** `weasyprint` (HTML→PDF) als Fallback, manuelle Nachbearbeitung in LibreOffice → PDF/A |
| **Betreuer nicht verfügbar für A15-Unterschrift** | Niedrig | **Plan B:** Stellvertreter benennen, Termin **jetzt** fixieren (Kalenderblocker) |
| **Dateigröße > 50 MB** | Niedrig | **Plan B:** `pngquant --quality=70-85`, `jpegoptim --max=85`, Diagramme als SVG (nicht PNG) |
| **IHK-Portal down / Post verzögert** | Sehr niedrig | **Plan B:** Beides parallel (Post Einschreiben + Portal), Tracking behalten |

---

## 📅 MEILENSTEINE (Fixpunkte im Kalender)

| Datum | Meilenstein | Art |
|-------|-------------|-----|
| **11.07.2026** | Alle Screenshots + Anhang-PDFs fertig | **Hart** |
| **18.07.2026** | Finales PDF (Master + Anhang) PDF/A-1b validiert | **Hart** |
| **25.07.2026** | Präsentation + Prüferfragen sitzen | **Hart** |
| **01.08.2026** | 3 Exemplare gedruckt, gebunden, USB-Stick ready | **Hart** |
| **01.11.2026** | **ABGABE IHK STUTTGART** | **Absolut** |

---

## ⏱️ ZEITBUDGET (Realistisch)

| Aktivität | Stunden |
|-----------|---------|
| Screenshots + Anhang-Inhalte (Woche 1) | 18 h |
| Export-Pipeline + PDF-Qualität (Woche 2) | 10 h |
| Präsentation + Prüferfragen (Woche 3) | 12 h |
| Puffer, Druck, Logistik (Woche 4) | 6 h |
| **Gesamt** | **46 h** (≈ 11,5 h/Woche) |

**Verfügbarkeit:** 10–15 h/Woche neben Beruf → **machbar**.

---

## 🎯 DEFINITION OF DONE (Abgabe)

> **Die Projektarbeit ist "abgabereif", wenn:**
> - [ ] Ein PDF (`PROJEKTARBEIT_ZERO_TRUST_KOMPLETT.pdf`) existiert, das **Master + alle 15 Anhänge** enthält
> - [ ] PDF/A-1b validiert (`veraPDF` = 0 Errors)
> - [ ] Alle 18 Checklisten-Punkte ✅
> - [ ] 3 Exemplare gedruckt & gebunden
> - [ ] 1 USB-Stick mit PDF/A
> - [ ] Abnahmeprotokoll (A15) **unterschrieben** von allen 5 Parteien
> - [ ] Eidesstattliche Erklärung **unterschrieben & datiert 01.11.2026**
> - [ ] Post-Einschreiben an IHK Stuttgart aufgegeben (Tracking) **ODER** Portal-Upload bestätigt
> - [ ] Einlieferungsbeleg archiviert (Papier + Foto)

---

## 🔥 NÄCHSTER KONKRETER SCHRITT (HEUTE)

```bash
# 1. Prototyp starten
cd ~/openclaw-workspace/ihk_zero_trust_projektarbeit_final/12_prototype_zero_trust
docker-compose up -d

# 2. Screenshots machen (9 Stück) → 10_screenshots/
# 3. Anhang A2–A15 als PDF erzeugen → export/ANHANG/
# 4. Master-MD bereinigen (TODO-Scan)
grep -rn "TODO_\|Simulation\|Platzhalter" 09_export/final/
```

---

*Stand: 09.07.2026 | Nächster Review: 11.07.2026 (Ende Woche 1)*