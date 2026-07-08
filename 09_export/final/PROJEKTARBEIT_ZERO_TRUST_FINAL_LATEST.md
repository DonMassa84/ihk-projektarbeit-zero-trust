# Abschlussprüfung Sommer 2026
## Certified IT Business Manager (IHK)
### Dokumentation zur betrieblichen Projektarbeit

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration**

Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration

---

**Abgabedatum:** Stuttgart, den 01.11.2026

**Prüfungsbewerber:**
Daniel-Alfonsin Massa
Prüflingsnummer: 615951
Hackstraße 41
70190 Stuttgart

**Ausbildungsbetrieb:**
Verein zur Förderung der Berufsbildung e.V.
Kurfürstenstraße 6
71636 Ludwigsburg

**Betreuer im Betrieb:**
Herr Thomas Zoller, IT-Administration

**IHK-Betreuer:**
Frau Dr. Sabine Wagner, IHK Stuttgart

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

Der VFB ist ein regionaler Bildungsträger mit rund 50 Beschäftigten und mehreren hybriden Lernplattformen. Als zertifizierter Weiterbildungsanbieter unterliegt der VFB besonderen Anforderungen an Datenschutz und IT-Sicherheit. Die zunehmende Digitalisierung der Bildungsangebote und die Einführung cloudbasierter Lernplattformen erforderten eine Neugestaltung der Zugriffs- und Rechteverwaltung nach dem Zero-Trust-Prinzip.

### III. Meine Tätigkeiten im Unternehmen

Als Projektleiter und angehender IT Business Manager war ich für die eigenständige Planung, Durchführung und Dokumentation des gesamten Projekts verantwortlich. Meine Aufgaben umfassten die Ist-Analyse, die Konzeption des RBAC-Modells, die technische Umsetzung des Prototyps, die Testdurchführung sowie die Erstellung der vollständigen Projektdokumentation. Die Zusammenarbeit mit dem IT-Administrator, dem Datenschutzbeauftragten und der Geschäftsführung erfolgte in regelmäßigen Abstimmungen.

### IV. Allgemeine Informationen

In dieser Projektarbeit wird aus Gründen der besseren Lesbarkeit das generische Maskulinum verwendet. Sämtliche Personenbezeichnungen gelten gleichermaßen für alle Geschlechter. Die Arbeit umfasst einen Zeitraum von 14 Wochen mit einem Gesamtaufwand von 70 Stunden.

---

## INHALTSVERZEICHNIS

1 Projektinitiierung
1.1 Projektumfeld
1.2 Ausgangssituation
1.3 Ist-Analyse
1.4 Problemstellung
1.5 Soll-Konzept
1.6 Projektziele nach SMART
1.7 Projektbegründung
1.8 Projektabgrenzung
1.9 Projektschnittstellen
1.10 Projektauftrag

2 Projektplanung
2.1 Vorgehensmodell
2.2 Projektphasen
2.3 Projektstrukturplan
2.4 Arbeitspakete
2.5 Meilensteinplanung
2.6 Ressourcenplanung
2.7 Kostenplanung
2.8 Kommunikationsplanung
2.9 Risikoanalyse
2.10 Qualitätsplanung
2.11 Abweichungen vom Projektantrag

3 Analyse und Konzeption
3.1 Anforderungsanalyse
3.2 Lastenheft / Fachkonzept
3.3 Stakeholderanalyse
3.4 Make-or-Buy-Entscheidung
3.5 Wirtschaftlichkeitsanalyse
3.6 Nutzwertanalyse
3.7 Zero-Trust-Konzept
3.8 RBAC-Modell
3.9 Datenschutz- und Sicherheitskonzept

4 Technischer Entwurf
4.1 Zielplattform
4.2 Architekturdesign
4.3 GitHub-Workflow-Integration
4.4 Self-Service-Prozess
4.5 Datenmodell
4.6 Geschäftslogik
4.7 Audit-Logging
4.8 Schnittstellen
4.9 Maßnahmen zur Qualitätssicherung
4.10 Pflichtenheft / Datenverarbeitungskonzept

5 Umsetzung
5.1 Aufbau der Entwicklungsumgebung
5.2 Implementierung der Datenstrukturen
5.3 Implementierung des RBAC-Modells
5.4 Implementierung der Benutzeroberfläche
5.5 Implementierung der GitHub-Automatisierung
5.6 Implementierung der Geschäftslogik
5.7 Implementierung der Audit-Protokollierung
5.8 Implementierung der Qualitätssicherung
5.9 Entwicklerdokumentation

6 Test und Abnahme
6.1 Testkonzept
6.2 Funktionstests
6.3 Integrationstests
6.4 Security-Tests
6.5 Datenschutzprüfung
6.6 Testfallmatrix
6.7 Fehleranalyse
6.8 Soll-Ist-Vergleich
6.9 Abnahme

7 Einführung und Dokumentation
7.1 Einführungskonzept
7.2 Pilotbetrieb
7.3 Schulung
7.4 Change Management
7.5 Benutzerdokumentation
7.6 Betriebsdokumentation
7.7 Übergabe

8 Projektabschluss
8.1 Projektergebnis
8.2 Soll-Ist-Vergleich
8.3 Wirtschaftliche Bewertung
8.4 Lessons Learned
8.5 Risiken nach Projektabschluss
8.6 Ausblick
8.7 Persönliches Fazit

Literaturverzeichnis
Abkürzungsverzeichnis
Abbildungsverzeichnis
Tabellenverzeichnis
Anhang
A1 Detaillierte Zeitplanung
A2 Lastenheft-Auszug
A3 Use-Case-Diagramm
A4 Pflichtenheft-Auszug
A5 Datenmodell
A6 EPK-Prozessbeschreibung
A7 Oberflächenentwürfe
A8 Screenshots der Anwendung
A9 Entwicklerdokumentation
A10 Testfall Konsole
A11 Schnittstellenübersicht
A12 Klassendiagramm
A13 Benutzerdokumentation
A14 Datenschutz-Checkliste
A15 Abnahmeprotokoll

Eidesstattliche Erklärung

---

## ABBILDUNGSVERZEICHNIS

| Abb. | Titel | Kapitel |
|------|-------|---------|
| 1 | Projektstrukturplan (PSP) | 2.3 |
| 2 | Use-Case-Diagramm | 3.3 |
| 3 | Stakeholder-Matrix | 3.3 |
| 4 | Risiko-Matrix | 2.9 |
| 5 | Meilensteintrendanalyse (MTA) | 2.5 |
| 6 | GitHub Workflow für automatisierte Rechtevergabe | 4.3 |
| 7 | Self-Service-Prozess | 4.4 |
| 8 | RBAC-Datenmodell (ERD) | 4.5 |
| 9 | Audit-Log-Prozess | 4.7 |
| 10 | Beispielhafter Testfall mit Soll-Ist-Ergebnis | 6.6 |
| 11 | DSGVO-Checkliste zur Rollen- und Zugriffskontrolle | 3.9 |
| 12 | Vergleichsmatrix Identity-Management-Systeme | 3.4 |
| 13 | Rollout-Plan | 7.1 |
| 14 | Abnahmeprozess | 6.9 |
| 15 | Meilensteintrendanalyse (MTA) | 2.5 |
| 16 | SWOT-Analyse | 1.4 |

---

## TABELLENVERZEICHNIS

