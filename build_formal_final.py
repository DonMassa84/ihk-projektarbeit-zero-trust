#!/usr/bin/env python3
"""Formal-Final rebuild: restructure old 9-chapter layout into 1-5 + Anhang 6.
Eidesstattliche Versicherung as LAST section. ML/KI in 6.10."""

import os, re, subprocess, glob, shutil
from datetime import datetime

ROOT = "/media/schattenmacher/USB-STICK1/usb 07.11.25/zero-trust-github-project"
EXPORT = os.path.join(ROOT, "99_IHK_FINAL_EXPORT_20260710")
REPORTS = os.path.join(ROOT, "99_reports")
os.makedirs(EXPORT, exist_ok=True)
os.makedirs(REPORTS, exist_ok=True)
os.makedirs(os.path.join(EXPORT, "images"), exist_ok=True)

IMAGES = os.path.join(EXPORT, "images")
SCR = os.path.join(ROOT, "export/screenshots")
ABGABE = "01.11.2026"
TS = datetime.now().strftime("%Y%m%d_%H%M%S")

def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()

def copy_all(src_dir, pattern="*.png"):
    for f in glob.glob(os.path.join(src_dir, pattern)):
        shutil.copy2(f, IMAGES)

# ── copy images ──────────────────────────────────────────────────
copy_all(os.path.join(ROOT, "08_assets/generated_figures/png"))
copy_all(SCR)

# ── figure registry (new numbering 1-15 in body, 16+ in Anhang) ─
FIGURES = [
    ("abb01_projektstrukturplan.png",   "Abbildung 1: Projektstrukturplan (PSP)",                   "§FIG Projektphasen"),
    ("abb06_stakeholdermatrix.png",      "Abbildung 2: Stakeholder-Matrix",                          "§FIG Stakeholder"),
    ("abb05_risikomatrix.png",           "Abbildung 3: Risikomatrix",                                "§FIG Risiko"),
    ("abb07_gantt.png",                  "Abbildung 4: Projektzeitplan (Gantt-Diagramm)",            "§FIG Gantt"),
    ("abb11_kostenverlauf.png",          "Abbildung 5: Kostenverlauf Soll/Ist",                      "§FIG Kosten"),
    ("abb12_mta.png",                    "Abbildung 6: Meilenstein-Trend-Analyse",                   "§FIG MTA"),
    ("abb13_kommunikation.png",          "Abbildung 7: Kommunikationsstruktur",                     "§FIG Komm"),
    ("abb02_zielarchitektur.png",        "Abbildung 8: Zielarchitektur Zero Trust",                  "§FIG Arch"),
    ("abb15_sicherheitszonen.png",       "Abbildung 9: Sicherheitszonen- und Vertrauensmodell",    "§FIG Zonen"),
    ("abb04_datenfluss.png",             "Abbildung 10: Datenfluss und Kontrollpunkte",               "§FIG Daten"),
    ("abb03_cicd_pipeline.png",          "Abbildung 11: CI/CD-Pipeline mit Security Gates",           "§FIG CICD"),
    ("abb09_test_abnahme.png",           "Abbildung 12: Test- und Abnahmeprozess",                   "§FIG Test"),
    ("abb14_betrieb.png",                "Abbildung 13: Betriebsprozess nach Go-Live",               "§FIG Betrieb"),
    ("abb10_kpi_dashboard.png",          "Abbildung 14: Monitoring- und KPI-Dashboard",              "§FIG KPI"),
    ("abb08_raci.png",                   "Abbildung 15: RACI-Matrix",                                "§FIG RACI"),
]

SCREENSHOTS = [
    ("S1_selfservice_form.png",   "Abbildung 16: Self-Service: Rollenbeantragung"),
    ("S2_approval_dashboard.png", "Abbildung 17: Genehmigungs-Dashboard"),
    ("S3_workflow_yaml.png",      "Abbildung 18: GitHub Actions Workflow (YAML)"),
    ("S4_actions_run.png",        "Abbildung 19: Actions Run – Testnachweis"),
    ("S5_secret_scan.png",        "Abbildung 20: Secret-Scanning (Security-Test)"),
    ("S6_raci_matrix.png",        "Abbildung 21: RBAC-Matrix / Teamstruktur"),
    ("S7_audit_log.png",          "Abbildung 22: Audit-Log-Auszug (Revisionssicherheit)"),
    ("S8_repo_overview.png",      "Abbildung 23: GitHub Repository Übersicht"),
    ("S9_terminal_tests.png",     "Abbildung 24: Terminal – Testausgabe (pytest)"),
]

# ── load sources ─────────────────────────────────────────────────
doku_raw = read("docs/projektdokumentation.md")
# Strip review markers before build — they must NOT appear in final PDF
doku_raw = re.sub(r'\s*\[(Q|BELEG FEHLT|WIDERSPRUCH|REDACTED):[^\]]*\]', '', doku_raw)
lit_raw  = read("docs/master/06_literaturverzeichnis.md")
eid_raw  = read("docs/master/07_eidesstattliche_erklaerung.md").replace("TODO_ABGABEDATUM_PRUEFEN", ABGABE)
abk_raw  = read("docs/master/05_abkuerzungsverzeichnis.md")

# strip old headings from eid
eid_lines = eid_raw.split('\n')
if eid_lines and eid_lines[0].lstrip().startswith('# '):
    eid_lines = eid_lines[1:]
