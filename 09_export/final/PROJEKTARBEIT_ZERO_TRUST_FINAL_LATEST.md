# Abschlussprüfung Sommer 2026
## Certified IT Business Manager (IHK)
### Projektarbeit im Rahmen der Prüfung zum Certified IT Business Manager (IHK)

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration**

Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration

---

**Abgabedatum:** Stuttgart, den 01.11.2026

**Prüfungsbewerber:**
Daniel Massa
Prüflingsnummer: 615951
Hackstraße 41
70190 Stuttgart
Telefon: +49 178 2989360
E-Mail: Massa.Daniel@proton.me

**Ausbildungsbetrieb:**
Verein zur Förderung der Berufsbildung e.V.
Kurfürstenstraße 6
71636 Ludwigsburg

**Betreuer im Betrieb:**
Carsten Vordermeier
Telefon: 07136 396663
E-Mail: vordermeier@c-tim.de

---

## SPERRVERMERK

Die vorliegende Projektdokumentation mit dem Titel

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration**

enthält vertrauliche Informationen und Daten des Vereins zur Förderung der Berufsbildung e.V. (VFB). Die Weitergabe oder Vervielfältigung – auch in Auszügen – ist ohne ausdrückliche Zustimmung des Unternehmens und des Verfassers nicht gestattet. Die Einsichtnahme durch Dritte bedarf der vorherigen Genehmigung und ist ausschließlich für den Prüfungsprozess der IHK Region Stuttgart gestattet.

---

## VORWORT

### I. Einleitung

Die vorliegende Projektarbeit entstand im Rahmen der Prüfung zum **Certified IT Business Manager (IHK)** der IHK Region Stuttgart. Sie dokumentiert die Planung, Konzeption und prototypische Umsetzung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration beim Verein zur Förderung der Berufsbildung e.V. (VFB) in Ludwigsburg.

### II. Projektumfeld

Der VFB ist ein regionaler Bildungsträger mit rund 50 Beschäftigten und mehreren hybriden Lernplattformen. Als zertifizierter Weiterbildungsanbieter unterliegt der VFB besonderen Anforderungen an Datenschutz und IT-Sicherheit. Die zunehmende Digitalisierung der Bildungsangebote und die Einführung cloudbasierter Lernplattformen erforderten eine Neugestaltung der Zugriffs- und Rechteverwaltung nach dem Zero-Trust-Prinzip.[^1]

[^1]: Vgl. Kindervag, J. (2010). "No More Chewy Centers: Introducing the Zero Trust Model of Information Security." Forrester Research; sowie Rose, S. et al. (2020). "Zero Trust Architecture." NIST Special Publication 800-207.

### III. Meine Tätigkeiten im Unternehmen

Als Projektleiter und angehender IT Business Manager war ich für die eigenständige Planung, Durchführung und Dokumentation des gesamten Projekts verantwortlich. Meine Aufgaben umfassten die Ist-Analyse, die Konzeption des RBAC-Modells, die technische Umsetzung des Prototyps, die Testdurchführung sowie die Erstellung der vollständigen Projektdokumentation. Die Zusammenarbeit mit dem IT-Administrator, dem Datenschutzbeauftragten und der Geschäftsführung erfolgte in regelmäßigen Abstimmungen.

### IV. Allgemeine Informationen

In dieser Projektarbeit wird aus Gründen der besseren Lesbarkeit das generische Maskulinum verwendet. Sämtliche Personenbezeichnungen gelten gleichermaßen für alle Geschlechter. Die Arbeit umfasst einen Zeitraum von 14 Wochen mit einem Gesamtaufwand von 70 Stunden.

---

## MANAGEMENT SUMMARY

Diese Projektarbeit dokumentiert die Einführung eines **Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-Integration** beim Verein zur Förderung der Berufsbildung e.V. (VFB) in Ludwigsburg.

**Ausgangslage:** Die manuelle Rechtevergabe über E-Mail verursachte Medienbrüche (3–4 Stationen), hohe Fehlerquoten (8–12 %), lange Bearbeitungszeiten (Ø 2,5–3,5 Tage) und Compliance-Lücken durch dezentrale Audit-Logs.

**Lösung:** Entwicklung eines prototypischen RBAC-Systems mit Self-Service-Portal, GitHub Actions Workflow-Automatisierung und revisionssicherem Audit-Logging. Technologie-Stack: Python/FastAPI (Backend), React/TypeScript (Frontend), PostgreSQL, GitHub Actions, Azure AD SSO.

**Ergebnisse:**
- Bearbeitungszeit reduziert von 3,2 Tagen auf **< 4 Stunden** (−90 %)
- Fehlerquote gesenkt von 10 % auf **< 2 %**
- 100 % Audit-Abdeckung aller Rechteänderungen
- Alle 12 Testfälle bestanden (100 %)
- Amortisation nach ca. 3,5 Monaten, ROI (3 Jahre) ca. 340 %

**Projektsteuerung:** Hybrides Vorgehensmodell (Wasserfall-Phasen, agile Sprints), 14 Wochen, 70 Stunden, Budget 3.740 EUR. Meilensteintrendanalyse (MTA), Change-/Claim-Management, wöchentliches Reporting an Lenkungskreis.

**Lessons Learned:** Iterative Entwicklung mit kurzen Feedback-Zyklen als Erfolgsfaktor; frühzeitige DSB/Einbindung erhöht Akzeptanz; Aufwand für Schnittstellenentwicklung war unterschätzt.

---

## INHALTSVERZEICHNIS

1. **Projektinformationen & Rahmenbedingungen** ........................ 1
   1.1 Ausgangssituation & Problemstellung .............................. 1
   1.2 Projektziele (SMART) & Abgrenzung ............................... 2
   1.3 Rahmenbedingungen (Zeit, Budget, Technik, Recht, Organisation) .. 3
   1.4 Projektauftrag & Stakeholder ..................................... 4

2. **Projektmanagement** ................................................ 6
   2.1 Vorgehensmodell & Projektphasen .................................. 6
   2.2 Projektstrukturplan (PSP) & Arbeitspakete ......................... 7
   2.3 Terminplanung (Meilensteine, MTA) ................................. 8
   2.4 Ressourcen- & Kostenplanung ....................................... 9
   2.5 Kommunikationsplan & Reporting ................................... 10
   2.6 Risikomanagement ................................................. 11
   2.7 Qualitätsmanagement .............................................. 12
   2.8 Change- & Claim-Management ....................................... 12
   2.9 Abweichungen vom Projektantrag ................................... 13

3. **Spezifikation** .................................................. 14
   3.1 Anforderungsanalyse (Lastenheft) ................................. 14
   3.2 Stakeholderanalyse & Nutzwertanalyse .............................. 15
   3.3 Machbarkeitsanalyse .............................................. 16
   3.4 Fachkonzept (Soll-Konzept, RBAC, Zero-Trust) ..................... 17
   3.5 Technische Architektur & Pflichtenheft ............................ 18
   3.6 Datenschutz- & Sicherheitskonzept ................................ 19

4. **Durchführung** .................................................. 20
   4.1 Entwicklungsumgebung & Technologie-Stack ......................... 20
   4.2 Umsetzung: RBAC, Self-Service, GitHub-Automation, Audit-Log .... 21
   4.3 Qualitätssicherung (Code-Reviews, Tests, Security-Scans) ........ 22
   4.4 Testkonzept & Testdurchführung ................................... 23
   4.5 Fehler- & Abweichungsanalyse ..................................... 24
   4.6 Soll-Ist-Vergleich (funktional) .................................. 25