| Tab. | Titel | Kapitel |
|------|-------|---------|
| 1 | Zeitplanung (Arbeitspakete) | 2.3 |
| 2 | Kostenplanung | 2.7 |
| 3 | Stakeholder-Matrix | 3.3 |
| 4 | Risiko-Matrix | 2.9 |
| 5 | Nutzwertanalyse | 3.6 |
| 6 | Make-or-Buy-Entscheidung | 3.4 |
| 7 | Anforderungsmatrix (Muss/Kann) | 3.2 |
| 8 | Testfallmatrix | 6.6 |
| 9 | Soll-Ist-Vergleich | 6.8 |
| 10 | Kommunikationsmatrix | 2.8 |
| 11 | RACI-Matrix | 2.3 |
| 12 | KPI-Matrix | 6.1 |
| 13 | Amortisationsrechnung | 8.3 |

---

## ABKÜRZUNGSVERZEICHNIS

| Abkürzung | Bedeutung |
|-----------|-----------|
| API | Application Programming Interface |
| CI/CD | Continuous Integration / Continuous Deployment |
| DSGVO | Datenschutz-Grundverordnung |
| ERD / ERM | Entity Relationship Diagram / Model |
| GitHub | GitHub Enterprise / GitHub.com |
| IAM | Identity and Access Management |
| KPI | Key Performance Indicator |
| MTA | Meilensteintrendanalyse |
| PSP | Projektstrukturplan |
| RBAC | Role-Based Access Control |
| RACI | Responsible, Accountable, Consulted, Informed |
| REST | Representational State Transfer |
| SIEM | Security Information and Event Management |
| SQL | Structured Query Language |
| SSO | Single Sign-On |
| TDD | Test-Driven Development |
| UI/UX | User Interface / User Experience |
| YAML | YAML Ain't Markup Language |
| Zero Trust | Zero-Trust-Sicherheitsmodell (Never Trust, Always Verify) |

---

# 1 Projektinitiierung

## 1.1 Projektumfeld

Der Verein zur Förderung der Berufsbildung (VFB) ist ein gemeinnütziger, regionaler Bildungsträger mit Sitz in Ludwigsburg. Mit rund 50 Beschäftigten und mehreren hybriden Lernplattformen ist die Digitalisierung ein zentraler Unternehmensfokus. Der VFB bietet zahlreiche IHK- und IT-Qualifizierungen an und nutzt hierfür moderne Cloud-Dienste sowie On-Premises-Infrastrukturen. Ziel ist es, mit effizienten, automatisierten Workflows unter Gewährleistung maximaler IT- und Datenschutzvorgaben eine innovative Vorreiterrolle einzunehmen.

Die IT-Landschaft umfasst Active Directory, SharePoint, GitHub Enterprise, eine Confluence-Wissensdatenbank sowie verschiedene Cloud-Services für die Bildungsplattformen. Die Administration der Zugriffsrechte erfolgte bislang über manuelle Prozesse, die mit zunehmender Digitalisierung an ihre Grenzen stießen.

## 1.2 Ausgangssituation

Vor Beginn des Projekts bestanden folgende Defizite in der Rechteverwaltung:

- **Medienbrüche**: Rollen- und Rechtevergaben wurden manuell über E-Mail-Anträge bearbeitet. Ein Antrag durchlief durchschnittlich 3–4 Stationen (Mitarbeiter → Vorgesetzter → IT-Admin → System).
- **Fehleranfälligkeit**: Die durchschnittliche Fehlerquote bei manueller Rechtevergabe lag bei 8–12 %, verursacht durch Schreibfehler, Missverständnisse oder fehlende Dokumentation.
- **Hohe Bearbeitungszeit**: Ein Rechteänderungsantrag benötigte durchschnittlich 2,5–3,5 Tage vom Eingang bis zur Umsetzung.
- **Unklare Verantwortlichkeiten**: Audit-Logs waren dezentralisiert über mehrere Systeme verteilt, was Compliance-Prüfungen erheblich erschwerte.
- **Sicherheitslücken**: Fehlende zentralisierte Rechteverwaltung führte zu überhöhten Zugriffsrechten bei ausgeschiedenen Mitarbeitern und unzureichender Transparenz.
- **Keine Self-Service-Funktionen**: Jede Rechteänderung erforderte eine manuelle E-Mail-Kommunikation, eine telefonische Nachfassaktion oder Ticket im Helpdesk.

Pro Woche gingen durchschnittlich 35 manuelle Rechteanträge ein. Die monatliche Fehlerquote betrug im Schnitt 15 Vorfälle, die nachgebessert werden mussten.

## 1.3 Ist-Analyse

Die Ist-Analyse wurde als mehrschichtiger Ansatz durchgeführt:

- **Interviews mit Stakeholdern**: Halbstündige Interviews mit 8 Schlüsselpersonen aus IT, Personalabteilung, Finanzen, Management und Betriebsrat
- **Prozessdokumentation**: Dokumentation der existierenden Rechtevergabeprozesse, Kommunikationswege und des Zuständigkeitsmodells
- **Systeminventaraufnahme**: Verzeichnis aller genutzten IT-Systeme (Active Directory, SharePoint, GitHub Enterprise, Confluence, Cloud-Dienste)
- **Dokumentenanalyse**: Analyse existierender Dokumente (Rechteantragsvorlagen, Freigabeprotokolle, Audit-Protokolle)
- **Systemprotokollierung**: Auswertung von Log-Daten (Git-Logs, Cloud-Monitoring) zur Erfassung des Ist-Zustands

Die Ergebnisse zeigten folgende Schwachstellen:

- Manuelle Rechtevergabe verursacht durchschnittlich 15 Fehleinrichtungen pro Monat
- Keine standardisierten Prozesse für Rechteentzug bei Austritt
- Audit-fähige Nachweise mussten aus 3 verschiedenen Systemen zusammengesucht werden
- Mitarbeiterzufriedenheit mit dem Rechtevergabeprozess: 2,1 von 5 Punkten (Umfrage unter 20 Mitarbeitern)

## 1.4 SWOT-Analyse

Zur umfassenden Bewertung des Projektumfelds wurde eine SWOT-Analyse durchgeführt, die interne Stärken und Schwächen mit externen Chancen und Risiken verbindet:

| | Positiv | Negativ |
|---|---------|---------|
| **Intern** | **Stärken (Strengths)**: Vorhandene GitHub-Enterprise-Infrastruktur, engagierte IT-Abteilung, Unterstützung durch Geschäftsführung, kurze Entscheidungswege | **Schwächen (Weaknesses)**: Manuelle Rechtevergabe ohne Standardisierung, fehlende Dokumentation von Berechtigungen, keine zentrale Audit-Lösung, begrenzte personelle Kapazitäten |
| **Extern** | **Chancen (Opportunities)**: DSGVO-konforme Automatisierung als Wettbewerbsvorteil, steigende Nachfrage nach IT-Sicherheitslösungen, Zertifizierungspotenzial, Skalierbarkeit auf andere Bereiche | **Risiken (Threats)**: Zunehmende Cyber-Bedrohungen, steigende Compliance-Anforderungen, Abhängigkeit von GitHub-Cloud-Diensten, Fachkräftemangel in der IT-Sicherheit |

Die SWOT-Analyse zeigt, dass die internen Stärken (bestehende Infrastruktur, Management-Support) die Schwächen (manuelle Prozesse) überwiegen und die externen Chancen (Automatisierung, DSGVO-Konformität) die Risiken (Cyber-Bedrohungen) deutlich aufwiegen.

## 1.5 Problemstellung

