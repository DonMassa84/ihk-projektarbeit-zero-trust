# Anhang A1 — Detaillierte Zeitplanung (Gantt)

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Prüfling:** Daniel Massa (615951)  
**Datum:** 01.11.2026

---

## Übersicht: 70 Stunden Gesamtaufwand

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
| 4.2 | Datenmodell (ERD) | 7 Entitäten, Relationen | 2 h | Daniel Massa |
| 4.3 | Schnittstellen-Spezifikation | REST, GitHub API, SAML | 1 h | Daniel Massa |
| **5. Umsetzung (Prototyp)** | | | **20 h** | |
| 5.1 | Dev-Environment Setup | Docker, CI/CD, Repo | 3 h | Daniel Massa |
| 5.2 | Datenstrukturen & Migration | PostgreSQL, Knex | 3 h | Daniel Massa |
| 5.3 | RBAC-Implementierung | Node.js, Middleware | 4 h | Daniel Massa |
| 5.4 | Frontend (Self-Service) | React/TS, Material UI | 4 h | Daniel Massa |
| 5.5 | GitHub-Automatisierung | Actions Workflow, YAML | 3 h | Daniel Massa |
| 5.6 | Audit-Logging & Export | Hash-Chain, CSV/JSON | 3 h | Daniel Massa |
| **6. Test & Abnahme** | | | **7 h** | |
| 6.1 | Testkonzept & Testfälle | 12 TF, Matrix | 2 h | Daniel Massa |
| 6.2 | Funktionstests (TF01–TF12) | Jest, Supertest, Playwright | 3 h | Daniel Massa |
| 6.3 | Security-Tests | CodeQL, Secret-Scan, Pen-Test | 1 h | Daniel Massa |
| 6.4 | Abnahme & Dokumentation | Protokoll A15 | 1 h | Daniel Massa + AG |
| **7. Einführung** | | | **3 h** | |
| 7.1 | Pilotkonzept & User-Guide | 15 Nutzer, 2 Wochen | 2 h | Daniel Massa |
| 7.2 | Schulungsmaterial | Video, FAQ, Admin-Guide | 1 h | Daniel Massa |
| **8. Dokumentation** | | | **5 h** | |
| 8.1 | Projektdokumentation (IHK) | Master-MD, Export | 3 h | Daniel Massa |
| 8.2 | Anhang erstellen | A1–A15 PDFs | 1 h | Daniel Massa |
| 8.3 | Präsentationsvorbereitung | 15 Min Vortrag | 1 h | Daniel Massa |

---

## Gantt-Chart (Meilensteine)

| Meilenstein | Geplant | Ist | Status |
|-------------|---------|-----|--------|
| M1: Ist-Analyse abgeschlossen | 15.08.2026 | 18.08.2026 | ✅ |
| M2: Konzeption abgeschlossen | 30.08.2026 | 05.09.2026 | ✅ |
| M3: Architekturdesign fertig | 15.09.2026 | 18.09.2026 | ✅ |
| M4: Prototyp funktionsfähig | 10.10.2026 | 12.10.2026 | ✅ |
| M5: Test/Abnahme abgeschlossen | 20.10.2026 | 22.10.2026 | ✅ |
| M6: Interne Fertigstellung | 25.10.2026 | 27.10.2026 | ✅ |
| M7: Korrekturphase | 31.10.2026 | 02.11.2026 | ✅ |
| **M8: Abgabe IHK** | **01.11.2026** | **01.11.2026** | 🎯 |

---

## Ressourcenplanung

| Rolle | Person | Stunden | Haupttätigkeiten |
|-------|--------|---------|------------------|
| Projektleiter / Prüfling | Daniel Massa | 70 h | Gesamtverantwortung, Konzeption, Umsetzung, Tests, Doku |
| Security-Consultant (ext.) | Prof. Dr. Schulze | 8 h | Security-Review, Compliance-Validierung |
| Datenschutzbeauftragter | Intern (DSB) | 4 h | DPIA, DSGVO-Prüfung, TOM-Freigabe |
| IT-Administration | Thomas Zoller | 4 h | GitHub-Setup, Azure AD, Server-Bereitstellung |
| Endnutzer (Pilot) | 15 Mitarbeitende | — | Testing, Feedback, Schulungsteilnahme |

---

## Budget-Übersicht

| Position | Menge | Satz | Betrag |
|----------|-------|------|--------|
| Projektleitung / Prüfling | 70 h | 45 EUR | 3.150 EUR |
| Fachbereichsabstimmung | 4 h | 50 EUR | 200 EUR |
| Datenschutzprüfung (DSB) | 2 h | 70 EUR | 140 EUR |
| Testumgebung / Tools | pauschal | 100 EUR | 100 EUR |
| Dokumentation / Schulung | pauschal | 150 EUR | 150 EUR |
| **Gesamtkosten** | | | **3.740 EUR** |

*Ist-Kosten: 3.820 EUR (+2 %) durch Security-Validierung +8 h*

---

*Ende Anhang A1. Vgl. Kapitel 2.3 (PSP), 2.4 (Arbeitspakete), 2.5 (Meilensteine), 2.7 (Kostenplanung) der Projektarbeit.*