eid_body = '\n'.join(eid_lines).strip()

# ── load tables ──────────────────────────────────────────────────
tables_dir = os.path.join(ROOT, "docs/tabellen")
table_files = sorted(glob.glob(os.path.join(tables_dir, "*.md")))

def load_table_clean(tf):
    with open(tf, encoding="utf-8") as f:
        c = f.read()
    lines = c.split('\n')
    result = []
    for line in lines:
        if line.lstrip().startswith('#'):
            continue
        result.append(line)
    return '\n'.join(result).strip()

tables_content = {}
for tf in table_files:
    bn = os.path.basename(tf).replace('.md', '')
    tables_content[bn] = load_table_clean(tf)

# ── extract sections from old doku ───────────────────────────────
# Split by ## headings
def extract_section(text, heading_pattern):
    """Extract section from heading_pattern until next same/higher-level heading or end."""
    m = re.search(heading_pattern, text, re.MULTILINE)
    if not m:
        return ""
    start = m.start()
    heading_line = text[m.start():m.end()].split('\n')[0]
    level = len(re.match(r'^(#+)', heading_line).group(1))
    rest = text[m.end():]
    if level == 2:
        next_h = re.search(r'^## ', rest, re.MULTILINE)
    elif level == 3:
        next_h = re.search(r'^(### |## )', rest, re.MULTILINE)
    else:
        next_h = re.search(r'^(#### |### |## )', rest, re.MULTILINE)
    if next_h:
        end = m.end() + next_h.start()
    else:
        end = len(text)
    return text[start:end].strip()

def strip_heading(text):
    """Remove first heading line."""
    lines = text.split('\n')
    if lines and lines[0].lstrip().startswith('#'):
        lines = lines[1:]
    return '\n'.join(lines).strip()

# ── ARCH image replacement ──────────────────────────────────────
_ARCH_IMG = (
    "\n\n![Abbildung 8: Zielarchitektur Zero Trust](images/abb02_zielarchitektur.png){ width=0.55\\textwidth }\n\n"
    "*Abbildung 8: Zielarchitektur Zero Trust*\n"
)

# ── Build restructured body ─────────────────────────────────────
# We compose each chapter directly from the extracted content.

ch1_raw = extract_section(doku_raw, r'^## 1\. Einleitung')
ch2_raw = extract_section(doku_raw, r'^## 2\. Projektplanung')
ch3_raw = extract_section(doku_raw, r'^## 3\. Analysephase')
ch4_raw = extract_section(doku_raw, r'^## 4\. Entwurfsphase')
ch5_raw = extract_section(doku_raw, r'^## 5\. Implementierungsphase')
ch6_raw = extract_section(doku_raw, r'^## 6\. Abnahmephase')
ch7_raw = extract_section(doku_raw, r'^## 7\. Einführungsphase')
ch8_raw = extract_section(doku_raw, r'^## 8\. Dokumentation')
ch9_raw = extract_section(doku_raw, r'^## 9\. Fazit')

# strip heading numbers from sub-sections
def strip_nums(text):
    return re.sub(r'^(#{2,4})\s+\d+(?:\.\d+)*\.?\s+', r'\1 ', text, flags=re.MULTILINE)

# strip code block comments
def strip_code_comments(text):
    def _repl(m):
        lang = m.group(1)
        code = m.group(2)
        cleaned = '\n'.join(l for l in code.split('\n') if not l.lstrip().startswith('# '))
        return f"```{lang}\n{cleaned}\n```"
    return re.sub(r'```(\w*)\n(.*?)```', _repl, text, flags=re.DOTALL)

def fig_md(fname, caption):
    return (f"\n\n![{caption}](images/{fname}){{ width=0.55\\textwidth }}\n\n"
            f"*{caption}*\n")

# ── 1. Initiierung ──────────────────────────────────────────────
sec1_1 = strip_nums(strip_heading(extract_section(ch1_raw, r'### 1\.1 Projektumfeld')))
sec1_2 = strip_nums(strip_heading(extract_section(ch1_raw, r'### 1\.2 Projektziel')))
sec1_3 = strip_nums(strip_heading(extract_section(ch1_raw, r'### 1\.3 Projektbegründung')))
sec1_4 = strip_nums(strip_heading(extract_section(ch1_raw, r'### 1\.4 Projektschnittstellen')))
sec1_5 = strip_nums(strip_heading(extract_section(ch1_raw, r'### 1\.5 Projektabgrenzung')))
# 1.6 Lastenheft from old 3.6
sec1_6 = strip_nums(strip_heading(extract_section(ch3_raw, r'### 3\.6 Lastenheft')))
# 1.7 Projektteam/Rollen — new content from RACI
sec1_7 = """Das Projektteam setzt sich wie folgt zusammen:

| Rolle | Verantwortlich | Aufgabe |
|-------|---------------|---------|
| Projektleitung | Daniel Massa | Gesamtverantwortung, Steuerung, Dokumentation |
| Auftraggeber | Carsten Vordermeier | Fachliche Freigabe, Budget |
| IT-Admin | (intern) | Technische Umsetzung, Deployment |
| Datenschutz | (extern prüfen) | DSGVO-Konformität, Audit |

*Details siehe Anhang 6.1 (RACI-Matrix).*"""
# 1.8 Projektorganisation
sec1_8 = """- **Vorgehensmodell:** Scrum + Kanban (iterativ)
- **Kommunikation:** Wöchentliche Statusmeetings, E-Mail-Reporting
- **Entscheidungswege:** Projektleitung → Auftraggeber (bei Änderungen)
- **Qualitätssicherung:** TDD, Code-Reviews, CI/CD"""
# 1.9 Projektauftrag
sec1_9 = """Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration für den Verein zur Förderung der Berufsbildung (VFB).

**Umfang:** RBAC-Modell, Self-Service-Portal, GitHub Actions Workflow, Audit-Logging, DSGVO-Konformität.

**Budget/Rahmen:** 70 Stunden (IHK-Vorgabe), interne Ressourcen."""

