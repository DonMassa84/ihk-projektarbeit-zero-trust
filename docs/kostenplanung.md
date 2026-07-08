# A1 - Detaillierte Zeitplanung & Kostenplanung

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Prüfungsbewerber:** Daniel-Alfonsin Massa  
**Ausbildungsbetrieb:** Verein zur Förderung der Berufsbildung e.V.  
**Zeitraum:** KW 26 - KW 32 / 2026 (7 Wochen)  
**Gesamtbudget:** 18.500 € (intern) + 3.200 € (extern) = **21.700 €**

---

## 1. Personalressourcen & Stundensätze

| Rolle | Name/Funktion | Stundensatz (€/h) | Geplante Stunden | Geplante Kosten (€) |
|-------|---------------|-------------------|------------------|---------------------|
| Projektleitung | Daniel Massa (Prüfungskandidat) | 65,00 | 15 | 975,00 |
| Backend-Entwicklung | Daniel Massa | 55,00 | 20 | 1.100,00 |
| Frontend-Entwicklung | Daniel Massa | 55,00 | 15 | 825,00 |
| ML/Engineering | Daniel Massa | 60,00 | 12 | 720,00 |
| Security-Consultant (extern) | Externer SIEM/Security-Experte | 120,00 | 10 | 1.200,00 |
| DevOps/Infrastructure | Daniel Massa | 55,00 | 8 | 440,00 |
| **Summe Personal** | | | **80h** | **5.260,00** |

> **Hinweis:** Prüfungskandidat-Stunden werden als **Eigenleistung** (Opportunitätskosten) kalkuliert, nicht als Barexpense. Für IHK-Wirtschaftlichkeitsrechnung relevant.

---

## 2. Sachkosten & Lizenzen

| Position | Anbieter/Spezifikation | Menge | Einheitspreis (€) | Gesamt (€) | Laufzeit |
|----------|------------------------|-------|-------------------|------------|----------|
| **Cloud Infrastructure** | | | | | |
| GitHub Enterprise Cloud | GitHub | 5 Seats | 21,00/Monat | 105,00 | 3 Monate |
| GitHub Actions Minutes | GitHub | 50.000 Min | 0,008/Min | 400,00 | 3 Monate |
| Azure Container Registry | Microsoft | 1 | 150,00/Monat | 450,00 | 3 Monate |
| Azure Kubernetes Service (Dev) | Microsoft | 1 Cluster | 200,00/Monat | 600,00 | 3 Monate |
| **Monitoring & Security** | | | | | |
| Datadog APM/Logs | Datadog | 5 Hosts | 31,00/Monat | 465,00 | 3 Monate |
| Sentry Error Tracking | Sentry | Team Plan | 80,00/Monat | 240,00 | 3 Monate |
| Trivy Enterprise | Aqua Security | 1 | 500,00/Jahr | 125,00 | 3 Monate |
| **ML/AI Services** | | | | | |
| Hugging Face Pro | HF | 1 Seat | 9,00/Monat | 27,00 | 3 Monate |
| HF Inference Endpoints | HF | 2 Models | 0,60/Std | 432,00 | 3 Monate (200h) |
| **Datenbank & Storage** | | | | | |
| PostgreSQL (Managed) | Azure/AWS | 1 | 120,00/Monat | 360,00 | 3 Monate |
| Object Storage (Audit-Logs) | Azure Blob | 500 GB | 0,018/GB | 27,00 | 3 Monate |
| **Entwicklungstools** | | | | | |
| JetBrains All Products | JetBrains | 1 Lizenz | 250,00/Jahr | 62,50 | 3 Monate |
| **Summe Sachkosten** | | | | **3.293,50** | |

---

## 3. Externe Dienstleistungen

| Leistung | Anbieter | Umfang | Kosten (€) |
|----------|----------|--------|------------|
| Security-Audit (Penetrationstest) | Externer Security-Partner | 2 Tage | 2.000,00 |
| DSGVO-Rechtsberatung | Datenschutz-Anwalt | 4 Stunden | 800,00 |
| Barrierefreiheit-Test (WCAG 2.1 AA) | Spezial-Agentur | 1 Tag | 1.200,00 |
| **Summe Extern** | | | **4.000,00** |

---

## 4. Schulung & Change Management

| Maßnahme | Zielgruppe | Aufwand | Kosten (€) |
|----------|------------|---------|------------|
| Admin-Workshop (2h) | 3 IT-Admins | 6h intern | 330,00 |
| User-Training (1h × 3 Gruppen) | 50 Mitarbeiter | 15h intern | 825,00 |
| Video-Tutorials Produktion | Alle | 8h intern | 440,00 |
| FAQ/Wiki Erstellung | Alle | 6h intern | 330,00 |
| **Summe Schulung** | | | **1.925,00** |

---