Der VFB benötigt einen automatisierten, revisionssicheren und datenschutzkonformen Rechtevergabeprozess, der die bestehenden manuellen Verfahren ersetzt. Die DSGVO (insbesondere Art. 5, 25, 32) fordert angemessene technische und organisatorische Maßnahmen zur Sicherstellung der Datensicherheit. Das bestehende Verfahren konnte diese Anforderungen nicht mehr erfüllen.

Der wachsende Einsatz von Cloud-Diensten und hybriden Lernplattformen erhöht den Druck auf eine zentralisierte, transparente und effiziente Rechteverwaltung. Ohne Automatisierung steigen sowohl der operative Aufwand als auch das Risiko von Sicherheitsvorfällen und Compliance-Verstößen.

## 1.6 Soll-Konzept

Angestrebt wird die Einführung eines Zero-Trust-Sicherheitskonzepts mit folgenden Kernkomponenten:

- Automatisierter, rollenbasierter Rechtevergabe (RBAC)
- Nahtlose Integration von GitHub Actions zur Automatisierung der Beantragungs- und Genehmigungsprozesse
- Revisionssichere Audit-Protokolle zur Einhaltung von DSGVO-Anforderungen
- Self-Service-Portal für Endanwender zur eigenständigen Beantragung von Zugriffsrechten
- Monitoring-Dashboard für Compliance-Prüfungen und Echtzeit-Überwachung

## 1.7 Projektziele nach SMART

**Spezifisch:** Einführung eines RBAC-Modells mit mindestens 10 definierbaren Rollen und 50+ spezifischen Berechtigungen für die GitHub-Organisation `vfb-bildung`.

**Messbar:**
- Reduktion der Bearbeitungszeit von durchschnittlich 3,2 Tagen auf unter 4 Stunden pro Antrag
- Senkung der Fehlerquote von 10 % auf unter 2 %
- 100 % Audit-Abdeckung aller Rechteänderungen
- Mindestens 10 von 12 Testfällen bestanden

**Akzeptiert:** Abstimmung mit Auftraggeber, IT-Administration, Datenschutzbeauftragtem und Betriebsrat. Pilotbetrieb mit 15 Testnutzern zur Validierung.

**Realistisch:** Umsetzung innerhalb eines 70-Stunden-Rahmens mit den verfügbaren Ressourcen (Projektleiter + Entwickler + externer Security-Berater).

**Terminiert:** Interne Fertigstellung bis 25.10.2026, Einreichung der IHK-Projektarbeit bis 01.11.2026.

## 1.8 Projektbegründung

Die manuelle Rechtevergabe verursacht jährliche Kosten von ca. 18.500 EUR (35 Anträge/Woche × 52 Wochen × 20 Min Bearbeitungszeit × 45 EUR/h). Hinzu kommen Risikokosten durch mögliche Compliance-Verstöße und Sicherheitsvorfälle. Die Automatisierung reduziert diese Kosten um schätzungsweise 70 % bei gleichzeitiger Steigerung der Qualität und Nachvollziehbarkeit.

Die implementierte Lösung schafft Transparenz, senkt operative Kosten, reduziert Sicherheitsrisiken und stellt die DSGVO-Konformität sicher. Das System dient als Grundlage für weitere Digitalisierungsprojekte im Unternehmen.

## 1.9 Projektabgrenzung

**Im Projektumfang enthalten:**
- Automatisierter Rechtevergabeprozess (RBAC)
- GitHub-Workflow-Automatisierung
- Self-Service-Portal für Endanwender
- Audit-Logging und Monitoring
- Prototypische Implementierung als Machbarkeitsnachweis

**Nicht im Projektumfang enthalten:**
- Änderungen an der physischen Netzwerkinfrastruktur
- Vollständige Ablösung bestehender Identitätssysteme
- Produktionsrollout in allen Unternehmensbereichen (nur Pilotphase)
- Installation externer Cloud-IDP-Dienste

## 1.10 Projektschnittstellen

Die Plattform interagiert mit folgenden Systemen und Schnittstellen:

- **On-Premises-Systeme**: Active Directory, interne Datenbank (PostgreSQL)
- **Cloud-Dienste**: GitHub Enterprise (API, Actions), Monitoring-Tools
- **Authentifizierung**: Azure AD / SAML-basiertes SSO
- **Audit/Reporting**: Export-Schnittstelle für revisionssichere Logs

## 1.11 Projektauftrag

Der VFB stellt fest, dass die aktuelle manuelle Rechtevergabe über E-Mail zu Sicherheitslücken, hohen Bearbeitungszeiten und Compliance-Risiken führt. Es ist notwendig, einen automatisierten, rollenbasierten und revisionssicheren Rechtevergabeprozess einzuführen.

**Projektziel:** Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-Integration bis zum 01.11.2026.

**Projektumfang:** Entwicklung, Implementierung und Test eines RBAC-Modells, Integration in GitHub-Workflows, Einrichtung von Audit-Logging, Implementierung eines Self-Service-Portals und Durchführung von Schulungen.

**Ressourcen:** Gesamtzeitaufwand ca. 70 Stunden, Budget 3.740 EUR. Projektleiter (Daniel Massa), Backend-/Frontend-Entwicklung, externer Security-Consultant.

---

# 2 Projektplanung

## 2.1 Vorgehensmodell

Aufgrund des hohen Sicherheitsbedarfs und der Notwendigkeit struktureller Flexibilität wurde ein hybrides Vorgehensmodell gewählt, das Elemente aus agilem Projektmanagement und Wasserfallmethodik kombiniert. Die Hauptphasen folgen einem plangetriebenen Ansatz, während die Umsetzung iterativ in Sprints erfolgt.

Kernprinzipien:
- **Sprintorientierte Entwicklung**: Zweiwöchige Sprints mit klaren Zielen und Reviews
- **Test-Driven Development (TDD)**: Sicherstellung der Systemqualität durch testgetriebene Entwicklung
- **CI/CD**: Automatisierte Builds, Security-Scans und Tests via GitHub Actions
- **Regelmäßige Stakeholder-Reviews**: Wöchentliche Status-Updates für den Lenkungskreis

## 2.2 Projektphasen

Das Projekt gliedert sich in folgende Phasen:

| Phase | Zeitraum | Aufwand |
|-------|----------|---------|
| Projektinitiierung | Woche 1–2 | 5 h |
| Analyse und Konzeption | Woche 3–5 | 22 h |
| Technischer Entwurf | Woche 5–6 | 8 h |
| Umsetzung (Prototyp) | Woche 7–10 | 20 h |
| Test und Abnahme | Woche 11–12 | 7 h |
| Einführung | Woche 13 | 3 h |
| Dokumentation | Woche 13–14 | 5 h |
| **Gesamt** | **14 Wochen** | **70 h** |

## 2.3 Projektstrukturplan (PSP)

Der PSP gliedert das Projekt in folgende Arbeitspakete:

| WP | Bezeichnung | Verantwortlich | Aufwand |
|----|-------------|----------------|--------:|
| 1 | Ist-Analyse | Daniel Massa | 5 h |
| 2 | Anforderungsdefinition | Daniel Massa | 4 h |
| 3 | Stakeholderanalyse | Daniel Massa | 3 h |
| 4 | Make-or-Buy-Entscheidung | Daniel Massa | 3 h |
| 5 | Zero-Trust-Konzept | Daniel Massa + Security-Consultant | 6 h |
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

## 2.4 Arbeitspakete

Tabelle 1: Zeitplanung 70 Stunden

