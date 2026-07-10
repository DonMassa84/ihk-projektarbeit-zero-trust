# IHK Claim-Evidence-Matrix – Final

**Stand:** 10.07.2026  
**Basis:** Repository-Inventur nach Abschluss der technischen Vorbereitung  
**Ziel:** 0 CONTRADICTED-Claims im Ergebnistext, 0 UNVERIFIED-Claims als abgeschlossene Projektergebnisse

**Status-Legende:**
- ✅ VERIFIED – Evidenz im Repository vorhanden
- ⚠️ PARTIALLY_VERIFIED – Teilweise belegbar
- ❌ UNVERIFIED – Keine Evidenz (als offener Punkt gekennzeichnet)
- 📋 NO_CLAIM / PLAN – Nur Plan oder Annahme, kein abgeschlossenes Ergebnis
- 🔴 OFFEN / AUSSTEHEND – Erfordert menschliche Handlung (Human-Gate)
- 🗑️ ENTFERNT – Aus dem Ergebnistext entfernt (nicht realisiert)

---

## 1. Initiierung

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 1.1 | Projektumfeld VFB mit ~50 Beschäftigten | 📋 PLAN | Im Konzept beschrieben, keine VFB-internen Belege im Repository. Als Plan dargestellt. |
| 1.2 | Ziel: Rechtevergabe -90%, Bearbeitungszeit <4h | 📋 PLAN | Zielvorgabe aus der Konzeption. Keine Baseline-Messung im Pilot. |
| 1.3 | Testabdeckung: 14 Testfälle der Pilot-API | ✅ VERIFIED | ✅ 14/14 Tests neu erstellt und bestanden (statt ursprünglich behaupteter 12). |
| 1.4 | Pilotphase: 15 Nutzer erfolgreich bedient | ❌ UNVERIFIED | Keine realen Nutzerdaten. Als Plan-Kennzeichnung im Text. |
| 1.5 | Gesamtaufwand: 70 Stunden (Plan) | 📋 PLAN | Plantabelle vorhanden. Ist-Spalte durch Autor zu ergänzen. |
| 1.6 | Projektorganisation: Iterativ mit Scrum-Elementen | ⚠️ PARTIALLY_VERIFIED | Planungsdokumente vorhanden. Keine Sprint-Reviews im Repo. |
| 1.7 | Entscheidung: Eigenentwicklung (FastAPI) | ✅ VERIFIED | ✅ FastAPI-Backend-Code vorhanden (12 Module). |
| 1.8 | Projektteam: Carsten Vordermeier (Auftraggeber) | ✅ VERIFIED | Auftraggeberbestätigung liegt vor (H3). |

## 2. Projektplanung

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 2.1 | Stakeholderanalyse mit Einfluss/Interesse | ⚠️ PARTIALLY_VERIFIED | Tabelle vorhanden. Keine validierenden Interviews. |
| 2.2 | Zeitplan erstellt (KW 24–35/2026 als Plan) | 📋 PLAN | 🗑️ **CONTRADICTED-Status aufgelöst.** Als Planzeitplan ohne Ist-Erreichung gekennzeichnet. Tatsächliche Erstellung an 2 Tagen (08.–10.07.). |
| 2.3 | Qualitätsmanagement: Tests, Reports, CI | ⚠️ PARTIALLY_VERIFIED | ✅ 14 Tests, Testreport, CI-Konfiguration vorhanden. Coverage 95 % nicht gemessen. |
| 2.4 | Security Tests: Trivy, Bandit, Secret Scanning | ⚠️ PARTIALLY_VERIFIED | ✅ Security-Scan-Reports erstellt. Kein OWASP ZAP (für Pilotumfang nicht erforderlich). |
| 2.5 | E2E Tests: Playwright | 🗑️ ENTFERNT | Nicht implementiert. Kein Frontend vorhanden. Aus Ergebnistext entfernt. |
| 2.6 | Kostenplanung (21.700 € / 3.790 € als Budgetrahmen) | 📋 PLAN | Plantabelle als Budgetrahmen gekennzeichnet. Ist-Kosten nicht erfasst. |
| 2.7 | Amortisation (Berechnung auf Planbasis) | 📋 PLAN | Reine Planrechnung ohne Ist-Daten. Als solche gekennzeichnet. |

## 3. Konzeptionierung

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 3.1 | RBAC-Engine mit Rollenmodell und Policy-Prüfung | ✅ VERIFIED | ✅ `policy_service.py`, `models.py`, Pilot-API implementiert und getestet. |
| 3.2 | Audit-Logger: SHA-256-Hash-Kette, Append-Only | ✅ VERIFIED | ✅ `audit_chain_service.py` implementiert, Kettenverifikation und Manipulationserkennung getestet. |
| 3.3 | React 18 + TypeScript + TailwindCSS Frontend | 🗑️ ENTFERNT | 🗑️ **CONTRADICTED aufgelöst.** Nicht implementiert. Aus dem Projektergebnis entfernt. |
| 3.4 | GitHub Actions CI/CD-Workflow (YAML) | ✅ VERIFIED | ✅ `.github/workflows/ci.yml` vorhanden. Noch kein realer GitHub-Run. |
| 3.5 | OPA-Policy-Engine | ⚠️ PARTIALLY_VERIFIED | Template-basierte Policy-Generierung. Keine OPA-Laufzeitintegration. |
| 3.6 | CI/CD mit Test- und Security-Gates (Konfiguration) | ⚠️ PARTIALLY_VERIFIED | ✅ CI-Konfiguration mit Test + Security-Scans. Kein realer CI-Run. |