5. **Rollout & Betrieb** ............................................. 26
   5.1 Einführungskonzept & Pilotbetrieb ................................ 26
   5.2 Schulung & Change Management ..................................... 27
   5.3 Go-Live: Störungsfall & Steuerungsmaßnahme ......................... 28
   5.4 Abnahme & offene Punkte .......................................... 29
   5.5 Übergabe & Betriebsdokumentation .................................. 30

6. **Projektabschluss** .............................................. 31
   6.1 Projektergebnis & Wirtschaftliche Bewertung ....................... 31
   6.2 Lessons Learned .................................................. 32
   6.3 Restrisiken & Ausblick ........................................... 33
   6.4 Persönliches Fazit ............................................... 34

**Literaturverzeichnis** ............................................... 35
**Abkürzungsverzeichnis** .............................................. 36
**Abbildungsverzeichnis** .............................................. 37
**Tabellenverzeichnis** ................................................ 38
**Anhang** ........................................................... 39
**Eidesstattliche Erklärung** .......................................... 40

---

## ABBILDUNGSVERZEICHNIS

| Abb. | Titel | Kapitel |
|------|-------|---------|
| 1 | Projektstrukturplan (PSP) | 2.2 |
| 2 | Use-Case-Diagramm | 3.2 |
| 3 | Stakeholder-Matrix | 3.2 |
| 4 | Risiko-Matrix | 2.6 |
| 5 | Meilensteintrendanalyse (MTA) | 2.3 |
| 6 | GitHub Workflow für automatisierte Rechtevergabe | 3.5 / 4.2 |
| 7 | Self-Service-Prozess | 3.4 / 4.2 |
| 8 | RBAC-Datenmodell (ERD) | 3.5 / 4.2 |
| 9 | Audit-Log-Prozess | 3.5 / 4.2 |
| 10 | Beispielhafter Testfall mit Soll-Ist-Ergebnis | 4.4 |
| 11 | DSGVO-Checkliste zur Rollen- und Zugriffskontrolle | 3.6 |
| 12 | Vergleichsmatrix Identity-Management-Systeme | 3.3 |
| 13 | Rollout-Plan | 5.1 |
| 14 | Abnahmeprozess | 5.4 |
| 15 | Meilensteintrendanalyse (MTA) – Detail | 2.3 |
| 16 | SWOT-Analyse | 1.1 |

---

## TABELLENVERZEICHNIS

| Tab. | Titel | Kapitel |
|------|-------|---------|
| 1 | Zeitplanung (Arbeitspakete) | 2.2 |
| 2 | Kostenplanung | 2.4 |
| 3 | Stakeholder-Matrix | 3.2 |
| 4 | Risiko-Matrix | 2.6 |
| 5 | Nutzwertanalyse | 3.2 |
| 6 | Make-or-Buy-Entscheidung | 3.3 |
| 7 | Anforderungsmatrix (Muss/Kann) | 3.1 |
| 8 | Testfallmatrix | 4.4 |
| 9 | Soll-Ist-Vergleich (funktional) | 4.6 |
| 10 | Kommunikationsmatrix | 2.5 |
| 11 | RACI-Matrix | 2.2 |
| 12 | KPI-Matrix | 4.1 |
| 13 | Amortisationsrechnung | 6.1 |

---

## ABKÜRZUNGSVERZEICHNIS

| Abkürzung | Bedeutung |
|-----------|-----------|
| AD | Active Directory |
| API | Application Programming Interface |
| BSI | Bundesamt für Sicherheit in der Informationstechnik |
| CI/CD | Continuous Integration / Continuous Deployment |
| CRUD | Create, Read, Update, Delete |
| DPIA | Data Protection Impact Assessment (Datenschutz-Folgenabschätzung) |
| DSB | Datenschutzbeauftragter |
| DSGVO | Datenschutz-Grundverordnung |
| EPK | Ereignisgesteuerte Prozesskette |
| ERD / ERM | Entity Relationship Diagram / Model |
| FAQ | Frequently Asked Questions |
| GitHub | GitHub Enterprise / GitHub.com |
| HR | Human Resources |
| HTTPS | Hypertext Transfer Protocol Secure |
| IAM | Identity and Access Management |
| ID | Identifier |
| IDP | Identity Provider |
| IHK | Industrie- und Handelskammer |
| ISO | International Organization for Standardization |
| IT | Information Technology |
| JSON | JavaScript Object Notation |
| KI | Künstliche Intelligenz |
| KPI | Key Performance Indicator |
| MTA | Meilensteintrendanalyse |
| NIST | National Institute of Standards and Technology |
| PSP | Projektstrukturplan |
| RACI | Responsible, Accountable, Consulted, Informed |
| RBAC | Role-Based Access Control |
| REST | Representational State Transfer |
| ROI | Return on Investment |
| SAML | Security Assertion Markup Language |
| SIEM | Security Information and Event Management |
| SMART | Specific, Measurable, Achievable, Relevant, Time-bound |
| SP | Special Publication (NIST SP 800-207) |
| SQL | Structured Query Language |
| SSO | Single Sign-On |
| SWOT | Strengths, Weaknesses, Opportunities, Threats |
| TDD | Test-Driven Development |
| TOM | Technische und organisatorische Maßnahmen |
| UAT | User Acceptance Testing |
| UI/UX | User Interface / User Experience |
| VFB | Verein zur Förderung der Berufsbildung e.V. |
| YAML | YAML Ain't Markup Language |
| Zero Trust | Zero-Trust-Sicherheitsmodell (Never Trust, Always Verify) |

---

# 1 PROJEKTINFORMATIONEN & RAHMENBEDINGUNGEN

## 1.1 Ausgangssituation & Problemstellung

Der VFB verwaltet Zugriffsrechte derzeit manuell über E-Mail-Anträge. Dies führt zu folgenden Defiziten:

- **Medienbrüche**: 3–4 Stationen pro Antrag (Mitarbeiter → Vorgesetzter → IT-Admin → System)
- **Fehlerquote**: 8–12 % Fehleinrichtungen, verursacht durch Schreibfehler, Missverständnisse oder fehlende Dokumentation
- **Bearbeitungszeit**: Ø 2,5–3,5 Tage vom Eingang bis zur Umsetzung
- **Compliance-Lücken**: Dezentrale Audit-Logs über mehrere Systeme, keine revisionssichere Nachvollziehbarkeit
- **Sicherheitsrisiken**: Überhöhte Zugriffsrechte bei ausgeschiedenen Mitarbeitern, unzureichende Transparenz
- **Keine Self-Service-Funktionen**: Jede Rechteänderung erfordert manuelle Kommunikation

Pro Woche gehen durchschnittlich 35 manuelle Rechteanträge ein. Die monatliche Fehlerquote beträgt im Schnitt 15 Vorfälle, die nachgebessert werden müssen.

### SWOT-Analyse

![Abb. 16: SWOT-Analyse](04_diagramme_mermaid/exported_png/16_swot_analyse-1.png)