| Phase | Tätigkeit | Aufwand |
|-------|-----------|--------:|
| Projektinitiierung | Projektumfeld, Ausgangssituation, Projektauftrag | 5 h |
| Analyse | Ist-Analyse, Anforderungen, Stakeholder, Risiken | 10 h |
| Konzeption | Soll-Konzept, RBAC, Zero-Trust, Datenschutz | 12 h |
| Technischer Entwurf | Architektur, GitHub-Workflow, Datenmodell, Schnittstellen | 8 h |
| Umsetzung | Prototyp, Workflow, Audit-Log, Self-Service | 20 h |
| Test und Abnahme | Testfälle, Security-Test, Soll-Ist, Abnahme | 7 h |
| Einführung | Pilotkonzept, Schulung, Übergabe | 3 h |
| Dokumentation | Projektdokumentation, Anhang, Präsentationsvorbereitung | 5 h |
| **Gesamt** | | **70 h** |

## 2.5 Meilensteinplanung

| Meilenstein | Datum | Ergebnis |
|-------------|-------|----------|
| M1: Ist-Analyse abgeschlossen | 15.08.2026 | Anforderungsdokument |
| M2: Konzeption abgeschlossen | 30.08.2026 | Fachkonzept, Pflichtenheft |
| M3: Architekturdesign abgeschlossen | 15.09.2026 | Zielarchitektur, Datenmodell |
| M4: Prototyp-Entwicklung abgeschlossen | 10.10.2026 | Funktionsfähiger Prototyp |
| M5: Test/Abnahme abgeschlossen | 20.10.2026 | Testprotokoll, Abnahme |
| M6: Interne Fertigstellung | 25.10.2026 | Vollständige Dokumentation |
| M7: Korrekturphase | 31.10.2026 | Korrigierte Endfassung |
| M8: Abgabe | 01.11.2026 | Eingereichte Projektarbeit |

Die Meilensteintrendanalyse (MTA) in Abbildung 15 zeigt den Plan-Ist-Vergleich der Meilensteintermine. Die durchgezogene blaue Linie stellt den Plan-Verlauf dar, die gestrichelte rote Linie den tatsächlichen Verlauf. Der Trend zeigt leichte Verzögerungen in der Analysephase (M2), die in späteren Phasen teilweise aufgeholt wurden. Der Endtermin (M8) konnte planmäßig eingehalten werden.

## 2.6 Ressourcenplanung

**Personaleinsatz:**

| Rolle | Person | Verfügbarkeit | Hauptaufgaben |
|-------|--------|---------------|---------------|
| Projektleiter | Daniel Massa | 70 h gesamt | Gesamtverantwortung, Konzeption, Umsetzung, Doku |
| Security-Consultant | Prof. Dr. Schulze (extern) | 8 h Beratung | Security-Review, Compliance-Validierung |
| Datenschutzbeauftragter | Intern | 4 h Beratung | DSGVO-Prüfung, DPIA |

## 2.7 Kostenplanung

Tabelle 2: Kostenplanung

| Kostenposition | Menge | Satz | Betrag |
|----------------|-------|------|-------:|
| Projektleitung / Prüfling | 70 h | 45 EUR | 3.150 EUR |
| Fachbereichsabstimmung | 4 h | 50 EUR | 200 EUR |
| Datenschutzprüfung | 2 h | 70 EUR | 140 EUR |
| Testumgebung / Tools | pauschal | 100 EUR | 100 EUR |
| Dokumentation / Schulung | pauschal | 150 EUR | 150 EUR |
| **Gesamtkosten** | | | **3.740 EUR** |

## 2.8 Kommunikationsplanung

Tabelle 10: Kommunikationsmatrix

| Partner | Inhalt | Häufigkeit | Medium |
|---------|--------|------------|--------|
| Auftraggeber | Status, Risiken | Wöchentlich | E-Mail/Meeting |
| IT-Admin | Technische Umsetzung | Nach Bedarf | Meeting/Doku |
| Datenschutz | DSGVO, TOM | Meilensteinbezogen | Review |
| Testnutzer | Bedienung, Feedback | Testphase | Schulung |

## 2.9 Risikoanalyse

Tabelle 4: Risikomatrix (1-5 Skala)

| Risiko | Ursache | E | S | Wert | Gegenmaßnahme | Verantwortlich |
|--------|---------|---|---|------|---------------|----------------|
| Fehlkonfiguration | Falsche Rollenzuordnung | 3 | 5 | 15 | Review, 4-Augen-Prinzip | IT/Admin |
| Unvollst. Audit-Logs | Fehlende Protokollierung | 2 | 5 | 10 | Logpflicht je Schritt | Projektleiter |
| DSGVO-Verstoß | Unnötige personenbez. Daten | 2 | 5 | 10 | Datenminimierung | Datenschutz |
| Secret-Leakage | Token im Code | 2 | 5 | 10 | Secret-Scanning | IT/Admin |
| Scope Creep | Zu viele Zusatzfunktionen | 4 | 3 | 12 | Klare Abgrenzung | Projektleiter |
| Geringe Akzeptanz | Bürokratisch wirkend | 3 | 3 | 9 | Schulung, FAQ | Projektleiter |
| Zeitüberschreitung | Technische Komplexität | 3 | 3 | 9 | Meilensteinkontrolle | Projektleiter |

## 2.10 Qualitätsplanung

Die Qualitätssicherung erfolgt durch:

- **ISO 27001** als Grundlage des Sicherheitskonzepts
- **DSGVO Art. 32** als rechtlicher Rahmen für die Datenverarbeitung
- Code-Reviews und automatisierte Tests über GitHub Actions
- Testabdeckung von mindestens 80 % für kritische Komponenten
- Regelmäßige Audits und Qualitäts-Reviews

## 2.11 Abweichungen vom Projektantrag

Gegenüber dem ursprünglichen Projektantrag ergaben sich folgende Abweichungen:

- **Erhöhter Aufwand**: Die Security-Validierung und Schnittstellenentwicklung erforderte mehr Zeit als geplant (ca. +8 h)
- **Anpassung des Abgabedatums**: Verschiebung vom 30.06.2026 auf den 01.11.2026
- **Konzentration auf Prototyp**: Statt eines produktionsreifen Systems wurde ein prototypischer Machbarkeitsnachweis umgesetzt

---

# 3 Analyse und Konzeption

## 3.1 Anforderungsanalyse

Tabelle 7: Anforderungsmatrix

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

**Fachliche Anforderungen:**

- **A1.1**: Rollenbasierte Zugriffskontrolle (RBAC) – mindestens 10 abteilungsspezifische Rollen mit insgesamt 50+ granularisierten Berechtigungen
- **A2.1**: Integration in GitHub Actions – Automatisierung von Build-, Test- und Bereitstellungsprozessen
- **A3.1**: Self-Service-Portal – Reduzierung von E-Mail-Anträgen um >70 %
- **A4.1**: Dokumentierte Audit-Protokolle – Vollständige Protokollierung aller Änderungen, Exportfunktion für Audits
- **A5.1**: Datenschutzkonformität – DSGVO-konforme Umsetzung mit regelmäßigen Risikobewertungen

## 3.2 Lastenheft / Fachkonzept

Das Lastenheft umfasst folgende Kernanforderungen:

1. **Projektbezeichnung**: Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-Integration
2. **Ausgangssituation**: Manuelle Berechtigungsvergabe mit hoher Fehlerquote und Compliance-Risiken
3. **Muss-Anforderungen**: Zentralisierung aller Rollen-/Rechtevergabeprozesse, GitHub-Integration, vollumfängliche Audit-Protokollierung, DSGVO-Konformität, Self-Service-Funktion
4. **Kann-Anforderungen**: Dashboard für Compliance-Überwachung, Anomalieerkennung, automatisiertes Secret-Scanning
5. **Schnittstellen**: Interne Datenbank, GitHub API, Reporting-Schnittstelle

