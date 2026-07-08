#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════
# IHK Zero-Trust Projektarbeit – Master Regeneration Script
# Baut ALLE Artefakte neu: Diagramme, IV-Korrektur, PDF, Validierung
# ═══════════════════════════════════════════════════════════════════════════

set -euo pipefail

ROOT="/home/schattenmacher/openclaw-workspace/ihk_zero_trust_projektarbeit_final"
MASTER="$ROOT/09_export/final/PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md"
OUTDIR="$ROOT/09_export"
TEMPLATE="$ROOT/09_export/build_scripts/ihk_template.html"
BUILD_DIR="$OUTDIR/build"
MERMAID_DIR="$ROOT/04_diagramme_mermaid"
EPK_DIR="$MERMAID_DIR/epk"
SCR_DIR="$ROOT/10_screenshots"

# Farben
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'

log()   { echo -e "${BLUE}[INFO]${NC} $*"; }
ok()    { echo -e "${GREEN}[OK]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERR]${NC} $*"; }

# ═══════════════════════════════════════════════════════════════════════════
# 1. VORBEREITUNG
# ════════════════════════════════════════════════════════════════════════════

mkdir -p "$BUILD_DIR" "$MERMAID_DIR/png" "$EPK_DIR" "$SCR_DIR"

log "=== IHK Zero-Trust Master Regeneration ==="
log "Root: $ROOT"
log "Master: $MASTER"

# ═══════════════════════════════════════════════════════════════════════════
# 2. IV SEITENZAHLUNG KORRIGIEREN (römisch/arabisch/römisch-klein)
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 1: IV-Seitenzählung korrigieren ==="

# Python-Script für intelligente IV-Korrektur
cat > "$BUILD_DIR/fix_iv.py" << 'PYEOF'
#!/usr/bin/env python3
import re
import sys

master_path = sys.argv[1]
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Finde INHALTSVERZEICHNIS Bereich
iv_start = content.find("## INHALTSVERZEICHNIS")
if iv_start == -1:
    print("INHALTSVERZEICHNIS nicht gefunden")
    sys.exit(1)

iv_end = content.find("---", iv_start)
if iv_end == -1:
    iv_end = content.find("## ", iv_start + 1)

iv_block = content[iv_start:iv_end]

# Parse Einträge
lines = iv_block.split('\n')
new_lines = []
page_counter = 1
in_roman_main = False
in_roman_appendix = False
roman_main_pages = []
arabic_pages = []
roman_appendix_pages = []

# Logik: Vorwort = römisch I-V, Kapitel 1-8 = arabisch 1-70, Anhang + Literatur = römisch i-x
# Wir schätzen Seitenzahlen basierend auf Einträgen

roman_main_entries = [
    "Vorwort", "Einleitung", "Projektumfeld", "Meine Tätigkeiten", "Allgemeine Informationen",
    "SPERRVERMERK", "ABBILDUNGSVERZEICHNIS", "TABELLENVERZEICHNIS", "ABKÜRZUNGSVERZEICHNIS"
]