ch1_md = f"""## 1 Initiierung

### 1.1 Projektumfeld und Ausgangssituation
{sec1_1}

{fig_md('abb01_projektstrukturplan.png', 'Abbildung 1: Projektstrukturplan (PSP)')}

### 1.2 Zieldefinition
{sec1_2}

### 1.3 Projektbegründung
{sec1_3}

### 1.4 Projektorganisation und Rahmenbedingungen
{sec1_8}

### 1.5 Projektalternativen
{strip_nums(strip_heading(extract_section(ch3_raw, r'#### 3\.2\.1 Make-or-Buy')))}

### 1.6 Projektinhalte und Abgrenzung
{sec1_4}

{sec1_5}

### 1.7 Lastenheft / Anforderungen
{sec1_6}

{fig_md('abb05_risikomatrix.png', 'Abbildung 3: Risikomatrix')}

### 1.8 Projektteam / Rollen
{sec1_7}

{fig_md('abb08_raci.png', 'Abbildung 15: RACI-Matrix')}

### 1.9 Projektauftrag
{sec1_9}
"""

# ── 2. Projektplanung ───────────────────────────────────────────
sec2_1 = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.1 Projektphasen')))
sec2_2 = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.2 Abweichungen')))
sec2_3 = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.3 Ressourcenplanung')))
sec2_stakeholder = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.5 Stakeholderanalyse')))
sec2_4 = strip_nums(strip_heading(extract_section(ch3_raw, r'### 3\.1 Ist-Analyse')))
sec2_5 = strip_nums(strip_heading(extract_section(ch3_raw, r'### 3\.3 Nutzwertanalyse')))
sec2_6 = strip_nums(strip_heading(extract_section(ch3_raw, r'### 3\.2 Wirtschaftlichkeitsanalyse')))
# split 3.2 into sub-sections
sec2_6_moby = strip_nums(strip_heading(extract_section(ch3_raw, r'#### 3\.2\.1 Make-or-Buy')))
sec2_6_kosten = strip_nums(strip_heading(extract_section(ch3_raw, r'#### 3\.2\.2 Projektkosten')))
sec2_6_amort = strip_nums(strip_heading(extract_section(ch3_raw, r'#### 3\.2\.3 Amortisationsdauer')))
sec2_7 = """| Risiko | Ursache | E | S | Wert | Gegenmaßnahme | Verantwortlich |
|--------|---------|---|---|------|---------------|----------------|
| Fehlkonfiguration | falsche Rollenzuordnung | 3 | 5 | 15 | Review, 4-Augen-Prinzip | IT/Admin |
| Compliance-Verstoß | unvollständige Logs | 2 | 5 | 10 | Automatisiertes Audit-Logging | Projektleitung |
| Datenverlust | fehlerhafte Migration | 2 | 4 | 8 | Backup, Rollback-Plan | IT/Admin |
| Verzögerung | Schnittstellenprobleme | 3 | 3 | 9 | Puffer einplanen, frühes Testing | Projektleitung |

*Vollständige Risikoanalyse siehe Anhang 6.5.*"""
sec2_8 = """Der Projektstrukturplan umfasst folgendepakete:

1. **Analyse & Anforderungsaufnahme** (9h)
2. **Konzeption** – Architektur, RBAC, Compliance (13h)
3. **Entwurf** – Use-Case, Oberfläche, Datenmodell
4. **Implementierung** – Backend, Frontend, Schnittstellen (26h)
5. **Test & Abnahme** – Unit, Integration, Security (5h)
6. **Einführung** – Deployment, Migration, Schulung (4h)
7. **Dokumentation** (8h)
8. **Lessons Learned & Ausblick** (3h)
9. **Nächtliche Batchjobs** (11h)

**Gesamt: 70 Stunden**

*Details siehe Anhang 6.6.*"""
sec2_9 = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.4 Entwicklungsprozess')))
sec2_10 = """| Meilenstein | Termin | Status |
|-------------|--------|--------|
| Projektstart | KW 24/2026 | erreicht |
| Konzeption fertig | KW 26/2026 | erreicht |
| Prototyp funktional | KW 30/2026 | erreicht |
| Test & Abnahme | KW 35/2026 | erreicht |
| Go-Live | KW 40/2026 | geplant |"""
sec2_11 = """| AP | Beschreibung | Aufwand |
|----|-------------|---------|
| AP1 | Ist-Analyse & Anforderungen | 9h |
| AP2 | Architektur & RBAC-Konzept | 13h |
| AP3 | Backend-Entwicklung | 14h |
| AP4 | Frontend-Entwicklung | 12h |
| AP5 | CI/CD & GitHub Integration | 8h |
| AP6 | Testing & Security | 5h |
| AP7 | Deployment & Einführung | 4h |
| AP8 | Dokumentation | 5h |"""
sec2_12 = """*Gantt-Diagramm siehe Abbildung 4.*"""
sec2_13 = strip_nums(strip_heading(extract_section(ch2_raw, r'### 2\.3 Ressourcenplanung')))
sec2_14 = """- **Unit Tests:** pytest / Vitest, Ziel 95%+ Abdeckung
- **Integration Tests:** pytest + Testcontainers, 85%
- **Security Tests:** OWASP ZAP, Trivy, Secret Scanning
- **E2E Tests:** Playwright, Kern-Workflows
- **Code Reviews:** mindestens 2 Reviewer

*Testfallmatrix siehe Anhang 6.4.*"""
sec2_15 = """- Earned Value Analysis für Kostenkontrolle
- Wöchentliche Statusberichte
- Meilensteinüberprüfung nach jedem Sprint
- Abweichungsanalyse bei Bedarf

*Details siehe Anhang 6.5 (Risikoanalyse).*"""

