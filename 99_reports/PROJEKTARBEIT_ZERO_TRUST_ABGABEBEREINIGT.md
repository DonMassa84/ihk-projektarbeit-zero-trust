# Projektarbeit im Rahmen der Prüfung zum Certified IT Business Manager (IHK)

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
Carsten Vordermeier

**IHK-Betreuer:**
Frau Dr. Sabine Wagner, IHK Region Stuttgart

---

## SPERRVERMERK

Die vorliegende Projektdokumentation mit dem Titel "Zero-Trust-Sicherheitskonzept mit GitHub-Integration" enthält vertrauliche Informationen und Daten des Vereins zur Förderung der Berufsbildung e.V. (VFB). Die Weitergabe oder Vervielfältigung – auch in Auszügen – ist ohne ausdrückliche Zustimmung des Unternehmens und des Verfassers nicht gestattet. Die Einsichtnahme durch Dritte bedarf der vorherigen Genehmigung und ist ausschließlich für den Prüfungsprozess der IHK Region Stuttgart gestattet.

---

## INHALTSVERZEICHNIS

Sperrvermerk ...................................................................................................... II
Abbildungsverzeichnis ........................................................................................... III
Tabellenverzeichnis ............................................................................................... IV
Abkürzungsverzeichnis ........................................................................................... V
1 Initiierung ........................................................................................................ 1
  1.1 Ausgangslage und Projektumfeld ................................................................... 1
  1.2 Auftrag und Projektziele ................................................................................ 3
  1.3 Zielsetzung nach SMART ................................................................................ 4
  1.4 Projektabgrenzung ........................................................................................ 5
  1.5 Stakeholderanalyse ....................................................................................... 6
  1.6 Rolle des Projektleiters ................................................................................. 7
2 Projektplanung .................................................................................................. 8
  2.1 Vorgehensmodell .......................................................................................... 8
  2.2 Projektstrukturplan (PSP) .............................................................................. 9
  2.3 Meilensteinplanung ....................................................................................... 10
  2.4 Ressourcen- und Zeitplanung ......................................................................... 11
  2.5 Kostenplanung .............................................................................................. 12
  2.6 Risikomanagement ........................................................................................ 13
  2.7 Kommunikationsplanung ................................................................................ 15
  2.8 Qualitätsplanung .......................................................................................... 16
3 Konzeptionierung ............................................................................................... 17
  3.1 Ist-Analyse ................................................................................................... 17
  3.2 Soll-Konzept ................................................................................................ 19
  3.3 Architekturentscheidungen und Alternativenbewertung .................................. 20
  3.4 Make-or-Buy-Entscheidung ............................................................................ 21
  3.5 Nutzwertanalyse ........................................................................................... 22
  3.6 Wirtschaftlichkeitsanalyse ............................................................................ 23
  3.7 Zero-Trust-Konzept ....................................................................................... 24
  3.8 RBAC-Modell ................................................................................................ 25
  3.9 Datenschutz- und Sicherheitskonzept ............................................................ 26
4 Durchführung .................................................................................................... 27
  4.1 Kick-off und Entwicklungsaufbau .................................................................. 27
  4.2 Implementierung der Datenstrukturen ........................................................... 28
  4.3 Implementierung des RBAC-Modells .............................................................. 29
  4.4 Implementierung der Benutzeroberfläche ...................................................... 30
  4.5 Implementierung der GitHub-Automatisierung ................................................ 31
  4.6 Implementierung der Audit-Protokollierung ................................................... 32
  4.7 Probleme und Lösungen ................................................................................ 33
  4.8 Abweichungen vom Plan ............................................................................... 33
  4.9 Test und Abnahme ........................................................................................ 34
5 Abschluss .......................................................................................................... 36
  5.1 Soll-Ist-Vergleich .......................................................................................... 36
  5.2 Wirtschaftlichkeitsbetrachtung ...................................................................... 37
  5.3 Übergabe ..................................................................................................... 38
  5.4 Lessons Learned .......................................................................................... 38
  5.5 Risiken nach Projektabschluss ....................................................................... 39
  5.6 Ausblick ....................................................................................................... 40
  5.7 Persönliches Fazit ......................................................................................... 40
6 Anhang ............................................................................................................. 41
  A1 Projektstrukturplan (PSP) ................................................................................ 41
  A2 Lastenheft-Auszug .......................................................................................... 42
  A3 Use-Case-Diagramm ....................................................................................... 43
  A4 Pflichtenheft-Auszug ...................................................................................... 44
  A5 Datenmodell .................................................................................................. 45
  A6 EPK-Prozessbeschreibung ................................................................................ 46
  A7 Oberflächenentwürfe ...................................................................................... 47
  A8 Screenshots der Anwendung ........................................................................... 48
  A9 Entwicklerdokumentation (§9 PO) .................................................................... 49
  A10 Testfall-Matrix .............................................................................................. 50
  A11 Schnittstellenübersicht .................................................................................. 51
  A12 Klassendiagramm .......................................................................................... 52
  A13 Benutzerdokumentation ................................................................................ 53
  A14 Datenschutz-Checkliste ................................................................................. 54
  A15 Abnahmeprotokoll ........................................................................................ 55
Eidesstattliche Versicherung .................................................................................. 56

---

## ABBILDUNGSVERZEICHNIS

| Abb. | Titel | Kapitel |
|------|-------|---------|
| 1 | Projektstrukturplan (PSP) | 2.2 |
| 2 | Use-Case-Diagramm | 3.3 |
| 3 | Stakeholder-Matrix | 1.5 |
| 4 | Risiko-Matrix | 2.6 |
| 5 | Meilensteintrendanalyse (MTA) | 2.3 |
| 6 | GitHub Workflow für automatisierte Rechtevergabe | 3.3 |
| 7 | Self-Service-Prozess | 3.3 |
| 8 | RBAC-Datenmodell (ERD) | 3.8 |
| 9 | Audit-Log-Prozess | 4.6 |
| 10 | Testfall mit Soll-Ist-Ergebnis | 4.9 |
| 11 | DSGVO-Checkliste zur Rollen- und Zugriffskontrolle | 3.9 |
| 12 | Vergleichsmatrix Identity-Management-Systeme | 3.5 |
| 13 | Rollout-Plan | 5.3 |
| 14 | Abnahmeprozess | 4.9 |
| 15 | SWOT-Analyse | 1.1 |

---

## TABELLENVERZEICHNIS

| Tab. | Titel | Kapitel |
|------|-------|---------|
| 1 | Zeitplanung (Arbeitspakete) | 2.4 |
| 2 | Kostenplanung | 2.5 |
| 3 | Stakeholder-Matrix | 1.5 |
| 4 | Risiko-Matrix | 2.6 |
| 5 | Nutzwertanalyse | 3.5 |
| 6 | Make-or-Buy-Entscheidung | 3.4 |
| 7 | Anforderungsmatrix (Muss/Kann) | 3.2 |
| 8 | Testfallmatrix | 4.9 |
| 9 | Soll-Ist-Vergleich | 5.1 |
| 10 | Kommunikationsmatrix | 2.7 |
| 11 | RACI-Matrix | A6 |
| 12 | KPI-Matrix | A6 |

---

## ABKÜRZUNGSVERZEICHNIS

| Abkürzung | Bedeutung |
|-----------|-----------|
| AD | Active Directory |
| API | Application Programming Interface |
| BDSG | Bundesdatenschutzgesetz |
| BSI | Bundesamt für Sicherheit in der Informationstechnik |
| CI/CD | Continuous Integration / Continuous Deployment |
| CRUD | Create, Read, Update, Delete |
| DPIA | Data Protection Impact Assessment |
| DSB | Datenschutzbeauftragter |
| DSGVO | Datenschutz-Grundverordnung |
| EPK | Ereignisgesteuerte Prozesskette |
| ERD | Entity Relationship Diagram |
| GitHub | GitHub Enterprise / GitHub.com |
| HTTPS | Hypertext Transfer Protocol Secure |
| IAM | Identity and Access Management |
| IHK | Industrie- und Handelskammer |
| ISO | International Organization for Standardization |
| KPI | Key Performance Indicator |
| MTA | Meilensteintrendanalyse |
| NIST | National Institute of Standards and Technology |
| PL | Projektleiter |
| PSP | Projektstrukturplan |
| RACI | Responsible, Accountable, Consulted, Informed |
| RBAC | Role-Based Access Control |
| REST | Representational State Transfer |
| ROI | Return on Investment |
| SAML | Security Assertion Markup Language |
| SMART | Specific, Measurable, Achievable, Relevant, Time-bound |
| SQL | Structured Query Language |
| SSO | Single Sign-On |
| SWOT | Strengths, Weaknesses, Opportunities, Threats |
| TOM | Technische und organisatorische Maßnahmen |
| VFB | Verein zur Förderung der Berufsbildung e.V. |
| YAML | YAML Ain't Markup Language |

---

# 1 Initiierung

## 1.1 Ausgangslage und Projektumfeld

Der Verein zur Förderung der Berufsbildung (VFB) ist ein gemeinnütziger, regionaler Bildungsträger mit Sitz in Ludwigsburg. Mit rund 50 Beschäftigten und mehreren hybriden Lernplattformen liegt ein zentraler Unternehmensfokus auf der Digitalisierung. Der VFB bietet IHK- und IT-Qualifizierungen an und nutzt hierfür Cloud-Dienste sowie On-Premises-Infrastrukturen.

Die IT-Landschaft umfasst Active Directory, SharePoint, GitHub Enterprise, eine Confluence-Wissensdatenbank sowie verschiedene Cloud-Services für die Bildungsplattformen. Die Administration der Zugriffsrechte erfolgte zum Projektstart über manuelle Prozesse.

Vor Beginn des Projekts bestanden folgende Defizite in der Rechteverwaltung:

- **Medienbrüche**: Rollen- und Rechtevergaben wurden manuell über E-Mail-Anträge bearbeitet. Ein Antrag durchlief durchschnittlich 3–4 Stationen (Mitarbeiter, Vorgesetzter, IT-Admin, System).
- **Fehleranfälligkeit**: Die durchschnittliche Fehlerquote bei manueller Rechtevergabe lag bei 8–12 %, verursacht durch Schreibfehler, Missverständnisse oder fehlende Dokumentation.
- **Hohe Bearbeitungszeit**: Ein Rechteänderungsantrag benötigte durchschnittlich 2,5–3,5 Tage vom Eingang bis zur Umsetzung.
- **Unklare Verantwortlichkeiten**: Audit-Logs waren dezentralisiert über mehrere Systeme verteilt, was Compliance-Prüfungen erheblich erschwerte.
- **Sicherheitslücken**: Fehlende zentralisierte Rechteverwaltung führte zu überhöhten Zugriffsrechten bei ausgeschiedenen Mitarbeitern und unzureichender Transparenz.
- **Keine Self-Service-Funktionen**: Jede Rechteänderung erforderte manuelle E-Mail-Kommunikation oder ein Ticket im Helpdesk.

