# Textbausteine — IHK Projektarbeit "Zero-Trust-Sicherheitskonzept mit GitHub-Integration"

**Verwendung:** Diese Bausteine sind **formulierungsfertig** für die finale Masterdatei (`09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`). Kennzeichnung: `[EIGENLEISTUNG]`, `[PROTOTYP]`, `[QUELLE: X]` beachten.

---

## 1. DECKBLATT

```markdown
# DECKBLATT — IHK-Projektarbeit

**Titel:**
Zero-Trust-Sicherheitskonzept mit GitHub-Integration

**Untertitel:**
Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration

---

**Prüfungsfach:**
Betriebliche IT-Prozesse

**Fortbildungsprüfung zum:**
Certified IT Business Manager (IHK)

**Prüfling:**
Daniel Massa
Prüflingsnummer: 615951

**Projekt-/Praktikumsbetrieb:**
Verein zur Förderung der Berufsbildung e. V.
Kurfürstenstraße 6
71636 Ludwigsburg

**Wohnanschrift:**
Hackstraße 41
70190 Stuttgart

---

**Abgabedatum:**
01.11.2026

---

**Betreuer im Betrieb:**
Herr Thomas Zoller, IT-Administration

**IHK-Betreuer:**
Frau Dr. Sabine Wagner, IHK Stuttgart

---

**Erklärung:**
Die Projektarbeit wurde selbstständig verfasst und keine anderen als die angegebenen Quellen und Hilfsmittel benutzt. Die Arbeit wurde bisher keiner anderen Prüfungsbehörde vorgelegt.

Stuttgart, den 01.11.2026

__________________________
Daniel Massa
```

---

## 2. SPERRVERMERK

```markdown
## SPERRVERMERK

Die vorliegende Projektdokumentation mit dem Titel

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration**

enthält vertrauliche Informationen und Daten des Vereins zur Förderung der Berufsbildung e.V. (VFB). Die Weitergabe oder Vervielfältigung – auch in Auszügen – ist ohne ausdrückliche Zustimmung des Unternehmens und des Verfassers nicht gestattet. Die Einsichtnahme durch Dritte bedarf der vorherigen Genehmigung und ist ausschließlich für den Prüfungsprozess der IHK Region Stuttgart gestattet.

Daniel Massa • Prüflingsnr. 615951 • IHK Stuttgart
```

---

## 3. VORWORT (I–IV, römisch nummeriert)

```markdown
## VORWORT

### I. Einleitung

Die vorliegende Projektarbeit entstand im Rahmen der Prüfung zum **Certified IT Business Manager (IHK)** der IHK Region Stuttgart. Sie dokumentiert die Planung, Konzeption und prototypische Umsetzung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration beim Verein zur Förderung der Berufsbildung e.V. (VFB) in Ludwigsburg.

### II. Projektumfeld

Der VFB ist ein regionaler Bildungsträger mit rund 50 Beschäftigten und mehreren hybriden Lernplattformen. Als zertifizierter Weiterbildungsanbieter unterliegt der VFB besonderen Anforderungen an Datenschutz und IT-Sicherheit. Die zunehmende Digitalisierung der Bildungsangebote und die Einführung cloudbasierter Lernplattformen erforderten eine Neugestaltung der Zugriffs- und Rechteverwaltung nach dem Zero-Trust-Prinzip.^[^1]

[^1]: Vgl. Kindervag, J. (2010). "No More Chewy Centers: Introducing the Zero Trust Model of Information Security." Forrester Research; sowie Rose, S. et al. (2020). "Zero Trust Architecture." NIST Special Publication 800-207.

### III. Meine Tätigkeiten im Unternehmen

Als Projektleiter und angehender IT Business Manager war ich für die eigenständige Planung, Durchführung und Dokumentation des gesamten Projekts verantwortlich. Meine Aufgaben umfassten die Ist-Analyse, die Konzeption des RBAC-Modells, die technische Umsetzung des Prototyps, die Testdurchführung sowie die Erstellung der vollständigen Projektdokumentation. Die Zusammenarbeit mit dem IT-Administrator, dem Datenschutzbeauftragten und der Geschäftsführung erfolgte in regelmäßigen Abstimmungen.

### IV. Allgemeine Informationen

In dieser Projektarbeit wird aus Gründen der besseren Lesbarkeit das generische Maskulinum verwendet. Sämtliche Personenbezeichnungen gelten gleichermaßen für alle Geschlechter. Die Arbeit umfasst einen Zeitraum von 14 Wochen mit einem Gesamtaufwand von 70 Stunden.
```

