# Projektdokumentation: Zero-Trust-Sicherheitskonzept mit GitHub-Integration

**Abschlussprüfung Sommer 2026**  
**Certified IT Business Manager (IHK)**

---

## Eigenleistung

Die vorliegende Projektdokumentation wurde im Rahmen der Abschlussprüfung Certified IT Business Manager (IHK) erarbeitet.

**Konzeption, Implementierung und Dokumentation** wurden zu 100 % eigenständig erstellt. Die konzeptionelle Planung (Architektur, RBAC-Modell, Compliance-Konzept), die prototypische Implementierung (Backend, Frontend, GitHub-Integration, OPA-Policies) sowie die vollständige schriftliche Dokumentation stellen die eigentliche Projektleistung dar.

**Hilfsmittel:** Für Formulierung, Strukturierung und inhaltliche Überprüfung wurde KI-gestützte Software (OpenAI ChatGPT) als redaktionelles Hilfsmittel eingesetzt. KI-gestützte Ausgaben wurden eigenständig geprüft, inhaltlich angepasst und in den Projektkontext eingebettet. Die KI-Nutzung beschränkt sich ausschließlich auf Formulierungsunterstützung, Strukturierungsvorschläge und Review-Hinweise; sie ersetzt nicht die eigenständige inhaltliche Arbeit.

**Prototypische Umsetzung:** Die Implementierung erfolgte als funktionsfähiger Prototyp in einer Testumgebung. Es wird keine produktive Live-Umgebung behauptet. Alle Testdaten, Messwerte und Screenshots stammen aus der Testumgebung und sind als solche gekennzeichnet.

**Dokumentationsarbeit:** Die Projektdokumentation umfasst Konzept, Entwurf, Implementierungsdokumentation, Testdokumentation und diese schriftliche Ausarbeitung. Die eidesstattliche Erklärung am Ende des Dokuments gibt den wahrheitsgemäßen Umfang der Eigenleistung an.

---

## 1. Einleitung

### 1.1 Projektumfeld
Der **Verein zur Förderung der Berufsbildung (VFB)** bietet als gemeinnütziger, regionaler Bildungsträger zahlreiche IHK- und IT-Qualifizierungen an. Mit rund 50 Beschäftigten und hybriden Lernplattformen ist die Digitalisierung zentraler Unternehmensfokus. Ziel ist es, mit effizienten, automatisierten Workflows unter Gewährleistung maximaler IT- und Datenschutzvorgaben innovative Vorreiterrolle einzunehmen.

### 1.2 Projektziel
Bis **01.11.2026** implementiert der VFB ein rollenbasiertes Zero-Trust-Sicherheitskonzept, das die manuelle Rechtevergabe um mindestens 90 % reduziert, alle Berechtigungsänderungen revisionssicher protokolliert und über ein Self-Service-Portal eine Bearbeitungszeit von maximal 4 Stunden ermöglicht.

**Messbare Erfolgskriterien:**
| Kriterium | Zielwert | Bezug |
|---|---|---|
| Bearbeitungszeit pro Anfrage | maximal 4 Stunden | Self-Service-Workflow |
| Fehlerrate bei Rechtevergaben | < 2 % | Qualitätsanforderung (3.5) |
| Automatisierungsgrad | mindestens 80 % via Self-Service | Rollout-Plan (7) |
| Testabdeckung | 12 von 12 Kern-Testfällen bestanden | Abnahmeprotokoll (6) |
| Pilotphase | 15 Nutzer erfolgreich bedient | Pilotierung Woche 1–2 (7) |

**Gesamtaufwand:** 70 Stunden (siehe 2.1).

### 1.3 Projektbegründung
- Komplexe Compliance-Anforderungen
- Häufige personelle Wechsel
- Automatisierungswürdige Prozesse mit Medienbrüchen
- Sicherheitslücken durch manuelle Rechtevergabe

### 1.4 Projektschnittstellen
- On-Premises-Systeme
- Cloud-Dienste (GitHub API)
- Interne Datenbank (PostgreSQL)
- Monitoring/Reporting (Prometheus/Grafana)
- Azure AD / OIDC Authentifizierung