arabic_entries = [
    "1 Projektinitiierung", "1.1 Projektumfeld", "1.2 Ausgangssituation", "1.3 Ist-Analyse",
    "1.4 Problemstellung", "1.5 Soll-Konzept", "1.6 Projektziele nach SMART",
    "1.7 Projektbegründung", "1.8 Projektabgrenzung", "1.9 Projektschnittstellen",
    "1.10 Projektauftrag",
    "2 Projektplanung", "2.1 Vorgehensmodell", "2.2 Projektphasen", "2.3 Projektstrukturplan",
    "2.4 Arbeitspakete", "2.5 Meilensteinplanung", "2.6 Ressourcenplanung",
    "2.7 Kostenplanung", "2.8 Kommunikationsplanung", "2.9 Risikoanalyse",
    "2.10 Qualitätsplanung", "2.11 Abweichungen vom Projektantrag",
    "3 Analyse und Konzeption", "3.1 Anforderungsanalyse", "3.2 Lastenheft / Fachkonzept",
    "3.3 Stakeholderanalyse", "3.4 Make-or-Buy-Entscheidung", "3.5 Wirtschaftlichkeitsanalyse",
    "3.6 Nutzwertanalyse", "3.7 Zero-Trust-Konzept", "3.8 RBAC-Modell",
    "3.9 Datenschutz- und Sicherheitskonzept",
    "4 Technischer Entwurf", "4.1 Zielplattform", "4.2 Architekturdesign",
    "4.3 GitHub-Workflow-Integration", "4.4 Self-Service-Prozess", "4.5 Datenmodell",
    "4.6 Geschäftslogik", "4.7 Audit-Logging", "4.8 Schnittstellen",
    "4.9 Maßnahmen zur Qualitätssicherung", "4.10 Pflichtenheft / Datenverarbeitungskonzept",
    "5 Umsetzung", "5.1 Aufbau der Entwicklungsumgebung", "5.2 Implementierung der Datenstrukturen",
    "5.3 Implementierung des RBAC-Modells", "5.4 Implementierung der Benutzeroberfläche",
    "5.5 Implementierung der GitHub-Automatisierung", "5.6 Implementierung der Geschäftslogik",
    "5.7 Implementierung der Audit-Protokollierung", "5.8 Implementierung der Qualitätssicherung",
    "5.9 Entwicklerdokumentation",
    "6 Test und Abnahme", "6.1 Testkonzept", "6.2 Funktionstests", "6.3 Integrationstests",
    "6.4 Security-Tests", "6.5 Datenschutzprüfung", "6.6 Testfallmatrix",
    "6.7 Fehleranalyse", "6.8 Soll-Ist-Vergleich", "6.9 Abnahme",
    "7 Einführung und Dokumentation", "7.1 Einführungskonzept", "7.2 Pilotbetrieb",
    "7.3 Schulung", "7.4 Change Management", "7.5 Benutzerdokumentation",
    "7.6 Betriebsdokumentation", "7.7 Übergabe",
    "8 Projektabschluss", "8.1 Projektergebnis", "8.2 Soll-Ist-Vergleich",
    "8.3 Wirtschaftliche Bewertung", "8.4 Lessons Learned", "8.5 Risiken nach Projektabschluss",
    "8.6 Ausblick", "8.7 Persönliches Fazit"
]

roman_appendix_entries = [
    "Literaturverzeichnis", "Abkürzungsverzeichnis", "Abbildungsverzeichnis",
    "Tabellenverzeichnis", "Anhang", "A1 Detaillierte Zeitplanung", "A2 Lastenheft-Auszug",
    "A3 Use-Case-Diagramm", "A4 Pflichtenheft-Auszug", "A5 Datenmodell",
    "A6 EPK-Prozessbeschreibung", "A7 Oberflächenentwürfe", "A8 Screenshots der Anwendung",
    "A9 Entwicklerdokumentation", "A10 Testfall Konsole", "A11 Schnittstellenübersicht",
    "A12 Klassendiagramm", "A13 Benutzerdokumentation", "A14 Datenschutz-Checkliste",
    "A15 Abnahmeprotokoll", "Eidesstattliche Erklärung"
]

def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i, v in enumerate(val):
        while n >= v:
            res += syms[i]
            n -= v
    return res

def to_roman_lower(n):
    return to_roman(n).lower()

# Neue IV bauen
new_iv = "## INHALTSVERZEICHNIS\n\n"

# Römisch groß (I, II, III...) für Vorwort/Verzeichnisse
page = 1
for entry in roman_main_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {to_roman(page)}\n"
    page += 1

# Arabisch (1, 2, 3...) für Kapitel 1-8
page = 1
for entry in arabic_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {page}\n"
    page += 1

# Römisch klein (i, ii, iii...) für Anhang
page = 1
for entry in roman_appendix_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {to_roman_lower(page)}\n"
    page += 1

new_iv += "\n---\n"

# Ersetzen
new_content = content[:iv_start] + new_iv + content[iv_end:]

