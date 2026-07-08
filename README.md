# Zero-Trust-Sicherheitskonzept mit GitHub-Integration 🤗

**IHK-Abschlussprojekt: Certified IT Business Manager (Sommer 2026)**  
**Prüfling:** Daniel-Alfonsin Massa (615951)  
**Abgabedatum:** 01.11.2026  
**Enhanced with Hugging Face ML/AI Capabilities**

---

## 📋 Projektübersicht

Einführung eines modernen **Zero-Trust-Sicherheitskonzepts** mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration beim **Verein zur Förderung der Berufsbildung e.V., Ludwigsburg**.

| Bereich | Beschreibung |
|---------|-------------|
| 🔐 **RBAC** | Rollenbasierte Zugriffskontrolle mit Self-Service-Portal |
| 🔄 **GitHub Integration** | Automatisierte Rechtevergabe via GitHub Actions |
| 📋 **Audit-Logs** | Revisionssichere Protokollierung (DSGVO-konform) |
| 🤖 **ML Enhancements** | Anomalieerkennung, Policy-Generierung, Semantische Suche |
| 🖥️ **Self-Service** | Beantragung und Genehmigung von Rollen |

---

## 📂 Projektstruktur

```
zero-trust-github-integration/
│
├── 📄 README.md                          ← Projektübersicht
├── 📄 AI_HANDOFF.md                      ← Projektstatus (intern)
│
├── 📐 docs/
│   ├── 📋 master/                        ← Deckblatt, Verzeichnisse, Glossar
│   ├── 📊 tabellen/                      ← 12 IHK-Tabellen
│   │   ├── 01_zeitplanung_70h.md
│   │   ├── 02_kostenplanung.md
│   │   ├── 03_stakeholdermatrix.md
│   │   ├── 04_risikomatrix.md
│   │   ├── 05_nutzwertanalyse.md
│   │   ├── 06_make_or_buy.md
│   │   ├── 07_anforderungsmatrix.md
│   │   ├── 08_testfallmatrix.md
│   │   ├── 09_soll_ist_vergleich.md
│   │   ├── 10_kommunikationsmatrix.md
│   │   ├── 11_raci_matrix.md
│   │   └── 12_kpi_matrix.md
│   ├── 📉 diagramme/                    ← 10 Mermaid-Diagramme
│   │   ├── 01_projektstrukturplan.md
│   │   ├── 02_use_case_diagramm.md
│   │   ├── 03_github_workflow.md
│   │   ├── 04_rbac_datenmodell.md
│   │   ├── 05_self_service_prozess.md
│   │   ├── 06_schnittstellenuebersicht.md
│   │   ├── 07_abnahmeprozess.md
│   │   ├── 08_risikoprozess.md
│   │   ├── 09_rollout_plan.md
│   │   └── 10_audit_log_prozess.md
│   ├── 🎤 praesentation/                ← Präsentationsgliederung
│   ├── 🖼️ screenshots/                  ← Screenshot-Aufgabenliste
│   ├── 📝 kostenplanung.md
│   └── 📝 projektdokumentation.md
│
│── ⚙️ src/
│   ├── backend/                         ← FastAPI Backend
│   │   ├── app/
│   │   │   ├── api/                     ← REST Endpoints
│   │   │   ├── core/                    ← Config, DB, Security
│   │   │   ├── models/                  ← SQLAlchemy: User, Role, AuditLog, ...
│   │   │   ├── services/
│   │   │   │   ├── rbac_service.py      ← RBAC Engine
│   │   │   │   ├── audit_service.py     ← Audit-Log Service
│   │   │   │   ├── github_service.py    ← GitHub API Integration
│   │   │   │   └── ml_service.py        ← HuggingFace ML Service
│   │   │   └── ml/
│   │   │       ├── anomaly_detector.py  ← Anomalieerkennung
│   │   │       ├── policy_generator.py  ← Policy-Generierung
│   │   │       └── embeddings.py        ← Semantische Suche
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── frontend/                        ← React/TypeScript Webportal
│   │   ├── src/
│   │   ├── package.json
│   │   └── Dockerfile
│   │
│   └── ml/                              ← ML Training & Inference
│       ├── training/
│       ├── inference/
│       └── notebooks/
│
├── 🤗 hf-spaces/                        ← HuggingFace Spaces Demos
│   ├── anomaly-dashboard/               ← Gradio: Anomalieerkennung
│   ├── policy-generator/               ← Gradio: Policy-Generierung
│   └── audit-explorer/                  ← Streamlit: Audit-Suche
│
├── 🚀 .github/workflows/                ← CI/CD Pipelines
│   ├── ci.yml                           ← Lint, Test, Build
│   ├── rbac-workflow.yml                ← RBAC Auto-Provisioning
│   ├── policy-check.yml                 ← Secret Scanning & Policy
│   └── ml-training.yml                  ← ML Training Pipeline
│
├── 🐳 docker-compose.yml                ← Core: Postgres, Redis, Backend, Frontend
├── 🐳 docker-compose.ml.yml             ← ML: MLflow, Anomaly-API, Gradio
│
├── 📦 requirements.txt                  ← Python Dependencies
├── 📦 requirements-ml.txt               ← ML Dependencies
├── 📋 MODEL_CARD.md                     ← ML Model Documentation
└── 🔐 .env.example                      ← Environment Template
```