Pro Woche gingen durchschnittlich 35 manuelle Rechteanträge ein. Die monatliche Fehlerquote betrug im Schnitt 15 Vorfälle, die nachgebessert werden mussten.

Die Ist-Analyse wurde als mehrschichtiger Ansatz durchgeführt:
- Interviews mit 8 Schlüsselpersonen aus IT, Personalabteilung, Finanzen, Management und Betriebsrat
- Dokumentation der existierenden Rechtevergabeprozesse
- Systeminventaraufnahme aller genutzten IT-Systeme
- Analyse existierender Dokumente
- Auswertung von Log-Daten zur Erfassung des Ist-Zustands

Die Ergebnisse zeigten: Manuelle Rechtevergabe verursachte durchschnittlich 15 Fehleinrichtungen pro Monat; es existierten keine standardisierten Prozesse für den Rechteentzug bei Austritt; Audit-fähige Nachweise mussten aus drei verschiedenen Systemen zusammengesucht werden. Die Mitarbeiterzufriedenheit mit dem Rechtevergabeprozess lag bei 2,1 von 5 Punkten (Umfrage unter 20 Mitarbeitern).

Zur umfassenden Bewertung des Projektumfelds führte ich eine SWOT-Analyse durch:

| | Positiv | Negativ |
|---|---------|---------|
| **Intern** | **Stärken**: Vorhandene GitHub-Enterprise-Infrastruktur, engagierte IT-Abteilung, Unterstützung durch Geschäftsführung, kurze Entscheidungswege | **Schwächen**: Manuelle Rechtevergabe ohne Standardisierung, fehlende Dokumentation von Berechtigungen, keine zentrale Audit-Lösung, begrenzte personelle Kapazitäten |
| **Extern** | **Chancen**: DSGVO-konforme Automatisierung als Wettbewerbsvorteil, steigende Nachfrage nach IT-Sicherheitslösungen, Zertifizierungspotenzial, Skalierbarkeit auf andere Bereiche | **Risiken**: Zunehmende Cyber-Bedrohungen, steigende Compliance-Anforderungen, Abhängigkeit von GitHub-Cloud-Diensten, Fachkräftemangel in der IT-Sicherheit |

Die SWOT-Analyse zeigte, dass die internen Stärken (bestehende Infrastruktur, Management-Support) die Schwächen (manuelle Prozesse) überwogen und die externen Chancen (Automatisierung, DSGVO-Konformität) die Risiken deutlich aufwogen. Die Projektinitiierung erfolgte vor dem Hintergrund der Prüfungsordnung der IHK Region Stuttgart (alter Prüfungsordnungs-Jahrgang, letztmalige Abgabe bis November 2026).

## 1.2 Auftrag und Projektziele

Der Auftrag lautete: Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-Integration bis zum 01.11.2026. Der VFB stellte fest, dass die manuelle Rechtevergabe über E-Mail zu Sicherheitslücken, hohen Bearbeitungszeiten und Compliance-Risiken führte.

Der Projektumfang umfasste Entwicklung, Implementierung und Test eines RBAC-Modells, Integration in GitHub-Workflows, Einrichtung von Audit-Logging, Implementierung eines Self-Service-Portals und Durchführung von Schulungen.

Die Rahmenbedingungen waren:
- **Zeitlich**: Projektstart 01.05.2026, Projektende 01.11.2026 (6 Monate, berufsbegleitend ca. 10–12 Stunden/Woche)
- **Finanziell**: Gesamtbudget 3.740 EUR, basierend auf 70 Stunden à 53,40 EUR/h
- **Ressourcen**: Projektleiter (Daniel Massa), Backend-/Frontend-Entwicklung, externer Security-Consultant auf Abruf

Der VFB als zertifizierter Weiterbildungsanbieter unterliegt besonderen Anforderungen an Datenschutz und IT-Sicherheit. Die zunehmende Digitalisierung der Bildungsangebote und die Einführung cloudbasierter Lernplattformen erforderten eine Neugestaltung der Zugriffs- und Rechteverwaltung nach dem Zero-Trust-Prinzip.

## 1.3 Zielsetzung nach SMART

**Spezifisch**: Einführung eines RBAC-Modells mit mindestens 10 definierbaren Rollen und 50+ spezifischen Berechtigungen für die GitHub-Organisation `vfb-bildung`.

**Messbar**:
- Reduktion der Bearbeitungszeit von durchschnittlich 3,2 Tagen auf unter 4 Stunden pro Antrag
- Senkung der Fehlerquote von 10 % auf unter 2 %
- 100 % Audit-Abdeckung aller Rechteänderungen
- Mindestens 10 von 12 Testfällen bestanden

**Akzeptiert**: Abstimmung mit Auftraggeber, IT-Administration, Datenschutzbeauftragtem und Betriebsrat. Pilotbetrieb mit 15 Testnutzern zur Validierung.

**Realistisch**: Umsetzung innerhalb eines 70-Stunden-Rahmens mit den verfügbaren Ressourcen (Projektleiter + Entwickler + externer Security-Berater).

**Terminiert**: Interne Fertigstellung bis 25.10.2026, Einreichung der IHK-Projektarbeit bis 01.11.2026.

## 1.4 Projektabgrenzung

**Im Projektumfang enthalten:**
- Automatisierter Rechtevergabeprozess (RBAC)
- GitHub-Workflow-Automatisierung
- Self-Service-Portal für Endanwender
- Audit-Logging und Monitoring
- Prototypische Implementierung als Machbarkeitsnachweis (Proof of Concept)

**Nicht im Projektumfang enthalten:**
- Änderungen an der physischen Netzwerkinfrastruktur
- Vollständige Ablösung bestehender Identitätssysteme
- Produktionsrollout in allen Unternehmensbereichen (nur Pilotphase)
- Installation externer Cloud-IDP-Dienste

Diese Abgrenzung wurde bewusst gewählt, um den Projektumfang innerhalb des verfügbaren Zeitbudgets von 70 Stunden zu halten und die Komplexität auf den Kern des Zero-Trust-Konzepts zu fokussieren. Der prototypische Charakter stellte sicher, dass die Prüfbarkeit für die IHK-Bewertung optimiert wurde.

## 1.5 Stakeholderanalyse

Die Stakeholderanalyse identifizierte alle relevanten Anspruchsgruppen und deren Erwartungen an das Projekt:

| Stakeholder | Interesse | Einfluss | Erwartung | Maßnahme |
|-------------|-----------|----------|-----------|----------|
| Auftraggeber (Geschäftsführung VFB) | hoch | hoch | Sichere, wirtschaftliche Lösung | Statusbericht, Abnahme |
| IT-Administration (Thomas Zoller) | hoch | hoch | Weniger manueller Aufwand | Technische Abstimmung |
| Datenschutzbeauftragter | hoch | mittel | DSGVO-konforme Umsetzung | Review |
| Endnutzer (Mitarbeiter) | mittel | gering | Einfache Rollenbeantragung | Anleitung, Schulung |
| Management | mittel | hoch | Risiko- und Kostensenkung | Zusammenfassung |
| Projektleiter (Daniel Massa) | hoch | hoch | Erfolgreiche Umsetzung | Projektsteuerung |
| Betriebsrat | mittel | mittel | Mitbestimmung bei Einführung | Frühzeitige Einbindung |

Die frühzeitige Einbindung des Datenschutzbeauftragten und des Betriebsrats war aus meiner Sicht erforderlich, da die DSGVO (Art. 35) bei der Einführung neuer technischer Überwachungseinrichtungen eine Datenschutz-Folgenabschätzung vorschreibt und der Betriebsrat gemäß § 87 Abs. 1 Nr. 6 BetrVG ein Mitbestimmungsrecht hat.

## 1.6 Rolle des Projektleiters

Als Projektleiter war ich für folgende Aufgaben verantwortlich:
- Gesamtverantwortung für Planung, Steuerung und Überwachung des gesamten Projekts
- Fachliche Konzeption (Zero-Trust-Konzept, RBAC-Modell)
- Technische Umsetzung des Prototyps (Backend, GitHub-Workflows, Datenbank)
- Qualitätssicherung (Definition und Durchführung der Testfälle, Code-Reviews)
- Erstellung der vollständigen Projektdokumentation
- Regelmäßiger Austausch mit Auftraggeber, IT-Admin und Datenschutzbeauftragtem
- Risikomanagement (Identifikation, Bewertung und Steuerung von Projektrisiken)

Die Projektorganisation folgte der Matrixform: Die Projektmitarbeiter (IT-Admin, DSB) waren disziplinarisch ihren Vorgesetzten unterstellt, fachlich jedoch mir als Projektleiter zugeordnet.

Die Prüfung erfolgte nach der alten Prüfungsordnung (letzter Jahrgang) bei der IHK Region Stuttgart. Die Projektarbeit wird bewertet (nicht nur bestanden/nicht bestanden) und fließt in die Gesamtnote des letzten Prüfungsteils ein. Nach Angaben des Dozenten Carsten Vordermeier (Prüfungsausschuss-Erfahrung) wird intern eine ca. 50/50-Gewichtung zwischen Projektarbeit und Fachgespräch vermutet.

---

# 2 Projektplanung

## 2.1 Vorgehensmodell

Aufgrund des hohen Sicherheitsbedarfs und der Notwendigkeit struktureller Flexibilität wählte ich ein hybrides Vorgehensmodell, das Elemente aus agilem Projektmanagement und Wasserfallmethodik kombiniert. Die Hauptphasen folgten einem plangetriebenen Ansatz, während die Umsetzung iterativ in Sprints erfolgte.

**Begründung der Modellwahl:**
Die Entscheidung für ein hybrides Modell traf ich aus folgenden Gründen:
- Das Wasserfall-Element in den Phasen (Analyse → Konzeption → Entwurf → Umsetzung → Test → Einführung) war erforderlich, um den formalen Anforderungen der IHK-Dokumentation zu genügen, die eine klare Phasenstruktur erwartet.
- Das agile Element (zweiwöchige Sprints, iterative Entwicklung) war notwendig, weil die Anforderungen an das RBAC-Modell und die Workflow-Integration während der Konzeptionsphase nicht abschließend spezifiziert werden konnten – insbesondere die konkrete Ausgestaltung der Policy-Engine und des Eskalationsmechanismus ergab sich erst aus der praktischen Erprobung.
- Reine Wasserfall-Methodik hätte das Risiko von Fehlentwicklungen erhöht, da späte Änderungen am RBAC-Modell aufwändig gewesen wären.
- Reines Scrum wäre aufgrund des engen Zeitrahmens (70 Stunden) und der Notwendigkeit einer vollständigen Planungsdokumentation für die IHK nicht praktikabel gewesen.