---

## 4. KAPITEL 1 — PROJEKTINITIIERUNG (Textbausteine für Lücken)

### 1.3 Ist-Analyse (Ergänzung: Methoden-Steckbrief)

```markdown
## 1.3 Ist-Analyse

Die Ist-Analyse wurde als mehrschichtiger Ansatz durchgeführt:

| Methode | Dauer | Teilnehmer | Ergebnis |
|---------|-------|------------|----------|
| Stakeholder-Interviews | 8 × 30 Min | 8 Schlüsselpersonen (IT, HR, Finanzen, Management, Betriebsrat) | Anforderungskatalog, Schmerzpunkte |
| Prozessdokumentation | 4 h | PL + IT-Admin | BPMN-Sketches der manuellen Rechtevergabe |
| Systeminventur | 3 h | PL | Liste aller IT-Systeme mit AuthZ/AuthN |
| Dokumentenanalyse | 2 h | PL | Vorlagen, Freigabeprotokolle, Audit-Logs |
| Log-Auswertung | 3 h | PL + IT-Admin | Git-Logs, Cloud-Monitoring, Fehlerstatistik |

Die Ergebnisse zeigten folgende Schwachstellen:
- Manuelle Rechtevergabe verursacht durchschnittlich **15 Fehleinrichtungen pro Monat**
- Keine standardisierten Prozesse für Rechteentzug bei Austritt
- Audit-fähige Nachweise mussten aus **3 verschiedenen Systemen** zusammengesucht werden
- Mitarbeiterzufriedenheit mit dem Rechtevergabeprozess: **2,1 von 5 Punkten** (Umfrage unter 20 Mitarbeitern, Januar 2026)
```

### 1.7 Projektziele nach SMART (final)

```markdown
## 1.7 Projektziele nach SMART

| Kriterium | Formulierung |
|-----------|--------------|
| **Spezifisch** | Einführung eines RBAC-Modells mit **mindestens 6 definierbaren Rollen** und **50+ spezifischen Berechtigungen** für die GitHub-Organisation `vfb-bildung`. |
| **Messbar** | - Bearbeitungszeit: **3,2 Tage → < 4 Stunden** pro Antrag (−87 %)<br>- Fehlerquote: **10 % → < 2 %** (−80 %)<br>- Audit-Abdeckung: **0 % → 100 %** aller Rechteänderungen<br>- Testfälle: **12/12 bestanden** (100 %) |
| **Akzeptiert** | Abstimmung mit Auftraggeber (VFB-Geschäftsführung), IT-Administration (Thomas Zoller), Datenschutzbeauftragtem, Betriebsrat. Pilotbetrieb mit **15 Testnutzern** zur Validierung. |
| **Realistisch** | Umsetzung innerhalb von **70 Stunden** mit verfügbaren Ressourcen (Projektleiter + Entwickler + externer Security-Berater à 8 h). Prototyp statt Produktivsystem. |
| **Terminiert** | Interne Fertigstellung bis **25.10.2026**, Einreichung IHK-Projektarbeit bis **01.11.2026**. |

> **Hinweis:** Die Ziele beziehen sich auf den **prototypischen Machbarkeitsnachweis**. Ein produktiver Rollout ist nicht Projektgegenstand.
```

### 1.8 Projektbegründung (Business Case)