---

## 🚀 Quick Start

### Projekt erkunden
```bash
# Repo klonen
git clone https://github.com/DonMassa84/zero-trust-github-integration.git
cd zero-trust-github-integration

# Projektdokumentation anzeigen
cat docs/projektdokumentation.md

# IHK-Tabellen anzeigen
ls docs/tabellen/

# Diagramme anzeigen
ls docs/diagramme/
```

### Prototyp starten
```bash
cp .env.example .env
docker compose up -d
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
```

### ML Services starten
```bash
docker compose -f docker-compose.ml.yml up -d
# HF Spaces (Gradio): http://localhost:7860
# MLflow: http://localhost:5000
```

---

## 📊 IHK-Tabellen (12)

| # | Tabelle | Inhalt |
|---|---|------|
| 1 | [Zeitplanung 70h](docs/tabellen/01_zeitplanung_70h.md) | Projektdurchführung in 8 Phasen |
| 2 | [Kostenplanung](docs/tabellen/02_kostenplanung.md) | Kosten + Amortisation |
| 3 | [Stakeholdermatrix](docs/tabellen/03_stakeholdermatrix.md) | Einfluss/Interesse der Beteiligten |
| 4 | [Risikomatrix](docs/tabellen/04_risikomatrix.md) | 7 Risiken bewertet |
| 5 | [Nutzwertanalyse](docs/tabellen/05_nutzwertanalyse.md) | Manuell vs IAM vs GitHub |
| 6 | [Make-or-Buy](docs/tabellen/06_make_or_buy.md) | Entscheidungsmatrix |
| 7 | [Anforderungsmatrix](docs/tabellen/07_anforderungsmatrix.md) | Muss/Kann-Anforderungen |
| 8 | [Testfallmatrix](docs/tabellen/08_testfallmatrix.md) | 12 Testfälle |
| 9 | [Soll-Ist-Vergleich](docs/tabellen/09_soll_ist_vergleich.md) | Zielerreichung |
| 10 | [Kommunikationsmatrix](docs/tabellen/10_kommunikationsmatrix.md) | Reporting-Struktur |
| 11 | [RACI-Matrix](docs/tabellen/11_raci_matrix.md) | Verantwortlichkeiten |
| 12 | [KPI-Matrix](docs/tabellen/12_kpi_matrix.md) | Projekt-Kennzahlen |

---

## 📉 Diagramme (10 Mermaid)

| # | Diagramm | Beschreibung |
|---|---|------|
| 1 | [Projektstrukturplan](docs/diagramme/01_projektstrukturplan.md) | PSP: 6 Hauptphasen |
| 2 | [Use-Case-Diagramm](docs/diagramme/02_use_case_diagramm.md) | Rollenbeantragung, Genehmigung, Audit |
| 3 | [GitHub Workflow](docs/diagramme/03_github_workflow.md) | Actions: Antrag → Policy-Check → Provisioning |
| 4 | [RBAC Datenmodell](docs/diagramme/04_rbac_datenmodell.md) | ERD: User, Role, Permission, AuditLog |
| 5 | [Self-Service Prozess](docs/diagramme/05_self_service_prozess.md) | Sequence: Nutzer → Portal → Admin → Audit |
| 6 | [Schnittstellen](docs/diagramme/06_schnittstellenuebersicht.md) | Architektur-Überblick |
| 7 | [Abnahmeprozess](docs/diagramme/07_abnahmeprozess.md) | Test → Review → Freigabe |
| 8 | [Risikoprozess](docs/diagramme/08_risikoprozess.md) | Erkennung → Bewertung → Maßnahme |
| 9 | [Rollout-Plan](docs/diagramme/09_rollout_plan.md) | Pilot → Phase 1 → Vollausbau |
| 10 | [Audit-Log Prozess](docs/diagramme/10_audit_log_prozess.md) | Event → Speicherung → Auswertung |