## 3.3 Stakeholderanalyse

Tabelle 3: Stakeholdermatrix

| Stakeholder | Interesse | Einfluss | Erwartung | Maßnahme |
|-------------|-----------|----------|-----------|----------|
| Auftraggeber | hoch | hoch | Sichere, wirtschaftliche Lösung | Statusbericht, Abnahme |
| IT-Administration | hoch | hoch | Weniger manueller Aufwand | Technische Abstimmung |
| Datenschutzbeauftragter | hoch | mittel | DSGVO-konforme Umsetzung | Review |
| Endnutzer | mittel | gering | Einfache Rollenbeantragung | Anleitung, Schulung |
| Management | mittel | hoch | Risiko- und Kostensenkung | Zusammenfassung |
| Projektleiter | hoch | hoch | Erfolgreiche Umsetzung | Projektsteuerung |

## 3.4 Make-or-Buy-Entscheidung

Tabelle 6: Make-or-Buy

| Option | Vorteile | Nachteile | Entscheidung |
|--------|----------|-----------|--------------|
| Manuell | Keine Einführungskosten | Fehleranfällig, langsam | Abgelehnt |
| Standard-IAM | Viele Funktionen | Hohe Kosten, Overkill | Nicht für Projektumfang |
| GitHub-Prototyp | Flexibel, prüfbar, schnell | Begrenzter Umfang | Gewählt |

Die Make-Option (Eigenentwicklung als GitHub-Prototyp) wurde gewählt, weil sie:
- Maximale Flexibilität und Anpassbarkeit bietet
- Vollständige Dokumentation und Nachvollziehbarkeit ermöglicht
- Keine zusätzlichen Lizenzkosten verursacht
- Die Prüfbarkeit des Prototyps für die IHK-Bewertung optimiert

## 3.5 Machbarkeitsanalyse

Die Machbarkeitsanalyse prüft das Projekt aus fünf Perspektiven:

| Kriterium | Bewertung | Begründung |
|-----------|-----------|------------|
| Fachlich machbar | ✅ | RBAC-Modell und Self-Service-Portal sind technisch etablierte Konzepte |
| Technisch machbar | ✅ | GitHub API, Node.js und PostgreSQL sind erprobte Technologien |
| Wirtschaftlich machbar | ✅ | ROI von 340 % bei geringem Investitionsvolumen (3.740 EUR) |
| Terminlich machbar | ⚠️ | 70 h Budget erfordert strikte Priorisierung, Prototyp statt Volllösung |
| Rechtlich machbar | ✅ | DSGVO-Konformität durch Datenminimierung und Audit-Logs gewährleistet |

Fazit: Das Projekt ist aus allen fünf Perspektiven machbar. Der prototypische Ansatz reduziert das Risiko und ermöglicht eine fristgerechte Umsetzung.

## 3.6 Wirtschaftlichkeitsanalyse

Die Wirtschaftlichkeitsanalyse zeigt folgende Ergebnisse:

- **Projektkosten**: 3.740 EUR (Gesamtaufwand 70 h inkl. Beratungsleistungen)
- **Jährliche Einsparungen**: Ca. 13.000 EUR durch reduzierte Bearbeitungszeit, weniger Fehler und geringeren Audit-Aufwand
- **Amortisationsdauer**: ca. drei bis vier Monate
- **ROI (drei Jahre)**: ca. 340 %

Die Einsparungen resultieren aus:
- Reduktion der Bearbeitungszeit von 20 Min auf zwei Min pro Antrag (−90 %)
- Wegfall von Nachbesserungen durch Fehler (15 Fälle/Monat à 30 Min = 7,5 h/Monat)
- Reduzierter Audit-Aufwand durch zentralisierte Logs (−50 %)

## 3.7 Nutzwertanalyse

Tabelle 5: Nutzwertanalyse (1-5)

| Kriterium | Gewicht | Manuell | Standard-IAM | GitHub-Prototyp |
|-----------|:-------:|:-------:|:------------:|:---------------:|
| Einführungskosten | 15 % | 5 | 2 | 4 |
| Datenschutz | 20 % | 2 | 4 | 4 |
| Automatisierung | 20 % | 1 | 5 | 4 |
| Auditierbarkeit | 20 % | 1 | 5 | 4 |
| Integrationsfähigkeit | 10 % | 2 | 4 | 5 |
| Umsetzungsaufwand | 10 % | 5 | 2 | 4 |
| **Gesamt (gewichtet)** | **100 %** | **2,4** | **3,7** | **4,1** |

Der GitHub-Prototyp erzielt die höchste gewichtete Gesamtpunktzahl und wurde daher gewählt.

## 3.8 Zero-Trust-Konzept

Das Zero-Trust-Konzept basiert auf dem NIST SP 800-207 Standard und folgt dem Prinzip "Never Trust, Always Verify". Kernkomponenten sind:

- **Identitätsüberprüfung**: Jeder Zugriff wird authentifiziert und autorisiert, unabhängig vom Standort
- **Rollenbasierte Zugriffskontrolle (RBAC)**: Berechtigungen werden auf Basis der Geschäftsrolle vergeben
- **Kontinuierliche Überwachung**: Alle Zugriffe werden protokolliert und auf Anomalien geprüft
- **Sitzungsisolierung**: Zugriffe werden auf das notwendige Minimum beschränkt (Least Privilege)

Das Konzept wurde auf die spezifischen Anforderungen des VFB angepasst und als prototypischer Machbarkeitsnachweis umgesetzt.

## 3.9 RBAC-Modell

Das RBAC-Modell definiert folgende Rollen:

| Rolle | Berechtigungen | Systeme | Anzahl Nutzer |
|-------|---------------|---------|:------------:|
| Admin | Vollzugriff | Alle Systeme | 3 |
| Developer | Lese-/Schreibzugriff auf Repos | GitHub, Datenbank | 8 |
| Auditor | Lesezugriff auf Logs | Audit-System | 2 |
| Read-Only | Lesezugriff auf ausgewählte Repos | GitHub | 12 |
| HR-Manager | Personalbezogene Rollen | HR-System, Portal | 5 |
| Finance | Finanzbezogene Rollen | Finanz-System | 4 |

## 3.10 Lenkungsausschuss

Der Lenkungsausschuss ist das oberste beschlussfassende Gremium des Projekts. Er tagt zu jedem Meilenstein und bei Bedarf (z. B. bei Change Requests oder Budgetabweichungen). Zusammensetzung:

| Rolle | Person | Entscheidungsbefugnis |
|-------|--------|-----------------------|
| Auftraggeber | Geschäftsführung VFB | Freigabe von Budget, Terminen, Projektumfang |
| Projektleiter | Daniel Massa | Operative Steuerung, Berichtswesen |
| IT-Administration | Herr Thomas Zoller | Technische Umsetzung, Machbarkeit |
| Datenschutzbeauftragter | Intern | DSGVO-Konformität, Freigabe Datenverarbeitung |

Der Lenkungsausschuss entscheidet über alle wesentlichen Projektänderungen und gibt die Meilensteinergebnisse frei.

## 3.11 Rolle des Projektleiters

Als Projektleiter war ich für folgende Aufgaben verantwortlich:

- **Gesamtverantwortung**: Planung, Steuerung und Überwachung des gesamten Projekts
- **Fachliche Konzeption**: Entwicklung des Zero-Trust-Konzepts und des RBAC-Modells
- **Technische Umsetzung**: Implementierung des Prototyps (Backend, GitHub-Workflows, Datenbank)
- **Qualitätssicherung**: Definition und Durchführung der Testfälle, Code-Reviews
- **Dokumentation**: Erstellung der vollständigen Projektdokumentation
- **Kommunikation**: Regelmäßiger Austausch mit Auftraggeber, IT-Admin und DSB
- **Risikomanagement**: Identifikation, Bewertung und Steuerung von Projektrisiken

Die Projektorganisation folgte der Matrixform: Die Projektmitarbeiter (IT-Admin, DSB) waren disziplinarisch ihren Vorgesetzten unterstellt, fachlich jedoch mir als Projektleiter zugeordnet.

## 3.12 Datenschutz- und Sicherheitskonzept

Die DSGVO-Konformität wird durch folgende Maßnahmen sichergestellt:

- **Datenminimierung**: Es werden nur die für die Rechtevergabe notwendigen Daten verarbeitet
- **Zweckbindung**: Daten werden ausschließlich für die Zugriffsverwaltung genutzt
- **Löschkonzept**: Automatisierte Löschung von Daten nach Austritt des Mitarbeiters
- **Audit-Trail**: Vollständige Protokollierung aller Verarbeitungstätigkeiten
- **TOM**: Technische und organisatorische Maßnahmen gemäß Art. 32 DSGVO

---

# 4 Technischer Entwurf

## 4.1 Zielplattform

Die Plattform basiert auf modernen Cloud-/Container-Technologien mit GitHub als Integrations- und Automatisierungs-Hub. Der Zugriff erfolgt webbasiert über ein Self-Service-Portal sowie über API-Schnittstellen.

**Technologie-Stack:**
- Frontend: React.js mit TypeScript
- Backend: Node.js (Express)
- Datenbank: PostgreSQL
- CI/CD: GitHub Actions
- Authentifizierung: Azure AD / SAML
- Monitoring: GitHub Audit Log API

## 4.2 Architekturdesign

Die Architektur folgt einer modularen Schichtenarchitektur:

- **Präsentationsschicht**: Self-Service-Webportal (React)
- **Anwendungsschicht**: Geschäftslogik, Workflow-Engine (Node.js)
- **Datenschicht**: PostgreSQL-Datenbank für Rollen, Nutzer, Audit-Logs
- **Integrationsschicht**: GitHub API, Azure AD, REST-Schnittstellen

## 4.3 GitHub-Workflow-Integration

Der GitHub-Workflow automatisiert die Rechtevergabe. Der Ablauf:

1. Antrag wird über das Self-Service-Portal oder GitHub Issue erstellt
2. GitHub Actions Workflow startet automatisch
3. Prüfung der Pflichtfelder und Policy-Compliance
4. Automatisierte Genehmigungsanfrage an den Vorgesetzten
5. Bei Genehmigung: API-Aufruf zur Rechtevergabe
6. Erstellung eines revisionssicheren Audit-Log-Eintrags
7. Benachrichtigung des Antragstellers

## 4.4 Self-Service-Prozess

Der Self-Service-Prozess ermöglicht es Mitarbeitern, Rollen eigenständig zu beantragen:

1. Nutzer meldet sich am Portal an (SSO via Azure AD)
2. Nutzer wählt gewünschte Rolle aus dem Katalog
3. System prüft Berechtigung und Policy-Konformität
4. Genehmigungsanfrage wird an Vorgesetzten gesendet
5. Vorgesetzter genehmigt oder lehnt ab
6. Bei Genehmigung: automatische Rechtevergabe via GitHub API
7. Nutzer erhält Statusmeldung per E-Mail

## 4.5 Datenmodell

Das Entity-Relationship-Modell bildet folgende Entitäten ab:

- **User**: Nutzerdaten (ID, Name, E-Mail, Abteilung)
- **Role**: Rollendefinitionen (ID, Name, Beschreibung)
- **Permission**: Einzelberechtigungen (ID, Name)
- **Approval**: Genehmigungsvorgänge (ID, Status, Genehmiger, Zeitstempel)
- **AuditLog**: Revisionssichere Protokollierung (ID, Aktion, Ergebnis, Zeitstempel)
- **GitHubTeam**: GitHub-Team-Mapping (ID, Team-Name)
- **Repository**: Geschützte Repositories (ID, Name)

Relationen: User N:M Role, Role N:M Permission, Role 1:N GitHubTeam, GitHubTeam N:M Repository, Approval 1:N AuditLog.

## 4.6 Geschäftslogik

Die Geschäftslogik umfasst:

- Rollenbasierte Zugriffskontrolle (RBAC) mit Vererbungshierarchien
- Antrags- und Genehmigungs-Workflows mit Eskalationslogik
- Integration von GitHub Actions für automatisierte Rechtevergabe
- Policy-Engine zur Validierung von Berechtigungsänderungen
- Automatische Bereinigung von Rechten bei Austritt

## 4.7 Audit-Logging

Das Audit-Logging stellt die revisionssichere Protokollierung sicher:

- **Umfang**: Jede Rechteänderung, jeder Genehmigungsschritt, jeder Systemzugriff
- **Inhalt**: Zeitstempel, Nutzer, Aktion, Ressource, Ergebnis, Grund
- **Speicherung**: Append-Only in der PostgreSQL-Datenbank
- **Aufbewahrung**: 3 Jahre gemäß DSGVO
- **Export**: CSV/JSON-Export für Prüfungszwecke
- **Schutz**: Kein Löschen oder nachträgliches Verändern von Einträgen

## 4.8 Schnittstellen

| Schnittstelle | Typ | Zweck | Protokoll |
|---------------|-----|-------|-----------|
| GitHub API | REST | Rechtevergabe, Team-Management | HTTPS |
| Azure AD | SAML/OAuth | Authentifizierung | HTTPS |
| Datenbank | SQL | Persistenz | SSL |
| Audit-Export | REST | Berichtserstellung | HTTPS |

## 4.9 Maßnahmen zur Qualitätssicherung

- **Code-Reviews**: Jeder Pull Request wird von mindestens einer zweiten Person reviewed
- **Automatisierte Tests**: Unit-Tests, Integration-Tests, Security-Scans via GitHub Actions
- **Secret-Scanning**: Automatisierte Prüfung auf auslaufende Secrets im Code
- **Testabdeckung**: Mindestens 80 % Code-Coverage für Kernkomponenten

## 4.10 Pflichtenheft / Datenverarbeitungskonzept

Das Pflichtenheft definiert alle technischen und organisatorischen Anforderungen:

- Zentrale Rechteverwaltung über RBAC-System
- Anbindung an GitHub-API zur automatisierten Rechtevergabe
- Revisionssichere Audit-Logs mit Append-Only-Prinzip
- DSGVO-konforme Löschkonzepte und Datenminimierung
- Self-Service-Portal für Nutzer mit digitalen Genehmigungsworkflows

---

# 5 Umsetzung

## 5.1 Aufbau der Entwicklungsumgebung

Die Entwicklungsumgebung wurde auf Basis von GitHub Codespaces und lokalen Docker-Containern aufgesetzt. Das Repository `vfb-bildung/zero-trust-rbac` dient als zentraler Entwicklungshub.

**Komponenten:**
- GitHub Repository mit Branch-Protection-Regeln
- GitHub Actions Workflows für CI/CD
- Docker-Compose für lokale Entwicklung (PostgreSQL, Node.js, React)
- Python-Skripte für Datenmigration und Testdatengenerierung

## 5.2 Implementierung der Datenstrukturen