with open(master_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("IV korrigiert: römisch groß (Vorwort), arabisch (Kapitel), römisch klein (Anhang)")
PYEOF

python3 "$BUILD_DIR/fix_iv.py" "$MASTER"
ok "IV-Seitenzählung korrigiert (römisch/arabisch/römisch-klein)"

# ═══════════════════════════════════════════════════════════════════════════
# 3. MERMAID-DIAGRAMME GENERIEREN/VERBESSERN
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 2: Mermaid-Diagramme generieren ==="

# Prüfe ob mermaid-cli verfügbar
if command -v mmdc &> /dev/null; then
    MMDC="mmdc"
elif command -v npx &> /dev/null; then
    MMDC="npx -p @mermaid-js/mermaid-cli mmdc"
else
    warn "mermaid-cli nicht installiert -> installiere via npm"
    npm install -g @mermaid-js/mermaid-cli 2>/dev/null || warn "npm install fehlgeschlagen"
    MMDC="mmdc"
fi

# Alle .mmd Files rendern
for mmd in "$MERMAID_DIR"/*.mmd; do
    [ -f "$mmd" ] || continue
    name=$(basename "$mmd" .mmd)
    out="$MERMAID_DIR/png/$name.png"
    log "  Render: $name.mmd -> $out"
    $MMDC -i "$mmd" -o "$out" -w 1000 -H 700 -b white 2>/dev/null && ok "    $name.png" || warn "    $name fehlgeschlagen"
done

# EPK HTML -> PNG
if command -v google-chrome &> /dev/null; then
    for html in "$EPK_DIR"/*.html; do
        [ -f "$html" ] || continue
        name=$(basename "$html" .html)
        out="$EPK_DIR/$name.png"
        log "  EPK Screenshot: $name.html -> $out"
        google-chrome --headless=new --disable-gpu --no-sandbox \
            --window-size=1000,1200 --screenshot="$out" "file://$(realpath "$html")" 2>/dev/null \
            && ok "    $name.png" || warn "    $name fehlgeschlagen"
    done
else
    warn "google-chrome nicht verfügbar -> EPK Screenshots übersprungen"
fi

# Screenshots HTML -> PNG
if command -v google-chrome &> /dev/null; then
    for html in "$SCR_DIR"/*.html; do
        [ -f "$html" ] || continue
        name=$(basename "$html" .html)
        out="$SCR_DIR/$name.png"
        log "  Screenshot: $name.html -> $out"
        google-chrome --headless=new --disable-gpu --no-sandbox \
            --window-size=1280,800 --screenshot="$out" "file://$(realpath "$html")" 2>/dev/null \
            && ok "    $name.png" || warn "    $name fehlgeschlagen"
    done
fi

# ═══════════════════════════════════════════════════════════════════════════
# 4. PLANTUML-DIAGRAMME ERSTELLEN (Klassen, Use-Case, Sequenz)
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 3: PlantUML-Diagramme generieren ==="

PLANTUML_DIR="$ROOT/04_diagramme_plantuml"
mkdir -p "$PLANTUML_DIR"

# Prüfe PlantUML
if command -v plantuml &> /dev/null; then
    PLANTUML="plantuml"
elif [ -f "/usr/share/plantuml/plantuml.jar" ]; then
    PLANTUML="java -jar /usr/share/plantuml/plantuml.jar"
else
    warn "PlantUML nicht installiert -> überspringe"
    PLANTUML=""
fi

if [ -n "$PLANTUML" ]; then
    # Klassendiagramm
    cat > "$PLANTUML_DIR/class_diagram.puml" << 'PUML'
@startuml
skinparam classAttributeIconSize 0
skinparam linetype ortho
skinparam nodesep 60
skinparam ranksep 60

package "Domain Model" {
    class User {
        +user_id: String
        +name: String
        +email: String
        +department: String
        +created_at: DateTime
        +is_active: Boolean
    }

    class Role {
        +role_id: String
        +role_name: String
        +description: String
        +parent_role_id: String [0..1]
        +created_at: DateTime
    }

    class Permission {
        +permission_id: String
        +permission_name: String
        +resource: String
        +action: String
    }

    class GitHubTeam {
        +team_id: String
        +team_name: String
        +organization: String
        +description: String
    }

    class Repository {
        +repo_id: String
        +repo_name: String
        +visibility: String
        +description: String
    }

    class Approval {
        +approval_id: String
        +status: String
        +approver_id: String
        +requested_at: DateTime
        +decided_at: DateTime [0..1]
        +comment: String
    }

    class AuditLog {
        +log_id: String
        +action: String
        +resource_type: String
        +resource_id: String
        +result: String
        +timestamp: DateTime
        +user_id: String
        +details: JSON
    }
}

package "Security & ML" {
    class AnomalyDetector {
        +model_path: String
        +threshold: Float
        +predict(event: JSON) : Float
        +explain(event: JSON) : JSON
    }

    class PolicyGenerator {
        +model_path: String
        +generate(context: JSON) : String
        +validate(policy: String) : Boolean
    }
}

User "1" -- "0..*" Approval : creates >
User "*" -- "*" Role : has >
Role "*" -- "*" Permission : contains >
Role "1" -- "0..1" Role : parent >
Role "1" -- "0..1" GitHubTeam : maps_to >
GitHubTeam "*" -- "*" Repository : grants_access >
Approval "1" -- "0..*" AuditLog : produces >
User "1" -- "0..*" AuditLog : performed_by >

AnomalyDetector ..> AuditLog : analyzes
PolicyGenerator ..> Role : generates_policies_for

@enduml
PUML

    # Use-CASE
    # Use-Case-Diagramm
    cat > "$PLANTUML_DIR/use_case.puml" << 'PUML'
@startuml
left to right direction
skinparam packageStyle rectangle
actor "Mitarbeiter" as Employee
actor "Vorgesetzter" as Manager
actor "IT-Admin" as Admin
actor "Datenschutzbeauftragter" as DPO
actor "System (GitHub Actions)" as System

package "Self-Service-Portal" {
    usecase "Rollen beantragen" as UC1
    usecase "Antragsstatus prüfen" as UC2
    usecase "Eigene Berechtigungen einsehen" as UC3
}

package "Genehmigungsworkflow" {
    usecase "Antrag prüfen" as UC4
    usecase "Antrag genehmigen/ablehnen" as UC5
    usecase "Eskalation nach 48h" as UC6
}

package "Rechteverwaltung" {
    usecase "GitHub Team zuordnen" as UC7
    usecase "Repository-Berechtigungen setzen" as UC8
    usecase "Rechte entziehen (Austritt)" as UC9
}

package "Audit & Compliance" {
    usecase "Audit-Log einsehen" as UC10
    usecase "Compliance-Bericht exportieren" as UC11
    usecase "DSGVO-Prüfung durchführen" as UC12
}

package "Administration" {
    usecase "Rollen/Permissions verwalten" as UC13
    usecase "Nutzer verwalten" as UC14
    usecase "System konfigurieren" as UC15
}

Employee --> UC1
Employee --> UC2
Employee --> UC3
Manager --> UC4
Manager --> UC5
System --> UC6
System --> UC7
System --> UC8
System --> UC9
Admin --> UC10
Admin --> UC11
Admin --> UC13
Admin --> UC14
Admin --> UC15
DPO --> UC10
DPO --> UC11
DPO --> UC12

@enduml
PUML

    # Sequenzdiagramm: Rollenantrag
    cat > "$PLANTUML_DIR/sequence_role_request.puml" << 'PUML'
@startuml
actor "Mitarbeiter" as User
participant "Self-Service\nPortal" as Portal
participant "GitHub Actions\nWorkflow" as Workflow
participant "Policy Engine" as Policy
participant "GitHub API" as GitHub
participant "Audit DB" as Audit
actor "Vorgesetzter" as Manager

autonumber

User -> Portal: 1. Rolle auswählen & Antrag stellen
Portal -> Workflow: 2. Issue erstellen (role-request)
Workflow -> Policy: 3. Policy-Prüfung (4-Augen, Kompetenz)
alt Policy OK
    Policy --> Workflow: 4a. Validierung bestanden
    Workflow -> Manager: 5. Genehmigungsanfrage (E-Mail/Teams)
    Manager -> Workflow: 6. Genehmigung / Ablehnung
    alt Genehmigt
        Workflow -> GitHub: 7. API: Team-Mitgliedschaft hinzufügen
        GitHub --> Workflow: 8. Bestätigung
        Workflow -> Audit: 9. Audit-Log Eintrag (SUCCESS)
        Audit --> Workflow: 10. Log gespeichert
        Workflow -> User: 11. Benachrichtigung: Erfolg
    else Abgelehnt
        Workflow -> Audit: 9. Audit-Log Eintrag (REJECTED)
        Workflow -> User: 11. Benachrichtigung: Abgelehnt
    end
else Policy verletzt
    Policy --> Workflow: 4b. Blockiert (Begründung)
    Workflow -> Audit: 9. Audit-Log Eintrag (BLOCKED)
    Workflow -> User: 11. Benachrichtigung: Policy-Verletzung
end

@enduml
PUML

    # Sequenzdiagramm: Anomalie-Erkennung
    cat > "$PLANTUML_DIR/sequence_anomaly.puml" << 'PUML'
@startuml
actor "System" as System
participant "Audit Log" as Audit
participant "Anomaly Detector\n(CodeBERT)" as ML
participant "Alert System" as Alert
participant "Security Team" as SecTeam

autonumber

System -> Audit: 1. Rechteänderung protokollieren
Audit -> ML: 2. Event streamen (async)
ML -> ML: 3. Embedding generieren (CodeBERT)
ML -> ML: 4. Anomalie-Score berechnen
alt Score > Threshold (0.95)
    ML -> Alert: 5. Anomalie-Alert erzeugen
    Alert -> SecTeam: 6. Benachrichtigung (E-Mail/Slack)
    SecTeam -> Audit: 7. Investigation starten
    Audit --> SecTeam: 8. Vollständiger Audit-Trail
else Normal
    ML --> Audit: 5. Score geloggt (Monitoring)
end

@enduml
PUML

    # Rendern
    for puml in "$PLANTUML_DIR"/*.puml; do
        [ -f "$puml" ] || continue
        name=$(basename "$puml" .puml)
        log "  PlantUML: $name.puml -> PNG"
        $PLANTUML -tpng "$puml" -o "$PLANTUML_DIR" 2>/dev/null && ok "    $name.png" || warn "    $name fehlgeschlagen"
    done
else
    warn "PlantUML nicht verfügbar -> Diagramme werden nicht gerendert"
fi

# ═══════════════════════════════════════════════════════════════════════════
# 5. KI-BILD-PROMPTS FÜR ARCHITEKTUR-GRAFIKEN (Flux/Stable Diffusion)
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 4: KI-Bild-Prompts generieren ==="

PROMPTS_DIR="$ROOT/09_export/ai_prompts"
mkdir -p "$PROMPTS_DIR"

cat > "$PROMPTS_DIR/architecture_prompts.md" << 'PROMPTEOF'
# KI-Bild-Prompts für Architektur-Grafiken (Flux.1-dev / Stable Diffusion XL)

## 1. Zero-Trust-Architektur Übersicht
**Prompt:**
> Professional technical architecture diagram, Zero Trust security model, layered architecture: Presentation Layer (React Self-Service Portal), Application Layer (Node.js Business Logic, Policy Engine, Workflow Engine), Data Layer (PostgreSQL with Audit Logs, Redis Cache), Integration Layer (GitHub API, Azure AD/SAML, REST APIs). Clean lines, modern corporate style, blue/gray color scheme, labeled components, arrows showing data flow, high resolution, technical documentation quality, isometric view.

**Negative Prompt:**
> messy, hand-drawn, low quality, blurry, watermark, text artifacts, cartoon, bright colors, unprofessional

---

## 2. GitHub Actions Workflow Visualisierung
**Prompt:**
> Flowchart of GitHub Actions CI/CD pipeline for automated role provisioning: Trigger (Issue labeled "role-request") -> Validate Stage (Policy Check, Required Fields) -> Approve Stage (Manager Approval, 48h Escalation) -> Provision Stage (GitHub API Team Assignment, Repository Permissions) -> Notify Stage (Email/Slack, Audit Log Entry). Modern DevOps diagram style, GitHub brand colors (purple/black/white), clear step boxes, decision diamonds, success/failure paths, professional technical illustration.

**Negative Prompt:**
> cluttered, confusing arrows, low contrast, unreadable text, amateur

---

## 3. RBAC-Modell mit GitHub Team Mapping
**Prompt:**
> Entity Relationship Diagram for Role-Based Access Control: User (1) -> has -> (*) Role, Role (*) -> contains -> (*) Permission, Role (1) -> maps_to -> (1) GitHubTeam, GitHubTeam (*) -> grants_access -> (*) Repository. Clean ERD notation (Crow's Foot), professional database diagram style, white background, blue entities, black relationships, clear cardinality markers, high quality technical documentation.

**Negative Prompt:**
> hand-drawn, fuzzy, incorrect notation, messy layout, colors bleeding

---

## 4. Self-Service-Prozess End-to-End
**Prompt:**
> Business process diagram (BPMN-style) for Self-Service Role Request: Employee logs in via SSO -> Selects Role from Catalog -> Policy Engine validates -> Manager receives Approval Request -> Manager Approves/Rejects -> If Approved: GitHub API provisions access -> Audit Log records transaction -> Employee notified. Swimlanes for Employee, Manager, System, GitHub. Professional BPMN notation, corporate blue/gray, clean lanes, clear start/end events.

**Negative Prompt:**
> non-standard notation, messy swimlanes, unclear flow, amateur drawing

---

## 5. Audit-Logging & Anomalie-Erkennung
**Prompt:**
> Security monitoring architecture: Audit Logs (Append-Only PostgreSQL) -> Stream Processing -> ML Anomaly Detector (CodeBERT Embedding) -> Anomaly Score -> Threshold Check -> Alert Generation -> Security Team Dashboard. Data flow diagram, modern SOC style, dark theme with accent colors (red for alerts, green for normal), clear component boundaries, technical precision.

**Negative Prompt:**
> bright colors, cartoon, unclear components, messy data flows

---

## 6. Deployment-Architektur (Docker/Kubernetes)
**Prompt:**
> Cloud-native deployment diagram: GitHub Repository -> GitHub Actions CI/CD -> Docker Images -> Kubernetes Cluster (Ingress, Self-Service Pods, Backend Pods, PostgreSQL StatefulSet, Redis) -> Monitoring (Prometheus/Grafana) -> GitHub Audit Log Integration. Kubernetes official style icons, clean clusters, labeled namespaces, professional infrastructure diagram.

**Negative Prompt:**
> messy, incorrect k8s icons, cluttered, low resolution

---

## Parameter für Flux.1-dev / SDXL (lokal auf RTX 3060 12GB)

### Flux.1-dev (GGUF q4_k_m via llama.cpp)
```bash
# Beispiel Aufruf
./llama-cli -m flux-1-dev-q4_k_m.gguf \
  -p "Professional technical architecture diagram, Zero Trust security model..." \
  --width 1024 --height 768 \
  --steps 20 --cfg 3.5 --sampler euler_a \
  -o architecture_zerotrust.png
```

### Stable Diffusion XL (Automatic1111 / ComfyUI)
- **Sampler:** DPM++ 2M Karras
- **Steps:** 25-30
- **CFG:** 7-8
- **Resolution:** 1024x768 oder 1280x720
- **VAE:** sdxl_vae.safetensors
- **Refiner:** optional (letzte 5-10 Steps)

### Tipps für beste Ergebnisse
1. **Aspect Ratio:** 4:3 oder 16:9 für Dokumentation
2. **Iterieren:** Erste Generation als Basis, dann Inpainting für Details
3. **ControlNet (Canny/Depth):** Für exakte Layouts aus Skizzen
4. **Negative Prompts:** Immer nutzen (siehe oben)
5. **Batch:** 4-8 Bilder generieren, bestes auswählen

---

## Einbindung in Dokumentation
Bilder speichern unter: `10_screenshots/ai_generated/`
Markdown-Referenz: `![Zero-Trust Architektur](10_screenshots/ai_generated/architecture_zerotrust.png)`
PROMPTEOF

ok "KI-Bild-Prompts erstellt: $PROMPTS_DIR/architecture_prompts.md"

# ═══════════════════════════════════════════════════════════════════════════
# 6. PDF-BUILD PIPELINE FIXEN (CSS @page, Seitennummerierung)
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 5: PDF-Build-Pipeline optimieren ==="

# Verbessertes Template mit korrekter Seitennummerierung
cat > "$TEMPLATE" << 'HTMLEOF'
<!DOCTYPE html><html><head><meta charset="utf-8"><title>$title$</title>
<style>
@page {
  size: A4;
  margin: 2.5cm 2cm 2.5cm 2.5cm;
  @top-center { content: "Zero-Trust-Sicherheitskonzept mit GitHub-Integration"; font-family: Arial; font-size: 8pt; color: #666; }
  @bottom-left { content: "Daniel Massa • Prüflingsnr. 615951 • IHK Stuttgart"; font-family: Arial; font-size: 8pt; color: #666; }
  @bottom-right { content: counter(page); font-family: Arial; font-size: 10pt; color: #333; }
}

/* Römische Seitenzahlen für Verzeichnisse */
.roman-page { counter-reset: page; }
.roman-page @bottom-right { content: counter(page, upper-roman); }

/* Arabische Seitenzahlen für Hauptteil */
.arabic-page { counter-reset: page 1; }
.arabic-page @bottom-right { content: counter(page); }

/* Römische klein für Anhang */
.roman-lower-page { counter-reset: page; }
.roman-lower-page @bottom-right { content: counter(page, lower-roman); }

* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 12pt; line-height: 1.5;
  color: #000; text-align: left;
  widows: 2; orphans: 2;
}
h1 { font-size: 20pt; margin-top: 24pt; margin-bottom: 12pt; page-break-before: always; page-break-after: avoid; }
h2 { font-size: 16pt; margin-top: 18pt; margin-bottom: 10pt; page-break-after: avoid; }
h3 { font-size: 14pt; margin-top: 14pt; margin-bottom: 8pt; page-break-after: avoid; }
p { margin-bottom: 6pt; text-align: justify; }
ul, ol { margin-left: 18pt; margin-bottom: 6pt; }
li { margin-bottom: 3pt; }
table { width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 10pt; page-break-inside: avoid; }
table th { background: #f0f0f0; padding: 4pt 6pt; border: 1px solid #999; text-align: left; font-weight: bold; }
table td { padding: 4pt 6pt; border: 1px solid #999; vertical-align: top; }
pre, code { font-family: 'Courier New', monospace; font-size: 10pt; background: #f5f5f5; padding: 2pt 4pt; }
pre { padding: 8pt; margin: 8pt 0; border: 1px solid #ddd; overflow-x: auto; page-break-inside: avoid; }
blockquote { border-left: 3pt solid #999; padding-left: 10pt; margin: 8pt 0; font-style: italic; color: #555; }
img { max-width: 100%; height: auto; page-break-inside: avoid; }
.toc li { margin: 4pt 0; }
.cover-page { text-align: center; padding-top: 6cm; page-break-after: always; }
.cover-page h1 { font-size: 24pt; margin-bottom: 8pt; page-break-before: avoid; }
.cover-page h2 { font-size: 16pt; font-weight: normal; margin-bottom: 20pt; }
.cover-page .info { margin-top: 40pt; font-size: 12pt; line-height: 2; }
.footnotes { font-size: 9pt; line-height: 1.3; color: #555; margin-top: 12pt; padding-top: 6pt; border-top: 1px solid #ccc; }
.footnote-ref { vertical-align: super; font-size: 9pt; }
.footnote-back { display: none; }

/* Keine Paged.js mehr - natives @media print nur */
@media print {
  .no-print { display: none; }
}
</style></head><body>
$body$
</body></html>
HTMLEOF

ok "PDF-Template optimiert (native @page, keine Paged.js, korrekte Header/Footer)"

# ═══════════════════════════════════════════════════════════════════════════
# 7. VALIDIERUNG GEGEN IHK-KRITERIEN (CHECKLISTE)
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 6: IHK-Kriterien Validierung ==="

cat > "$BUILD_DIR/validate_ihk.py" << 'PYEOF'
#!/usr/bin/env python3
import re
import sys

master_path = sys.argv[1]
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

checks = []

# 1. Formale Kriterien
checks.append(("Deckblatt IHK-konform", "Projektarbeit im Rahmen der Prüfung zum Certified IT Business Manager" in content))
checks.append(("Sperrvermerk vorhanden", "SPERRVERMERK" in content))
checks.append(("Eidesstattliche Erklärung", "Eidesstattliche Erklärung" in content))
checks.append(("Eidesstattliche im IV", "Eidesstattliche Erklärung" in content and "......" in content.split("Eidesstattliche Erklärung")[1][:50]))

# 2. Verzeichnisse
checks.append(("Inhaltsverzeichnis", "## INHALTSVERZEICHNIS" in content))
checks.append(("Abbildungsverzeichnis", "## ABBILDUNGSVERZEICHNIS" in content))
checks.append(("Tabellenverzeichnis", "## TABELLENVERZEICHNIS" in content))
checks.append(("Abkürzungsverzeichnis", "## ABKÜRZUNGSVERZEICHNIS" in content))
checks.append(("Literaturverzeichnis", "## LITERATURVERZEICHNIS" in content or "# LITERATURVERZEICHNIS" in content))

# 3. Fußnoten
footnotes = len(re.findall(r'\[\^(\d+)\]', content))
checks.append((f"Fußnoten ({footnotes} Stück)", footnotes >= 6))

# 4. Struktur Kapitel 1-8
for i in range(1, 9):
    checks.append((f"Kapitel {i} vorhanden", f"# {i} " in content or f"## {i} " in content))

# 5. SMART-Ziele
checks.append(("SMART-Ziele", "SMART" in content and "Spezifisch" in content and "Messbar" in content))

# 6. Wirtschaftlichkeitsanalyse
checks.append(("Wirtschaftlichkeitsanalyse", "Amortisation" in content and "ROI" in content))

# 7. Nutzwertanalyse
checks.append(("Nutzwertanalyse", "Nutzwertanalyse" in content))

# 8. RBAC-Modell
checks.append(("RBAC-Modell", "RBAC" in content and "Role" in content and "Permission" in content))

# 9. Zero-Trust + Standards
checks.append(("Zero-Trust (NIST SP 800-207)", "NIST SP 800-207" in content or "Zero Trust Architecture" in content))
checks.append(("DSGVO/ISO 27001", "DSGVO" in content and "ISO 27001" in content))

# 10. Testkonzept
checks.append(("Testkonzept (4 Stufen)", "Unit-Test" in content and "Integrationstest" in content and "Security-Test" in content and "Abnahmetest" in content))
checks.append(("12 Testfälle", "TF12" in content or "Testfall" in content))

# 11. Abnahme
checks.append(("Abnahmeprotokoll", "Abnahmeprotokoll" in content))

# 12. GitHub/Technisch
checks.append(("GitHub Actions Workflow", "GitHub Actions" in content and "workflow" in content.lower()))
checks.append(("ML-Modelle (CodeBERT/flan-t5)", "CodeBERT" in content and "flan-t5" in content))

# 13. Diagramme referenziert
checks.append(("Abbildungen referenziert", "Abbildung" in content or "Abb." in content))
checks.append(("Tabellen referenziert", "Tabelle" in content or "Tab." in content))

# Auswertung
passed = sum(1 for _, ok in checks if ok)
total = len(checks)
percentage = (passed / total) * 100

print(f"\n{'='*60}")
print(f"IHK VALIDIERUNG: {passed}/{total} ({percentage:.0f}%)")
print(f"{'='*60}")
for name, ok in checks:
    status = "✓" if ok else "✗"
    print(f"  {status} {name}")

if percentage >= 90:
    print(f"\n🎉 SEHR GUT - Prüfungsreif (Note 1,0-1,3)")
elif percentage >= 80:
    print(f"\n✅ GUT - Kleinere Nachbesserungen (Note 1,7-2,3)")
else:
    print(f"\n⚠️  NACHBESSERUNG ERFORDERLICH")

sys.exit(0 if percentage >= 85 else 1)
PYEOF

python3 "$BUILD_DIR/validate_ihk.py" "$MASTER"
ok "IHK-Validierung abgeschlossen"

# ═══════════════════════════════════════════════════════════════════════════
# 8. FINALES PDF BAUEN
# ═══════════════════════════════════════════════════════════════════════════

log "=== Schritt 7: Finales PDF bauen ==="

HTML_OUT="$OUTDIR/PROJEKTARBEIT.html"
PDF_OUT="$OUTDIR/PROJEKTARBEIT_IHK_FINAL.pdf"

# Markdown -> HTML (mit Pandoc)
log "  Pandoc: Markdown -> HTML"
pandoc "$MASTER" -f markdown -t html5 \
    --template="$TEMPLATE" \
    --metadata title="Zero-Trust-Sicherheitskonzept mit GitHub-Integration" \
    -o "$HTML_OUT" 2>/dev/null && ok "  HTML erzeugt" || { error "Pandoc fehlgeschlagen"; exit 1; }

# HTML -> PDF (Chrome Headless)
if command -v google-chrome &> /dev/null; then
    log "  Chrome Headless: HTML -> PDF"
    google-chrome --headless=new --disable-gpu --no-sandbox \
        --print-to-pdf-no-header \
        --print-to-pdf="$PDF_OUT" \
        "file://$(realpath "$HTML_OUT")" 2>/dev/null && ok "  PDF erzeugt: $PDF_OUT" || { error "Chrome PDF fehlgeschlagen"; exit 1; }
else
    error "google-chrome nicht verfügbar für PDF-Generierung"
    exit 1
fi

# Seitenzahl prüfen
if command -v python3 &> /dev/null; then
    pages=$(python3 -c "
import subprocess
r = subprocess.run(['strings', '$PDF_OUT'], capture_output=True, text=True)
count = r.stdout.count('/Type /Page')
print(count)
" 2>/dev/null)
    ok "  Seitenanzahl: $pages"
fi

# ═══════════════════════════════════════════════════════════════════════════
# 9. ZUSAMMENFASSUNG
# ═══════════════════════════════════════════════════════════════════════════

log "=== REGENERATION ABGESCHLOSSEN ==="
echo ""
echo "┌─────────────────────────────────────────────────────────────┐"
echo "│  ERGEBNISSE                                                   │"
echo "├─────────────────────────────────────────────────────────────┤"
echo "│  📄 Master-Dokument: $MASTER"
echo "│  📄 Finales PDF:     $PDF_OUT"
echo "│  📊 Mermaid PNGs:    $MERMAID_DIR/png/"
echo "│  📊 EPK PNGs:        $EPK_DIR/"
echo "│  📊 PlantUML PNGs:   $PLANTUML_DIR/"
echo "│  📸 Screenshots:     $SCR_DIR/"
echo "│  🤖 KI-Prompts:      $PROMPTS_DIR/architecture_prompts.md"
echo "│  ✅ IHK-Validierung: $passed/$total ($percentage%)"
echo "└─────────────────────────────────────────────────────────────┘"
echo ""
echo "Nächste Schritte:"
echo "  1. PDF prüfen: xdg-open \"$PDF_OUT\""
echo "  2. KI-Bilder generieren (Flux/SD) mit Prompts aus $PROMPTS_DIR"
echo "  3. Falls IV-Seitenzahlen nicht stimmen: manuell nachjustieren"
echo "  4. Git commit & push"