---

## 🤗 Hugging Face Integration

### 1. Anomalieerkennung (Audit-Logs)
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="DonMassa84/zero-trust-anomaly-detector")
result = classifier("ROLE_ESCALATION on super-admin-role")
# {'label': 'ANOMALY', 'score': 0.89}
```

### 2. Policy-Generierung (NLP → Rego)
```python
from transformers import pipeline

generator = pipeline("text-generation", model="DonMassa84/zero-trust-policy-generator")
policy = generator("Read-only access for developers on production")
# package zero_trust.policies.readonly
# default allow = false
```

### 3. HF Spaces
- [Anomaly Dashboard](hf-spaces/anomaly-dashboard/) - Gradio UI für Live-Analyse
- [Policy Generator](hf-spaces/policy-generator/) - OPA Rego Generator
- [Audit Explorer](hf-spaces/audit-explorer/) - Semantische Suche

---

## 📐 Architektur

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Frontend   │────▶│   Backend    │────▶│  PostgreSQL   │
│   (React)    │     │  (FastAPI)   │     │  (RBAC, Audit)│
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                    ┌───────┼──────────┐
                    │       │          │
              ┌─────┴┐  ┌──┴──┐  ┌────┴────┐
              │GitHub│  │ OPA │  │Prometheus│
              │Actions│  │Policy│  │  Grafana │
              └──────┘  └─────┘  └─────────┘
                            │
                    ┌───────┴───────┐
                    │   🤗 HF ML   │
                    │  (Anomaly,    │
                    │   Policy,     │
                    │   Embeddings) │
                    └───────────────┘
```

---

## 📈 Projektkennzahlen

| Metrik | Soll | Ist | Status |
|--------|------|-----|--------|
| Gesamtaufwand | 70h | 70h | ✅ |
| Amortisation | 12 Monate | ~11 Monate | ✅ |
| Fehlerrate Rechtevergabe | <2% | 1.2% | ✅ |
| Bearbeitungszeit/Anfrage | <4h | 3.5h | ✅ |
| User Satisfaction | >4/5 | 4.3/5 | ✅ |
| DSGVO-Konformität | 100% | 100% | ✅ |

---

## 📋 Status (Stand: 08.07.2026)

| Bereich | Status | Details |
|---------|--------|---------|
| **Projektstruktur** | ✅ | 33 Dateien, 14 Bereiche |
| **Tabellen** | ✅ | 12/12 IHK-Tabellen |
| **Diagramme** | ✅ | 10/10 Mermaid-Diagramme |
| **Backend Code** | ✅ | FastAPI, RBAC, GitHub, ML |
| **CI/CD** | ✅ | GitHub Actions, Docker |
| **HF Spaces** | ✅ | Anomaly Dashboard, Policy Generator |
| **Screenshots** | 🔴 | 0/9 erstellt |
| **Prüferfragen** | 🔴 | Nicht erstellt |
| **Präsentation** | 🟡 | Gliederung vorhanden |
| **DOCX/PDF Export** | 🔴 | Noch nicht exportiert |

**Gesamt: 🟡 Gelb – Noch nicht einreichungsreif**

---

## 📅 Nächste Schritte

### Diese Woche
1. 🔴 Screenshots erstellen (9 Stück aus Prototyp)
2. 🔴 DOCX/PDF exportieren
3. 🔴 Prüferfragen-Katalog (50+)

### Vor Einreichung (01.11.2026)
4. 🟡 Präsentation ausbauen (Folien + Sprechtext)
5. 🟡 Quellenverzeichnis finalisieren
6. 🟡 Rechtschreibprüfung & Formatierung

---

## 📄 Lizenz & Kontakt

**Prüfling:** Daniel-Alfonsin Massa (615951) · dmassa00@gmail.com  
**Betrieb:** Verein zur Förderung der Berufsbildung e.V., Kurfürstenstraße 6, 71636 Ludwigsburg  
**Prüfung:** Certified IT Business Manager (IHK) · Sommer 2026  
**Abgabe:** 01.11.2026

---

*Projektarbeit zur IHK-Abschlussprüfung · Enhanced with 🤗 Hugging Face*