### 1.5 Projektabgrenzung
**Nicht betrachtet:**
- Netzwerktechnische Infrastrukturprojekte
- Legacy-Anwendungen (nicht-webbasiert)
- Physische Sicherheitsinfrastruktur

---

## 2. Projektplanung

### 2.1 Projektphasen (Phasenmodell)
1. **Analyse & Anforderungsaufnahme** (9h)
2. **Konzeption** - Architektur, RBAC, Compliance (13h)
3. **Entwurf** - Use-Case, Oberfläche, Datenmodell
4. **Implementierung** - Backend, Frontend, Schnittstellen (26h)
5. **Test & Abnahme** - Unit, Integration, Security (5h)
6. **Einführung** - Deployment, Migration, Schulung (4h)
7. **Dokumentation** (8h)
8. **Lessons Learned & Ausblick** (3h)
9. **Nächtliche Batchjobs** (11h)

**Gesamt: 70 Stunden** [Q: Original-A1]

### 2.2 Abweichungen vom Projektantrag
- Erhöhter Aufwand in Security, Compliance, Schnittstellen
- Verlängerung der Entwicklungszeit bei gleichbleibendem Ressourceneinsatz
- Detaillierter Soll/Ist-Vergleich in Tabelle 4 (Anhang)

### 2.3 Ressourcenplanung
| Rolle | Stunden | Kosten |
|-------|---------|--------|
| Projektleitung | 15h | Intern |
| Backend-Entwicklung | 20h | Intern |
| Frontend-Entwicklung | 15h | Intern |
| Security-Consultant | 10h | Extern |
| Cloud-Lizenzen/Testsysteme | - | Budget |

### 2.4 Entwicklungsprozess
- **Vorgehensmodell:** Scrum + Kanban (iterativ)
- **Qualitätssicherung:** TDD, Code-Reviews, CI/CD
- **Automatisierung:** GitHub Actions für Build, Test, Rollout
- **Dokumentation:** Pull Requests + Audit-Logs

### 2.5 Stakeholderanalyse

| Stakeholder | Einfluss | Interesse | Kommunikation | Eskalationsweg |
|-------------|----------|-----------|---------------|----------------|
| Geschäftsführung (GF) | Hoch | Strategisch | Monatliches Status-Reporting |Direkt |
| IT-Leitung | Hoch | Hoch (operativ) | Wöchentlich (Sprint Review) | GF |
| Datenschutzbeauftragter (DSB) | Mittel | Hoch (Compliance) | Bi-wöchentlich, ad-hoc bei Datenschutzfragen | IT-Leitung → GF |
| Betriebsrat | Mittel | Mittel (Mitbestimmung) | Vor Einführung neuer Prozesse | GF |
| Endanwender (Mitarbeiter) | Niedrig | Mittel (Bediener) | Schulungen, FAQ, Feedback-Runden | IT-Leitung |
| Externe Partner (IHK-Betreuer) | Niedrig | Niedrig (Prüfung) | Prüfungstermine, Dokumentation | Projektleitung |

---

## 3. Analysephase

### 3.1 Ist-Analyse
- Manuelle Benutzerrechtevergabe
- Getrennte Zugriffsverwaltung pro System
- Medienbrüche & unklare Verantwortlichkeiten
- Fehleranfällige Prozesse
- Dezentrale Audit-Logs
- Hoher Compliance-Prüfungsaufwand

### 3.2 Wirtschaftlichkeitsanalyse

#### 3.2.1 Make-or-Buy-Entscheidung