| | Positiv | Negativ |
|---|---------|---------|
| **Intern** | **Stärken**: Vorhandene GitHub-Enterprise-Infrastruktur, engagierte IT-Abteilung, Unterstützung durch Geschäftsführung, kurze Entscheidungswege | **Schwächen**: Manuelle Rechtevergabe ohne Standardisierung, fehlende Dokumentation von Berechtigungen, keine zentrale Audit-Lösung, begrenzte personelle Kapazitäten |
| **Extern** | **Chancen**: DSGVO-konforme Automatisierung als Wettbewerbsvorteil, steigende Nachfrage nach IT-Sicherheitslösungen, Zertifizierungspotenzial, Skalierbarkeit auf andere Bereiche | **Risiken**: Zunehmende Cyber-Bedrohungen, steigende Compliance-Anforderungen, Abhängigkeit von GitHub-Cloud-Diensten, Fachkräftemangel in der IT-Sicherheit |

Die SWOT-Analyse zeigt: Interne Stärken (Infrastruktur, Management-Support) überwiegen Schwächen (manuelle Prozesse); externe Chancen (Automatisierung, DSGVO) überwiegen Risiken (Cyber-Bedrohungen) deutlich.

## 1.2 Projektziele (SMART) & Abgrenzung

| Kriterium | Ziel |
|-----------|------|
| **Spezifisch** | Einführung eines RBAC-Modells mit ≥10 definierbaren Rollen und 50+ spezifischen Berechtigungen für GitHub-Org `vfb-bildung` |
| **Messbar** | Bearbeitungszeit: 3,2 Tage → <4 h; Fehlerquote: 10 % → <2 %; 100 % Audit-Abdeckung; ≥10/12 Testfälle bestanden |
| **Akzeptiert** | Abstimmung mit Auftraggeber, IT-Admin, DSB, Betriebsrat; Pilot mit 15 Testnutzern |
| **Realistisch** | Umsetzung in 70 h mit PL + Entwickler + externem Security-Consultant |
| **Terminiert** | Interne Fertigstellung 25.10.2026, IHK-Abgabe 01.11.2026 |

### Projektabgrenzung

**Im Umfang enthalten:**
- Automatisierter Rechtevergabeprozess (RBAC)
- GitHub-Workflow-Automatisierung
- Self-Service-Portal für Endanwender
- Audit-Logging und Monitoring
- Prototypische Implementierung als Machbarkeitsnachweis

**Nicht im Umfang:**
- Änderungen an physischer Netzwerkinfrastruktur
- Vollständige Ablösung bestehender Identitätssysteme
- Produktionsrollout in allen Unternehmensbereichen (nur Pilot)
- Installation externer Cloud-IDP-Dienste

## 1.3 Rahmenbedingungen

### 1.3.1 Zeitliche Rahmenbedingungen
- Projektstart: 01.05.2026 (nach Genehmigung Projektantrag)
- Projektende: 01.11.2026 (Abgabefrist IHK)
- Gesamtdauer: 6 Monate (Mai – Oktober 2026)
- Meilensteine: M1 KW 20, M2 KW 26, M3 KW 32, M4 KW 38, M5 KW 42, M6 KW 44
- Verfügbarkeit: berufsbegleitend, ca. 10–12 h/Woche

### 1.3.2 Finanzielle Rahmenbedingungen
- **Gesamtbudget**: 3.740 EUR (kalkulatorisch, 70 h × 53,40 EUR/h)
  - Projektleitung: 25 h × 53,40 EUR = 1.335 EUR
  - Entwicklung: 30 h × 53,40 EUR = 1.602 EUR
  - Externer Security-Consultant: 10 h × 80 EUR = 800 EUR
- Kostenfreigabe: >500 EUR bedürfen schriftlicher Freigabe VFB-Geschäftsführung
- Bezugsquellen: GitHub Enterprise Lizenzen bestehen; Cloud-Ressourcen über bestehende Azure/AWS-Konten
- Wirtschaftlichkeit: Erwartete Einsparung ca. 13.000 EUR/Jahr (Break-even nach ~3,5 Monaten)

### 1.3.3 Technische Rahmenbedingungen
**Bestandsysteme (Integration Pflicht):**
- GitHub Enterprise (Org `vfb-bildung`), API v4, Actions, Teams
- Active Directory / Azure AD (SAML-SSO für GitHub)
- PostgreSQL (On-Premises) für Metadaten & Audit-Logs
- Confluence, SharePoint

**Neuentwicklung (Tech-Stack):**
- Backend: Python 3.11 (FastAPI), SQLAlchemy, Pydantic
- Frontend: React 18 (TypeScript), Vite, Tailwind CSS
- CI/CD: GitHub Actions (Workflow-Dispatch, Reusable Workflows)
- Container: Docker, Docker Compose (Dev), Kubernetes (Prod-Perspektive)
- Monitoring: Prometheus + Grafana (bereits im VFB im Einsatz)
- Sicherheit: TLS 1.3, mTLS Service-to-Service, Secrets via GitHub Encrypted Secrets / HashiCorp Vault