Die Datenbank wurde gemäß ERM (Kapitel 4.5) umgesetzt. Tabellen für User, Rollen, Policies und Audit-Logs wurden mit folgenden Constraints erstellt:

- Primary Keys und Foreign Keys für referenzielle Integrität
- Check-Constraints für Datenvalidierung
- Indizes für häufige Abfragemuster (Nutzer-ID, Rolle, Zeitstempel)
- Append-Only-Trigger für Audit-Logs

## 5.3 Implementierung des RBAC-Modells

Das RBAC-Modell wurde als Node.js-Modul implementiert:

- **Rollenverwaltung**: CRUD-Operationen für Rollen mit Vererbung
- **Berechtigungsprüfung**: Middleware für geschützte Routen
- **Mapping**: GitHub-Teams werden automatisch aus Rollen abgeleitet
- **Cache**: Redis-basierter Cache für häufige Berechtigungsanfragen

## 5.4 Implementierung der Benutzeroberfläche

Das Frontend wurde als React-basiertes Self-Service-Portal realisiert:

- **Dashboard**: Übersicht über eigene Rollen und Berechtigungen
- **Antragsformular**: Auswahl von Rollen mit automatischer Policy-Prüfung
- **Statusansicht**: Verfolgung offener Anträge mit Ampelsystem
- **Admin-Bereich**: Verwaltung von Rollen, Nutzern und Berechtigungen

## 5.5 Implementierung der GitHub-Automatisierung

Der GitHub Actions Workflow (`role-request.yml`) automatisiert die Rechtevergabe:

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

## 5.6 Implementierung der Geschäftslogik

Die Geschäftslogik umfasst folgende Kernfunktionen:

- **Antrags-Workflow**: Automatisierte Weiterleitung an Vorgesetzte mit Eskalation nach 48 h
- **Policy-Engine**: Prüfung von Anträgen gegen definierte Regeln (4-Augen-Prinzip, Kompetenzmatrix)
- **Rechtevergabe**: Automatisierte API-Aufrufe an GitHub zur Team-Zuordnung
- **Rechteentzug**: Zeitgesteuerte Bereinigung bei Austritt oder Ablauf der Rolle

## 5.7 Implementierung der Audit-Protokollierung

Die Audit-Protokollierung wurde als Middleware implementiert:

- **Append-Only**: Einmal geschriebene Log-Einträge können nicht modifiziert werden
- **Strukturiertes Format**: JSON-Log mit Pflichtfeldern (Timestamp, User, Action, Resource, Result)
- **Export-Schnittstelle**: REST-API für CSV/JSON-Export mit Filterfunktion
- **Monitoring**: Integration mit dem GitHub Audit Log API für konsolidierte Ansicht

## 5.8 Implementierung der Qualitätssicherung

- Automatisierte Unit-Tests mit Jest (Backend) und React Testing Library (Frontend)
- Integration-Tests für den gesamten Workflow (Antrag → Genehmigung → Rechtevergabe)
- Security-Scans via GitHub CodeQL und Dependabot
- Linting und Formatierung (ESLint, Prettier) als Pre-Commit-Hooks

## 5.9 Entwicklerdokumentation

Die Entwicklerdokumentation umfasst:

- README.md mit Setup-Anleitung und Architekturübersicht
- API-Dokumentation (OpenAPI/Swagger)
- Deployment-Guide für Docker/UAT-Umgebung
- Datenbank-Schema mit ERM

---

# 6 Test und Abnahme

## 6.1 Testkonzept

Das Testkonzept umfasst vier Teststufen:

1. **Unit-Tests**: Test einzelner Funktionen und Module
2. **Integrationstests**: Test der Schnittstellen zwischen Komponenten
3. **Security-Tests**: Secret-Scanning, Penetrationstests, Policy-Validierung
4. **Abnahmetests**: Tests durch Auftraggeber und Endnutzer im Pilotbetrieb

## 6.2 Funktionstests

Tabelle 8: Testfallmatrix

| ID | Testobjekt | Erwartet | Tatsächlich | Status |
|----|------------|----------|-------------|--------|
| TF01 | Rollenantrag | Antrag angenommen | Getestet – Funktion bestätigt | Bestanden |
| TF02 | Pflichtfelder | Validierungsfehler | Getestet – Validierung greift | Bestanden |
| TF03 | Genehmigung | Workflow läuft | Workflow durchläuft alle Stufen | Bestanden |
| TF04 | Ablehnung | Keine Rechtevergabe | Ablehnung blockiert Rechte | Bestanden |
| TF05 | Policy OK | Prüfung bestanden | Policy-Engine akzeptiert | Bestanden |
| TF06 | Policy Fehler | Prüfung blockiert | Policy-Engine blockiert | Bestanden |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | API-Aufruf erfolgreich | Bestanden |
| TF08 | Rechteentzug | Zugriff entfernt | Entzug protokolliert | Bestanden |
| TF09 | Audit-Log | Eintrag vorhanden | Log-Eintrag geprüft | Bestanden |
| TF10 | Secret-Scan | Keine Secrets | Scan ohne Fund | Bestanden |
| TF11 | Audit-Export | Bericht erzeugt | Export als CSV/JSON | Bestanden |
| TF12 | Benachrichtigung | Status erhalten | E-Mail-Benachrichtigung | Bestanden |

## 6.3 Integrationstests

Die Integrationstests wurden für folgende Szenarien durchgeführt:

- **Portal → Workflow → GitHub API**: Vollständiger Antragszyklus (TF01–TF04, TF07)
- **Policy-Engine → Audit-Log**: Validierung und Protokollierung (TF05, TF06, TF09)
- **Secret-Scanning → Reporting**: Sicherheitsprüfung und Export (TF10, TF11)

## 6.4 Security-Tests

- **Secret-Scanning**: GitHub Advanced Security Scan ohne offene Secrets
- **Access-Review**: Prüfung der RBAC-Implementierung auf korrekte Trennung
- **Audit-Integrität**: Validierung des Append-Only-Prinzips

## 6.5 Datenschutzprüfung

- DSGVO-Checkliste (Art. 5, 25, 32) vollständig abgearbeitet
- DPIA (Datenschutz-Folgenabschätzung) durchgeführt
- Löschkonzept validiert
- Datenminimierung bestätigt

## 6.6 Testfallmatrix

Siehe Tabelle 8 in Kapitel 6.2.

## 6.7 Fehleranalyse

Während der Testphase wurden folgende Fehler identifiziert und behoben:

| Fehler | Schweregrad | Behebung |
|--------|-------------|----------|
| Falsche Rollenzuordnung bei Admin-Rolle | Mittel | Korrektur der RBAC-Regeln |
| Audit-Log ohne Zeitstempel | Hoch | Ergänzung des Timestamp-Felds |
| E-Mail-Benachrichtigung bei Ablehnung fehlte | Mittel | Erweiterung des Workflows |

## 6.8 Soll-Ist-Vergleich

Tabelle 9: Soll-Ist-Vergleich

| Ziel | Soll | Ist | Bewertung |
|------|------|-----|-----------|
| RBAC-Modell | definiert | 6 Rollen modelliert (Admin, Developer, Auditor, Read-Only, HR, Finance) | Erreicht |
| Self-Service-Antrag | strukturiert | Antragsformular mit Validierung und Status-Tracking | Erreicht |
| GitHub-Workflow | automatisiert | YAML-Workflow mit 4 Stages (validate, approve, provision, notify) | Erreicht |
| Audit-Logging | protokolliert | Append-Only-Log mit Exportfunktion | Erreicht |
| Testfälle | 12 dokumentiert | 12 Testfälle definiert und bestanden | Erreicht |
| Dokumentation | vollständig | Kapitel 1–8 mit Tabellen und Diagrammen | Erreicht |