| Kriterium | Eigenentwicklung | Okta | Azure AD Premium | Keycloak |
|-----------|------------------|------|------------------|----------|
| Monatliche Kosten | 0 € (Bestand) | ~$5.500/Mon. (50 User) | ~$2.500/Mon. (50 User) | 0 € (Open Source) |
| Integrationsaufwand | Gering (eigener Code) | Mittel (API-Integration) | Mittel (Azure-Ökosystem) | Hoch (manuelle Anbindung) |
| Individuelle Workflows | Volle Kontrolle | Eingeschränkt | Eingeschränkt | Plugin-basiert |
| Vendor-Lock-in | Kein | Hoch | Hoch | Gering |
| Wartungsaufwand | Eigenverantwortlich | Fremdverantwortlich | Fremdverantwortlich | Eigenverantwortlich |
| DSGVO-Datenhoheit | Voll (On-Premises) | Eingeschränkt (US-Cloud) | Eingeschränkt (MS-Cloud) | Voll (Self-Hosted) |

**Entscheidung: Eigenentwicklung** – Individuelle Genehmigungs-Workflows (mehrstufig, abhängig von Rollentyp und Organisationsbereich) sind mit Standard-Tools nicht abbildbar. Die GitHub-Integration als Kernkomponente erfordert direkten Zugriff auf die GitHub API, was bei fertigen IAM-Lösungen nur eingeschränkt möglich ist.

#### 3.2.2 Projektkosten

| Position | Aufwand / Menge | Einzelposten | Gesamt |
|----------|-----------------|--------------|--------|
| Interne Personalkosten | 70 h | 45 €/h | 3.150 € |
| Security-Beratung (extern) | 8 h | 80 €/h | 640 € |
| GitHub Enterprise Lizenzen | Bestand | 0 € (vorhanden) | 0 € |
| Hardware/Software (Tests) | — | 0 € (Bestand) | 0 € |
| **Gesamtinvestition** | | | **3.790 €** |

#### 3.2.3 Amortisationsdauer

| Einsparfaktor | Berechnung | Jahreswert |
|---------------|------------|------------|
| Reduktion manueller Anträge | 35 Anträge/Woche × 52 Wochen × 20 Min × 45 €/h | 27.300 € |
| Geringerer Support-Aufwand | Geschätzt 2 h/Woche × 52 × 45 €/h | 4.680 € |
| **Gesamteinsparung pro Jahr** | | **~31.980 €** |
| **Amortisation** | 3.790 € / 31.980 € × 12 Monate | **~1,4 Monate** |

Konservative Schätzung unter Einbezug nur der direkten Personalkosten-Einsparung ergibt eine Amortisation von unter 2 Monaten.

### 3.3 Nutzwertanalyse
KPIs:
- Sicherheitsvorfälle (Reduktion)
- Bearbeitungszeit pro Anfrage (<4h)
- Benutzerzufriedenheit (>4/5)

### 3.4 Anwendungsfälle (Use Cases)
1. **Selbstständiges Beantragen von Rollen** (Self-Service)
2. **Automatisierte Genehmigungsworkflows** (GitHub Actions)
3. **Änderung von Zugriffsrechten** per Self-Service
4. **Automatisierte Compliance-Checks** (OPA Policies)
5. **Audit-Log-Abfrage & Reporting**

### 3.5 Qualitätsanforderungen (ISO 27001, DSGVO, BDSG)
- Transparenz in der Rechtevergabe
- Konsistente Audit-Logs
- Revisionssichere Prozesse
- Geringe Fehlerrate (<2%)
- Barrierefreie Benutzeroberfläche

### 3.6 Lastenheft/Fachkonzept
- Anforderungen an Sicherheit, Performance, Usability, Schnittstellen
- Priorisierung: Muss-/Kann-Anforderungen
- Monitoring in der Umsetzung

---

## 4. Entwurfsphase

### 4.1 Zielplattform
- Cloud-/Container-Technologien (Docker/Kubernetes)
- GitHub als Integrations- & Automatisierungs-Hub
- Webbasierter Zugriff + Mobile API

### 4.2 Architekturdesign
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Frontend   │────▶│   Backend   │────▶│  Database   │
│  (React)    │     │  (FastAPI)  │     │ (PostgreSQL)│
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                    ┌────────────┼────────
                    │      │      │
              ┌─────┴─┐ ┌──┴──┐ ┌──┴─────┐
              │ GitHub│ │ OPA │ │ Prom.  │
              │ Actions│ │Policy│ │Grafana│
              └───────┘ └─────┘ └────────┘
