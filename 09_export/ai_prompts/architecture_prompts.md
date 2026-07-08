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