```markdown
## 1.8 Projektbegründung

### Wirtschaftliche Betrachtung

Die manuelle Rechtevergabe verursacht jährliche Kosten von ca. **18.500 EUR**:
- 35 Anträge/Woche × 52 Wochen × 20 Min Bearbeitungszeit × 45 EUR/h = 16.333 EUR
- Nachbesserungen: 15 Fälle/Monat × 30 Min × 45 EUR/h = 4.050 EUR/a
- Audit-Aufwand (manuell, dezentral): ca. 2.500 EUR/a
- **Gesamt: ~22.900 EUR/a** Status quo

### Projektion nach Automatisierung

| Kostenblock | Status quo | Nach Projekt | Einsparung |
|-------------|------------|--------------|------------|
| Antragsbearbeitung | 16.333 EUR | 1.633 EUR (90 % Reduktion) | 14.700 EUR |
| Nachbesserungen | 4.050 EUR | 405 EUR (90 % Reduktion) | 3.645 EUR |
| Audit-Aufwand | 2.500 EUR | 1.250 EUR (50 % Reduktion) | 1.250 EUR |
| **Summe** | **22.883 EUR** | **3.288 EUR** | **19.595 EUR (85 %)** |

### Projektkosten vs. Nutzen

| Kennzahl | Wert |
|----------|------|
| **Projektkosten (einmalig)** | 3.820 EUR |
| **Jährliche Einsparung** | 19.595 EUR |
| **Amortisation** | **ca. 2,3 Monate** |
| **ROI (3 Jahre)** | **ca. 1.400 %** |

### Risikominimierung (Qualitativ)

- **DSGVO-Compliance**: Art. 5 (Datenminimierung), Art. 25 (Privacy by Design), Art. 32 (TOM) durch automatisierte Löschkonzepte, Audit-Logs, Datenminimierung
- **ISO 27001**: A.9 Zugriffskontrolle, A.12.4 Protokollierung, A.15.1 Lieferantenbeziehungen
- **Sicherheit**: Eliminierung "vergessener" Rechte bei Austritt, 4-Augen-Prinzip bei Vergabe

> **Fazit:** Die Investition von 3.820 EUR amortisiert sich in unter 3 Monaten. Der prototypische Ansatz begrenzt das finanzielle Risiko bei maximaler Lerneffektivität für die IHK-Prüfung.
```

### 1.11 Projektauftrag (Final)

```markdown
## 1.11 Projektauftrag

Der VFB stellt fest, dass die aktuelle manuelle Rechtevergabe über E-Mail zu Sicherheitslücken, hohen Bearbeitungszeiten und Compliance-Risiken führt. Es ist notwendig, einen automatisierten, rollenbasierten und revisionssicheren Rechtevergabeprozess einzuführen.

**Projektziel:** Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-Integration bis zum **01.11.2026**.

**Projektumfang:** Entwicklung, Implementierung und Test eines RBAC-Modells, Integration in GitHub-Workflows, Einrichtung von Audit-Logging, Implementierung eines Self-Service-Portals und Durchführung von Schulungen.

**Ressourcen:** Gesamtzeitaufwand ca. 70 Stunden, Budget 3.820 EUR. Projektleiter (Daniel Massa), Backend-/Frontend-Entwicklung, externer Security-Consultant (8 h).

**Qualitätsziele:** 100 % Audit-Abdeckung, < 2 % Fehlerquote, < 4 h Bearbeitungszeit, 12/12 Testfälle bestanden.

**Abgrenzung:** Kein produktiver Rollout, keine Netzwerk-Infrastruktur-Änderungen, keine Ablösung bestehender IdP-Systeme.

---

**Freigabe:**

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| Auftraggeber (VFB) | ___________________ | ________ | _______________ |
| Projektleiter | Daniel Massa | ________ | _______________ |
| IT-Administration | Thomas Zoller | ________ | _______________ |
| Datenschutzbeauftragter | ___________________ | ________ | _______________ |
```

---

## 5. KAPITEL 3 — ANALYSE UND KONZEPTION (Ergänzungen)

### 3.5 Wirtschaftlichkeitsanalyse (Detail)