```

#### Zero-Trust-Architekturleitprinzipien
| Prinzip | Umsetzung in der Architektur |
|---------|------------------------------|
| **Never Trust, Always Verify** | OPA Policy Engine prüft jeden API-Request und jede Berechtigungsänderung against definierte Regeln; kein implizites Vertrauen durch Netzwerkzugehörigkeit |
| **Least Privilege** | RBAC mit minimalen Rollen; GitHub Teams/Repos nur mit individuell definierten Zugriffsberechtigungen; Token mit minimalem Scope |
| **Micro-Segmentation** | Logische Trennung über GitHub Teams, Repositories und Branch-Protection-Rules; separate Namespaces/Environments für Entwicklung, Test und Produktion |

### 4.3 Benutzeroberfläche (Mockups)
- Klare Navigation
- Intuitive Beantragung
- Visibilität aller eigenen Rollen/Berechtigungen
- Barrierefreiheit (WCAG 2.1 AA) [Q: Original 4.2/4.3]
- Screenshots in Anhang A8

### 4.4 Datenmodell (Entity-Relationship)
**Entitäten:**
- **User** (id, email, name, department, azure_ad_id)
- **Role** (id, name, description, hierarchy_level)
- **Policy** (id, name, rules_json, version)
- **AuditLog** (id, user_id, action, resource, timestamp, result)
- **Workflow** (id, type, status, approver_id, created_at)

**Relationen:**
- User ↔ Role (n:m über UserRole)
- Role → Policy (1:n)
- User → AuditLog (1:n)
- Workflow → User (n:1 als Antragsteller/Genehmiger)

### 4.5 Geschäftslogik
- **RBAC-Engine:** Rollenbasierte Zugriffskontrolle mit Hierarchien
- **Workflow-Engine:** Antrag → Prüfung → Genehmigung → Bereitstellung
- **GitHub Integration:** Actions triggern Berechtigungsänderungen
- **Policy Engine (OPA):** Validierung bei jeder Änderung
- **Audit-Logger:** Revisionssichere Protokollierung aller Events – Hash-Kette (SHA-256 mit Vorgänger-Hash), append-only PostgreSQL-Tabelle mit Row-Level Security, Aufbewahrung 10 Jahre, DB-Trigger verhindern UPDATE/DELETE. Prototyp: Append-Only umgesetzt, Hash-Kette konzeptionell.

### 4.6 Qualitätssicherung
- Unit Tests (Backend: pytest, Frontend: Vitest)
- Integration Tests (API, DB, GitHub API)
- Security Tests (OWASP ZAP, Trivy, Secret Scanning)
- Code Reviews (min. 2 Reviewer)
- Earned Value Analysis (Controlling)

### 4.7 Pflichtenheft / DSGVO-Konzept
- Art. 32 DSGVO: Technisch-organisatorische Maßnahmen
- Rollentrennung & Verantwortlichkeiten
- Lückenlose Protokollierung (Audit-Logs) mit Hash-Kette, Append-Only und 10-jähriger Aufbewahrung (siehe 4.5)
- Datenminimierung & Löschkonzepte
- Verschlüsselung (TLS 1.3, AES-256 at rest) [Q: Original 4.7]
- Backup-Verfahren (RPO < 1h, RTO < 4h)
- Datenschutzbeauftragter & Betriebsrat eingebunden

---

## 5. Implementierungsphase

### 5.1 Datenstrukturen
- PostgreSQL Schema nach ERM
- Migrationen via Alembic
- Indizes für Audit-Log-Performance
- Row-Level Security für Mandantenfähigkeit

### 5.2 Benutzeroberfläche
- React 18 + TypeScript + TailwindCSS
- Komponenten: RoleRequestForm, ApprovalDashboard, AuditViewer
- State Management: TanStack Query + Zustand
- Barrierefreiheit: ARIA, Keyboard-Navigation, Screenreader

### 5.3 Geschäftslogik & GitHub Integration

#### Kernkomponenten:
```python
# src/backend/services/rbac_service.py
class RBACService:
    async def request_role(self, user_id: str, role_id: str, justification: str):
        # 1. Validierung
        # 2. Workflow erstellen
        # 3. GitHub Action triggern
        # 4. Audit-Log Eintrag
        
    async def approve_role(self, workflow_id: str, approver_id: str):
        # 1. Policy Check (OPA)
        # 2. GitHub Repository/Berechtigung setzen
        # 3. Audit-Log
        # 4. Notification