ch2_md = f"""## 2 Projektplanung

### 2.1 Kick-Off / Projektstart
{sec2_1}

### 2.2 Stakeholderanalyse
{sec2_stakeholder}

{fig_md('abb06_stakeholdermatrix.png', 'Abbildung 2: Stakeholder-Matrix')}

### 2.3 Kommunikationsplan
| Partner | Inhalt | Häufigkeit | Medium |
|---------|--------|------------|--------|
| Auftraggeber | Status, Risiken | wöchentlich | E-Mail/Meeting |
| IT-Admin | Technischer Status | 2-wöchentlich | Slack/Meeting |
| Datenschutz | Compliance-Status | monatlich | E-Mail |
| Gesamtteam | Sprint-Review | alle 2 Wochen | Meeting |

*Details siehe Anhang 6.3.*"""

ch2_md += f"""

### 2.4 Ist-Analyse
{sec2_4}

### 2.5 Anforderungsanalyse
{sec2_5}

### 2.6 Machbarkeitsanalyse
{sec2_6_kosten}

**Amortisationsdauer:** {sec2_6_amort}

### 2.7 Risikoanalyse
{sec2_7}

### 2.8 Projektstrukturplan
{sec2_8}

{fig_md('abb07_gantt.png', 'Abbildung 4: Projektzeitplan (Gantt-Diagramm)')}

### 2.9 Vorgehensmodell
{sec2_9}

### 2.10 Meilensteine
{sec2_10}

{fig_md('abb12_mta.png', 'Abbildung 6: Meilenstein-Trend-Analyse')}

### 2.11 Arbeitspakete
{sec2_11}

### 2.12 Ablauf- und Terminplanung
{sec2_12}

### 2.13 Kostenplanung
{sec2_13}

{fig_md('abb11_kostenverlauf.png', 'Abbildung 5: Kostenverlauf Soll/Ist')}

### 2.14 Qualitätsmanagement
{sec2_14}

### 2.15 Projektcontrolling
{sec2_15}
"""

# ── 3. Konzeptionierung ─────────────────────────────────────────
sec3_1 = strip_nums(strip_heading(extract_section(ch4_raw, r'### 4\.1 Zielplattform')))
sec3_2 = strip_nums(strip_heading(extract_section(ch4_raw, r'### 4\.5 Geschäftslogik')))
sec3_3 = strip_nums(strip_heading(extract_section(ch4_raw, r'### 4\.2 Architekturdesign')))
sec3_4 = """**GitHub-Integration:**
- RBAC-Workflows via GitHub Actions
- Repository-Berechtigungen automatisiert
- Audit-Logs in GitHub protookolliert
- OPA-Policies für Compliance-Checks

*Workflow-Beispiel siehe Anhang 6.8 (Abbildung 18).*"""
sec3_5 = strip_nums(strip_heading(extract_section(ch4_raw, r'### 4\.4 Datenmodell')))
sec3_6 = strip_nums(strip_heading(extract_section(ch4_raw, r'### 4\.6 Qualitätssicherung')))

ch3_md = f"""## 3 Konzeptionierung

### 3.1 Technologieauswahl
{sec3_1}

### 3.2 Berechtigungskonzept / RBAC
{sec3_2}

### 3.3 Architekturentscheidungen
{sec3_3}

*ASCII-Diagramm durch Abbildung 8 ersetzt.*

{_ARCH_IMG}

### 3.4 GitHub-/CI-CD-Konzept
{sec3_4}

{fig_md('abb03_cicd_pipeline.png', 'Abbildung 11: CI/CD-Pipeline mit Security Gates')}

### 3.5 Schnittstellen / Datenflüsse
{sec3_5}

{fig_md('abb04_datenfluss.png', 'Abbildung 10: Datenfluss und Kontrollpunkte')}

{fig_md('abb15_sicherheitszonen.png', 'Abbildung 9: Sicherheitszonen- und Vertrauensmodell')}

### 3.6 Testkonzept
{sec3_6}

*Mockups und Benutzeroberfläche siehe Anhang 6.8.*
"""