## 4. Durchführung und Steuerung

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 4.1 | Persistente Datenhaltung (SQLite-Dev / PostgreSQL-kompatibel) | ⚠️ PARTIALLY_VERIFIED | SQLite-Dev-DB implementiert und getestet. Keine Alembic-Migrationen. |
| 4.2 | FastAPI-Backend implementiert | ✅ VERIFIED | ✅ Erweitert auf 12 Module, 16 API-Endpunkte. |
| 4.3 | Testfall TF01–TF14 (14 Tests) alle bestanden | ✅ VERIFIED | ✅ 14/14 Tests neu geschrieben und bestanden (statt ursprünglich 12). |
| 4.4 | Secret-Scan und Security-Prüfung durchgeführt | ✅ VERIFIED | ✅ Secret-Scan-Report, Security-Scan-Report, Dependency-Scan vorhanden. |
| 4.5 | Kostenkontrolle (Plan) | 📋 PLAN | Keine EVA-Berechnungen. Als Plan dargestellt. |

## 5. Abschluss

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 5.1 | Projektabnahme | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Abnahme durch Auftraggeber durchgeführt (H7). |
| 5.2 | Fehlerrate (keine belastbare Messung im Pilot) | 🗑️ ENTFERNT | Keine belastbare Metrik. Aus Ergebnistext entfernt. |
| 5.3 | User Satisfaction (keine Befragung durchgeführt) | 🗑️ ENTFERNT | Nicht erhoben. Aus Ergebnistext entfernt. |
| 5.4 | DSGVO-Konformität (Prüfung durchgeführt) | ✅ VERIFIED | Datenschutzprüfung abgeschlossen (H5). Ausschließlich synthetische Testdaten. |
| 5.5 | Amortisation (reine Planrechnung) | 📋 PLAN | Ist-Kosten nicht erfasst. |
| 5.6 | Rollout (Pilot, kein Produktivrollout) | 📋 PLAN | Als Pilot gekennzeichnet. Kein Produktivrollout. |
| 5.7 | Eidesstattliche Erklärung (vorbereitet) | ⚠️ PARTIALLY_VERIFIED | Text vorhanden. Abgabedatum und Unterschrift fehlen (Human-Gate H10). |
| 5.8 | Eidesstattliche Erklärung unterschrieben | 🔴 OFFEN | Erfordert persönliche Unterschrift (Human-Gate H10). |

## 6. Anhang

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 6.1 | GitHub Actions Workflow (YAML) | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Reale `.github/workflows/ci.yml` vorhanden. |
| 6.2 | GitHub Actions Run (Screenshot) | 🗑️ ENTFERNT | 🗑️ **CONTRADICTED aufgelöst.** Simulations-Screenshot entfernt. Kein echter GitHub-Run. |
| 6.3 | Security-Scan-Ergebnisse | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Reale Reports in `reports/security/`. |
| 6.4 | pytest-Testausgabe | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Reale Testausgabe mit 14/14 bestanden. |
| 6.5 | ML-Anomalieerkennung (Modell nicht trainiert) | 📋 PLAN | Training-Skript vorhanden. Kein trainiertes Modell. Als Konzept dargestellt. |
| 6.6 | ML-Policy-Generierung (Template-Fallback) | ⚠️ PARTIALLY_VERIFIED | Code vorhanden. Template-Fallback ohne trainiertes Modell. |

## 7. Infrastruktur & Code

| # | Claim | Status | Behandlung |
|---|-------|--------|------------|
| 7.1 | Docker-Setup vorhanden | ✅ VERIFIED | `docker-compose.yml`, `Dockerfile` vorhanden. |
| 7.2 | Monitoring-Konfiguration (Prometheus/Grafana) | ⚠️ PARTIALLY_VERIFIED | Konfiguration vorhanden. Keine Laufzeit-Nachweise. |
| 7.3 | HF Spaces Apps (3 Stück) | ✅ VERIFIED | Vorhanden. |
| 7.4 | ML-Training-Skripte vorhanden | ⚠️ PARTIALLY_VERIFIED | Skripte vorhanden. Nicht ausgeführt. |
| 7.5 | Projekterstellung: 2 Tage technische Vorbereitung (08.–10.07.) | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Auf realen Zeitraum reduziert: 15 Commits an 2 Tagen (technische Vorbereitung, nicht mehrwöchiges Projekt). |
| 7.6 | Projektabnahmeprotokoll (A8) | ✅ VERIFIED | 🗑️ **CONTRADICTED aufgelöst.** Abnahmeprotokoll ausgefüllt (H7). |
| 7.7 | Kick-Off-Protokoll | ❌ UNVERIFIED | Keine Datei vorhanden. Als "nicht dokumentiert" gekennzeichnet. |

---

## Zusammenfassung

| Status | Anzahl | Bedeutung |
|--------|-------:|-----------|
| ✅ VERIFIED | **16** | Durch Repository-Evidenz gedeckt |
| ⚠️ PARTIALLY_VERIFIED | **9** | Teilweise belegbar |
| 📋 PLAN | **9** | Plan, Annahme oder Budgetrahmen |
| 🔴 OFFEN / AUSSTEHEND | **1** | Erfordert menschliche Handlung (H10) |
| 🗑️ ENTFERNT | **6** | Aus Ergebnistext entfernt |
| ❌ UNVERIFIED | **2** | Keine Evidenz, als offen markiert |
| 🚫 CONTRADICTED | **0** | ❌ **KEINE WIDERSPRÜCHE** |
| **Gesamt** | **43** | |

**Ergebnis:** 0 CONTRADICTED-Claims. 6 Claims entfernt. 16 Claims vollständig durch Evidenz gedeckt. Nur noch H10 (Unterschrift) offen.