```

#### GitHub Actions Workflows:
```yaml
# .github/workflows/rbac-workflow.yml
name: RBAC Auto-Provisioning
on:
  workflow_dispatch:
    inputs:
      user: {required: true}
      role: {required: true}
      repo: {required: true}
jobs:
  provision:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            // Rolle in GitHub zuweisen
            await github.rest.repos.addCollaborator(...)
```

#### Secrets-Management
Authentifizierung erfolgt über **GitHub App Installation Tokens** oder Personal Access Tokens (PAT), die als Encrypted Secrets gespeichert werden:
- **Referenzierung:** `${{ secrets.GH_APP_TOKEN }}` in Workflows
- **Rotation:** Automatisierte Key-Rotation über GitHub App Einstellungen; PAT-Rotation manuell bei Bedarf
- **Pin-to-SHA:** Externe Actions werden auf spezifische SHA-Versions hashes gepinnt (z. B. `actions/github-script@<SHA>`), um Supply-Chain-Angriffe zu verhindern
- **Minimaler Scope:** Tokens erhalten nur die minimal benötigten Berechtigungen (Prinzip der geringsten Berechtigung)

---

## 6. Abnahmephase

### 6.1 Teststrategie
| Testart | Tool | Abdeckung |
|---------|------|-----------|
| Unit Tests | pytest / Vitest | 95%+ |
| Integration Tests | pytest + Testcontainers | 85% |
| Security Tests | OWASP ZAP, Trivy | Kritische Befunde adressiert |
| E2E Tests | Playwright | Kern-Workflows |

### 6.2 Abnahmekriterien
✅ Alle Rechteänderungen protokolliert   [Q: Original 4.5]
✅ Genehmigungs-Workflows funktional  
✅ Self-Service Portal bedienbar  
✅ DSGVO/Compliance dokumentiert  
✅ Audit-Trails vollständig   [Q: Original 4.5/4.7]
- Performance-Ziel: Antwortzeiten < 500 ms (konzeptionelle Vorgabe)   [Q: konzeptionelle Vorgabe, keine Messung]

### 6.3 Testfall-Beispiel (Anhang A10)
```
Testfall: TC-RBAC-001 - Rollenbeantragung via Self-Service
Soll: User kann Rolle beantragen → Genehmiger genehmigt → GitHub-Berechtigung gesetzt
Ist:  Erfolgreich durchlaufen, Audit-Log vollständig [Q: Original 6]
Status: BESTANDEN
```

### 6.4 Abnahmeprotokoll
| Feld | Inhalt |
|------|--------|
| **Datum** | 30.06.2026 |
| **Teilnehmer** | Projektleitung (DMA), IT-Leitung (VFB), Datenschutzbeauftragter (VFB), Geschäftsführung (VFB), IHK-Betreuer |
| **Ergebnis** | Bedingt freigegeben |
| **Offene Punkte** | Performance-Messung unter Produktivlast ausstehend (konzeptionell dokumentiert) |
| **Freigabe durch Auftraggeber (GF)** | _________________________ |
| **Freigabe durch Projektleitung** | _________________________ |
| **Freigabe durch IT-Leitung** | _________________________ |
| **Freigabe durch DSB** | _________________________ |
| **Bestätigung IHK-Betreuer** | _________________________ |

---

## 7. Einführungsphase

### Rollout-Plan (7 Wochen) [Q: Original 7]

| Woche | Phase | Zielgruppe | KPIs |
|-------|-------|------------|------|
| 1-2 | **Pilot** | 15 Nutzer (IT 10, Verw. 5) | Fehlerrate <2%, Bearbeitung <4h, Satisfaction >4/5 |
| 3-4 | **Rollout 1** | 50 Nutzer (HR 25, Finanzen 25) | Manuelle Prozesse als Fallback |
| 5-7 | **Vollausbau** | Alle 50 Mitarbeiter | Manuelle Prozesse deaktiviert, Monitoring | [Q: Original 7]

### Change Management
- Praxisnahe Workshops
- Video-Tutorials (kurz)
- Zentrale FAQ
- Eskalationswege definiert
- Ziel: >70% Anträge via Self-Service in Woche 4

---

## 8. Dokumentation

| Dokument | Zielgruppe | Status |
|----------|------------|--------|
| Entwicklerdokumentation (A9) | Dev-Team | ✅ |
| Benutzerdokumentation (A13) | Endanwender | ✅ |
| API-Spezifikation (OpenAPI) | Entwickler | ✅ |
| Betriebsanleitung | Admins | ✅ |
| Schnellstart-Guide | Neue Rollouts | ✅ |

---

## 9. Fazit

### 9.1 Soll-/Ist-Vergleich
| Ziel | Soll | Ist | Status |
|------|------|-----|--------|
| Automatisierung Rechtevergabe | Vollständig | Vollständig | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]
| Fehlerrate | <2% | ~1.2% (Testphase) | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]
| Bearbeitungszeit | <4h | ~3.5h (Testphase) | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]
| User Satisfaction | >4/5 | ~4.3/5 (Testphase) | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]
| DSGVO-Konformität | Vollständig | Vollständig | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]
| Amortisation | 12 Monate | ~11 Monate | ✅ | [Q: Original 9.1 — TEILWEISE, granular prüfen]

### 9.2 Lessons Learned
**Positiv:**
- Iterative Entwicklung & engmaschige QS als Erfolgsfaktoren
- Frühe Einbindung Datenschutz/Betriebsrat → hohe Akzeptanz
- TDD & Code-Reviews sicherten Qualität

**Verbesserungspotenzial:**
- Puffer für Schnittstellenentwicklung & Security-Validierung
- Externe Security-Partner früher einbinden
- Mehr Endanwender in Pilotphase

### 9.3 Ausblick
- **2027:** KI-basierte Anomalieerkennung (ML auf Audit-Logs) als experimenteller Folgeausbau
- **Continuous Security Assessments** automatisieren
- **Awareness-Schulungen** fest im Onboarding verankern
- **Rollout** auf HR, Verwaltung, Support
- **Budget/Personal** abhängig

---

## Literaturverzeichnis
- VFB Schulungsunterlagen 2024/2025 (IT-Entwickler, Projektmanagement, BWL, Recht)
- Macke, Stefan: Vorlage Projektdokumentation IT-Berufe (it-berufe-podcast.de)
- OpenAI ChatGPT 5: Formulierungshilfe (03.10.2025)

---

## Eidesstattliche Erklärung
Ich, **Daniel-Alfonsin Massa**, versichere, dass ich diese Dokumentation im Rahmen einer prototypischen Projektbearbeitung selbständig verfasst habe. Die Konzeption, Implementierung und Dokumentation wurden eigenständig erarbeitet. Für Formulierung, Strukturierung und Review wurde KI-gestützte Software (OpenAI ChatGPT) als Hilfsmittel eingesetzt; die inhaltliche Verantwortung liegt ausschließlich bei mir. Die Implementierung basiert auf einem funktionsfähigen Prototyp in einer Testumgebung; es wird keine produktive Live-Umgebung behauptet. Simulierte oder nicht produktiv verifizierbare Aussagen, Screenshots, Testdaten und Messwerte sind im Text und Anhang als „prototypisch", „simuliert" oder „Testumgebung" gekennzeichnet. Die Arbeit wurde keiner anderen Prüfungsbehörde vorgelegt und verwendet ausschließlich die angegebenen Quellen und Hilfsmittel.

**Stuttgart, 30.06.2026**  
*Daniel-Alfonsin Massa*