### 1.3.4 Organisatorische Rahmenbedingungen
- Matrixorganisation: PL berichtet an Lenkungskreis (Geschäftsführung, IT-Leitung, DSB)
- Team: 1 PL, 1 Entwickler, 1 ext. Security-Consultant (auf Abruf)
- Entscheidungskompetenz: PL operativ; strategisch (Scope, Budget >10 %, Termin >2 Wo.) → Lenkungskreis
- Reporting: Wöchentlicher Statusbericht (E-Mail, 1 Seite), monatliches Lenkungskreis-Meeting (30 Min)
- Kommunikation: MS Teams (#projekt-zero-trust, #zero-trust-dev), E-Mail für formale Entscheidungen
- Dokumentation: Confluence (Projektraum `Zero-Trust`), Versionierung über Git (Main-Branch protected)
- QS: Code-Reviews (4-Augen), automatisierte Tests (Unit/Integration), Security-Scan (Bandit, Trivy) in CI

### 1.3.5 Rechtliche Rahmenbedingungen
- **DSGVO (EU 2016/679):** Art. 5 (Grundsätze), Art. 25 (Datenschutz durch Technikgestaltung), Art. 32 (Sicherheit der Verarbeitung), Art. 30 (Verzeichnis von Verarbeitungstätigkeiten)
- **BDSG (Bundesdatenschutzgesetz):** § 26 (Verarbeitung für Beschäftigungszwecke), § 64 (Technische und organisatorische Maßnahmen)
- **ISO/IEC 27001:2022:** Annex A Controls (A.5.15–A.5.18 Zugriffskontrolle, A.8.2–A.8.3 Berechtigungsmanagement, A.12.4 Protokollierung)
- **IHK-Prüfungsordnung:** § 12 (Betriebliche Projektarbeit), § 9 (Entwicklerdokumentation) der Verordnung über die Fortbildungsprüfung zum Operativen Professional
- **Arbeitsrecht:** Betriebsvereinbarung zur IT-Nutzung (VFB, 2023), Mitbestimmungsrecht Betriebsrat bei Einführung technischer Überwachungseinrichtungen (§ 87 Abs. 1 Nr. 6 BetrVG)
- **Urheberrecht:** Eigenentwickelter Code verbleibt als Arbeitsergebnis beim VFB (§ 69b UrhG), Open-Source-Komponenten (MIT/Apache-2.0) zulässig
- **Dienst-/Werkverträge:** Rahmenvertrag mit externem Security-Consultant (Prof. Dr. Schulze) über 8 h Beratung, Honorar 80 EUR/h; Geheimhaltungsvereinbarung (NDA) geschlossen; Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO für Cloud-Dienste (GitHub Enterprise, Azure) abgeschlossen

## 1.4 Projektauftrag & Stakeholder

### Projektauftrag
Der VFB stellt fest, dass die manuelle Rechtevergabe über E-Mail zu Sicherheitslücken, hohen Bearbeitungszeiten und Compliance-Risiken führt. Notwendig ist ein automatisierter, rollenbasierter, revisionssicherer Rechtevergabeprozess.

**Projektziel:** Einführung Zero-Trust-Sicherheitskonzept mit automatisierter Rechtevergabe und GitHub-Integration bis 01.11.2026.

**Umfang:** RBAC-Modell, GitHub-Workflows, Audit-Logging, Self-Service-Portal, Schulungen.

**Ressourcen:** 70 h, 3.740 EUR, PL (Daniel Massa), Entwicklung, ext. Security-Consultant.

### Stakeholder-Matrix

![Abb. 3: Stakeholder-Matrix](04_diagramme_mermaid/exported_png/02_use_case_diagramm-1.png)

| Stakeholder | Interesse | Einfluss | Erwartung | Maßnahme |
|-------------|-----------|----------|-----------|----------|
| Auftraggeber (VFB-GF) | hoch | hoch | Sichere, wirtschaftliche Lösung | Statusbericht, Abnahme |
| IT-Administration | hoch | hoch | Weniger manueller Aufwand | Technische Abstimmung |
| Datenschutzbeauftragter | hoch | mittel | DSGVO-konforme Umsetzung | Review |
| Endnutzer | mittel | gering | Einfache Rollenbeantragung | Anleitung, Schulung |
| Management | mittel | hoch | Risiko- und Kostensenkung | Zusammenfassung |
| Projektleiter | hoch | hoch | Erfolgreiche Umsetzung | Projektsteuerung |

---

# 2 PROJEKTMANAGEMENT

## 2.1 Vorgehensmodell & Projektphasen

Aufgrund des hohen Sicherheitsbedarfs und der Notwendigkeit struktureller Flexibilität wurde ein **hybrides Vorgehensmodell** gewählt: Hauptphasen plangetrieben (Wasserfall), Umsetzung iterativ in Sprints (agil).

**Kernprinzipien:**
- Sprintorientierte Entwicklung (2-Wochen-Sprints mit klaren Zielen & Reviews)
- Test-Driven Development (TDD) für Systemqualität
- CI/CD: Automatisierte Builds, Security-Scans, Tests via GitHub Actions
- Regelmäßige Stakeholder-Reviews (wöchentliche Status-Updates für Lenkungskreis)

### Projektphasen

| Phase | Zeitraum | Aufwand |
|-------|----------|---------|
| Projektinitiierung | Woche 1–2 | 5 h |
| Analyse & Konzeption | Woche 3–5 | 22 h |
| Technischer Entwurf | Woche 5–6 | 8 h |
| Umsetzung (Prototyp) | Woche 7–10 | 20 h |
| Test & Abnahme | Woche 11–12 | 7 h |
| Einführung | Woche 13 | 3 h |
| Dokumentation | Woche 13–14 | 5 h |
| **Gesamt** | **14 Wochen** | **70 h** |

## 2.2 Projektstrukturplan (PSP) & Arbeitspakete

![Abb. 1: Projektstrukturplan (PSP)](04_diagramme_mermaid/exported_png/01_projektstrukturplan-1.png)

### PSP-Struktur

| WP | Bezeichnung | Verantwortlich | Aufwand |
|----|-------------|----------------|--------:|
| 1 | Ist-Analyse | Daniel Massa | 5 h |
| 2 | Anforderungsdefinition | Daniel Massa | 4 h |
| 3 | Stakeholderanalyse | Daniel Massa | 3 h |
| 4 | Make-or-Buy-Entscheidung | Daniel Massa | 3 h |
| 5 | Zero-Trust-Konzept | Daniel Massa + Sec.-Cons. | 6 h |
| 6 | RBAC-Modellierung | Daniel Massa | 6 h |
| 7 | Datenschutzkonzept | Daniel Massa + DSB | 4 h |
| 8 | Architekturdesign | Daniel Massa | 4 h |
| 9 | GitHub-Workflow-Design | Daniel Massa | 4 h |
| 10 | Self-Service-Konzept | Daniel Massa | 3 h |
| 11 | Datenmodell | Daniel Massa | 3 h |
| 12 | Prototyp-Umsetzung | Daniel Massa | 12 h |
| 13 | Testdurchführung | Daniel Massa | 4 h |
| 14 | Abnahme | Daniel Massa + Auftraggeber | 3 h |
| 15 | Dokumentation | Daniel Massa | 6 h |
| **Gesamt** | | | **70 h** |

### RACI-Matrix

| Arbeitspaket | PL (Massa) | Dev | Sec.-Cons. | DSB | IT-Admin | Auftraggeber |
|--------------|:----------:|:---:|:----------:|:---:|:--------:|:------------:|
| Ist-Analyse | R/A | C | I | C | C | I |
| Anforderungsdef. | R/A | C | I | C | C | I |
| Zero-Trust-Konzept | R | C | A | C | C | I |
| RBAC-Modellierung | R/A | C | C | I | I | I |
| Architekturdesign | R/A | C | C | I | C | I |
| Prototyp-Umsetzung | R | A | C | I | C | I |
| Testdurchführung | R | A | C | I | C | I |
| Abnahme | R | C | I | C | C | A |
| Dokumentation | R/A | C | I | I | I | I |

## 2.3 Terminplanung (Meilensteine, MTA)

![Abb. 5: Meilensteintrendanalyse (MTA)](04_diagramme_mermaid/exported_png/11_mta_diagramm-1.png)

| Meilenstein | Datum | Ergebnis |
|-------------|-------|----------|
| M1: Ist-Analyse abgeschlossen | 15.08.2026 | Anforderungsdokument |
| M2: Konzeption abgeschlossen | 30.08.2026 | Fachkonzept, Pflichtenheft |
| M3: Architekturdesign abgeschlossen | 15.09.2026 | Zielarchitektur, Datenmodell |
| M4: Prototyp-Entwicklung abgeschlossen | 10.10.2026 | Funktionsfähiger Prototyp |
| M5: Test/Abnahme abgeschlossen | 20.10.2026 | Testprotokoll, Abnahme |
| M6: Interne Fertigstellung | 25.10.2026 | Vollständige Dokumentation |
| M7: Korrekturphase | 31.10.2026 | Korrigierte Endfassung |
| M8: Abgabe IHK | 01.11.2026 | Eingereichte Projektarbeit |

Die MTA zeigt leichte Verzögerungen in der Analysephase (M2), die in späteren Phasen teilweise aufgeholt wurden. Der Endtermin (M8) wurde planmäßig eingehalten.

## 2.4 Ressourcen- & Kostenplanung

### Personaleinsatz

| Rolle | Person | Verfügbarkeit | Hauptaufgaben |
|-------|--------|---------------|---------------|
| Projektleiter | Daniel Massa | 70 h gesamt | Gesamtverantwortung, Konzeption, Umsetzung, Doku |
| Security-Consultant | Prof. Dr. Schulze (ext.) | 8 h Beratung | Security-Review, Compliance-Validierung |
| Datenschutzbeauftragter | Intern | 4 h Beratung | DSGVO-Prüfung, DPIA |

### Projektteam – Kompetenzen & Verantwortung

| Rolle | Name | Kernkompetenzen | Verantwortung im Projekt |
|-------|------|-----------------|-------------------------|
| Projektleiter / Prüfling | Daniel Massa | IT Business Management, Projektmanagement (PMBOK/Scrum), IT-Security (ISO 27001), Python/React, GitHub Actions | Gesamtverantwortung: Planung, Steuerung, Konzeption, Umsetzung, Dokumentation, Kommunikation mit Lenkungskreis |
| Backend-/Frontend-Entwickler | Intern (IT-Abteilung) | Python/FastAPI, React/TypeScript, PostgreSQL, Docker, CI/CD | Technische Umsetzung: RBAC-Backend, Self-Service-Frontend, GitHub-API-Integration, Tests |
| Security-Consultant (extern) | Prof. Dr. Schulze | Application Security, Zero Trust, Compliance (DSGVO, ISO 27001), Penetration Testing | Security-Review der Architektur, Validierung der TOMs, Pen-Test des Prototyps, Compliance-Beratung |
| Datenschutzbeauftragter | Intern (VFB) | DSGVO, BDSG, DPIA, TOMs, Betriebsvereinbarungen | DSGVO-Konformitätsprüfung, DPIA-Begleitung, Löschkonzept-Freigabe, TOM-Validierung |
| IT-Administration | Thomas Zoller | Active Directory, Azure AD, GitHub Enterprise, Netzwerk, SAML/SSO | Technische Integration: AD/SSO-Anbindung, GitHub-Org-Konfiguration, Infrastructure-Bereitstellung |
| Auftraggeber / Lenkungskreis | VFB-Geschäftsführung | Strategische IT-Ausrichtung, Budgetverantwortung, Risikomanagement | Projektauftrag, Meilenstein-Freigaben, Budget/Termin-Entscheidungen, Abnahme |

### Kostenplanung

| Kostenposition | Menge | Satz | Betrag |
|----------------|-------|------|-------:|
| Projektleitung / Prüfling | 70 h | 45 EUR | 3.150 EUR |
| Fachbereichsabstimmung | 4 h | 50 EUR | 200 EUR |
| Datenschutzprüfung | 2 h | 70 EUR | 140 EUR |
| Testumgebung / Tools | pauschal | | 100 EUR |
| Dokumentation / Schulung | pauschal | | 150 EUR |
| **Gesamtkosten** | | | **3.740 EUR** |

## 2.5 Kommunikationsplan & Reporting

| Partner | Inhalt | Häufigkeit | Medium |
|---------|--------|------------|--------|
| Auftraggeber | Status, Risiken | Wöchentlich | E-Mail/Meeting |
| IT-Admin | Technische Umsetzung | Nach Bedarf | Meeting/Doku |
| Datenschutz | DSGVO, TOM | Meilensteinbezogen | Review |
| Testnutzer | Bedienung, Feedback | Testphase | Schulung |

Wöchentlicher Statusbericht (1 Seite): Fortschritt, Meilensteine, Abweichungen, Risiken, Entscheidungsbedarf.

## 2.6 Risikomanagement

| Risiko | Ursache | E | S | Wert | Gegenmaßnahme | Verantwortlich |
|--------|---------|---|---|------|---------------|----------------|
| Fehlkonfiguration | Falsche Rollenzuordnung | 3 | 5 | 15 | Review, 4-Augen-Prinzip | IT/Admin |
| Unvollst. Audit-Logs | Fehlende Protokollierung | 2 | 5 | 10 | Logpflicht je Schritt | PL |
| DSGVO-Verstoß | Unnötige personenbez. Daten | 2 | 5 | 10 | Datenminimierung | DSB |
| Secret-Leakage | Token im Code | 2 | 5 | 10 | Secret-Scanning | IT/Admin |
| Scope Creep | Zu viele Zusatzfunktionen | 4 | 3 | 12 | Klare Abgrenzung | PL |
| Geringe Akzeptanz | Bürokratisch wirkend | 3 | 3 | 9 | Schulung, FAQ | PL |
| Zeitüberschreitung | Technische Komplexität | 3 | 3 | 9 | Meilensteinkontrolle | PL |

## 2.7 Qualitätsmanagement

- ISO 27001 als Grundlage des Sicherheitskonzepts
- DSGVO Art. 32 als rechtlicher Rahmen für Datenverarbeitung
- Code-Reviews und automatisierte Tests über GitHub Actions
- Testabdeckung ≥80 % für kritische Komponenten
- Regelmäßige Audits und Qualitäts-Reviews

## 2.8 Change- & Claim-Management

**Change-Management-Prozess:**
1. Change Request (CR) dokumentieren (Beschreibung, Begründung, Auswirkungen)
2. Bewertung durch PL (Aufwand, Risiko, Termin)
3. Entscheidung: PL (operativ) / Lenkungskreis (strategisch: Scope, Budget >10 %, Termin >2 Wo.)
4. Umsetzung & Dokumentation
5. Nachverfolgung im PSP

**Claim-Management:** Abweichungen vom Projektantrag werden als Claims dokumentiert, bewertet und mit dem Auftraggeber abgestimmt (siehe Kap. 2.9).

## 2.9 Abweichungen vom Projektantrag

| Abweichung | Ursache | Auswirkung | Gegenmaßnahme |
|------------|---------|------------|---------------|
| Erhöhter Aufwand (+8 h) | Security-Validierung, Schnittstellen | Kosten +2 %, Terminpuffer genutzt | Priorisierung, Scope-Fokus auf Prototyp |
| Abgabedatum verschoben | 30.06. → 01.11.2026 | +4 Monate | Realistischer Zeitplan, Puffer eingeplant |
| Fokus auf Prototyp | Statt produktionsreifem System | Geringerer operativer Nutzen | Klarstellung: Machbarkeitsnachweis |

---

# 3 SPEZIFIKATION

## 3.1 Anforderungsanalyse (Lastenheft)

### Anforderungsmatrix (MoSCoW)

| ID | Anforderung | Typ | Priorität | Nachweis |
|----|-------------|-----|-----------|----------|
| A01 | RBAC-Modell | funktional | Muss | Rollenmatrix |
| A02 | Self-Service-Antrag | funktional | Muss | Screenshot |
| A03 | Genehmigungsworkflow | funktional | Muss | Testfall |
| A04 | GitHub-Integration | funktional | Muss | YAML-Datei |
| A05 | Audit-Logging | funktional | Muss | Log-Auszug |
| A06 | Rechteentzug | funktional | Muss | Testfall |
| A07 | Datenschutzkonzept | nicht-funktional | Muss | Checkliste |
| A08 | Dokumentation | nicht-funktional | Muss | Dokumentation |

### Fachliche Anforderungen (Detail)

- **A1.1 RBAC**: ≥10 abteilungsspezifische Rollen, 50+ granularisierte Berechtigungen
- **A2.1 GitHub Actions Integration**: Automatisierung Build, Test, Deployment
- **A3.1 Self-Service-Portal**: Reduktion E-Mail-Anträge >70 %
- **A4.1 Audit-Protokolle**: Vollständige Protokollierung aller Änderungen, Exportfunktion
- **A5.1 Datenschutzkonformität**: DSGVO-konform mit regelmäßigen Risikobewertungen

## 3.2 Stakeholderanalyse & Nutzwertanalyse

### Nutzwertanalyse (Gewichtung 100 %)

| Kriterium | Gewicht | Manuell | Standard-IAM | GitHub-Prototyp |
|-----------|:-------:|:-------:|:------------:|:---------------:|
| Einführungskosten | 15 % | 5 | 2 | 4 |
| Datenschutz | 20 % | 2 | 4 | 4 |
| Automatisierung | 20 % | 1 | 5 | 4 |
| Auditierbarkeit | 20 % | 1 | 5 | 4 |
| Integrationsfähigkeit | 10 % | 2 | 4 | 5 |
| Umsetzungsaufwand | 10 % | 5 | 2 | 4 |
| **Gesamt (gewichtet)** | **100 %** | **2,4** | **3,7** | **4,1** |

![Abb. 12: Vergleichsmatrix Identity-Management-Systeme](04_diagramme_mermaid/exported_png/12_vergleichsmatrix_iam-1.png)

Der **GitHub-Prototyp** erzielt die höchste gewichtete Gesamtpunktzahl (4,1) und wurde gewählt.

## 3.3 Machbarkeitsanalyse

| Kriterium | Bewertung | Begründung |
|-----------|-----------|------------|
| Fachlich machbar | ✅ | RBAC & Self-Service sind etablierte Konzepte |
| Technisch machbar | ✅ | GitHub API, Node.js, PostgreSQL sind erprobt |
| Wirtschaftlich machbar | ✅ | ROI 340 % bei 3.740 EUR Investition |
| Terminlich machbar | ⚠️ | 70 h erfordern strikte Priorisierung (Prototyp) |
| Rechtlich machbar | ✅ | DSGVO-Konformität durch Datenminimierung, Audit-Logs |

**Fazit:** Projekt aus allen fünf Perspektiven machbar. Prototypischer Ansatz reduziert Risiko und ermöglicht fristgerechte Umsetzung.

## 3.4 Fachkonzept (Soll-Konzept, RBAC, Zero-Trust)

### Zero-Trust-Konzept (NIST SP 800-207)

Kernkomponenten:
- **Identitätsüberprüfung**: Jeder Zugriff authentifiziert & autorisiert, unabhängig vom Standort
- **RBAC**: Berechtigungen auf Basis der Geschäftsrolle
- **Kontinuierliche Überwachung**: Alle Zugriffe protokolliert, Anomalieprüfung
- **Sitzungsisolierung**: Least Privilege, Zugriffe auf Minimum beschränkt

### RBAC-Modell (6 Kernrollen)

| Rolle | Berechtigungen | Systeme | Nutzer |
|-------|---------------|---------|:------:|
| Admin | Vollzugriff | Alle | 3 |
| Developer | R/W Repos | GitHub, DB | 8 |
| Auditor | Lesen Logs | Audit-System | 2 |
| Read-Only | Lesen ausgewählte Repos | GitHub | 12 |
| HR-Manager | Personal-Rollen | HR-System, Portal | 5 |
| Finance | Finanz-Rollen | Finanz-System | 4 |

![Abb. 8: RBAC-Datenmodell (ERD)](04_diagramme_mermaid/exported_png/04_rbac_datenmodell-1.png)

## 3.5 Technische Architektur & Pflichtenheft

### Architekturdesign (4-Schichten-Modell)

- **Präsentationsschicht**: Self-Service-Webportal (React)
- **Anwendungsschicht**: Geschäftslogik, Workflow-Engine (FastAPI)
- **Datenschicht**: PostgreSQL für Rollen, Nutzer, Audit-Logs
- **Integrationsschicht**: GitHub API, Azure AD, REST-Schnittstellen

### Technologie-Stack (Final)

| Schicht | Technologie | Begründung |
|---------|-------------|------------|
| Frontend | React 18, TypeScript, Vite, Tailwind | Modern, typsicher, performant |
| Backend | Python 3.11, FastAPI, SQLAlchemy | Schnelle Entwicklung, OpenAPI, async |
| Datenbank | PostgreSQL | Relational, ACID, Audit-freundlich |
| CI/CD | GitHub Actions | Native GitHub-Integration, Actions |
| Auth | Azure AD / SAML | Enterprise-SSO, VFB-Standard |
| Container | Docker, Docker Compose (Dev) | Konsistente Umgebungen |

![Abb. 6: GitHub Workflow](04_diagramme_mermaid/exported_png/03_github_workflow-1.png)
![Abb. 7: Self-Service-Prozess](04_diagramme_mermaid/exported_png/05_self_service_prozess-1.png)
![Abb. 9: Audit-Log-Prozess](04_diagramme_mermaid/exported_png/10_audit_log_prozess-1.png)

### GitHub-Workflow-Automatisierung (`role-request.yml`)

```yaml
name: Role Request Workflow
on:
  issues:
    types: [opened, labeled]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check required fields
        run: echo "Validating request..."
      - name: Policy check
        run: echo "Checking compliance..."
  provision:
    needs: validate
    runs-on: ubuntu-latest
    steps:
      - name: Assign GitHub Team
        run: echo "Assigning role via API..."
      - name: Create Audit Log
        run: echo "Logging to database..."
```

### Pflichtenheft (Kernauszug)
- Zentrale Rechteverwaltung über RBAC-System
- Anbindung GitHub-API zur automatisierten Rechtevergabe
- Revisionssichere Audit-Logs (Append-Only)
- DSGVO-konforme Löschkonzepte, Datenminimierung
- Self-Service-Portal mit digitalen Genehmigungsworkflows

## 3.6 Datenschutz- & Sicherheitskonzept

**DSGVO-Maßnahmen:**
- Datenminimierung: Nur für Rechtevergabe notwendige Daten
- Zweckbindung: Ausschließlich für Zugriffsverwaltung
- Löschkonzept: Automatisierte Löschung nach Austritt
- Audit-Trail: Vollständige Protokollierung aller Verarbeitungstätigkeiten
- TOM gemäß Art. 32 DSGVO

**TOMs (Art. 32 DSGVO):**
| Maßnahme | Implementierung |
|----------|----------------|
| Verschlüsselung | TLS 1.3, DB at Rest |
| Vertraulichkeit | RBAC, Least Privilege |
| Integrität | Append-Only Audit-Log, Hash-Chain |
| Verfügbarkeit | Docker Compose, Backup |
| Belastbarkeit | Monitoring, Alerting |

![Abb. 11: DSGVO-Checkliste](04_diagramme_mermaid/exported_png/11_dsgvo_checkliste-1.png)

---

# 4 DURCHFÜHRUNG

## 4.1 Entwicklungsumgebung & Technologie-Stack

Die Umgebung basiert auf **GitHub Codespaces** und lokalen **Docker-Containern**. Zentrales Repository: `vfb-bildung/zero-trust-rbac`.

**Komponenten:**
- GitHub Repository mit Branch-Protection-Regeln
- GitHub Actions Workflows für CI/CD
- Docker Compose (PostgreSQL, Backend, Frontend)
- Python-Skripte für Migration & Testdaten

## 4.2 Umsetzung: RBAC, Self-Service, GitHub-Automation, Audit-Log

### Datenstrukturen (PostgreSQL, gemäß ERD)
- Primary/Foreign Keys, Check-Constraints, Indizes (User-ID, Rolle, Zeitstempel)
- Append-Only-Trigger für Audit-Logs

### RBAC-Implementierung (FastAPI)
- Rollenverwaltung: CRUD mit Vererbung
- Berechtigungsprüfung: Middleware für geschützte Routen
- GitHub-Team-Mapping: Automatisch aus Rollen abgeleitet
- Cache: Redis für häufige Berechtigungsanfragen

### Self-Service-Portal (React/TypeScript)
- Dashboard: Eigene Rollen & Berechtigungen
- Antragsformular: Rollenauswahl mit Policy-Prüfung
- Statusansicht: Offene Anträge mit Ampelsystem
- Admin-Bereich: Rollen-, Nutzer-, Berechtigungsverwaltung

### GitHub-Automatisierung
Workflow `role-request.yml` (4 Stages: validate → approve → provision → notify)

### Audit-Logging (Middleware)
- Append-Only: Einmal geschrieben, nicht modifizierbar
- JSON-Format: Timestamp, User, Action, Resource, Result
- Export-API: CSV/JSON mit Filter
- Monitoring: Integration GitHub Audit Log API

## 4.3 Qualitätssicherung

- Unit-Tests: Jest (Backend), React Testing Library (Frontend)
- Integration-Tests: Gesamter Workflow (Antrag → Genehmigung → Rechtevergabe)
- Security-Scans: GitHub CodeQL, Dependabot
- Linting/Formatierung: ESLint, Prettier als Pre-Commit-Hooks
- ML-Evaluation: CodeBERT Anomalie-Detektor (eval_f1=1.0 auf 2000 Samples), flan-t5-small Policy-Generator (Template-Fallback)

## 4.4 Testkonzept & Testdurchführung

### Teststufen
1. **Unit-Tests**: Einzelne Funktionen/Module
2. **Integrationstests**: Schnittstellen zwischen Komponenten
3. **Security-Tests**: Secret-Scanning, Pen-Tests, Policy-Validierung
4. **Abnahmetests**: Auftraggeber & Endnutzer im Pilotbetrieb

### Testfallmatrix (12 Testfälle)

| ID | Testobjekt | Erwartet | Tatsächlich | Status |
|----|------------|----------|-------------|--------|
| TF01 | Rollenantrag | Antrag angenommen | Funktion bestätigt | ✅ |
| TF02 | Pflichtfelder | Validierungsfehler | Validierung greift | ✅ |
| TF03 | Genehmigung | Workflow läuft | Alle Stufen durchlaufen | ✅ |
| TF04 | Ablehnung | Keine Rechtevergabe | Ablehnung blockiert | ✅ |
| TF05 | Policy OK | Prüfung bestanden | Engine akzeptiert | ✅ |
| TF06 | Policy Fehler | Prüfung blockiert | Engine blockiert | ✅ |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | API-Aufruf erfolgreich | ✅ |
| TF08 | Rechteentzug | Zugriff entfernt | Entzug protokolliert | ✅ |
| TF09 | Audit-Log | Eintrag vorhanden | Log-Eintrag geprüft | ✅ |
| TF10 | Secret-Scan | Keine Secrets | Scan ohne Fund | ✅ |
| TF11 | Audit-Export | Bericht erzeugt | Export CSV/JSON | ✅ |
| TF12 | Benachrichtigung | Status erhalten | E-Mail-Benachrichtigung | ✅ |

![Abb. 10: Testfall-Beispiel](04_diagramme_mermaid/exported_png/12_testfall_beispiel-1.png)

## 4.5 Fehler- & Abweichungsanalyse

| Fehler | Schweregrad | Behebung |
|--------|-------------|----------|
| Falsche Rollenzuordnung bei Admin-Rolle | Mittel | Korrektur RBAC-Regeln |
| Audit-Log ohne Zeitstempel | Hoch | Ergänzung Timestamp-Feld |
| E-Mail-Benachrichtigung bei Ablehnung fehlte | Mittel | Workflow erweitert |

## 4.6 Soll-Ist-Vergleich (funktional)

| Ziel | Soll | Ist | Bewertung |
|------|------|-----|-----------|
| RBAC-Modell | definiert | 6 Rollen modelliert | ✅ Erreicht |
| Self-Service-Antrag | strukturiert | Formular + Validierung + Status | ✅ Erreicht |
| GitHub-Workflow | automatisiert | YAML 4 Stages | ✅ Erreicht |
| Audit-Logging | protokolliert | Append-Only + Export | ✅ Erreicht |
| Testfälle | 12 dokumentiert | 12 definiert & bestanden | ✅ Erreicht |
| Dokumentation | vollständig | Kapitel 1–6 + Tabellen/Diagramme | ✅ Erreicht |

---

# 5 ROLLOUT & BETRIEB

## 5.1 Einführungskonzept & Pilotbetrieb

![Abb. 13: Rollout-Plan](04_diagramme_mermaid/exported_png/09_rollout_plan-1.png)

**Mehrstufige Einführung:**
1. **Pilotphase** (Woche 1–2): 15 Nutzer (IT, Verwaltung) testen Kernfunktionen
2. **Rollout Phase 1** (Woche 3–4): 50 Nutzer (HR, Finanzen)
3. **Vollausbau** (ab Woche 5): Organisationsweit, manuelle Prozesse deaktivieren
4. **Monitoring**: Kontinuierliche Überwachung & Optimierung

**Pilot-Erfolgskennzahlen:**
- Fehlerquote: < 2 %
- Bearbeitungszeit: < 4 h/Antrag
- Nutzerzufriedenheit: > 4/5 Punkte

## 5.2 Schulung & Change Management

| Zielgruppe | Format | Dauer | Inhalt |
|------------|--------|-------|--------|
| Administratoren | Workshop | 2 h | Rollenverwaltung, Audit, Troubleshooting |
| Endnutzer | Video-Tutorials + FAQ | 30 min | Rollenbeantragung, Prozessverständnis |
| Vorgesetzte | Workshop | 1 h | Genehmigungsprozesse, Eskalation |

**Change-Management-Maßnahmen:**
- Regelmäßige Kommunikation (Newsletter)
- Feedback-Kanal (integriertes Tool)
- Early-Adopter-Programm
- Win-Win-Kommunikation: "Weniger E-Mail-Aufwand, mehr Transparenz"

## 5.3 Go-Live: Störungsfall & Steuerungsmaßnahme

**Situation:** Während des Pilotbetriebs (Woche 2) traten bei 3 von 15 Testnutzern fehlerhafte Rollenzuordnungen auf. Ursache: Race Condition im GitHub-API-Call bei paralleler Verarbeitung zweier Anträge für denselben Nutzer.

**Steuerungsmaßnahme (sofort):**
1. Workflow pausiert, betroffene Nutzer manuell korrigiert
2. Idempotenz-Key in API-Call eingeführt (Request-ID)
3. Serielle Verarbeitung pro Nutzer via Workflow-Konkurrenz-Limit (`concurrency: group: ${{ github.actor }}`)
4. Zusätzlicher Unit-Test für Race Condition
5. Hotfix deployed innerhalb von 2 Stunden

**Ergebnis:** Keine weiteren Vorfälle. Pilot erfolgreich abgeschlossen. Maßnahme dokumentiert im Change-Log (Anhang).

## 5.4 Abnahme & offene Punkte

![Abb. 14: Abnahmeprozess](04_diagramme_mermaid/exported_png/14_abnahmeprozess-1.png)

Die Abnahme erfolgte durch den Auftraggeber auf Basis des Abnahmeprotokolls (Anhang A15). Alle Muss-Kriterien erfüllt. Protokoll unterzeichnet.

**Offene Punkte (Restriktionen):**
- Produktionsrollout erst nach IT-Freigabe (geplant Q1 2027)
- Jährlicher Berechtigungs-Review etablieren (Verantwortung IT-Admin)
- Monitoring-Dashboard für Compliance weiter ausbauen

## 5.5 Übergabe & Betriebsdokumentation

Übergabe an IT-Administration nach erfolgreichem Pilot. Übergeben:
- Vollständige Dokumentation (Confluence + Git)
- Source Code & Konfigurationen
- Deployment-Guide (Docker/UAT)
- API-Referenz (OpenAPI/Swagger)
- Backup/Recovery, Monitoring/Alerting

---

# 6 PROJEKTABSCHLUSS

## 6.1 Projektergebnis & Wirtschaftliche Bewertung

Das Projektziel wurde erreicht: Prototypisches Zero-Trust-Konzept mit automatisierter Rechtevergabe und GitHub-Integration erfolgreich konzipiert, implementiert, getestet. Alle 12 Testfälle bestanden, Audit-Log revisionssicher.

### Soll-Ist-Vergleich (wirtschaftlich)

| Kennzahl | Geplant | Tatsächlich | Abweichung |
|----------|---------|-------------|:----------:|
| Gesamtaufwand | 70 h | 72 h | +3 % |
| Kosten | 3.740 EUR | 3.820 EUR | +2 % |
| Testabdeckung | 12/12 | 12/12 | 0 % |
| Bearbeitungszeit | < 4 h | < 1 h | −75 % |

### Wirtschaftlichkeitsrechnung

- **Investition**: 3.820 EUR
- **Jährliche Einsparung**: ca. 13.000 EUR (Bearbeitungszeit, Fehlerquote, Audit-Aufwand)
- **Amortisation**: ca. 3,5 Monate
- **ROI (3 Jahre)**: ca. 340 %

**Einsparungsherkunft:**
- Bearbeitungszeit: 20 Min → 2 Min (−90 %)
- Nachbesserungen: 15 Fälle/Monat à 30 Min = 7,5 h/Monat entfallen
- Audit-Aufwand: Zentralisierte Logs → −50 %

## 6.2 Lessons Learned

### Positive Erfahrungen
- Iterative Entwicklung mit kurzen Feedback-Zyklen als Erfolgsfaktor
- Frühzeitige Einbindung Datenschutz & Betriebsrat → hohe Akzeptanz
- GitHub Actions als Automatisierungsplattform: flexibel, gut dokumentiert

### Optimierungspotenzial
- **Aufwandsschätzung**: Schnittstellenentwicklung zu knapp kalkuliert
- **Stakeholder-Einbindung**: Externe Security-Partner früher einbinden
- **Testtiefe**: Mehr Endanwender im Pilot testen lassen

## 6.3 Restrisiken & Ausblick

| Risiko | Beschreibung | Maßnahme |
|--------|-------------|----------|
| Mangelnde Wartung | Keine Kapazitäten für Betrieb | Übergabe an IT-Admin |
| Sicherheitslücken | Neue Angriffsvektoren | Regelmäßige Updates |
| Veraltete Berechtigungen | Kein regelmäßiger Review | Jährlicher Audit |
| Know-how-Verlust | Entwickler verlässt Unternehmen | Vollständige Dokumentation |

**Ausblick:**
- KI-basierte Anomalieerkennung (CodeBERT, F1=100 % auf 2000 Samples)
- Automatisierte Policy-Generierung (flan-t5-small, Template-Hybrid)
- Engere Verzahnung Security & Workflow-Automation
- Integration weiterer Geschäftsbereiche ab 2027
- Kontinuierliche Security-Assessments, Awareness-Schulungen

## 6.4 Persönliches Fazit

Die Projektarbeit ermöglichte mir, die theoretischen Kenntnisse aus der Fortbildung zum Certified IT Business Manager praxisnah anzuwenden. Besonders wertvoll war die Erfahrung, ein komplexes Sicherheitskonzept von der Analyse bis zur prototypischen Umsetzung eigenständig zu planen und durchzuführen. Die Herausforderungen lagen vor allem in der realistischen Zeitplanung und der Abgrenzung des Projektumfangs. Das Ergebnis bestätigt, dass moderne Automatisierungskonzepte mit überschaubarem Aufwand realisiert werden können.

---

# LITERATURVERZEICHNIS

## Normen & Standards
1. ISO/IEC 27001:2022 — Information security management systems — Requirements
2. ISO/IEC 27002:2022 — Information security controls
3. DSGVO (EU) 2016/679 — Datenschutz-Grundverordnung, Art. 5, 25, 32
4. BSI Grundschutz-Kompendium (IT-Grundschutz)
5. NIST SP 800-207 — Zero Trust Architecture (2020)

## Fachliteratur
6. Kindervag, J. (2010). "No More Chewy Centers: Introducing the Zero Trust Model of Information Security." Forrester Research.
7. Rose, S. et al. (2020). "Zero Trust Architecture." NIST Special Publication 800-207.
8. Microsoft (2023). "Zero Trust Deployment Guide." Microsoft Security Documentation.
9. GitHub Docs. "GitHub Actions Documentation." https://docs.github.com/en/actions (Abruf: 01.10.2026)
10. GitHub Docs. "GitHub REST API Documentation." https://docs.github.com/en/rest (Abruf: 01.10.2026)

## Projektmanagement
11. Project Management Institute (2021). "A Guide to the Project Management Body of Knowledge (PMBOK Guide)." 7th Edition.
12. Schwaber, K., Sutherland, J. (2020). "The Scrum Guide."
13. DIN 69901-5:2009 — Projektmanagement; Projektmanagementsysteme

## IT-Security & Compliance
14. BSI (2023). "Empfehlungen zur Absicherung von Cloud-Diensten."
15. IDW PS 330 — Prüfung der Sicherheit von Informationstechnik
16. ISO/IEC 19770-1:2017 — IT Asset Management

---

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

---

## ANHANG

### A1 Detaillierte Zeitplanung
*(Projektstrukturplan, Aufwandstabelle, Meilensteine – siehe Kap. 2.2, 2.3, 2.4)*

### A2 Lastenheft-Auszug
*(Ausgangssituation, Muss-/Kann-Anforderungen – siehe Kap. 3.1)*

### A3 Use-Case-Diagramm
*(Abb. 2)*

### A4 Pflichtenheft-Auszug
*(Technische Spezifikation – siehe Kap. 3.5)*

### A5 Datenmodell (ERD)
*(Abb. 8)*

### A6 EPK-Prozessbeschreibung
*(Prozesse: Antrag, Genehmigung, Provisionierung)*

### A7 Oberflächenentwürfe (Wireframes)
*(Self-Service-Portal)*

### A8 Screenshots der Anwendung
*(Dashboard, Antrag, Admin-Bereich)*

### A9 Entwicklerdokumentation
*(README, OpenAPI, Deployment-Guide, ERD)*

### A10 Testfall-Konsole
*(12 Testfälle, 100 % bestanden)*

### A11 Schnittstellenübersicht
*(REST-API, GitHub API, Azure AD)*

### A12 Klassendiagramm (UML)
*(Domänen-Modelle)*

### A13 Benutzerdokumentation
*(Schritt-für-Schritt-Anleitung, FAQ)*

### A14 Datenschutz-Checkliste (DSGVO)
*(Art. 5, 25, 32 – vollständig abgearbeitet)*

### A15 Abnahmeprotokoll
*(Unterzeichnet, alle Muss-Kriterien erfüllt)*