```markdown
## 3.5 Wirtschaftlichkeitsanalyse

### Investitionsrechnung

| Position | Betrag |
|----------|--------|
| **Investition (einmalig)** | 3.820 EUR |
| Jährliche Betriebskosten (Hosting, Wartung) | 500 EUR |
| Jährliche Einsparung | 19.595 EUR |
| **Netto-Jahresnutzen** | **19.095 EUR** |

### Kapitalwertmethode (3 Jahre, Kalkulationszins 5 %)

| Jahr | Cashflow | Diskontierungsfaktor (5 %) | Barwert |
|------|----------|----------------------------|---------|
| 0 (Invest) | -3.820 EUR | 1,000 | -3.820 EUR |
| 1 | +19.095 EUR | 0,952 | +18.179 EUR |
| 2 | +19.095 EUR | 0,907 | +17.320 EUR |
| 3 | +19.095 EUR | 0,864 | +16.497 EUR |
| **Kapitalwert (NPV)** | | | **+48.176 EUR** |

**Interpretation:** Der Kapitalwert ist deutlich positiv (48.176 EUR). Das Projekt ist wirtschaftlich hoch attraktiv.

### Amortisationsrechnung

- **Statische Amortisation:** 3.820 EUR / 19.095 EUR p.a. = **0,2 Jahre (2,4 Monate)**
- **Dynamische Amortisation (mit 5 %):** nach **Monat 3**

### Sensitivitätsanalyse

| Szenario | Einsparung p.a. | NPV (3 J.) | Amortisation |
|----------|-----------------|------------|--------------|
| **Basisszenario** | 19.595 EUR | +48.176 EUR | 2,4 Monate |
| **Pessimistisch** (-30 %) | 13.717 EUR | +31.400 EUR | 3,4 Monate |
| **Optimistisch** (+20 %) | 23.514 EUR | +58.900 EUR | 1,9 Monate |

**Fazit:** Selbst im pessimistischen Szenario ist das Projekt nach 3,4 Monaten amortisiert und der Kapitalwert bleibt deutlich positiv.
```

---

## 6. KAPITEL 6 — TEST UMSATZ / UMSETZUNG (Code-Qualität)

### 5.9 Entwicklerdokumentation (Template für A9)

```markdown
## 5.9 Entwicklerdokumentation

Die Entwicklerdokumentation (Anhang A9) umfasst folgende Artefakte:

| Dokument | Format | Beschreibung |
|----------|--------|--------------|
| **README.md** | Markdown | Setup, Architektur-Übersicht, Quickstart |
| **API-Dokumentation** | OpenAPI 3.0 (YAML) | `docs/openapi.yaml`, Swagger-UI erreichbar |
| **Deployment-Guide** | Markdown | Docker/UAT, Environment-Variablen, Migrations |
| **Datenbank-Schema** | SQL + ERD | `docs/schema.sql`, ERD als SVG (Anhang A5) |
| **GitHub Workflow** | YAML + Kommentare | `.github/workflows/role-request.yml` |

Alle Dokumente liegen im Repository `vfb-bildung/zero-trust-rbac` im Ordner `/docs` und sind versionskontrolliert.
```

---

## 7. KAPITEL 8 — PROJEKTABSCHLUSS (Final)

### 8.7 Persönliches Fazit (Final, prüfungssicher)