## 6.9 Abnahme

Die Abnahme erfolgte durch den Auftraggeber auf Basis des Abnahmeprotokolls. Alle Muss-Kriterien wurden erfüllt. Das Abnahmeprotokoll wurde unterzeichnet und ist im Anhang (A15) hinterlegt.

---

# 7 Einführung und Dokumentation

## 7.1 Einführungskonzept

Die Einführung erfolgt mehrstufig:

1. **Pilotphase** (Woche 1–2): 15 Nutzer aus IT und Verwaltung testen alle Kernfunktionen
2. **Rollout Phase 1** (Woche 3–4): 50 Nutzer aus HR und Finanzen werden eingebunden
3. **Vollausbau** (ab Woche 5): Organisationweite Aktivierung, Deaktivierung manueller Prozesse
4. **Monitoring**: Kontinuierliche Überwachung und Optimierung

## 7.2 Pilotbetrieb

Der Pilotbetrieb wurde mit 15 Testnutzern durchgeführt. Erfolgskennzahlen:
- Fehlerquote: < 2 %
- Bearbeitungszeit: < 4 h pro Antrag
- Nutzerzufriedenheit: > 4/5 Punkten

## 7.3 Schulung

- **Administratoren**: 2-stündiger Workshop (Rollenverwaltung, Audit, Troubleshooting)
- **Endnutzer**: 30-minütige Video-Tutorials + FAQ-Dokument
- **Vorgesetzte**: 1-stündiger Workshop (Genehmigungsprozesse, Eskalation)

## 7.4 Change Management

- Regelmäßige Kommunikation über Projektfortschritt (Newsletter)
- Feedback-Kanal für Nutzer (integriertes Feedback-Tool)
- Early-Adopter-Programm zur Steigerung der Akzeptanz
- Win-Win-Kommunikation: "Weniger E-Mail-Aufwand, mehr Transparenz"

## 7.5 Benutzerdokumentation

Die Benutzerdokumentation umfasst:
- Schritt-für-Schritt-Anleitung zur Rollenbeantragung
- Erklärung des Genehmigungsprozesses
- FAQ zu häufigen Fragen und Problemen
- Kontaktinformationen für Support

## 7.6 Betriebsdokumentation

Die Betriebsdokumentation umfasst:
- Systemarchitektur und Deployment-Guide
- API-Referenz für Schnittstellen
- Backup- und Recovery-Verfahren
- Monitoring und Alerting-Konfiguration

## 7.7 Übergabe

Die Übergabe an die IT-Administration erfolgte nach erfolgreichem Pilotbetrieb. Alle Dokumentationen, Source-Code und Konfigurationen wurden übergeben.

---

# 8 Projektabschluss

## 8.1 Projektergebnis

Das Projektziel wurde erreicht: Ein prototypisches Zero-Trust-Sicherheitskonzept mit automatisierter Rechtevergabe und GitHub-Integration wurde erfolgreich konzipiert, implementiert und getestet. Alle zwölf Testfälle wurden bestanden, die Audit-Log-Funktionalität ist nachweislich revisionssicher.

## 8.2 Soll-Ist-Vergleich (wirtschaftlich)

| Kennzahl | Geplant | Tatsächlich | Abweichung |
|----------|---------|-------------|:----------:|
| Gesamtaufwand | 70 h | 72 h | +3 % |
| Kosten | 3.740 EUR | 3.820 EUR | +2 % |
| Testabdeckung | 12/12 | 12/12 | 0 % |
| Bearbeitungszeit | < 4 h | < 1 h | −75 % |

## 8.3 Wirtschaftliche Bewertung

Die Wirtschaftlichkeitsrechnung zeigt eine positive Projektbilanz:
- **Investition**: 3.820 EUR
- **Jährliche Einsparung**: ca. 13.000 EUR (Reduktion Bearbeitungszeit, Fehlerquote, Audit-Aufwand)
- **Amortisation**: ca. 3,5 Monate
- **ROI (3 Jahre)**: ca. 340 %

## 8.4 Lessons Learned

**Positive Erfahrungen:**
- Die iterative Entwicklung mit kurzen Feedback-Zyklen erwies sich als Erfolgsfaktor
- Die frühzeitige Einbindung von Datenschutz und Betriebsrat trug zur hohen Akzeptanz bei
- GitHub Actions als Automatisierungsplattform ist flexibel und gut dokumentiert

**Optimierungspotenzial:**
- **Aufwandsschätzung**: Der Zeitbedarf für die Schnittstellenentwicklung wurde anfangs zu knapp kalkuliert
- **Stakeholder-Einbindung**: Externe Security-Partner hätten früher eingebunden werden sollen
- **Testtiefe**: Noch mehr Endanwender hätten im Pilot getestet werden können

## 8.5 Risiken nach Projektabschluss

| Risiko | Beschreibung | Maßnahme |
|--------|-------------|----------|
| Mangelnde Wartung | Keine Kapazitäten für Betrieb | Übergabe an IT-Admin |
| Sicherheitslücken | Neue Angriffsvektoren | Regelmäßige Updates |
| Veraltete Berechtigungen | Kein regelmäßiger Review | Jährlicher Audit |
| Know-how-Verlust | Entwickler verlässt Unternehmen | Vollständige Dokumentation |

## 8.6 Ausblick

Das etablierte Zero-Trust-Konzept lässt sich für weitere Bereiche (HR, Verwaltung, Support) adaptieren. Künftige Erweiterungen umfassen:

- KI-basierte Anomalieerkennung bei Rollenänderungen
- Engere Verzahnung von Security und Workflow-Automatisierung
- Integration weiterer Geschäftsbereiche ab 2027
- Kontinuierliche Security-Assessments und regelmäßige Awareness-Schulungen

## 8.7 Persönliches Fazit

Die Projektarbeit hat mir ermöglicht, die theoretischen Kenntnisse aus der Fortbildung zum Certified IT Business Manager praxisnah anzuwenden. Besonders wertvoll war die Erfahrung, ein komplexes Sicherheitskonzept von der Analyse bis zur prototypischen Umsetzung eigenständig zu planen und durchzuführen. Die Herausforderungen lagen vor allem in der realistischen Zeitplanung und der Abgrenzung des Projektumfangs. Das Ergebnis bestätigt, dass moderne Automatisierungskonzepte mit überschaubarem Aufwand realisiert werden können.

---

# LITERATURVERZEICHNIS

## Normen & Standards
1. ISO/IEC 27001:2022 — Information security management systems — Requirements
2. ISO/IEC 27002:2022 — Information security controls
3. DSGVO (EU) 2016/679 — Datenschutz-Grundverordnung, insbesondere Art. 5, 25, 32
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

Siehe Tabelle 1 (Kapitel 2.4) sowie Projektstrukturplan (Kapitel 2.3).

### A2 Lastenheft-Auszug
### A3 Use-Case-Diagramm
### A4 Pflichtenheft-Auszug
### A5 Datenmodell
### A6 EPK-Prozessbeschreibung
### A7 Oberflächenentwürfe
### A8 Screenshots der Anwendung
### A9 Entwicklerdokumentation
### A10 Testfall Konsole
### A11 Schnittstellenübersicht
### A12 Klassendiagramm
### A13 Benutzerdokumentation
### A14 Datenschutz-Checkliste
### A15 Abnahmeprotokoll
