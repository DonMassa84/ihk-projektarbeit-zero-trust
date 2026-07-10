# WORK BREAKDOWN STRUCTURE (Entwurf)

> **Status:** ENTWURF – noch nicht freigegeben  
> **Hinweis:** Alle Zeiten sind PLAN-Werte. Keine Ist-Zeiten eingetragen.

---

## AP 1 – Projektauftrag und Kick-off

| Feld | Wert |
|------|------|
| **Ziel** | Verbindliche Projektbasis schaffen |
| **Tätigkeiten** | Projektauftrag finalisieren, Kick-off-Termin durchführen, Projektakte anlegen |
| **Ergebnis** | Freigegebener Projektauftrag, Kick-off-Protokoll |
| **Vorgänger** | – |
| **Verantwortlich** | Projektleiter + Auftraggeber |
| **Planstunden** | 4 h |
| **Abnahmekriterium** | Projektauftrag unterschrieben |
| **Erwartete Evidenz** | `project-evidence/01_project_order/`, `project-evidence/02_kickoff/` |
| **Risiko** | Auftraggeber nicht verfügbar |

---

## AP 2 – Ist-Analyse und Anforderungen

| Feld | Wert |
|------|------|
| **Ziel** | Aktuelle Berechtigungssituation erfassen |
| **Tätigkeiten** | Bestandsaufnahme Ist-Prozess, Stakeholder-Gespräche, Anforderungsdokumentation |
| **Ergebnis** | Anforderungsliste, Ist-Prozess-Dokumentation |
| **Vorgänger** | AP 1 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 6 h |
| **Abnahmekriterium** | Anforderungsliste vom Auftraggeber bestätigt |
| **Erwartete Evidenz** | `project-evidence/12_communication/` |
| **Risiko** | Unklare Anforderungen |

---

## AP 3 – Variantenbewertung und Lösungsentscheidung

| Feld | Wert |
|------|------|
| **Ziel** | Nachvollziehbare Entscheidung für die Pilot-Lösung |
| **Tätigkeiten** | Alternativen analysieren (Make, Buy, Open Source), Nutzwertanalyse, Entscheidung dokumentieren |
| **Ergebnis** | Entscheidungsprotokoll (ADR) |
| **Vorgänger** | AP 2 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 5 h |
| **Abnahmekriterium** | Entscheidung dokumentiert und begründet |
| **Erwartete Evidenz** | `project-evidence/04_decisions/` |
| **Risiko** | Vorentscheidung ohne Analyse |

---

## AP 4 – Architektur, Rollen- und Datenmodell

| Feld | Wert |
|------|------|
| **Ziel** | Technische Basis definieren |
| **Tätigkeiten** | Architektur-Skizze, ERD, Rollen-Matrix, API-Design, Datenmodell |
| **Ergebnis** | Architektur-Dokument, Datenmodell, API-Spezifikation |
| **Vorgänger** | AP 3 |
| **Verantwortlich** | Projektleiter + Technischer Reviewer |
| **Planstunden** | 8 h |
| **Abnahmekriterium** | Architektur-Review bestanden |
| **Erwartete Evidenz** | `project-evidence/09_reviews/` |
| **Risiko** | Überengineering |

---

## AP 5 – Backend-Grundstruktur und Datenhaltung

| Feld | Wert |
|------|------|
| **Ziel** | Lauffähiges Backend-Grundgerüst |
| **Tätigkeiten** | FastAPI-Projekt aufsetzen, Datenbank-Schema, Migrationen, Health-Endpoint, Datenbank-Zugriff |
| **Ergebnis** | FastAPI-App mit Datenbank-Anbindung |
| **Vorgänger** | AP 4 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 8 h |
| **Abnahmekriterium** | `GET /api/v1/health` → 200, Datenbank lesbar |
| **Erwartete Evidenz** | Git-Commit, Test-Log |
| **Risiko** | Datenbank-Setup-Probleme |

---

## AP 6 – Antrags-, Policy- und Genehmigungsworkflow

| Feld | Wert |
|------|------|
| **Ziel** | Kern-Workflow: Antrag → Prüfung → Genehmigung/Ablehnung |
| **Tätigkeiten** | CRUD-API für Rollenanträge, Policy-Engine-Integration, Genehmigungsendpoint, Statusmodell |
| **Ergebnis** | Vollständiger Antrags-Workflow |
| **Vorgänger** | AP 5 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 9 h |
| **Abnahmekriterium** | Antrag → Genehmigen → Status=APPROVED (API-Test) |
| **Erwartete Evidenz** | API-Test-Log, Git-Commit |
| **Risiko** | Policy-Logik komplex |