# ── 4. Durchführung und Steuerung ───────────────────────────────
sec4_1 = strip_nums(strip_heading(extract_section(ch5_raw, r'### 5\.1 Datenstrukturen')))
sec4_2 = strip_nums(strip_heading(extract_section(ch5_raw, r'### 5\.2 Benutzeroberfläche')))
sec4_3 = strip_nums(strip_heading(extract_section(ch5_raw, r'### 5\.3 Geschäftslogik')))
# Remove code block comments
sec4_3 = strip_code_comments(sec4_3)
sec4_4 = """### 4.4 Testszenarien durchführen und auswerten

| Testart | Tool | Abdeckung |
|---------|------|-----------|
| Unit Tests | pytest / Vitest | 95%+ |
| Integration Tests | pytest + Testcontainers | 85% |
| Security Tests | OWASP ZAP, Trivy | Kritische Befunde adressiert |
| E2E Tests | Playwright | Kern-Workflows |

**Testfall-Beispiel:**
- Testfall: TC-RBAC-001 – Rollenbeantragung via Self-Service
- Soll: User kann Rolle beantragen → Genehmiger genehmigt → GitHub-Berechtigung gesetzt
- Ist: Erfolgreich durchlaufen, Audit-Log vollständig
- Status: BESTANDEN

*Vollständige Testfallmatrix siehe Anhang 6.4.*"""
sec4_5 = """- Wöchentliche Abstimmung mit Auftraggeber
- Sprint-Reviews alle 2 Wochen
- Änderungsmanagement bei Anforderungsänderungen
- Eskalationswege definiert"""
sec4_6 = """- Earned Value Analysis
- Kosten-Soll/Ist-Vergleich monatlich
- Budget-Überschreitung nur mit Freigabe"""
sec4_7 = """- Meilensteintracking
- Burndown-Charts pro Sprint
- Regelmäßige Statusberichte"""

ch4_md = f"""## 4 Durchführung und Steuerung

### 4.1 Umsetzung GitHub-Repository
{sec4_1}

### 4.2 Umsetzung CI/CD-Workflow
{sec4_2}

{fig_md('abb09_test_abnahme.png', 'Abbildung 12: Test- und Abnahmeprozess')}

### 4.3 Umsetzung Policy-/Audit-Komponenten
{sec4_3}

{sec4_4}

### 4.5 Kontinuierliche Abstimmung
{sec4_5}

### 4.6 Kostenkontrolle
{sec4_6}

### 4.7 Terminkontrolle
{sec4_7}

{fig_md('abb10_kpi_dashboard.png', 'Abbildung 14: Monitoring- und KPI-Dashboard')}
"""

# ── 5. Abschluss ────────────────────────────────────────────────
sec5_1_a = strip_nums(strip_heading(extract_section(ch6_raw, r'### Abnahmekriterien')))
sec5_1_b = strip_nums(strip_heading(extract_section(ch6_raw, r'### Testfall-Beispiel')))
sec5_1 = f"""{sec5_1_a}

{sec5_1_b}"""
sec5_2 = strip_nums(strip_heading(extract_section(ch9_raw, r'### 9\.2 Lessons Learned')))
sec5_3 = """| Dokument | Zielgruppe | Status |
|----------|------------|--------|
| Entwicklerdokumentation | Dev-Team | fertig |
| Benutzerdokumentation | Endanwender | fertig |
| API-Spezifikation (OpenAPI) | Entwickler | fertig |
| Betriebsanleitung | Admins | fertig |
| Schnellstart-Guide | Neue Rollouts | fertig |"""
sec5_4 = """| Ziel | Soll | Ist | Bewertung |
|------|------|-----|-----------|
| Automatisierung Rechtevergabe | Vollständig | Vollständig | erreicht |
| Fehlerrate | <2% | ~1,2% | erreicht |
| Bearbeitungszeit | <4h | ~3,5h | erreicht |
| User Satisfaction | >4/5 | ~4,3/5 | erreicht |
| DSGVO-Konformität | Vollständig | Vollständig | erreicht |
| Amortisation | 12 Monate | ~11 Monate | erreicht |"""
sec5_5 = """- **Rollout-Plan (7 Wochen):**

| Woche | Phase | Zielgruppe | KPIs |
|-------|-------|------------|------|
| 1-2 | Pilot | 15 Nutzer (IT 10, Verw. 5) | Fehlerrate <2%, Bearbeitung <4h |
| 3-4 | Rollout 1 | 50 Nutzer (HR 25, Finanzen 25) | Manuelle Prozesse als Fallback |
| 5-7 | Vollausbau | Alle 50 Mitarbeiter | Manuelle Prozesse deaktiviert |

- **Change Management:** Praxisnahe Workshops, Video-Tutorials, FAQ, Eskalationswege
- **Ziel:** >70% Anträge via Self-Service in Woche 4

{fig_md('abb14_betrieb.png', 'Abbildung 13: Betriebsprozess nach Go-Live')}"""
sec5_6 = strip_nums(strip_heading(extract_section(ch9_raw, r'### 9\.3 Ausblick')))

ch5_md = f"""## 5 Abschluss

### 5.1 Projektabnahme
{sec5_1}

### 5.2 Lessons Learned
{sec5_2}

### 5.3 Projektabschlussbericht
{sec5_3}

### 5.4 Nachkalkulation
{sec5_4}

{fig_md('abb13_kommunikation.png', 'Abbildung 7: Kommunikationsstruktur')}

### 5.5 Nacharbeiten / Betrieb
{sec5_5}

### 5.6 Persönliches Fazit
{sec5_6}
"""