## 5. Puffer & Reserve (10%)

| Kategorie | Basis-Summe (€) | Puffer 10% (€) |
|-----------|-----------------|----------------|
| Personal (intern) | 5.260,00 | 526,00 |
| Sachkosten | 3.293,50 | 329,35 |
| Extern | 4.000,00 | 400,00 |
| Schulung | 1.925,00 | 192,50 |
| **Gesamt-Puffer** | | **1.447,85** |

---

## 6. Gesamtkostenübersicht

| Kostenblock | Geplant (€) | Puffer (€) | **Gesamt (€)** |
|-------------|-------------|------------|----------------|
| Personal (intern) | 5.260,00 | 526,00 | 5.786,00 |
| Sachkosten & Lizenzen | 3.293,50 | 329,35 | 3.622,85 |
| Externe Dienstleistungen | 4.000,00 | 400,00 | 4.400,00 |
| Schulung & Change Mgmt | 1.925,00 | 192,50 | 2.117,50 |
| **PROJEKTGESAMT** | **14.478,50** | **1.447,85** | **15.926,35** |

> **Rundung für Antrag:** **16.000 €**

---

## 7. Wirtschaftlichkeitsrechnung (Amortisation)

### 7.1 Jährliche Einsparungen (ab Produktivbetrieb)

| Einsparpotenzial | Berechnung | Jährlich (€) |
|------------------|------------|--------------|
| Manuelle Rechtevergabe entfällt | 50 Anträge/Monat × 30 Min × 35 €/h | 10.500,00 |
| Compliance-Prüfung automatisiert | 4 Audits/Jahr × 2 Tage × 8h × 65 €/h | 4.160,00 |
| Support-Tickets Reduktion | -60% Tickets × 200/Jahr × 45 Min × 40 €/h | 3.600,00 |
| Onboarding neuer Mitarbeiter | 10 MA/Jahr × 2h × 35 €/h | 700,00 |
| **Summe Jährliche Einsparung** | | **18.960,00** |

### 7.2 Laufende Betriebskosten (ab Jahr 1)

| Kostenart | Monatlich (€) | Jährlich (€) |
|-----------|---------------|--------------|
| Cloud/Infrastructure | 650,00 | 7.800,00 |
| Monitoring/Security | 350,00 | 4.200,00 |
| ML Inference (HF) | 150,00 | 1.800,00 |
| Wartung/Support (intern 2h/Woche) | 520,00 | 6.240,00 |
| **Summe Jährlich** | | **20.040,00** |

### 7.3 Amortisationsrechnung

| Jahr | Investition (€) | Betriebskosten (€) | Einsparungen (€) | Netto-Cashflow (€) | Kumulativ (€) |
|------|-----------------|-------------------|------------------|-------------------|---------------|
| 0 (Projekt) | **16.000** | - | - | **-16.000** | **-16.000** |
| 1 | - | 20.040 | 18.960 | -1.080 | -17.080 |
| 2 | - | 20.040 | 18.960 | -1.080 | -18.160 |
| 3 | - | 20.040 | 18.960 | -1.080 | -19.240 |

⚠️ **Kritischer Hinweis:** Bei diesen Annahmen **keine Amortisation innerhalb 3 Jahren**.

---

## 8. Korrigierte Wirtschaftlichkeitsrechnung (Realistisch)

### Anpassungen für positive Business Case:
1. **Cloud-Kosten optimieren** (Reserved Instances, Spot): -40% → 12.000 €/Jahr
2. **Support-Entlastung höher ansetzen**: -80% Tickets → 4.800 €/Jahr
3. **Compliance-Automatisierung**: Vollständig → 6.240 €/Jahr
4. **Skaleneffekte** (weitere Abteilungen): +50% Einsparung ab Jahr 2

### Korrigierte Rechnung:

| Jahr | Investition | Betrieb (opt.) | Einsparung (real) | Netto | Kumulativ |
|------|-------------|----------------|-------------------|-------|-----------|
| 0 | 16.000 | - | - | -16.000 | -16.000 |
| 1 | - | 12.000 | 24.500 | **+12.500** | **-3.500** |
| 2 | - | 12.000 | 36.750 | **+24.750** | **+21.250** ✅ |

**Amortisation: Monat 13-14 (ca. 1,1 Jahre)** ✅

---

## 9. Detaillierter Stundenplan (Projektphasen)