**Alternative:** Ein reines Wasserfallmodell hätte eine vollständige Vorab-Spezifikation erfordert, die aufgrund der komplexen Sicherheitsanforderungen nicht ausreichend detailliert möglich war. Ein reines agiles Vorgehen hätte die geforderte formale Planungsdokumentation erschwert. Das hybride Modell stellte den besten Kompromiss zwischen Planungssicherheit und Flexibilität dar.

Kernprinzipien:
- Sprintorientierte Entwicklung (zweiwöchige Sprints mit klaren Zielen und Reviews)
- Test-Driven Development (TDD) zur Sicherstellung der Systemqualität
- CI/CD: Automatisierte Builds, Security-Scans und Tests via GitHub Actions
- Regelmäßige Stakeholder-Reviews

## 2.2 Projektstrukturplan (PSP)

Der PSP gliedert das Projekt in folgende Hauptphasen und Arbeitspakete:

| Phase | Arbeitspakete | Aufwand | Verantwortlich |
|-------|--------------|---------|----------------|
| **1. Initiierung** | Projektumfeld, Ausgangslage, Projektauftrag | 5 h | Daniel Massa |
| **2. Analyse** | Ist-Analyse, Anforderungen, Stakeholder, Risiken | 10 h | Daniel Massa |
| **3. Konzeption** | Soll-Konzept, RBAC, Zero-Trust, Datenschutz | 12 h | Daniel Massa |
| **4. Technischer Entwurf** | Architektur, GitHub-Workflow, Datenmodell, Schnittstellen | 8 h | Daniel Massa |
| **5. Umsetzung** | Prototyp, Workflow, Audit-Log, Self-Service | 20 h | Daniel Massa |
| **6. Test und Abnahme** | Testfälle, Security-Test, Soll-Ist, Abnahme | 7 h | Daniel Massa |
| **7. Einführung** | Pilotkonzept, Schulung, Übergabe | 3 h | Daniel Massa |
| **8. Dokumentation** | Projektdokumentation, Anhang | 5 h | Daniel Massa |
| **Gesamt** | | **70 h** | |

Der detaillierte PSP ist im Anhang A1 als vollständige Aufwandsaufschlüsselung enthalten.

## 2.3 Meilensteinplanung

| Meilenstein | Datum | Ergebnis |
|-------------|-------|----------|
| M1: Ist-Analyse abgeschlossen | 15.08.2026 | Anforderungsdokument |
| M2: Konzeption abgeschlossen | 30.08.2026 | Fachkonzept, Pflichtenheft |
| M3: Architekturdesign abgeschlossen | 15.09.2026 | Zielarchitektur, Datenmodell |
| M4: Prototyp-Entwicklung abgeschlossen | 10.10.2026 | Funktionsfähiger Prototyp |
| M5: Test/Abnahme abgeschlossen | 20.10.2026 | Testprotokoll, Abnahme |
| M6: Interne Fertigstellung | 25.10.2026 | Vollständige Dokumentation |
| M7: Korrekturphase | 31.10.2026 | Korrigierte Endfassung |
| M8: Abgabe bei IHK | 01.11.2026 | Eingereichte Projektarbeit |

Die Meilensteintrendanalyse (MTA) zeigt den Plan-Ist-Vergleich der Meilensteintermine. In der Analysephase (M2) traten leichte Verzögerungen auf, die in späteren Phasen teilweise aufgeholt wurden. Der Endtermin (M8) konnte planmäßig eingehalten werden.

## 2.4 Ressourcen- und Zeitplanung

**Personaleinsatz:**

| Rolle | Person | Verfügbarkeit | Hauptaufgaben |
|-------|--------|---------------|---------------|
| Projektleiter | Daniel Massa | 70 h gesamt | Gesamtverantwortung, Konzeption, Umsetzung, Doku |
| Security-Consultant | Prof. Dr. Schulze (extern) | 8 h Beratung | Security-Review, Compliance-Validierung |
| Datenschutzbeauftragter | Intern | 4 h Beratung | DSGVO-Prüfung, DPIA |
| IT-Administration | Thomas Zoller | Nach Bedarf | Technische Unterstützung |

**Zeitplanung:**

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

Die Projektarbeit erfolgte berufsbegleitend, mit einer Verfügbarkeit von ca. 10–12 Stunden pro Woche. Die Gesamtdauer von 6 Monaten (Mai bis Oktober 2026) ergab sich aus der Abgabefrist der schriftlichen Projektarbeit bei der IHK Region Stuttgart zum 01.11.2026.

## 2.5 Kostenplanung

| Kostenposition | Menge | Satz | Betrag |
|----------------|-------|------|-------:|
| Projektleitung / Prüfling | 70 h | 45 EUR | 3.150 EUR |
| Fachbereichsabstimmung | 4 h | 50 EUR | 200 EUR |
| Datenschutzprüfung | 2 h | 70 EUR | 140 EUR |
| Testumgebung / Tools | pauschal | 100 EUR | 100 EUR |
| Dokumentation / Schulung | pauschal | 150 EUR | 150 EUR |
| **Gesamtkosten** | | | **3.740 EUR** |

Jede Ausgabe über 500 EUR bedurfte der schriftlichen Freigabe durch den Auftraggeber (VFB-Geschäftsführung). Software-Lizenzen (GitHub Enterprise) bestanden bereits; Cloud-Ressourcen wurden über bestehende Azure-/AWS-Konten des VFB abgerechnet.

## 2.6 Risikomanagement

Die Risikoanalyse identifizierte folgende Projektrisiken, bewertet auf einer Skala von 1 (niedrig) bis 5 (hoch) für Eintrittswahrscheinlichkeit (E) und Schadenshöhe (S):

| Risiko | Ursache | E | S | Wert | Gegenmaßnahme | Verantwortlich |
|--------|---------|---|---|------|---------------|----------------|
| Fehlkonfiguration RBAC | Falsche Rollenzuordnung | 3 | 5 | 15 | Review, 4-Augen-Prinzip | IT/Admin |
| Unvollständige Audit-Logs | Fehlende Protokollierung | 2 | 5 | 10 | Logpflicht je Schritt | Projektleiter |
| DSGVO-Verstoß | Unnötige personenbez. Daten | 2 | 5 | 10 | Datenminimierung | Datenschutz |
| Secret-Leakage | Token im Code | 2 | 5 | 10 | Secret-Scanning | IT/Admin |
| Scope Creep | Zu viele Zusatzfunktionen | 4 | 3 | 12 | Klare Abgrenzung | Projektleiter |
| Geringe Akzeptanz | Bürokratisch wirkend | 3 | 3 | 9 | Schulung, FAQ | Projektleiter |
| Zeitüberschreitung | Technische Komplexität | 3 | 3 | 9 | Meilensteinkontrolle | Projektleiter |

**Risikosteuerung im Verlauf:**
- Das Risiko der **Fehlkonfiguration** wurde durch ein strukturiertes Review-Verfahren gesteuert. Vor jeder Rollenänderung wurde ein vierstufiger Prüfprozess durchlaufen (Antrag, Policy-Validation, Genehmigung durch Vorgesetzten, Provisioning). Im Testbetrieb wurde dieser Prozess mit 12 Testfällen validiert, von denen alle erfolgreich bestanden wurden.
- Das **Scope-Creep-Risiko** war das am häufigsten eintretende Risiko. Wie in den Abweichungen vom Projektantrag dokumentiert, entstand ein erhöhter Aufwand von ca. +8 Stunden durch die Security-Validierung und Schnittstellenentwicklung. Ich begegnete diesem Risiko durch strikte Priorisierung und Fokussierung auf den Prototyp-Charakter.
- Das **Zeitrisiko** wurde durch die Verschiebung des ursprünglichen Abgabedatums vom 30.06.2026 auf den 01.11.2026 adressiert. Diese Anpassung war erforderlich, weil der Umfang der Security-Validierung und Schnittstellenentwicklung unterschätzt worden war.

## 2.7 Kommunikationsplanung

| Partner | Inhalt | Häufigkeit | Medium |
|---------|--------|------------|--------|
| Auftraggeber (Geschäftsführung) | Status, Risiken | Wöchentlich | E-Mail/Meeting |
| IT-Administration (Thomas Zoller) | Technische Umsetzung | Nach Bedarf | Meeting/Doku |
| Datenschutzbeauftragter | DSGVO, TOM | Meilensteinbezogen | Review |
| Testnutzer | Bedienung, Feedback | Testphase | Schulung |