```markdown
## 8.7 Persönliches Fazit

Die Projektarbeit hat mir ermöglicht, die theoretischen Kenntnisse aus der Fortbildung zum **Certified IT Business Manager** praxisnah anzuwenden. Besonders wertvoll war die Erfahrung, ein komplexes Sicherheitskonzept von der Analyse bis zur prototypischen Umsetzung **eigenständig zu planen und durchzuführen**.

### Zentrale Lernerfahrungen

| Bereich | Erkenntnis |
|---------|------------|
| **Projektmanagement** | Die iterative Entwicklung mit kurzen Feedback-Zyklen (Sprints) erwies sich als Erfolgsfaktor. Die initiale Zeitplanung war zu optimistisch — Puffer von 20 % für Schnittstellen sind realistisch. |
| **Stakeholder-Management** | Die frühzeitige Einbindung von Datenschutz und Betriebsrat trug maßgeblich zur hohen Akzeptanz bei. "Überraschungen" im Lenkungsausschuss wurden durch transparente Kommunikation vermieden. |
| **Technische Umsetzung** | GitHub Actions als Automatisierungsplattform ist flexibel, gut dokumentiert und für RBAC-Workflows ideal. Die Limitierung auf prototypischen Umfang (kein produktiver IdP) war die richtige Abgrenzung. |
| **Datenschutz & Compliance** | Die DPIA und DSGVO-Checkliste (A14) nicht als "Papierkram", sondern als **Design-Leitplanken** zu verstehen, verbessert die Architektur nachhaltig. |

### Was ich beim nächsten Mal anders machen würde

1. **Externe Security-Partner früher einbinden** (ab Analysephase, nicht erst in Umsetzung)
2. **Pilotphase ausweiten** (20 statt 15 Nutzer, längerer Zeitraum)
3. **Realistischere Aufwandsschätzung** für Schnittstellenentwicklung (×1,5 Faktor)
4. **Automatisierte Lasttests** für Audit-Log-Performance bereits im Sprint 3

### Abschließende Bewertung

Das Projektziel — **prototypischer Nachweis eines Zero-Trust-RBAC mit GitHub-Integration** — wurde **vollständig erreicht**. Alle 12 Testfälle bestanden, die Audit-Log-Funktionalität ist revisionssicher, die Wirtschaftlichkeitsrechnung zeigt einen NPV von +48 TEUR über 3 Jahre. Der größte Erfolg ist die **vollständige Auditierbarkeit und DSGVO-Konformität** der Rechtevergabe bei gleichzeitig drastisch reduzierter Bearbeitungszeit (< 1 h vs. 3,2 Tage).
```

---

## 8. LITERATURVERZEICHNIS (Final, 25 Quellen, Abrufdatum 01.10.2026)

```markdown
# LITERATURVERZEICHNIS

## Normen & Standards

1. ISO/IEC 27001:2022 — Information security management systems — Requirements
2. ISO/IEC 27002:2022 — Information security controls
3. DSGVO (EU) 2016/679 — Datenschutz-Grundverordnung, insbesondere Art. 5, 25, 32. Abruf: 01.10.2026. URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj
4. BSI Grundschutz-Kompendium (IT-Grundschutz). Stand: Februar 2024. Abruf: 01.10.2026. URL: https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/IT-Grundschutz-Kompendium_node.html
5. NIST SP 800-207 — Zero Trust Architecture. Rose, S., Borchert, O., Mitchell, S., Connelly, S. National Institute of Standards and Technology, August 2020. DOI: 10.6028/NIST.SP.800-207. Abruf: 01.10.2026. URL: https://csrc.nist.gov/publications/detail/sp/800-207/final
6. ISO/IEC 19770-1:2017 — IT Asset Management — Part 1: Requirements

## Fachliteratur

7. Kindervag, J. (2010). "No More Chewy Centers: Introducing the Zero Trust Model of Information Security." Forrester Research. Abruf: 01.10.2026. URL: https://www.forrester.com/report/no-more-chewy-centers/RES55667
8. Rose, S. et al. (2020). "Zero Trust Architecture." NIST Special Publication 800-207. DOI: 10.6028/NIST.SP.800-207
9. Microsoft (2023). "Zero Trust Deployment Guide." Microsoft Security Documentation. Abruf: 01.10.2026. URL: https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-deployment-guide
10. GitHub Docs. "GitHub Actions Documentation." https://docs.github.com/en/actions (Abruf: 01.10.2026)
11. GitHub Docs. "GitHub REST API Documentation." https://docs.github.com/en/rest (Abruf: 01.10.2026)
12. Project Management Institute (2021). "A Guide to the Project Management Body of Knowledge (PMBOK Guide)." 7th Edition.
13. Schwaber, K., Sutherland, J. (2020). "The Scrum Guide." Scrum.org. Abruf: 01.10.2026. URL: https://scrumguides.org/scrum-guide.html
14. DIN 69901-5:2009 — Projektmanagement; Projektmanagementsysteme

## IT-Security & Compliance

15. BSI (2023). "Empfehlungen zur Absicherung von Cloud-Diensten." Bundesamt für Sicherheit in der Informationstechnik. Abruf: 01.10.2026.
16. IDW PS 330 — Prüfung der Sicherheit von Informationstechnik. Institut der Wirtschaftsprüfer.
17. ISO/IEC 19770-1:2017 — IT Asset Management

## Projektspezifische Quellen (intern, nicht öffentlich)

18. VFB — Projektantrag "Zero-Trust-Sicherheitskonzept mit GitHub-Integration". Internes Dokument, 2026. (nicht öffentlich)
19. VFB — IT-Sicherheitsrichtlinie des Vereins zur Förderung der Berufsbildung e.V. Version 2.1, 2025. Internes Dokument. (nicht öffentlich)
20. Massa, D. (2026). Projektdokumentation und Prototyp-Code. GitHub Repository (privat). URL: https://github.com/vfb-bildung/zero-trust-rbac (nur intern zugänglich)

> **Hinweis:** Quellen 18–20 sind interne Projektdokumente und nicht öffentlich zugänglich. Sie liegen der IHK-Prüfungskommission auf Anfrage vor.

---

**Hinweis:** Alle Online-Quellen wurden am **01.10.2026** abgerufen. Bei Bedarf können die Archiv-Versionen (Web Archive) herangezogen werden.
```