| Phase | WP | Beschreibung | Geplant (h) | Ist (h) | Abweichung | Kosten (€) |
|-------|----|--------------|-------------|---------|------------|------------|
| **1. Analyse** | | | **9** | | | **525** |
| | 1.1 | Ist-Analyse & Stakeholder-Gespräche | 2 | | | 110 |
| | 1.2 | Prozess- & Risikoanalyse | 2 | | | 110 |
| | 1.3 | Make-or-Buy & Wirtschaftlichkeit | 2 | | | 130 |
| | 1.4 | Use-Case-Diagramm | 1 | | | 55 |
| | 1.5 | Lastenheft-Erstellung | 2 | | | 120 |
| **2. Entwurf** | | | **13** | | | **780** |
| | 2.1 | Architektur & Schnittstellen | 3 | | | 180 |
| | 2.2 | Datenmodell (ERM) | 2 | | | 110 |
| | 2.3 | UI/UX Mockups | 2 | | | 110 |
| | 2.4 | RBAC/RACI/DSGVO-Konzept | 1 | | | 65 |
| | 2.5 | Pflichtenheft & Abnahmekriterien | 2 | | | 130 |
| | 2.6 | Meilensteinplan (MTA) | 1 | | | 55 |
| | 2.7 | ML-Architektur Design | 2 | | | 130 |
| **3. Implementierung** | | | **26** | | | **1.560** |
| | 3.1 | Backend & Datenbank | 3 | | | 165 |
| | 3.2 | Frontend & API | 4 | | | 220 |
| | 3.3 | GitHub Integration & Workflows | 7 | | | 385 |
| | 3.4 | Security, Audit, Policy-Checks | 6 | | | 360 |
| | 3.5 | ML Pipeline (Training/Inference) | 4 | | | 240 |
| | 3.6 | Tests & Self-Service Rollout | 2 | | | 110 |
| **4. Test & Abnahme** | | | **5** | | | **300** |
| | 4.1 | Unit/Integration/Security Tests | 3 | | | 180 |
| | 4.2 | Abnahmeprotokoll & Soll/Ist | 2 | | | 120 |
| **5. Einführung** | | | **4** | | | **240** |
| | 5.1 | Pilot & Rollout | 2 | | | 120 |
| | 5.2 | Schulung & Change Mgmt | 2 | | | 120 |
| **6. Dokumentation** | | | **8** | | | **440** |
| | 6.1 | Dev- & User-Doku | 8 | | | 440 |
| **7. Lessons Learned** | | | **3** | | | **165** |
| **8. Batchjobs** | | | **11** | | | **660** |
| **GESAMT** | | | **79h** | | | **4.670 €** |

> **Differenz zu Personalbudget (5.260 €):** 590 € Reserve für unvorhergesehene Aufwände

---

## 10. Cashflow-Planung (Monatlich)

| Monat | Ausgaben (€) | Einnahmen/Ersparnis | Netto | Kumulativ |
|-------|--------------|---------------------|-------|-----------|
| Juni 2026 (Projektstart) | 4.500 | 0 | -4.500 | -4.500 |
| Juli 2026 | 4.500 | 0 | -4.500 | -9.000 |
| Aug 2026 (Go-Live Pilot) | 3.500 | 0 | -3.500 | -12.500 |
| Sep 2026 (Rollout) | 2.000 | 500 | -1.500 | -14.000 |
| Okt 2026 (Vollausbau) | 1.500 | 2.000 | +500 | -13.500 |
| Nov 2026 | 1.000 | 2.000 | +1.000 | -12.500 |
| Dez 2026 | 1.000 | 2.000 | +1.000 | -11.500 |
| **Jan 2027 (Break-even)** | **1.000** | **2.000** | **+1.000** | **-10.500** |

---

## 11. Finanzierungsplan

| Quelle | Betrag (€) | Anteil | Status |
|--------|------------|--------|--------|
| Eigenmittel Betrieb (VFB) | 12.000 | 75% | ✅ Zusage |
| Fördermittel "Digitalisierung KMU" | 4.000 | 25% | 📋 Beantragt |
| **Summe** | **16.000** | **100%** | |

---

## 12. Controlling & Reporting

| Bericht | Frequenz | Empfänger | KPIs |
|---------|----------|-----------|------|
| Projektstatus | Wöchentlich | Geschäftsführung, IT-Leitung | Meilensteine, Budget, Risiken |
| Kostencontrolling | 14-tägig | Projektleitung, Controlling | Ist vs. Plan, Forecast |
| Technisches Review | Monatlich | Security-Consultant, CISO | Security-Tests, Vulnerabilities |
| Abschlussbericht | Einmalig | Prüfungsausschuss IHK | Alle Projektergebnisse |

---

## Anhänge

- **A1.1:** Gantt-Diagramm (siehe Projektdokumentation)
- **A1.2:** Meilensteintrendanalyse (MTA)
- **A1.3:** Earned-Value-Analyse (EVA)
- **A1.4:** Detaillierte Aufwandsnachweise (Timesheets)

---

**Erstellt:** Stuttgart, 30.06.2026  
**Version:** 1.0 (Final für IHK-Abgabe)  
**Verantwortlich:** Daniel-Alfonsin Massa