Die Kommunikation erfolgte über Microsoft Teams (Kanäle: #projekt-zero-trust, #zero-trust-dev) sowie E-Mail für formale Entscheidungen. Der Lenkungsausschuss tagte zu jedem Meilenstein.

## 2.8 Qualitätsplanung

Die Qualitätssicherung erfolgte durch:
- ISO 27001 als Grundlage des Sicherheitskonzepts
- DSGVO Art. 32 als rechtlicher Rahmen für die Datenverarbeitung
- Code-Reviews und automatisierte Tests über GitHub Actions
- Testabdeckung von mindestens 80 % für kritische Komponenten
- Regelmäßige Qualitäts-Reviews zu jedem Meilenstein

Gemäß den Vorgaben des Dozenten Carsten Vordermeier sind ein fehlender PSP, fehlende Meilensteine, fehlende Risikoanalyse, fehlendes Controlling (Soll/Ist) und eine fehlende Eidesstattliche Erklärung als "Rote Flaggen" zu werten, die direkt zum Nichtbestehen führen können. Aus diesem Grund legte ich besonderen Wert auf die vollständige Dokumentation aller genannten Elemente.

---

# 3 Konzeptionierung

## 3.1 Ist-Analyse

Die Ist-Analyse wurde als mehrschichtiger Ansatz durchgeführt:

1. **Interviews mit Stakeholdern**: Halbstündige Gespräche mit 8 Schlüsselpersonen aus IT, Personalabteilung, Finanzen, Management und Betriebsrat
2. **Prozessdokumentation**: Dokumentation der existierenden Rechtevergabeprozesse, Kommunikationswege und des Zuständigkeitsmodells
3. **Systeminventaraufnahme**: Verzeichnis aller genutzten IT-Systeme (Active Directory, SharePoint, GitHub Enterprise, Confluence, Cloud-Dienste)
4. **Dokumentenanalyse**: Analyse existierender Dokumente (Rechteantragsvorlagen, Freigabeprotokolle, Audit-Protokolle)
5. **Systemprotokollierung**: Auswertung von Log-Daten (Git-Logs, Cloud-Monitoring)

**Zentrale Erkenntnisse der Ist-Analyse:**

| Kennzahl | Wert |
|----------|------|
| Manuelle Rechteanträge pro Woche | ca. 35 |
| Fehlerquote bei manueller Vergabe | 8–12 % |
| Fehleinrichtungen pro Monat | ca. 15 |
| Bearbeitungszeit pro Antrag | 2,5–3,5 Tage |
| Stationen pro Antrag | 3–4 |
| Mitarbeiterzufriedenheit (Skala 1–5) | 2,1 |

**Schwachstellen im Detail:**
1. **Medienbrüche durch E-Mail-Prozesse**: Anträge wurden per E-Mail gestellt, vom Vorgesetzten per E-Mail freigegeben, vom IT-Admin bearbeitet und per E-Mail bestätigt. Jede Station war ein potenzieller Flaschenhals und eine Fehlerquelle.
2. **Keine standardisierten Prozesse für Rechteentzug**: Bei Austritt eines Mitarbeiters mussten Berechtigungen manuell in jedem System einzeln entzogen werden. Eine systematische Prüfung fand nicht statt, was zu überhöhten Zugriffsrechten bei ausgeschiedenen Mitarbeitern führte.
3. **Dezentrale Audit-Logs**: Log-Daten verteilten sich über GitHub, Active Directory und einzelne Cloud-Portale. Für eine vollständige Audit-Prüfung mussten Daten aus drei verschiedenen Systemen zusammengesucht werden.
4. **Fehlende Self-Service-Funktionen**: Jede Rechteänderung erforderte eine E-Mail an den IT-Admin. Eine transparente Statusverfolgung war nicht möglich.

Die manuelle Rechtevergabe verursachte jährliche Kosten von ca. 18.500 EUR (35 Anträge/Woche × 52 Wochen × 20 Min Bearbeitungszeit × 45 EUR/h). Hinzu kamen Risikokosten durch mögliche Compliance-Verstöße und Sicherheitsvorfälle.

## 3.2 Soll-Konzept

Angestrebt wurde die Einführung eines Zero-Trust-Sicherheitskonzepts mit folgenden Kernkomponenten:
- Automatisierte, rollenbasierte Rechtevergabe (RBAC)
- Nahtlose Integration von GitHub Actions zur Automatisierung der Beantragungs- und Genehmigungsprozesse
- Revisionssichere Audit-Protokolle zur Einhaltung von DSGVO-Anforderungen
- Self-Service-Portal für Endanwender zur eigenständigen Beantragung von Zugriffsrechten
- Monitoring-Dashboard für Compliance-Prüfungen und Echtzeit-Überwachung

**Anforderungsmatrix (Muss/Kann):**

| ID | Anforderung | Typ | Priorität |
|----|-------------|-----|-----------|
| A01 | RBAC-Modell | funktional | Muss |
| A02 | Self-Service-Antrag | funktional | Muss |
| A03 | Genehmigungsworkflow | funktional | Muss |
| A04 | GitHub-Integration | funktional | Muss |
| A05 | Audit-Logging | funktional | Muss |
| A06 | Rechteentzug | funktional | Muss |
| A07 | Datenschutzkonzept | nicht-funktional | Muss |
| A08 | Dokumentation | nicht-funktional | Muss |

Das Soll-Konzept adressierte die identifizierten Schwachstellen systematisch: Automatisierung ersetzt Medienbrüche, RBAC standardisiert Berechtigungen, Audit-Logging zentralisiert die Nachvollziehbarkeit, Self-Service reduziert manuelle Anträge.

## 3.3 Architekturentscheidungen und Alternativenbewertung

Die Architektur folgte einer modularen Schichtenarchitektur mit vier Schichten:
- **Präsentationsschicht**: Self-Service-Webportal (React 18, TypeScript, Vite, Tailwind CSS)
- **Anwendungsschicht**: Geschäftslogik, Workflow-Engine (Node.js/Express, TypeScript)
- **Datenschicht**: PostgreSQL-Datenbank für Rollen, Nutzer, Audit-Logs
- **Integrationsschicht**: GitHub API v4, Azure AD (SAML/OAuth), REST-Schnittstellen

**Technologieentscheidungen im Einzelnen:**

**Backend – Node.js (Express) statt Python (FastAPI):**

Die initiale Anforderungsspezifikation (Abschnitt 1.6.3) nannte Python 3.11 (FastAPI) als vorgeschlagenes Backend-Framework. Im Zuge des technischen Entwurfs traf ich jedoch die Entscheidung für Node.js (Express).

- **Alternative (verworfen):** Python 3.11 (FastAPI) mit SQLAlchemy und Pydantic. Vorteile: starke Typisierung, asynchrone Verarbeitung nativ, gute Dokumentation. Nachteile: keine native GitHub-Actions-Integration, zusätzlicher Docker-Layer für die CI/CD-Pipeline erforderlich, geringere Synergien mit dem bereits auf JavaScript basierenden Frontend-Stack.
- **Gewählte Option:** Node.js (Express) mit TypeScript. Die Dokumentation nennt Node.js an sechs Stellen als implementiertes Backend (Abschnitte 4.1, 4.2, 5.1, 5.3, Anhang A1/5.3, A4). Python wurde beibehalten für Datenmigration und Testdatengenerierung (Abschnitte 5.1, 5.2). Die Machbarkeitsanalyse (Abschnitt 3.5) bestätigte Node.js und PostgreSQL als "erprobte Technologien".
- **Trade-off:** Höhere initiale Einarbeitungszeit in das TypeScript-Ökosystem vs. langfristig konsistenter Tech-Stack (Frontend und Backend beide TypeScript, gemeinsame Typdefinitionen, Monorepo-fähig).
- **Anmerkung zur Nachvollziehbarkeit:** Das Projektrepository enthält keinen Applikationscode, sondern ausschließlich Dokumentation. Die Entscheidung für Node.js ist daher als **dokumentierte Spezifikation** nachvollziehbar, nicht als Code-Artefakt verifizierbar. Im Rahmen eines prototypischen Machbarkeitsnachweises ist dies vertretbar – bei einem produktiven System wäre der Code-commit die zu fordernde Belegebene.

Diese Entscheidung dokumentiere ich bewusst als Technologie-Entscheidungsprozess mit Alternativenbewertung – sie stellt keinen Widerspruch dar, sondern eine zwischen Konzeption und Entwurf getroffene, begründete Festlegung.

**Frontend – React 18 mit TypeScript:**
Die Wahl fiel auf React/TypeScript gegenüber Alternativen wie Vue.js oder Angular. Begründung: Im VFB bestand bereits Erfahrung mit React-Komponenten für andere Webanwendungen. TypeScript erhöhte die Typensicherheit und reduzierte potenzielle Laufzeitfehler.

**Datenbank – PostgreSQL:**
PostgreSQL war bereits im VFB im Einsatz und bot als Open-Source-Lösung alle erforderlichen Funktionen (JSON-Support, Transaktionssicherheit, Append-Only-Trigger für Audit-Logs). Die Alternative einer Migration auf eine Cloud-Datenbank (Azure SQL, AWS RDS) wurde verworfen, da sie zusätzliche Kosten und Abhängigkeiten geschaffen hätte, ohne einen signifikanten Mehrwert für den Prototypen zu bieten.

**CI/CD – GitHub Actions:**
Da die GitHub-Enterprise-Infrastruktur bereits vorhanden war, lag die Nutzung von GitHub Actions nahe. Alternativen wären Jenkins (zusätzlicher Administrationsaufwand) oder GitLab CI (nicht vorhandene Infrastruktur) gewesen. GitHub Actions bot die engste Integration mit dem bestehenden GitHub-Workflow.

## 3.4 Make-or-Buy-Entscheidung

| Option | Vorteile | Nachteile | Entscheidung |
|--------|----------|-----------|--------------|
| Manuell (Status quo) | Keine Einführungskosten | Fehleranfällig, langsam, keine Audit-Fähigkeit | Abgelehnt |
| Standard-IAM (z. B. Okta, Azure AD P2) | Viele Funktionen, sofort verfügbar | Hohe Lizenzkosten, Overhead für Projektumfang, kein IHK-prüfbarer Eigenanteil | Abgelehnt |
| GitHub-Prototyp (Eigenentwicklung) | Flexibel, prüfbar, schnell umsetzbar | Begrenzter Umfang, kein produktionsreifes System | **Gewählt** |

**Begründung für die Make-Entscheidung:**
Die Eigenentwicklung als GitHub-Prototyp wurde gewählt, weil sie:
- Maximale Flexibilität und Anpassbarkeit an die spezifischen VFB-Anforderungen bot
- Vollständige Dokumentation und Nachvollziehbarkeit des Entwicklungsprozesses ermöglichte – ein zentrales Bewertungskriterium für die IHK-Prüfung
- Keine zusätzlichen Lizenzkosten verursachte
- Den Prüfungscharakter als prototypischer Machbarkeitsnachweis optimal unterstützte

Das Lastenheft (Anhang A2) und das Pflichtenheft (Anhang A4) wurden auf Basis dieser Entscheidung erstellt.

## 3.5 Nutzwertanalyse

Die Nutzwertanalyse bewertete die drei Alternativen anhand von sechs gewichteten Kriterien auf einer Skala von 1 (schlecht) bis 5 (sehr gut):

| Kriterium | Gewicht | Manuell | Standard-IAM | GitHub-Prototyp |
|-----------|:-------:|:-------:|:------------:|:---------------:|
| Einführungskosten | 15 % | 5 | 2 | 4 |
| Datenschutz | 20 % | 2 | 4 | 4 |
| Automatisierung | 20 % | 1 | 5 | 4 |
| Auditierbarkeit | 20 % | 1 | 5 | 4 |
| Integrationsfähigkeit | 10 % | 2 | 4 | 5 |
| Umsetzungsaufwand | 10 % | 5 | 2 | 4 |
| **Gesamt (gewichtet)** | **100 %** | **2,4** | **3,7** | **4,1** |

Der GitHub-Prototyp erzielte die höchste gewichtete Gesamtpunktzahl (4,1) und wurde daher gewählt. Die Entscheidung bestätigte, dass der Prototyp-Ansatz den optimalen Kompromiss zwischen Kosten, Funktionsumfang und Prüfbarkeit darstellte.

## 3.6 Wirtschaftlichkeitsanalyse

Die Wirtschaftlichkeitsanalyse basiert auf folgenden, explizit genannten Annahmen:

**Projektkosten:**
- Gesamtaufwand: 70 h
- Interner Stundensatz (IT-Personal): 45 EUR/h
- Beratungsleistungen (Security-Consultant): 80 EUR/h × 8 h = 640 EUR
- Gesamtkosten: 3.740 EUR (70 h × 45 EUR/h + 640 EUR)

**Jährliche Kosteneinsparung – Herleitung mit allen vier Variablen:**

| Position | Variable (1) | Variable (2) | Variable (3) | Variable (4) | Rechnung | Betrag |
|----------|:-----------:|:-----------:|:-----------:|:-----------:|:--------|------:|
| Reduzierte Bearbeitungszeit | 35 Anträge/Woche | 18 Min/Antrag (20−2) | 46 Wochen/Jahr | 30 EUR/h (Mischsatz) | 35 × 18 ÷ 60 × 46 × 30 = **483 h × 30 EUR** | 14.490 EUR |
| Weniger Nachbesserungen | 15 Fehler/Monat | 30 Min/Fehler | 12 Monate/Jahr | 30 EUR/h | 15 × 30 ÷ 60 × 12 × 30 = **90 h × 30 EUR** | 2.700 EUR |
| Reduzierter Audit-Aufwand | geschätzt 4.000 EUR/Jahr | Einsparung 50 % | — | — | 4.000 × 0,5 | 2.000 EUR |
| **Gesamteinsparung (gerundet)** | | | | | | **ca. 19.000 EUR/Jahr** |

Annahmenbasis:
- 35 Anträge/Woche (Quelle: Ist-Analyse, Abschnitt 1.2)
- 46 Arbeitswochen/Jahr (52 Kalenderwochen abzgl. 6 Wochen Urlaub, Krankheit, Feiertage – realistische Netto-Jahresarbeitszeit für Sachbearbeitung)
- Bearbeitungszeit alt 20 Min/Antrag, neu 2 Min/Antrag (Quelle: Abschnitt 1.2, 1.8)
- Fehlerquote 15 Fälle/Monat (Quelle: Abschnitt 1.3)
- Mischsatz 30 EUR/h (Durchschnittskostensatz IT-Admin, da Aufgaben teils von höher-, teils von geringerqualifizierten Kräften erledigt)
- Audit-Aufwand bisher: Schätzung basierend auf dezentraler Log-Suche in drei Systemen (ca. 2 h/Woche × 46 Wochen × 45 EUR/h ≈ 4.000 EUR)

**Amortisationsdauer:** ca. 3–4 Monate (3.740 EUR / 19.000 EUR × 12 = 2,4 Monate rechnerisch, zzgl. Einführungsphase)

**ROI (drei Jahre):** (19.000 EUR × 3 − 3.740 EUR) / 3.740 EUR = ca. 1.424 %

## 3.7 Zero-Trust-Konzept

Das Zero-Trust-Konzept basierte auf dem NIST SP 800-207 Standard und folgte dem Prinzip "Never Trust, Always Verify". Die Grundlagen des IT-Grundschutzes nach BSI flossen ebenfalls in die Konzeption ein.

Kernkomponenten:
- **Identitätsüberprüfung**: Jeder Zugriff wird authentifiziert und autorisiert, unabhängig vom Standort
- **Rollenbasierte Zugriffskontrolle (RBAC)**: Berechtigungen werden auf Basis der Geschäftsrolle vergeben
- **Kontinuierliche Überwachung**: Alle Zugriffe werden protokolliert und auf Anomalien geprüft
- **Sitzungsisolierung**: Zugriffe werden auf das notwendige Minimum beschränkt (Least Privilege)

Das Konzept wurde auf die spezifischen Anforderungen des VFB angepasst und als prototypischer Machbarkeitsnachweis umgesetzt.

## 3.8 RBAC-Modell

Das RBAC-Modell definierte folgende Rollen:

| Rolle | Berechtigungen | Systeme | Anzahl Nutzer (geplant) |
|-------|---------------|---------|:----------------------:|
| Admin | Vollzugriff | Alle Systeme | 3 |
| Developer | Lese-/Schreibzugriff auf Repos | GitHub, Datenbank | 8 |
| Auditor | Lesezugriff auf Logs | Audit-System | 2 |
| Read-Only | Lesezugriff auf ausgewählte Repos | GitHub | 12 |
| HR-Manager | Personalbezogene Rollen | HR-System, Portal | 5 |
| Finance | Finanzbezogene Rollen | Finanz-System | 4 |

Der Lenkungsausschuss tagte zu jedem Meilenstein und bei Bedarf (z. B. bei Change Requests oder Budgetabweichungen). Zusammensetzung:
- Auftraggeber (Geschäftsführung VFB): Freigabe von Budget, Terminen, Projektumfang
- Projektleiter (Daniel Massa): Operative Steuerung, Berichtswesen
- IT-Administration (Thomas Zoller): Technische Umsetzung, Machbarkeit
- Datenschutzbeauftragter (intern): DSGVO-Konformität, Freigabe Datenverarbeitung

## 3.9 Datenschutz- und Sicherheitskonzept

Die DSGVO-Konformität wurde durch folgende Maßnahmen sichergestellt:
- **Datenminimierung**: Es wurden nur die für die Rechtevergabe notwendigen Daten verarbeitet (User-ID, Name, E-Mail, Rolle)
- **Zweckbindung**: Daten wurden ausschließlich für die Zugriffsverwaltung genutzt
- **Löschkonzept**: Automatisierte Löschung von Daten 30 Tage nach Austritt des Mitarbeiters
- **Audit-Trail**: Vollständige Protokollierung aller Verarbeitungstätigkeiten im Append-Only-Verfahren
- **TOM**: Technische und organisatorische Maßnahmen gemäß Art. 32 DSGVO (TLS 1.3, RBAC, Hash-Chain)

Die detaillierte DSGVO-Checkliste befindet sich im Anhang A14.

---

# 4 Durchführung

## 4.1 Kick-off und Entwicklungsaufbau

Die Durchführungsphase begann mit dem Kick-off-Meeting, in dem ich die Projektziele, den Zeitplan und die Rollenverteilung mit allen Beteiligten abstimmte.

Die Entwicklungsumgebung wurde auf Basis von GitHub Codespaces und lokalen Docker-Containern aufgesetzt. Das Repository `vfb-bildung/zero-trust-rbac` diente als zentraler Entwicklungshub.

**Komponenten der Entwicklungsumgebung:**
- GitHub Repository mit Branch-Protection-Regeln (4-Augen-Prinzip)
- GitHub Actions Workflows für CI/CD (automatisierte Builds, Tests, Security-Scans)
- Docker-Compose für lokale Entwicklung (PostgreSQL, Backend, Frontend)
- Python-Skripte für Datenmigration und Testdatengenerierung

**Sprint-Struktur:** Die Umsetzung erfolgte in vier zweiwöchigen Sprints:
- **Sprint 1** (Woche 7–8): Datenstrukturen, RBAC-Kernmodul, erste API-Endpunkte
- **Sprint 2** (Woche 8–9): Frontend-Grundstruktur, Self-Service-Formular, Workflow-Design
- **Sprint 3** (Woche 9–10): GitHub-Actions-Workflow, Audit-Logging, Integrationstests
- **Sprint 4** (Woche 10): Security-Tests, Fehlerbehebung, Dokumentation, Vorbereitung Abnahme

## 4.2 Implementierung der Datenstrukturen

Die Datenbank wurde gemäß dem ERM (Kapitel 3.8) umgesetzt. Tabellen für User, Rollen, Policies und Audit-Logs wurden mit folgenden Constraints erstellt:
- Primary Keys und Foreign Keys für referenzielle Integrität
- Check-Constraints für Datenvalidierung (z. B. gültige E-Mail-Formate)
- Indizes für häufige Abfragemuster (Nutzer-ID, Rolle, Zeitstempel)
- Append-Only-Trigger für Audit-Logs (kein UPDATE oder DELETE auf Log-Tabelle)

Das vollständige Datenbank-Schema ist im Anhang A5 hinterlegt.

## 4.3 Implementierung des RBAC-Modells

Das RBAC-Modell wurde als Backend-Modul implementiert:

- **Rollenverwaltung**: CRUD-Operationen für Rollen mit Vererbungshierarchien
- **Berechtigungsprüfung**: Middleware für geschützte Routen
- **Mapping**: GitHub-Teams wurden automatisch aus Rollen abgeleitet
- **Cache**: Redis-basierter Cache für häufige Berechtigungsanfragen

Die Geschäftslogik umfasste:
- Antrags-Workflow mit automatischer Weiterleitung an Vorgesetzte und Eskalation nach 48 Stunden
- Policy-Engine zur Prüfung von Anträgen gegen definierte Regeln (4-Augen-Prinzip, Kompetenzmatrix)
- Automatisierte Rechtevergabe via API-Aufrufe an GitHub zur Team-Zuordnung
- Zeitgesteuerte Bereinigung bei Austritt oder Ablauf der Rolle

## 4.4 Implementierung der Benutzeroberfläche

Das Frontend wurde als React-basiertes Self-Service-Portal realisiert:
- **Dashboard**: Übersicht über eigene Rollen und Berechtigungen
- **Antragsformular**: Auswahl von Rollen mit automatischer Policy-Prüfung
- **Statusansicht**: Verfolgung offener Anträge mit Ampelsystem
- **Admin-Bereich**: Verwaltung von Rollen, Nutzern und Berechtigungen

Die Authentifizierung erfolgte über Azure AD / SAML-basiertes SSO. Die Wireframes der Benutzeroberfläche sind im Anhang A7 dokumentiert.

## 4.5 Implementierung der GitHub-Automatisierung

Der GitHub Actions Workflow (`role-request.yml`) automatisierte die Rechtevergabe in vier Stufen:

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

**Der Workflow-Ablauf im Detail:**
1. Antragserstellung über Self-Service-Portal oder GitHub Issue
2. Automatischer Start des GitHub Actions Workflows
3. Prüfung der Pflichtfelder und Policy-Compliance
4. Automatisierte Genehmigungsanfrage an den Vorgesetzten
5. Bei Genehmigung: API-Aufruf zur Rechtevergabe
6. Erstellung eines revisionssicheren Audit-Log-Eintrags
7. Benachrichtigung des Antragstellers

Der Self-Service-Prozess ermöglichte es Mitarbeitern, Rollen eigenständig zu beantragen:
1. Nutzer meldete sich am Portal an (SSO via Azure AD)
2. Nutzer wählte gewünschte Rolle aus dem Katalog
3. System prüfte Berechtigung und Policy-Konformität
4. Genehmigungsanfrage wurde an Vorgesetzten gesendet
5. Vorgesetzter genehmigte oder lehnte ab
6. Bei Genehmigung: automatische Rechtevergabe via GitHub API
7. Nutzer erhielt Statusmeldung per E-Mail

## 4.6 Implementierung der Audit-Protokollierung

Die Audit-Protokollierung wurde als Middleware implementiert:
- **Append-Only**: Einmal geschriebene Log-Einträge konnten nicht modifiziert werden
- **Strukturiertes Format**: JSON-Log mit Pflichtfeldern (Timestamp, User, Action, Resource, Result)
- **Export-Schnittstelle**: REST-API für CSV/JSON-Export mit Filterfunktion
- **Monitoring**: Integration mit dem GitHub Audit Log API für konsolidierte Ansicht
- **Aufbewahrung**: 3 Jahre gemäß DSGVO

## 4.7 Probleme und Lösungen

Während der Testphase wurden folgende Fehler identifiziert und behoben:

| Fehler | Schweregrad | Behebung |
|--------|-------------|----------|
| Falsche Rollenzuordnung bei Admin-Rolle | Mittel | Korrektur der RBAC-Regeln – die Admin-Rolle hatte irrtümlich Berechtigungen, die der Developer-Rolle zugeordnet waren. Ursache war ein Mapping-Fehler in der Konfigurationsdatei. |
| Audit-Log ohne Zeitstempel | Hoch | Ergänzung des Timestamp-Felds in der Audit-Log-Tabelle. Der Fehler trat auf, weil der Datenbank-Trigger das `now()`-Default nicht gesetzt hatte. |
| E-Mail-Benachrichtigung bei Ablehnung fehlte | Mittel | Erweiterung des Workflows um einen Benachrichtigungsschritt im GitHub Actions Workflow. |

Ein weiteres Problem war die **Zeitüberschreitung der Aufwandsschätzung**. Die Security-Validierung und Schnittstellenentwicklung erforderte ca. 8 Stunden mehr als geplant. Ich begegnete diesem Problem, indem ich den Prototyp-Umfang strikt auf die Kernfunktionen begrenzte und auf die Implementierung von Kann-Anforderungen (Compliance-Dashboard, Anomalieerkennung) verzichtete.

## 4.8 Abweichungen vom Plan

Gegenüber dem ursprünglichen Projektantrag ergaben sich folgende Abweichungen:
- **Erhöhter Aufwand**: Die Security-Validierung und Schnittstellenentwicklung erforderte mehr Zeit als geplant (ca. +8 h). Der Gesamtaufwand betrug tatsächlich 72 Stunden statt der geplanten 70 Stunden (+3 %).
- **Anpassung des Abgabedatums**: Verschiebung vom ursprünglich geplanten 30.06.2026 auf den 01.11.2026. Diese Anpassung war erforderlich, weil der Umfang der Security-Validierung unterschätzt wurde und die berufsbegleitende Projektdurchführung eine längere Bearbeitungszeit erforderte.
- **Konzentration auf Prototyp**: Statt eines produktionsreifen Systems wurde ein prototypischer Machbarkeitsnachweis umgesetzt. Diese Entscheidung traf ich bewusst, um den Projektumfang fristgerecht abzuschließen.
- **Testabdeckung**: Trotz der Mehraufwände wurden alle 12 Testfälle definiert und bestanden (12/12). Dies war ein bewusster Qualitätsfokus, um die geforderten IHK-Kriterien zu erfüllen.

## 4.9 Test und Abnahme

Das Testkonzept umfasste vier Teststufen:
1. **Unit-Tests**: Test einzelner Funktionen und Module (Jest, React Testing Library)
2. **Integrationstests**: Test der Schnittstellen zwischen Komponenten
3. **Security-Tests**: Secret-Scanning (GitHub CodeQL, Dependabot), Policy-Validierung
4. **Abnahmetests**: Tests durch Auftraggeber und Endnutzer im Pilotbetrieb

**Testfallmatrix (Ergebnisse):**

| ID | Testobjekt | Erwartet | Status |
|----|------------|----------|--------|
| TF01 | Rollenantrag | Antrag angenommen | Bestanden |
| TF02 | Pflichtfelder | Validierungsfehler | Bestanden |
| TF03 | Genehmigung | Workflow läuft | Bestanden |
| TF04 | Ablehnung | Keine Rechtevergabe | Bestanden |
| TF05 | Policy OK | Prüfung bestanden | Bestanden |
| TF06 | Policy Fehler | Prüfung blockiert | Bestanden |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | Bestanden |
| TF08 | Rechteentzug | Zugriff entfernt | Bestanden |
| TF09 | Audit-Log | Eintrag vorhanden | Bestanden |
| TF10 | Secret-Scan | Keine Secrets | Bestanden |
| TF11 | Audit-Export | Bericht erzeugt | Bestanden |
| TF12 | Benachrichtigung | Status erhalten | Bestanden |

Die Integrationstests wurden für folgende Szenarien durchgeführt:
- Portal → Workflow → GitHub API: Vollständiger Antragszyklus (TF01–TF04, TF07)
- Policy-Engine → Audit-Log: Validierung und Protokollierung (TF05, TF06, TF09)
- Secret-Scanning → Reporting: Sicherheitsprüfung und Export (TF10, TF11)

Die Abnahme erfolgte durch den Auftraggeber auf Basis des Abnahmeprotokolls (Anhang A15). Alle Muss-Kriterien wurden erfüllt.

Der Pilotbetrieb wurde mit 15 Testnutzern durchgeführt. Erfolgskennzahlen: Fehlerquote < 2 %, Bearbeitungszeit < 4 Stunden pro Antrag, Nutzerzufriedenheit > 4/5 Punkten.

---

# 5 Abschluss

## 5.1 Soll-Ist-Vergleich

| Ziel | Soll | Ist | Bewertung |
|------|------|-----|-----------|
| RBAC-Modell | definiert | 6 Rollen modelliert (Admin, Developer, Auditor, Read-Only, HR, Finance) | Erreicht |
| Self-Service-Antrag | strukturiert | Antragsformular mit Validierung und Status-Tracking | Erreicht |
| GitHub-Workflow | automatisiert | YAML-Workflow mit 4 Stages (validate, approve, provision, notify) | Erreicht |
| Audit-Logging | protokolliert | Append-Only-Log mit Exportfunktion | Erreicht |
| Testfälle | 12 dokumentiert | 12 Testfälle definiert und bestanden | Erreicht |
| Dokumentation | vollständig | Kapitel 1–6 mit Tabellen und Diagrammen | Erreicht |

**Kennzahlenvergleich:**

| Kennzahl | Geplant | Tatsächlich | Abweichung |
|----------|---------|-------------|:----------:|
| Gesamtaufwand | 70 h | 72 h | +3 % |
| Kosten | 3.740 EUR | 3.820 EUR | +2 % |
| Testabdeckung | 12/12 | 12/12 | 0 % |
| Bearbeitungszeit | < 4 h | < 1 h | −75 % |

Die Abweichungen von +3 % beim Aufwand und +2 % bei den Kosten resultierten aus dem erhöhten Aufwand für die Security-Validierung. Die Bearbeitungszeit konnte mit unter 1 Stunde das geplante Ziel von 4 Stunden deutlich unterschreiten.

## 5.2 Wirtschaftlichkeitsbetrachtung

Die Wirtschaftlichkeitsrechnung zeigte auf Basis der in Abschnitt 3.6 hergeleiteten Annahmen eine positive Projektbilanz:
- **Investition (Ist)**: 3.820 EUR (Gesamtaufwand 72 h inkl. Mehraufwand)
- **Jährliche Einsparung (prognostiziert)**: ca. 19.000 EUR (Herleitung siehe Abschnitt 3.6)
- **Amortisation**: ca. 3,5 Monate (konservativ gerundet)
- **ROI (3 Jahre)**: ca. 1.424 %

Die Einsparungen resultierten aus:
- Reduktion der Bearbeitungszeit von 20 Minuten auf ca. 2 Minuten pro Antrag (−90 %)
- Wegfall von Nachbesserungen durch Fehler (15 Fälle/Monat à 30 Min = 7,5 h/Monat)
- Reduzierter Audit-Aufwand durch zentralisierte Logs (−50 %)

## 5.3 Übergabe

Die Übergabe an die IT-Administration erfolgte nach erfolgreichem Pilotbetrieb. Alle Dokumentationen, Source-Code und Konfigurationen wurden übergeben.

Die Einführung erfolgte mehrstufig:
1. **Pilotphase** (Woche 1–2): 15 Nutzer aus IT und Verwaltung testeten alle Kernfunktionen
2. **Rollout Phase 1** (Woche 3–4): 50 Nutzer aus HR und Finanzen sollten eingebunden werden
3. **Vollausbau** (ab Woche 5): Organisationsweite Aktivierung geplant
4. **Monitoring**: Kontinuierliche Überwachung und Optimierung

## 5.4 Lessons Learned

**Positive Erfahrungen:**
- Die iterative Entwicklung mit kurzen Feedback-Zyklen erwies sich als Erfolgsfaktor. Durch die Sprint-Struktur konnten Fehler frühzeitig erkannt und behoben werden, bevor sie sich in der Gesamtarchitektur manifestierten.
- Die frühzeitige Einbindung von Datenschutzbeauftragtem und Betriebsrat trug zur hohen Akzeptanz bei. Dies bestätigte die Risikobewertung aus der Planungsphase.
- GitHub Actions als Automatisierungsplattform erwies sich als flexibel und gut dokumentiert. Die Integration in die bestehende GitHub-Infrastruktur verlief reibungslos.

**Optimierungspotenzial:**
- **Aufwandsschätzung**: Der Zeitbedarf für die Schnittstellenentwicklung (GitHub API, Azure AD Integration) wurde anfangs zu knapp kalkuliert. Die Abweichung von +8 Stunden hätte durch eine detailliertere technische Risikoanalyse in der Planungsphase vermieden werden können.
- **Stakeholder-Einbindung**: Externe Security-Partner hätten früher eingebunden werden sollen. Der Security-Consultant wurde erst in der Konzeptionsphase hinzugezogen. Ein früherer Einbezug hätte die Architekturentscheidungen von Anfang an absichern können.
- **Testtiefe**: Noch mehr Endanwender hätten im Pilot getestet werden können. Die Stichprobe von 15 Testnutzern war ausreichend für den Prototypen, aber für einen produktiven Rollout wäre eine breitere Testbasis erforderlich gewesen.

## 5.5 Risiken nach Projektabschluss

| Risiko | Beschreibung | Maßnahme |
|--------|-------------|----------|
| Mangelnde Wartung | Keine Kapazitäten für Betrieb | Übergabe an IT-Administration, Dokumentation der Betriebsprozesse |
| Sicherheitslücken | Neue Angriffsvektoren | Regelmäßige Updates, Security-Scans via GitHub Dependabot |
| Veraltete Berechtigungen | Kein regelmäßiger Review | Jährlicher Audit durch Datenschutzbeauftragten |
| Know-how-Verlust | Entwickler verlässt Unternehmen | Vollständige Dokumentation, Übergabe-Workshop |

## 5.6 Ausblick

Das etablierte Zero-Trust-Konzept ließ sich für weitere Bereiche (HR, Verwaltung, Support) adaptieren. Künftige Erweiterungen umfassten:
- Automatisierte Policy-Generierung auf Basis von Templates
- Engere Verzahnung von Security und Workflow-Automatisierung
- Integration weiterer Geschäftsbereiche ab 2027
- Kontinuierliche Security-Assessments und regelmäßige Awareness-Schulungen

## 5.7 Persönliches Fazit

Die Projektarbeit hat mir ermöglicht, die theoretischen Kenntnisse aus der Fortbildung zum Certified IT Business Manager praxisnah anzuwenden. Besonders wertvoll war die Erfahrung, ein komplexes Sicherheitskonzept von der Analyse bis zur prototypischen Umsetzung eigenständig zu planen und durchzuführen. Die Herausforderungen lagen vor allem in der realistischen Zeitplanung und der Abgrenzung des Projektumfangs. Das Ergebnis bestätigt, dass moderne Automatisierungskonzepte mit überschaubarem Aufwand realisiert werden können.

Die Prüfungsvorbereitung nach der alten Prüfungsordnung (letzter Jahrgang) bot den Vorteil einer verlängerten Bearbeitungszeit bis November 2026. Die Empfehlung des Dozenten Carsten Vordermeier, auf "Klassiker statt Experimente" zu setzen, habe ich beherzigt und ein solides, prüfbares Projekt umgesetzt.

---

# 6 Anhang

## A1 Projektstrukturplan (PSP)

| Phase | Arbeitspaket | Beschreibung | Aufwand | Verantwortlich |
|-------|-------------|--------------|---------|----------------|
| **1. Projektinitiierung** | | | **5 h** | |
| 1.1 | Projektumfeld & Ausgangslage | Unternehmensanalyse, IT-Landschaft | 2 h | Daniel Massa |
| 1.2 | Projektauftrag erstellen | Scope, Ziele, Abgrenzung | 2 h | Daniel Massa |
| 1.3 | Kick-off vorbereiten | Agenda, Stakeholder einladen | 1 h | Daniel Massa |
| **2. Analyse** | | | **10 h** | |
| 2.1 | Ist-Analyse (Interviews, Logs) | 8 Stakeholder, Systeminventur | 5 h | Daniel Massa |
| 2.2 | Anforderungsdefinition | Lastenheft, MoSCoW | 3 h | Daniel Massa |
| 2.3 | Stakeholderanalyse | Matrix, Kommunikationsplan | 2 h | Daniel Massa |
| **3. Konzeption** | | | **12 h** | |
| 3.1 | Zero-Trust-Konzept | NIST 800-207 Mapping | 4 h | Daniel Massa |
| 3.2 | RBAC-Modellierung | 6 Rollen, 50+ Berechtigungen | 4 h | Daniel Massa |
| 3.3 | Datenschutzkonzept | DPIA, DSGVO-Checkliste | 2 h | Daniel Massa + DSB |
| 3.4 | Make-or-Buy / Nutzwert | 3 Optionen, 6 Kriterien | 2 h | Daniel Massa |
| **4. Technischer Entwurf** | | | **8 h** | |
| 4.1 | Architekturdesign | 4-Schichten-Modell | 2 h | Daniel Massa |
| 4.2 | GitHub-Workflow-Design | 4 Stages, YAML | 3 h | Daniel Massa |
| 4.3 | Datenmodell (ERD) | 7 Entitäten, Relationen | 2 h | Daniel Massa |
| 4.4 | Schnittstellen-Spezifikation | REST, GitHub API, SAML | 1 h | Daniel Massa |
| **5. Umsetzung (Prototyp)** | | | **20 h** | |
| 5.1 | Dev-Environment Setup | Docker, CI/CD, Repo | 3 h | Daniel Massa |
| 5.2 | Datenstrukturen & Migration | PostgreSQL, Knex | 3 h | Daniel Massa |
| 5.3 | RBAC-Implementierung | Node.js/Python, Middleware | 4 h | Daniel Massa |
| 5.4 | Frontend (Self-Service) | React/TS, Material UI | 4 h | Daniel Massa |
| 5.5 | GitHub-Automatisierung | Actions Workflow, YAML | 3 h | Daniel Massa |
| 5.6 | Audit-Logging & Export | Append-Only, CSV/JSON | 3 h | Daniel Massa |
| **6. Test & Abnahme** | | | **7 h** | |
| 6.1 | Testkonzept & Testfälle | 12 TF, Matrix | 2 h | Daniel Massa |
| 6.2 | Funktionstests (TF01–TF12) | Jest, Supertest, Playwright | 3 h | Daniel Massa |
| 6.3 | Security-Tests | CodeQL, Secret-Scan, Pen-Test | 1 h | Daniel Massa |
| 6.4 | Abnahme & Dokumentation | Protokoll A15 | 1 h | Daniel Massa + AG |
| **7. Einführung** | | | **3 h** | |
| 7.1 | Pilotkonzept & User-Guide | 15 Nutzer, 2 Wochen | 2 h | Daniel Massa |
| 7.2 | Schulungsmaterial | Video, FAQ, Admin-Guide | 1 h | Daniel Massa |
| **8. Dokumentation** | | | **5 h** | |
| 8.1 | Projektdokumentation (IHK) | Master, Export | 3 h | Daniel Massa |
| 8.2 | Anhang erstellen | A1–A15 | 1 h | Daniel Massa |
| 8.3 | Präsentationsvorbereitung | 15 Min Vortrag | 1 h | Daniel Massa |
| **Gesamtaufwand** | | | **70 h** | |
| Ist-Kosten (mit Mehraufwand) | | | 3.820 EUR | |

## A2 Lastenheft-Auszug

**Ausgangssituation:** Der VFB verwaltet Zugriffsrechte manuell über E-Mail-Anträge.
- Medienbrüche: 3–4 Stationen pro Antrag
- Fehlerquote: 8–12 % Fehleinrichtungen
- Bearbeitungszeit: Ø 2,5–3,5 Tage
- Compliance-Lücken: Dezentrale Audit-Logs
- Sicherheitsrisiken: Überhöhte Rechte bei Austritten

**Muss-Anforderungen:**

| ID | Anforderung | Beschreibung |
|----|-------------|--------------|
| MU-01 | RBAC-Modell | Mind. 6 Rollen, 50+ Berechtigungen für GitHub-Org |
| MU-02 | Self-Service-Antrag | Web-Portal zur Rollenbeantragung mit Validierung |
| MU-03 | Genehmigungsworkflow | Automatische Weiterleitung, 48h-Eskalation |
| MU-04 | GitHub-Integration | Automatisierte Team-Zuordnung via GitHub API |
| MU-05 | Audit-Logging | Revisionssichere Protokollierung, Append-Only |
| MU-06 | Rechteentzug | Automatisierter Entzug bei Austritt/Rollenwechsel |
| MU-07 | DSGVO-Konformität | Datenminimierung, Löschkonzept, TOM (Art. 32) |
| MU-08 | Dokumentation | Vollständige Projektdokumentation (IHK-Vorgaben) |

## A3 Use-Case-Diagramm

**Akteure:** Mitarbeiter, Vorgesetzter, IT-Admin, GitHub Actions, Datenschutzbeauftragter

| UC-ID | Anforderung | Testfall |
|-------|-------------|----------|
| UC-01 | MU-02 (Self-Service-Antrag) | TF01, TF02 |
| UC-04 | MU-03 (Genehmigung) | TF03 |
| UC-05 | MU-03 (Ablehnung) | TF04 |
| UC-07 | MU-04 (GitHub-Integration) | TF07 |
| UC-08 | MU-05 (Audit-Log) | TF09 |
| UC-10 | MU-06 (Rechteentzug) | TF08 |
| UC-11 | MU-05 (Audit-Export) | TF11 |
| UC-12 | MU-07 (DSGVO) | A14 |

## A4 Pflichtenheft-Auszug

| ID | Anforderung | Beschreibung | Realisierung |
|----|-------------|--------------|--------------|
| PT-01 | Zentrale Rechteverwaltung | Alle Rollen/Berechtigungen in einer DB | PostgreSQL + RBAC-Modell |
| PT-02 | GitHub-API-Integration | Team-Membership via API verwalten | GitHub REST API v3 |
| PT-03 | Audit-Log Append-Only | Kein UPDATE/DELETE auf Logs | DB-Trigger, Hash-Chain |
| PT-04 | Self-Service Web-UI | React/TS Portal, SSO via Azure AD | React 18, TypeScript |
| PT-05 | GitHub Actions Workflow | 4 Stages | `.github/workflows/role-request.yml` |
| PT-06 | Policy Engine | 4-Augen-Prinzip, Kompetenzmatrix | Backend-Middleware |
| PT-07 | Audit-Export | CSV/JSON, Filter | REST `/api/export` |
| PT-08 | Secret-Scanning | GitHub CodeQL + Dependabot | GitHub Advanced Security |

## A5 Datenmodell

**Entity-Relationship-Modell:**

```
USER ── USER_ROLE ── ROLE ── ROLE_PERMISSION ── PERMISSION
  │                    │
  │                    └── GITHUB_TEAM ── REPOSITORY
  │
  └── APPROVAL ── AUDIT_LOG
```

**PostgreSQL DDL (Auszug):**
```sql
CREATE TABLE "user" (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    department VARCHAR(100)
);

CREATE TABLE role (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE user_role (
    user_id UUID REFERENCES "user"(id),
    role_id UUID REFERENCES role(id),
    granted_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE audit_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    action VARCHAR(50) NOT NULL,
    user_id UUID REFERENCES "user"(id),
    timestamp TIMESTAMPTZ DEFAULT now(),
    hash VARCHAR(64) NOT NULL,
    previous_hash VARCHAR(64)
);
```

## A6 EPK-Prozessbeschreibung

**Prozess:** Automatisierte Rechtevergabe (Self-Service → Genehmigung → Provisioning)

**RACI-Matrix:**

| Aktivität | Nutzer | Vorgesetzter | System | IT-Admin | Auditor |
|-----------|--------|--------------|--------|----------|---------|
| Antrag stellen | **R** | I | A | I | I |
| Validieren | I | I | **R/A** | I | I |
| Genehmigen | I | **R/A** | C | I | I |
| Provisioning | I | I | **R/A** | C | I |
| Audit-Log | I | I | **R/A** | C | **R** |
| Eskalation | I | I | C | **R/A** | I |

R = Responsible, A = Accountable, C = Consulted, I = Informed

## A7 Oberflächenentwürfe (Wireframes)

Die Wireframes zeigen die geplanten UI-Oberflächen des Self-Service-Portals:

**Dashboard (Startseite nach Login):**
- Kacheln: Meine Rollen (3), Offene Anträge (1), Letzte Aktivitäten (5)
- Aktionsschaltflächen: "+ Rolle beantragen", "Meine Berechtigungen"

**Rollenantrag (Self-Service-Formular):**
- Dropdown: Gewünschte Rolle (Developer, Auditor, Read-Only, etc.)
- Textfeld: Begründung
- Optional: Ressource (Repository)
- Schaltflächen: Absenden, Abbrechen

## A8 Screenshots der Anwendung

- Abb. A8.1: GitHub Repo-Übersicht (`vfb-bildung/zero-trust-rbac`)
- Abb. A8.2: GitHub Actions Workflow (CI/CD-Pipeline)
- Abb. A8.3: YAML Workflow-Datei (`role-request.yml`)
- Abb. A8.4: Testlauf GitHub Actions
- Abb. A8.5: Secret-Scanning Ergebnis (CodeQL)
- Abb. A8.6: Rollen- und Teamstruktur (RBAC-Modell)
- Abb. A8.7: Audit-Log-Auszug
- Abb. A8.8: Self-Service-Formular (Simulation)
- Abb. A8.9: Terminal-Testausgabe

## A9 Entwicklerdokumentation (§9 PO)

**Repository:** `vfb-bildung/zero-trust-rbac` (private)
**Version:** 1.0

**Quickstart:**
```
git clone https://github.com/vfb-bildung/zero-trust-rbac.git
cd zero-trust-rbac
cp .env.example .env
docker-compose up -d
cd frontend && npm install && npm run dev
```

**Services:**

| Service | Port | Beschreibung |
|---------|------|--------------|
| Frontend (React) | 3000 | Self-Service-Portal |
| Backend (FastAPI) | 4000 | REST API, Webhooks |
| PostgreSQL | 5432 | Persistenz |
| Redis | 6379 | Cache (Berechtigungen) |
| GitHub Actions | — | CI/CD, Provisioning |

## A10 Testfall-Matrix

**Testdatum:** 15.10.2026 | **Ergebnis:** 12/12 bestanden (100 %)

| ID | Testobjekt | Erwartet | Status |
|----|------------|----------|--------|
| TF01 | Rollenantrag | Antrag angenommen | Bestanden |
| TF02 | Pflichtfelder | Validierungsfehler | Bestanden |
| TF03 | Genehmigung | Workflow läuft | Bestanden |
| TF04 | Ablehnung | keine Rechtevergabe | Bestanden |
| TF05 | Policy OK | Prüfung bestanden | Bestanden |
| TF06 | Policy Fehler | Prüfung blockiert | Bestanden |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | Bestanden |
| TF08 | Rechteentzug | Zugriff entfernt | Bestanden |
| TF09 | Audit-Log | Eintrag vorhanden | Bestanden |
| TF10 | Secret-Scan | keine Secrets | Bestanden |
| TF11 | Audit-Export | Bericht erzeugt | Bestanden |
| TF12 | Benachrichtigung | Status erhalten | Bestanden |

## A11 Schnittstellenübersicht

**Base URL:** `https://api.vfb-bildung.de/api/v1`

| Methode | Pfad | Beschreibung |
|---------|------|--------------|
| POST | `/role-requests` | Neuen Rollenantrag erstellen |
| GET | `/role-requests/{id}` | Antragsstatus abrufen |
| PUT | `/role-requests/{id}/approve` | Antrag genehmigen |
| PUT | `/role-requests/{id}/reject` | Antrag ablehnen |
| GET | `/users/me/roles` | Eigene Rollen abrufen |
| GET | `/users/me/permissions` | Eigene Berechtigungen abrufen |
| POST | `/audit/export` | Audit-Log exportieren |
| GET | `/health` | Health-Check |

## A12 Klassendiagramm

**Kernklassen:**

```
┌──────────────────┐      ┌──────────────────┐
│      User        │      │      Role        │
├──────────────────┤      ├──────────────────┤
│ - id: UUID       │      │ - id: UUID       │
│ - email: String  │      │ - name: String   │
│ - fullName: Str  │      │ - description: T │
│ - department: Str│      └────────┬─────────┘
└────────┬─────────┘               │
         │ 1                      N │
         │                         │
         │ N  ┌────────────────────┘
         ├────┤    UserRole
         │    ├─────────────────────┐
         │    │ - grantedAt: Time   │
         │    └─────────────────────┘
         │
         │ 1  ┌──────────────────┐
         ├────┤   Approval       │
         │    ├──────────────────┤
         │    │ - status: Enum   │
         │    │ - decidedAt: Time│
         │    └────────┬─────────┘
         │             │
         │             │ 1:N
         │    ┌────────┴────────┐
         │    │   AuditLog      │
         │    ├─────────────────┤
         │    │ - action: Str   │
         │    │ - hash: String  │
         │    │ - prevHash: Str │
         │    └─────────────────┘
```

## A13 Benutzerdokumentation

**Zielgruppe:** Endnutzer (Mitarbeiter VFB)

**1. Anmeldung:**
1. Öffnen Sie `https://rbac.vfb-bildung.de`
2. Klicken Sie auf "Mit Azure AD anmelden"
3. Nach erfolgreicher Anmeldung gelangen Sie zum Dashboard

**2. Dashboard:**
- Meine Rollen: Alle aktuell aktiven Rollen mit Berechtigungen
- Offene Anträge: Anträge, die noch geprüft/ausstehen
- Letzte Aktivitäten: Letzte 5 Änderungen an Ihren Rollen

**3. Rolle beantragen:**
1. Klicken Sie auf "+ Rolle beantragen" (Dashboard)
2. Wählen Sie die gewünschte Rolle aus dem Dropdown
3. Geben Sie eine Begründung ein
4. Optional: Wählen Sie eine Ressource (Repository/Team)
5. Klicken Sie auf "Absenden"

Nach dem Absenden erhalten Sie eine Bestätigung. Der Vorgesetzte wird per E-Mail benachrichtigt. Der Status wird im Dashboard aktualisiert.

## A14 Datenschutz-Checkliste

**Rechtmäßigkeit (Art. 6 DSGVO):**

| Prüfpunkt | Status |
|-----------|--------|
| Rechtsgrundlage für Verarbeitung? | Art. 6 Abs. 1 lit. f (berechtigtes Interesse) |
| Verhältnismäßigkeit? | Nur notwendige Daten (User-ID, Name, E-Mail, Rolle) |
| Interessenabwägung durchgeführt? | DPIA dokumentiert |

**TOMs (Art. 32 DSGVO):**

| Maßnahme | Implementierung | Status |
|----------|----------------|--------|
| Verschlüsselung | TLS 1.3, DB at Rest | Umgesetzt |
| Vertraulichkeit | RBAC, Least Privilege | Umgesetzt |
| Integrität | Append-Only Audit-Log, Hash-Chain | Umgesetzt |
| Verfügbarkeit | Docker Compose, Backup | Umgesetzt |
| Belastbarkeit | Monitoring, Alerting | Umgesetzt |

## A15 Abnahmeprotokoll

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration
**Prüfling:** Daniel Massa (615951)
**Betrieb:** VFB Ludwigsburg

| Kriterium | Soll | Ist | Bewertung |
|-----------|------|-----|-----------|
| RBAC-Modell definiert (6 Rollen) | ✓ | ✓ | Erfüllt |
| Self-Service-Antrag prototypisch | ✓ | ✓ | Erfüllt |
| GitHub-Workflow automatisiert | ✓ | ✓ | Erfüllt |
| Audit-Logging implementiert | ✓ | ✓ | Erfüllt |
| Testfälle (12) durchgeführt | ✓ | 12/12 bestanden | Erfüllt |
| DSGVO-Konformität (DPIA) | ✓ | ✓ | Erfüllt |
| Dokumentation vollständig | ✓ | ✓ | Erfüllt |
| Wirtschaftlichkeit (ROI > 0) | ✓ | 3,5 Monate Amortisation | Erfüllt |

**Abnahmeteilnehmer:**
- Auftraggeber (VFB): _______________
- Projektleiter / Prüfling: Daniel Massa
- IT-Administration: Thomas Zoller
- Datenschutzbeauftragter: _______________
- IHK-Betreuer: Frau Dr. Sabine Wagner

**Abnahmeerklärung:** Hiermit wird die ordnungsgemäße Durchführung des Projekts bestätigt. Alle Muss-Kriterien wurden erfüllt.

---

## LITERATURVERZEICHNIS

### Normen & Standards
1. ISO/IEC 27001:2022 — Information security management systems — Requirements
2. ISO/IEC 27002:2022 — Information security controls
3. DSGVO (EU) 2016/679 — Datenschutz-Grundverordnung, insbesondere Art. 5, 25, 32
4. BSI Grundschutz-Kompendium (IT-Grundschutz)
5. NIST SP 800-207 — Zero Trust Architecture (2020)

### Fachliteratur
6. Kindervag, J. (2010). "No More Chewy Centers: Introducing the Zero Trust Model of Information Security." Forrester Research.
7. Rose, S. et al. (2020). "Zero Trust Architecture." NIST Special Publication 800-207.
8. Microsoft (2023). "Zero Trust Deployment Guide." Microsoft Security Documentation.
9. GitHub Docs. "GitHub Actions Documentation." https://docs.github.com/en/actions (Abruf: 01.10.2026)
10. GitHub Docs. "GitHub REST API Documentation." https://docs.github.com/en/rest (Abruf: 01.10.2026)

### Projektmanagement
11. Project Management Institute (2021). "A Guide to the Project Management Body of Knowledge (PMBOK Guide)." 7th Edition.
12. Schwaber, K., Sutherland, J. (2020). "The Scrum Guide."
13. DIN 69901-5:2009 — Projektmanagement; Projektmanagementsysteme

### IT-Security & Compliance
14. BSI (2023). "Empfehlungen zur Absicherung von Cloud-Diensten."
15. IDW PS 330 — Prüfung der Sicherheit von Informationstechnik
16. ISO/IEC 19770-1:2017 — IT Asset Management

---

## EIDESSTATTLICHE VERSICHERUNG

Ich, **Daniel Massa**, Prüflingsnummer **615951**, wohnhaft **Hackstraße 41, 70190 Stuttgart**,

versichere hiermit an Eides statt, dass ich die vorliegende Dokumentation zur betrieblichen Projektarbeit mit dem Thema

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration**
Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration

selbstständig verfasst und keine anderen als die angegebenen Quellen und Hilfsmittel benutzt habe.

Die Arbeit wurde bisher keiner anderen Prüfungsbehörde vorgelegt.

Alle Zitate und Übernahmen aus fremden Werken sind als solche kenntlich gemacht. Sämtliche verwendeten Quellen sind im Literaturverzeichnis aufgeführt.

Die in der Arbeit beschriebenen Projektergebnisse, Messwerte, Testergebnisse und Screenshots stammen aus der tatsächlichen Projektbearbeitung. Nicht verifizierbare oder prototypische Aussagen sind als solche gekennzeichnet.

Ich bin mir bewusst, dass eine falsche Versicherung an Eides statt strafrechtliche Konsequenzen nach sich ziehen kann.

Stuttgart, den **01.11.2026**

____________________________________
**Daniel Massa**

---

