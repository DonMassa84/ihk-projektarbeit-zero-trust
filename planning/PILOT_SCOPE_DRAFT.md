# PILOT-SCOPE – Zero-Trust-Rollenworkflow (Entwurf)

> **Status:** ENTWURF – noch nicht freigegeben  
> **Zweck:** Definition des minimalen realen Pilotumfangs  
> **Nächster Schritt:** Abstimmung mit Auftraggeber, dann Freigabe

---

## 1. Projekttitel (Vorschlag)

> **Zero-Trust-Sicherheitskonzept mit GitHub-Integration – Pilot eines rollenbasierten Berechtigungsworkflows**

---

## 2. MUSS-Umfang (im Pilot zwingend enthalten)

| # | Funktion | Fachliches Ziel | Abnahmekriterium | Evidenz | Risiko | Verantwortlich |
|---|----------|-----------------|------------------|---------|--------|----------------|
| M1 | FastAPI-Backend | Berechtigungslogik als API bereitstellen | API läuft, Health-Endpoint antwortet mit 200 | Log aus `curl localhost:8000/api/v1/health` | Gering | Projektleiter |
| M2 | 6 Pilotrollen | Differenzierte Zugriffssteuerung abbilden | 6 Rollen in DB definiert und abrufbar | DB-Dump oder API-Response | Gering | Projektleiter |
| M3 | Rollenanforderung via API | Benutzer kann Rolle beantragen | POST /api/v1/rbac/request → 200 + ID | API-Test-Log | Gering | Projektleiter |
| M4 | Pflichtfeldvalidierung | Unvollständige Anträge werden abgewiesen | POST ohne Pflichtfeld → 400 | Test-Log | Gering | Projektleiter |
| M5 | Policy-Prüfung | Antrag wird gegen Regeln validiert | Policy verweigert nicht berechtigte Rollen | Testfall | Mittel | Projektleiter |
| M6 | Statusmodell (DRAFT→SUBMITTED→APPROVED→REJECTED→PROVISIONED→FAILED) | Nachvollziehbarer Antragslebenszyklus | Statusübergänge dokumentiert und getestet | Test-Log | Gering | Projektleiter |
| M7 | Explizite Genehmigungsentscheidung | Genehmiger kann Antrag annehmen/ablehnen | POST /approve → Status=APPROVED; POST /reject → Status=REJECTED | Test-Log | Gering | Projektleiter |
| M8 | GitHub-Teamzuordnung (Dry-Run) | Berechtigung wird in GitHub abgebildet | API-Call an GitHub (Mock oder reale Test-Org) dokumentiert | Log / Screenshot | Mittel | Projektleiter |
| M9 | Persistente Daten (SQLite/PostgreSQL) | Daten überdauern Neustart | App-Neustart → Daten noch vorhanden | Test | Gering | Projektleiter |
| M10 | Audit-Ereignisse | Jede Aktion wird protokolliert | GET /api/v1/audit/logs → Einträge vorhanden | API-Response | Gering | Projektleiter |
| M11 | Hash-Verkettung der Audit-Ereignisse | Manipulationsschutz der Audit-Logs | Jeder Eintrag enthält SHA-256 des vorherigen | DB-Export | Mittel | Projektleiter |
| M12 | Automatisierte Tests | Regression wird erkannt | pytest → 0 failures | CI-Log | Gering | Projektleiter |
| M13 | GitHub-Actions-CI | Tests laufen automatisch bei Push | Workflow-Lauf dokumentiert | CI-Run-Screenshot | Mittel | Projektleiter |
| M14 | Dokumentierter Fehler- und Retestfall | Fehlerbehandlung nachweisbar | Testfall schlägt fehl → Korrektur → Retest OK | Test-Log (2 Durchläufe) | Mittel | Projektleiter |
| M15 | Betriebs- und Übergabedokumentation | Pilot ist übergebbar | README mit Architektur, API, Deployment | Datei im Repo | Gering | Projektleiter |

---

## 3. NICHT im Projekt

| # | Ausgeschlossener Bereich | Begründung |
|---|-------------------------|------------|
| N1 | Vollständiges Enterprise-IAM | Übersteigt 70h-Rahmen |
| N2 | Ablösung eines Identity Providers | Nicht Bestandteil des Pilots |
| N3 | Produktiver unternehmensweiter Rollout | Pilotstatus – kein Produktivbetrieb |
| N4 | Privileged Access Management (PAM) | Separates Themengebiet |
| N5 | Automatische Personalstammdatenintegration | Keine Schnittstelle zu HR-System |
| N6 | Behauptete Revisionssicherheit | Technisch nicht vollständig erreichbar im Pilot |
| N7 | React-Frontend (falls nicht verbindlich beauftragt) | UI-Entwicklung übersteht Zeitrahmen; API-first |
| N8 | Produktive Verarbeitung realer personenbezogener Daten | Nur Testdaten im Pilot |

---

## 4. Liefergegenstände

| # | Liefergegenstand | Form |
|---|-----------------|------|
| L1 | FastAPI-Backend mit API | Quellcode im Repository |
| L2 | Datenmodell (Rollen, Anträge, Audit) | SQLite/PostgreSQL-Schema |
| L3 | GitHub-Integration (Dry-Run) | API-Code + Testprotokoll |
| L4 | Audit-Log mit Hash-Verkettung | Quellcode + DB-Export |
| L5 | CI-Pipeline (GitHub Actions) | `.github/workflows/*.yml` |
| L6 | Test- und Coverage-Report | CI-Output / HTML-Report |
| L7 | Abnahmeprotokoll | Unterschriebenes Dokument |
| L8 | Projektdokumentation (IHK-Form) | PDF |

---

## 5. Abnahmekriterien (Gesamt)

1. Mindestens 10 der 15 MUSS-Funktionen sind implementiert und getestet.
2. CI-Pipeline läuft und produziert Test-Reports.
3. Ein dokumentierter Fehler- und Retest-Zyklus liegt vor.
4. Das Abnahmeprotokoll ist unterschrieben.
5. Keine offenen kritischen Mängel.