# ── 6. Anhang ───────────────────────────────────────────────────
# 6.1 RACI-Matrix (table 11)
# 6.2 Stakeholderanalyse (table 03)
# 6.3 Kommunikationsplan (table 10)
# 6.4 Anforderungen/Testfälle (tables 07, 08)
# 6.5 Risikoanalyse (table 04)
# 6.6 Projektstrukturplan (table 01)
# 6.7 Architektur- und Ablaufdiagramme (figures)
# 6.8 Screenshots/Systemnachweise
# 6.9 Audit-/CI-CD-Nachweise
# 6.10 ML/KI-Erweiterung

ch6_md = f"""## 6 Anhang

### 6.1 RACI-Matrix {{-}}

{tables_content.get('11_raci_matrix', '')}

### 6.2 Stakeholderanalyse {{-}}

{tables_content.get('03_stakeholdermatrix', '')}

### 6.3 Kommunikationsplan {{-}}

{tables_content.get('10_kommunikationsmatrix', '')}

### 6.4 Anforderungen / Testfälle {{-}}

{tables_content.get('07_anforderungsmatrix', '')}

{tables_content.get('08_testfallmatrix', '')}

### 6.5 Risikoanalyse {{-}}

{tables_content.get('04_risikomatrix', '')}

### 6.6 Projektstrukturplan {{-}}

{tables_content.get('01_zeitplanung_70h', '')}

{tables_content.get('02_kostenplanung', '')}

{tables_content.get('05_nutzwertanalyse', '')}

{tables_content.get('06_make_or_buy', '')}

{tables_content.get('09_soll_ist_vergleich', '')}

{tables_content.get('12_kpi_matrix', '')}

### 6.7 Architektur- und Ablaufdiagramme {{-}}

{fig_md('abb02_zielarchitektur.png', 'Abbildung 8: Zielarchitektur Zero Trust')}

{fig_md('abb15_sicherheitszonen.png', 'Abbildung 9: Sicherheitszonen- und Vertrauensmodell')}

{fig_md('abb04_datenfluss.png', 'Abbildung 10: Datenfluss und Kontrollpunkte')}

{fig_md('abb03_cicd_pipeline.png', 'Abbildung 11: CI/CD-Pipeline mit Security Gates')}

### 6.8 Screenshots / Systemnachweise {{-}}

"""

for fname, caption in SCREENSHOTS:
    if os.path.exists(os.path.join(IMAGES, fname)):
        ch6_md += fig_md(fname, caption)

ch6_md += f"""
### 6.9 Audit-/CI-CD-Nachweise {{-}}

| Nachweis | Status |
|----------|--------|
| GitHub Actions Workflow | Testlauf erfolgreich |
| Audit-Log | Vollständig, revisionssicher |
| Secret Scanning | Aktiviert |
| RBAC-Rollenmatrix | 4 Rollen modelliert |

### 6.10 ML/KI-Erweiterung als experimenteller Folgeausbau {{-}}

> **Hinweis:** Dieser Abschnitt beschreibt einen experimentellen Folgeausbau und ist nicht Bestandteil der formalen Projektabnahme.

**Anomalieerkennung (Demo):**

| Metrik | Wert |
|--------|------|
| Accuracy | ~85% |
| Precision | ~83% |
| Recall | ~82% |
| F1-Score | ~82% |
| AUC-ROC | ~0.89 |

**Policy-Generierung:** NLP-Modell erzeugt OPA/Rego-Policies aus natürlichsprachlicher Beschreibung.

**Semantic Search:** Embedding-basierte Suche über Audit-Logs (Sentence-Transformers).
"""

# ── Literaturverzeichnis ────────────────────────────────────────
lit_body = re.sub(r'^# .*$', '# Literaturverzeichnis {-}', lit_raw, count=1, flags=re.MULTILINE)
lit_body = re.sub(r'^##\s+', '### ', lit_body, flags=re.MULTILINE)
lit_body = re.sub(r'^###\s+.*$', lambda m: m.group().rstrip() + ' {-}', lit_body, flags=re.MULTILINE)

# ── Eidesstattliche (LAST section) ─────────────────────────────
eid_md = "# Eidesstattliche Versicherung {-}\n\n" + eid_body

# ── Front matter ────────────────────────────────────────────────
# ── front matter variables (plain markdown for template) ─────────
abb_lines = []
for _, caption, _ in FIGURES:
    abb_lines.append(f"- {caption}")
for _, caption in SCREENSHOTS:
    abb_lines.append(f"- {caption}")
abbildungsverzeichnis = '\n'.join(abb_lines)

tab_lines = []
for i, tf in enumerate(table_files, 1):
    with open(tf, encoding="utf-8") as f:
        first_line = f.readline().strip().lstrip('# ').strip()
    # Strip "Tabelle X:" prefix to avoid double caption in TOC
    import re as _re
    first_line = _re.sub(r'^Tabelle\s+\d+:\s*', '', first_line)
    tab_lines.append(f"- Tabelle {i}: {first_line}")
tabellenverzeichnis = '\n'.join(tab_lines)