---

## AP 7 – GitHub-Integration und Audit-Verkettung

| Feld | Wert |
|------|------|
| **Ziel** | GitHub-Teamzuordnung + fälschungssicheres Audit-Log |
| **Tätigkeiten** | GitHub-API-Client, Team-Zuordnung (Mock/real), Audit-Log mit SHA-256-Hash-Kette, Append-Only |
| **Ergebnis** | GitHub-Dry-Run, Audit-Log mit Hash-Kette |
| **Vorgänger** | AP 6 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 8 h |
| **Abnahmekriterium** | Audit-Eintrag enthält prev_hash; GitHub-Call dokumentiert |
| **Erwartete Evidenz** | Test-Log, Commit |
| **Risiko** | GitHub-API-Rate-Limits |

---

## AP 8 – Tests, CI und Fehlerkorrektur

| Feld | Wert |
|------|------|
| **Ziel** | Automatisierte Qualitätssicherung |
| **Tätigkeiten** | pytest-Tests schreiben, GitHub Actions Workflow, Coverage-Report, Fehler dokumentieren und korrigieren |
| **Ergebnis** | CI-Pipeline + Test-Reports |
| **Vorgänger** | AP 5, AP 6, AP 7 |
| **Verantwortlich** | Projektleiter + Technischer Reviewer |
| **Planstunden** | 8 h |
| **Abnahmekriterium** | CI-Lauf erfolgreich, Coverage > 70 % |
| **Erwartete Evidenz** | CI-Log, Coverage-Report, Review-Protokoll |
| **Risiko** | CI-Konfiguration zeitaufwändig |

---

## AP 9 – Pilotreview, Schulung und Abnahme

| Feld | Wert |
|------|------|
| **Ziel** | Pilotabschluss mit bestätigter Abnahme |
| **Tätigkeiten** | Pilot mit Testnutzer durchführen, Feedback einholen, Schulung durchführen, Abnahmeprotokoll erstellen |
| **Ergebnis** | Schulungsprotokoll, Abnahmeprotokoll |
| **Vorgänger** | AP 8 |
| **Verantwortlich** | Projektleiter + Auftraggeber + Pilotnutzer |
| **Planstunden** | 5 h |
| **Abnahmekriterium** | Abnahmeprotokoll unterschrieben |
| **Erwartete Evidenz** | `project-evidence/10_training/`, `project-evidence/11_acceptance/` |
| **Risiko** | Pilotnutzer nicht verfügbar |

---

## AP 10 – Soll-Ist-Auswertung und Abschlussdokumentation

| Feld | Wert |
|------|------|
| **Ziel** | IHK-konforme Dokumentation aus echten Daten |
| **Tätigkeiten** | Soll-Ist-Vergleich, Kostenauswertung, Lessons Learned, PDF-Build |
| **Ergebnis** | IHK-PDF, Abschlussbericht |
| **Vorgänger** | AP 9 |
| **Verantwortlich** | Projektleiter |
| **Planstunden** | 9 h |
| **Abnahmekriterium** | PDF entspricht IHK-Formalien, alle Claims VERIFIED |
| **Erwartete Evidenz** | PDF, SHA256 |
| **Risiko** | Zeitknappheit |

---

## Gesamtsumme

| AP | Bezeichnung | Plan (h) |
|----|-------------|---------:|
| 1 | Projektauftrag und Kick-off | 4 |
| 2 | Ist-Analyse und Anforderungen | 6 |
| 3 | Variantenbewertung und Lösungsentscheidung | 5 |
| 4 | Architektur, Rollen- und Datenmodell | 8 |
| 5 | Backend-Grundstruktur und Datenhaltung | 8 |
| 6 | Antrags-, Policy- und Genehmigungsworkflow | 9 |
| 7 | GitHub-Integration und Audit-Verkettung | 8 |
| 8 | Tests, CI und Fehlerkorrektur | 8 |
| 9 | Pilotreview, Schulung und Abnahme | 5 |
| 10 | Soll-Ist-Auswertung und Abschlussdokumentation | 9 |
| **Gesamt** | | **70** |