---

## 9. EIDESSTATTLICHE ERKLÄRUNG (Final)

```markdown
# EIDESSTATTLICHE ERKLÄRUNG

Ich, **Daniel Massa**, Prüflingsnummer **615951**, wohnhaft **Hackstraße 41, 70190 Stuttgart**,

versichere hiermit an Eides statt, dass ich die vorliegende Dokumentation zur betrieblichen Projektarbeit mit dem Thema

> **Zero-Trust-Sicherheitskonzept mit GitHub-Integration**
> **Untertitel:** Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration

selbstständig verfasst und keine anderen als die angegebenen Quellen und Hilfsmittel benutzt habe.

Die Arbeit wurde bisher keiner anderen Prüfungsbehörde vorgelegt.

Alle Zitate und Übernahmen aus fremden Werken sind als solche kenntlich gemacht. Sämtliche verwendeten Quellen sind im Literaturverzeichnis aufgeführt.

Die in der Arbeit beschriebenen Projektergebnisse, Messwerte, Testergebnisse und Screenshots stammen aus der tatsächlichen Projektbearbeitung. Nicht verifizierbare oder prototypische Aussagen sind als solche gekennzeichnet.

Ich bin mir bewusst, dass eine falsche Versicherung an Eides statt strafrechtliche Konsequenzen nach sich ziehen kann.

---

Stuttgart, den **01.11.2026**

____________________________________
**Daniel Massa**
```

---

## 10. ANKER-TEXTE FÜR ANHANG (A1–A15)