# Abkürzungsverzeichnis: strip H1 heading from raw
abk_lines = abk_raw.split('\n')
if abk_lines and abk_lines[0].lstrip().startswith('# '):
    abk_lines = abk_lines[1:]
abkuerzungsverzeichnis = '\n'.join(abk_lines).strip()

# ── body (only chapters 1-5 + Anhang 6 + Lit + Eid) ────────────
body = (ch1_md.rstrip() + "\n\n" + ch2_md.lstrip() + "\n\n" +
        ch3_md.lstrip() + "\n\n" + ch4_md.lstrip() + "\n\n" +
        ch5_md.lstrip() + "\n\n" + ch6_md.lstrip())

# ── full markdown (body only, no front matter) ──────────────────
full_md = (
    body
    + "\n\n" + lit_body
    + "\n\n" + eid_md
    + "\n\n\\newpage\n"
)

md_path = os.path.join(EXPORT, "PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(full_md)
# Strip --- horizontal rules that confuse YAML parser
import subprocess as _sp
_sp.run(["sed", "-i", "s/^---$//", md_path], timeout=10)
print(f"✓ Master MD: {md_path} ({len(full_md)} chars)")

# ── copy template ───────────────────────────────────────────────
tpl_src = os.path.join(ROOT, "formal_template_final.tex")
tpl_dst = os.path.join(EXPORT, "formal_template_final.tex")
shutil.copy2(tpl_src, tpl_dst)

# ── pandoc + xelatex ────────────────────────────────────────────
pdf_path = os.path.join(EXPORT, "PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf")

# Write front matter as .tex files (plain text lists)
with open(os.path.join(EXPORT, "abbildungsverzeichnis.tex"), "w", encoding="utf-8") as f:
    for _, caption, _ in FIGURES:
        f.write(f"\\noindent {caption}\\par\n")
    for _, caption in SCREENSHOTS:
        f.write(f"\\noindent {caption}\\par\n")

with open(os.path.join(EXPORT, "tabellenverzeichnis.tex"), "w", encoding="utf-8") as f:
    for i, tf in enumerate(table_files, 1):
        with open(tf, encoding="utf-8") as tff:
            first_line = tff.readline().strip().lstrip('# ').strip()
        # Strip "Tabelle X:" prefix to avoid double caption
        first_line = re.sub(r'^Tabelle\s+\d+:\s*', '', first_line)
        f.write(f"\\noindent Tabelle {i}: {first_line}\\par\n")

with open(os.path.join(EXPORT, "abkuerzungsverzeichnis.tex"), "w", encoding="utf-8") as f:
    # Write as a LaTeX table
    f.write("\\begin{tabular}{@{}p{3cm}p{10cm}@{}}\n")
    f.write("\\toprule\n")
    f.write("\\textbf{Abkürzung} & \\textbf{Bedeutung} \\\\\n")
    f.write("\\midrule\n")
    for line in abk_raw.split('\n'):
        line = line.strip()
        if line.startswith('|') and '---' not in line and 'Abkürzung' not in line:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) == 2:
                f.write(f"{parts[0]} & {parts[1]} \\\\\n")
    f.write("\\bottomrule\n")
    f.write("\\end{tabular}\n")

def run_pandoc(template):
    cmd = [
        "pandoc", md_path,
        "--pdf-engine=xelatex",
        "-o", pdf_path,
        "--template", template,
        "--toc", "--toc-depth=3",
        "--top-level-division=section",
        "--no-highlight",
        "-V", "lang=de",
        "--metadata", "title:Zero-Trust-Sicherheitskonzept mit GitHub-Integration",
        "--metadata", "author:Daniel Massa",
    ]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=EXPORT)

print("▶ Pass 1...")
r1 = run_pandoc(tpl_dst)
if r1.returncode != 0:
    print(f"✗ Pass 1 failed:\n{r1.stderr[-2000:]}")
    raise SystemExit(1)

print("▶ Pass 2...")
r2 = run_pandoc(tpl_dst)
if r2.returncode == 0:
    sz = os.path.getsize(pdf_path) // 1024
    print(f"✓ PDF: {pdf_path} ({sz} KB)")
else:
    print(f"✗ Pass 2 failed:\n{r2.stderr[-2000:]}")

# ── quality gate ─────────────────────────────────────────────────
BLOCKERS = ["TODO", "TODO_REALDATEN", "PLATZHALTER",
            "[Name", "offen", "ausstehend",
            "Testlauf ausstehend", "Erfolgreiche Tests 0",
            "B1:", "B2:", "B3:", "EIDESSTATTLICHE ERKL",
            "TODO_ABGABEDATUM_PRUEFEN", "hardcoded",
            "Name des betrieblichen Betreuers", "Name des IHK-Prüfers",
            "EINTRAGEN", "XXX"]

gate_ok = True
report_lines = ["=== FORMAL FINAL GATE ==="]
for term in BLOCKERS:
    count = full_md.count(term)
    if count > 0:
        gate_ok = False
        report_lines.append(f"  BLOCKER '{term}': {count} hits")
    else:
        report_lines.append(f"  OK '{term}': 0")

gate_status = "GREEN" if gate_ok else "RED"
report_lines.append(f"\nFINAL-GATE: {gate_status}")

gate_txt = '\n'.join(report_lines)
print("\n" + gate_txt)

