# Projektdokumentation: Zero-Trust-Sicherheitskonzept mit GitHub-Integration

**Abschlussprüfung Sommer 2026**  
**Certified IT Business Manager (IHK)**

---

## 1. Einleitung

### 1.1 Projektumfeld
Der **Verein zur Förderung der Berufsbildung (VFB)** bietet als gemeinnütziger, regionaler Bildungsträger zahlreiche IHK- und IT-Qualifizierungen an. Mit rund 50 Beschäftigten und hybriden Lernplattformen ist die Digitalisierung zentraler Unternehmensfokus. Ziel ist es, mit effizienten, automatisierten Workflows unter Gewährleistung maximaler IT- und Datenschutzvorgaben innovative Vorreiterrolle einzunehmen.

### 1.2 Projektziel
Implementierung eines modernen **Zero-Trust-Sicherheitskonzepts** mit:
- Automatisierter, rollenbasierter Rechtevergabe (RBAC)
- Nahtloser GitHub-Workflow-Integration
- Revisionssicheren Audit-Protokollen (DSGVO-konform)
- Self-Service-Portal für Benutzeranträge

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

**Gesamt: 70 Stunden**

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
**Entscheidung: Eigenentwicklung**  
Begründung: Höhere Initialkosten, aber:
- Maximale Flexibilität
- Eigentum am Quellcode
- Bessere Integrationsmöglichkeiten
- Keine Vendor-Lock-in

#### 3.2.2 Projektkosten
Hauptkostenblöcke:
- Interne Personalkosten
- Beratungsleistungen (Security/Compliance)
- Cloud- & Monitoring-Lizenzen
- Hardware/Software für Tests

#### 3.2.3 Amortisationsdauer
**~12 Monate** durch:
- Effizienzsteigerungen
- Geringerer Aufwand für Rechtevergabe
- Weniger Support-Tickets
- Schnellere Revisionen

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

### 4.3 Benutzeroberfläche (Mockups)
- Klare Navigation
- Intuitive Beantragung
- Visibilität aller eigenen Rollen/Berechtigungen
- Barrierefreiheit (WCAG 2.1 AA)
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
- **Audit-Logger:** Revisionssichere Protokollierung aller Events

### 4.6 Qualitätssicherung
- Unit Tests (Backend: pytest, Frontend: Vitest)
- Integration Tests (API, DB, GitHub API)
- Security Tests (OWASP ZAP, Trivy, Secret Scanning)
- Code Reviews (min. 2 Reviewer)
- Earned Value Analysis (Controlling)

### 4.7 Pflichtenheft / DSGVO-Konzept
- Art. 32 DSGVO: Technisch-organisatorische Maßnahmen
- Rollentrennung & Verantwortlichkeiten
- Lückenlose Protokollierung (Audit-Logs)
- Datenminimierung & Löschkonzepte
- Verschlüsselung (TLS 1.3, AES-256 at rest)
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

---

## 6. Abnahmephase

### Teststrategie
| Testart | Tool | Abdeckung |
|---------|------|-----------|
| Unit Tests | pytest / Vitest | 95%+ |
| Integration Tests | pytest + Testcontainers | 85% |
| Security Tests | OWASP ZAP, Trivy | Kritische Befunde adressiert |
| E2E Tests | Playwright | Kern-Workflows |

### Abnahmekriterien
✅ Alle Rechteänderungen protokolliert  
✅ Genehmigungs-Workflows funktional  
✅ Self-Service Portal bedienbar  
✅ DSGVO/Compliance dokumentiert  
✅ Audit-Trails vollständig  
✅ Performance <500ms (API)  

### Testfall-Beispiel (Anhang A10)
```
Testfall: TC-RBAC-001 - Rollenbeantragung via Self-Service
Soll: User kann Rolle beantragen → Genehmiger genehmigt → GitHub-Berechtigung gesetzt
Ist:  Erfolgreich durchlaufen, Audit-Log vollständig
Status: BESTANDEN
```

---

## 7. Einführungsphase

### Rollout-Plan (7 Wochen)

| Woche | Phase | Zielgruppe | KPIs |
|-------|-------|------------|------|
| 1-2 | **Pilot** | 15 Nutzer (IT 10, Verw. 5) | Fehlerrate <2%, Bearbeitung <4h, Satisfaction >4/5 |
| 3-4 | **Rollout 1** | 50 Nutzer (HR 25, Finanzen 25) | Manuelle Prozesse als Fallback |
| 5-7 | **Vollausbau** | Alle 50 Mitarbeiter | Manuelle Prozesse deaktiviert, Monitoring |

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
| Automatisierung Rechtevergabe | Vollständig | Vollständig | ✅ |
| Fehlerrate | <2% | ~1.2% (Testphase) | ✅ |
| Bearbeitungszeit | <4h | ~3.5h (Testphase) | ✅ |
| User Satisfaction | >4/5 | ~4.3/5 (Testphase) | ✅ |
| DSGVO-Konformität | Vollständig | Vollständig | ✅ |
| Amortisation | 12 Monate | ~11 Monate | ✅ |

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
Ich, **Daniel-Alfonsin Massa**, versichere, dass ich diese Dokumentation selbständig verfasst und keine anderen als die angegebenen Quellen/Hilfsmittel benutzt habe. Die Arbeit wurde keiner anderen Prüfungsbehörde vorgelegt.

**Stuttgart, 30.06.2026**  
*Daniel-Alfonsin Massa*