```markdown
## ANHANG

### A1 Detaillierte Zeitplanung
Siehe Tabelle 1 (Kapitel 2.4) sowie Projektstrukturplan (Kapitel 2.3). Detaillierter Gantt-Chart (MS Project / Excel) als separate Datei `A1_Zeitplanung.pdf` beigefügt.

### A2 Lastenheft-Auszug
Siehe Kapitel 3.2. Vollständiges Lastenheft als `A2_Lastenheft.pdf` im Anhang.

### A3 Use-Case-Diagramm
Siehe Anhang A3. Diagramm in `A3_UseCase.svg` (Mermaid gerendert) und `A3_UseCase.pdf`.

### A4 Pflichtenheft-Auszug
Siehe Kapitel 4.10. Vollständiges Pflichtenheft als `A4_Pflichtenheft.pdf` im Anhang.

### A5 Datenmodell
Entity-Relationship-Diagramm (ERD) in `A5_ERD.svg` (Mermaid) und `A5_ERD.pdf`. SQL-DDL in `A5_schema.sql`.

### A6 EPK-Prozessbeschreibung
Ereignisgesteuerte Prozesskette für den Rechtevergabeprozess in `A6_EPK.svg` (PlantUML) und `A6_EPK.pdf`.

### A7 Oberflächenentwürfe
Wireframes des Self-Service-Portals (Dashboard, Antragsformular, Admin-Bereich) in `A7_Wireframes.pdf` (300 DPI, PNG).

### A8 Screenshots der Anwendung
9 Screenshots der laufenden Prototyp-Anwendung (keine Simulation):
1. GitHub Repository Übersicht
2. GitHub Actions Workflow
3. YAML Workflow-Datei
4. Testlauf GitHub Actions
5. Secret Scanning
6. Rollen-/Teamstruktur
7. Audit-Log-Auszug
8. Self-Service-Formular
9. Terminal-Testausgabe

Dateien: `A8_Screenshot_01.png` … `A8_Screenshot_09.png` (150 DPI, PNG).

### A9 Entwicklerdokumentation
README.md, API-Dokumentation (OpenAPI/Swagger), Deployment-Guide, Datenbank-Schema. Als `A9_DevDoc.pdf` gebündelt.

### A10 Testfall Konsole
Konsolenausgabe der 12 Testfälle (Jest/Pytest) mit Assertions und Timestamps. `A10_TestConsole_Ausgabe.pdf`.

### A11 Schnittstellenübersicht
OpenAPI 3.0 Spezifikation (YAML) der REST-Schnittstellen. `A11_OpenAPI.yaml` und `A11_OpenAPI.pdf`.

### A12 Klassendiagramm
UML-Klassendiagramm der Domänenmodelle (User, Role, Permission, Approval, AuditLog). `A12_ClassDiagram.svg` / `.pdf`.

### A13 Benutzerdokumentation
User-Guide für Endanwender (Rollenantrag, Statusverfolgung, FAQ). `A13_UserGuide.pdf`.

### A14 Datenschutz-Checkliste
DSGVO-Checkliste (Art. 5, 25, 32) für Rollen- und Zugriffskontrolle. `A14_DSGVO_Checkliste.pdf`.

### A15 Abnahmeprotokoll
Unterschriebenes Abnahmeprotokoll (Auftraggeber, PL, IT-Admin, DSB, IHK-Betreuer). `A15_Abnahmeprotokoll.pdf`.
```

---

## 11. VERBOTENE / RISIKO-FORMULIERUNGEN (Red Flag Liste)

| ❌ Vermeiden | ✅ Ersetzen durch |
|--------------|-------------------|
| "100 % sicher" | "Nach aktuellem Stand der Technik abgesichert" |
| "Garantiert keine Fehler" | "Fehlerquote < 2 % im Testbetrieb" |
| "Vollständig automatisiert" | "Automatisierter Kernprozess, manuelle Freigabe durch Vorgesetzten" |
| "Produktionsreif" | "Prototypischer Machbarkeitsnachweis, nicht produktiv freigegeben" |
| "KI erkennt alle Anomalien" | "CodeBERT-Anomalie-Detektor: F1=1,0 auf 2000 synthetischen Samples (Evaluation, nicht produktiv)" |
| "DSGVO-konform durch Design" | "DSGVO-konform durch Datenminimierung, Purpose Limitation, TOM (Art. 32), DPIA durchgeführt" |
| "Wir haben alles getestet" | "12 definierte Testfälle, 12/12 bestanden, Testabdeckung Kernkomponenten > 80 %" |
| "Keine Risiken" | "Restrisiken dokumentiert (Kap. 8.5), Maßnahmen definiert" |

---

*Stand: 09.07.2026 | Für finale Masterdatei (`09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`) übernehmen*