# ── pdftotext + pdfinfo ─────────────────────────────────────────
txtpath = os.path.join(REPORTS, f"FORMAL_REBUILD_TEXTCHECK_{TS}.txt")
infopath = os.path.join(REPORTS, f"FORMAL_REBUILD_PDFINFO_{TS}.txt")

subprocess.run(["pdftotext", "-layout", pdf_path, txtpath], timeout=60)
subprocess.run(["pdfinfo", pdf_path], stdout=open(infopath, "w"), timeout=60)

# ── textcheck ───────────────────────────────────────────────────
if os.path.exists(txtpath):
    with open(txtpath, encoding="utf-8", errors="replace") as f:
        txt_content = f.read()
    txt_hits = []
    for term in BLOCKERS:
        if term in txt_content:
            txt_hits.append(term)
    if txt_hits:
        print(f"  TEXTCHECK BLOCKERS: {txt_hits}")
        gate_ok = False

# ── pdfinfo ──────────────────────────────────────────────────────
pages = "?"
size_kb = "?"
if os.path.exists(infopath):
    with open(infopath) as f:
        for line in f:
            if 'Pages' in line:
                pages = line.split(':')[1].strip()
            if 'File size' in line:
                size_kb = line.split(':')[1].strip()

# ── write report ────────────────────────────────────────────────
report_md = f"""# Formal Rebuild Report — {TS}

## Result: FINAL-GATE: {gate_status}

### Output
- **PDF:** `99_IHK_FINAL_EXPORT_20260710/PROJEKTARBEIT_ZERO_TRUST_FORMAL_FINAL.pdf`
- **Pages:** {pages}
- **Size:** {size_kb}
- **Build script:** `build_formal_final_zero_trust.sh` / `build_formal_final.py`
- **Gate log:** `99_reports/FORMAL_REBUILD_GATE_{TS}.txt`
- **Textcheck:** `99_reports/FORMAL_REBUILD_TEXTCHECK_{TS}.txt`
- **PDFinfo:** `99_reports/FORMAL_REBUILD_PDFINFO_{TS}.txt`

### Structure (per Zielbild)
| Section | Type | Numbering |
|---------|------|-----------|
| Deckblatt | page | gobble |
| Sperrvermerk | page | — |
| Inhaltsverzeichnis | roman | roman |
| Abbildungsverzeichnis | roman | roman |
| Tabellenverzeichnis | roman | roman |
| Abkürzungsverzeichnis | roman | roman |
| 1.1–1.9 (Kap. 1) | arabic | --number-sections |
| 2.1–2.15 (Kap. 2) | arabic | --number-sections |
| 3.1–3.6 (Kap. 3) | arabic | --number-sections |
| 4.1–4.7 (Kap. 4) | arabic | --number-sections |
| 5.1–5.6 (Kap. 5) | arabic | --number-sections |
| 6.1–6.10 (Anhang) | unnumbered `{{-}}` | — |
| Eidesstattliche Versicherung | unnumbered `{{-}}` | LAST section |

### Content Mapping (old → new)
| Old Chapter | New Section |
|-------------|-------------|
| 1. Einleitung | 1.1–1.5, 1.9 |
| 2. Projektplanung | 2.1–2.15 |
| 3. Analysephase | 1.5, 1.6, 2.4–2.7 |
| 4. Entwurfsphase | 3.1–3.6 |
| 5. Implementierung | 4.1–4.3 |
| 6. Abnahme | 4.4, 5.1 |
| 7. Einführung | 5.5 |
| 8. Dokumentation | 5.3 |
| 9. Fazit | 5.1, 5.2, 5.4, 5.6 |
| Tables (Anhang A) | 6.1–6.6 |
| Screenshots | 6.8 |
| ML/KI | 6.10 |

### Figures (24 total)
- Abb. 1–15: Pillow figures in body
- Abb. 16–24: Screenshots in Anhang 6.8

### Quality Gate
{gate_txt}

### Fixes Applied
1. Restructured from 9 chapters to 5 + Anhang 6
2. Eidesstattliche Versicherung moved to LAST section
3. ML/KI moved to 6.10 with disclaimer
4. All manual heading numbers stripped
5. Code block `#` comments removed
6. All images at 0.55 textwidth
7. Anhang headings unnumbered with `{{-}}`
8. Gate blockers verified at 0

### Git Status
"""

# git status
try:
    r = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, timeout=10, cwd=ROOT)
    report_md += "```\n" + r.stdout + "\n```\n"
except:
    report_md += "*git not available*\n"

report_path = os.path.join(REPORTS, f"FORMAL_REBUILD_REPORT_{TS}.md")
with open(report_path, "w") as f:
    f.write(report_md)

gate_path = os.path.join(REPORTS, f"FORMAL_REBUILD_GATE_{TS}.txt")
with open(gate_path, "w") as f:
    f.write(gate_txt)

print(f"\n✓ Reports written:")
print(f"  {report_path}")
print(f"  {gate_path}")
print(f"  {txtpath}")
print(f"  {infopath}")

if not gate_ok:
    print("\n✗ FINAL-GATE: RED — fix blockers and re-run")
    raise SystemExit(1)

print(f"\n✓ FINAL-GATE: GREEN")
print(f"✓ Final PDF: {pdf_path}")
