# Anhang A13 — Benutzerdokumentation (User Guide)

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Version:** 1.0 | **Datum:** 01.11.2026  
**Zielgruppe:** Endnutzer (Mitarbeiter VFB)  

---

# Benutzerhandbuch: Self-Service-Portal für Rollenverwaltung

## 1. Einleitung

Dieses Handbuch beschreibt die Nutzung des **Self-Service-Portals** zur Beantragung und Verwaltung von Zugriffsrechten im Rahmen des Zero-Trust-Sicherheitskonzepts des VFB.

**Ziel:** Sie können Rollen eigenständig beantragen, den Status verfolgen und Ihre aktuellen Berechtigungen einsehen — ohne E-Mail-Wege oder Tickets.

---

## 2. Anmeldung (Single Sign-On)

1. Öffnen Sie: `https://rbac.vfb-bildung.de` (oder intern: `http://rbac.intern`)
2. Klicken Sie auf **"Mit Azure AD anmelden"**
3. Sie werden zur Microsoft-Anmeldung weitergeleitet
3. Nach erfolgreicher Anmeldung gelangen Sie zum **Dashboard**

> **Hinweis:** Sie benötigen keine separaten Zugangsdaten — Ihre VFB-Microsoft-Identität wird verwendet.

---

## 3. Dashboard (Startseite)

Nach der Anmeldung sehen Sie drei Kacheln:

| Kachel | Inhalt |
|--------|--------|
| **Meine Rollen** | Alle aktuell aktiven Rollen mit Berechtigungen |
| **Offene Anträge** | Anträge, die noch geprüft/ausstehen |
| **Letzte Aktivitäten** | Letzte 5 Änderungen an Ihren Rollen |

**Schnellaktionen:**
- **[+ Rolle beantragen]** → Neues Antragsformular
- **[Meine Berechtigungen]** → Detaillierte Übersicht aller Berechtigungen

---

## 4. Rolle beantragen

### Schritt-für-Schritt

1. Klicken Sie auf **"+ Rolle beantragen"** (Dashboard oder Navigation)
2. Füllen Sie das Formular aus:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| **Gewünschte Rolle** | ✅ | Dropdown mit allen verfügbaren Rollen (z. B. *Developer*, *Read-Only*, *Auditor*) |
| **Begründung** | ✅ | Mind. 10 Zeichen — warum brauchen Sie diese Rolle? (z. B. *"Schreibzugriff auf repo:vfb-bildung/frontend für Sprint 23"*) |
| **Ressource** | optional | Konkreter Repository- oder Team-Name (z. B. `vfb-bildung/frontend`) |

3. Klicken Sie auf **"Antrag stellen"**

### Was passiert dann?

1. **Automatische Prüfung** (Sekunden):
   - Sind alle Pflichtfelder ausgefüllt?
   - Erfüllen Sie die Policy-Regeln? (4-Augen-Prinzip, Kompetenzmatrix)
2. **Genehmigungsanfrage** wird an Ihren **direkten Vorgesetzten** gesendet (E-Mail + GitHub Notification)
3. **Status** wechselt zu **🟡 In Prüfung**
4. **Frist:** 48 Stunden für Genehmigung → danach **automatische Eskalation** an IT-Admin

### Rollen-Katalog (Auszug)

| Rolle | Typische Nutzer | Berechtigungen |
|-------|-----------------|----------------|
| **Developer** | Entwickler, DevOps | Repo Read/Write, Team-Management (eigene Teams) |
| **Read-Only** | Stakeholder, QA, PM | Repo Read, Issues lesen |
| **Auditor** | Revision, Compliance | Audit-Log Read, Reports exportieren |
| **Read-Only** | Externe, Praktikanten | Nur definierte Repos Read |
| **HR-Manager** | Personalabteilung | HR-System Rollen |
| **Finance** | Buchhaltung | Finanz-System Rollen |

---

## 5. Antragsstatus verfolgen

Gehen Sie auf **"Meine Anträge"** (Navigation oder Dashboard):

| Status | Bedeutung | Aktion |
|--------|-----------|--------|
| 🟢 **Genehmigt** | Rolle wurde vergeben | Nichts — Zugriff ist aktiv |
| 🟡 **In Prüfung** | Vorgesetzter prüft noch | Warten (max. 48h) |
| 🔴 **Abgelehnt** | Vorgesetzter hat abgelehnt | Begründung einsehen, ggf. neu beantragen |
| ⚫ **Eskaliert** | 48h verstrichen ohne Reaktion | IT-Admin prüft manuell |

**Details anzeigen:** Klicken Sie auf einen Antrag → **Detailansicht** mit Zeitstrahl, Begründung, Genehmiger, GitHub-Actions-Status.

---

## 6. Eigene Rollen & Berechtigungen einsehen

**Meine Rollen** (Dashboard-Kachel oder Navigation):

| Rolle | Berechtigungen | Seit | Status |
|-------|----------------|------|--------|
| Developer | `repo.read`, `repo.write` (vfb-bildung/*) | 15.03.2026 | ✅ Aktiv |
| Read-Only | `repo.read` (vfb-bildung/frontend) | 01.01.2026 | ✅ Aktiv |

**Detaillierte Berechtigungen:** Klicken Sie auf eine Rolle → zeigt alle einzelnen Permissions (Resource, Action, Scope).

---

## 7. Häufige Fragen (FAQ)

| Frage | Antwort |
|-------|---------|
| **Wie lange dauert die Genehmigung?** | Meist < 4 Stunden, max. 48 Stunden (danach Eskalation). |
| **Kann ich einen Antrag zurückziehen?** | Ja — solange Status "In Prüfung" ist: Antrag öffnen → "Zurückziehen". |
| **Was tun bei Ablehnung?** | Begründung lesen (im Detail), ggf. Begründung anpassen & neu beantragen. |
| **Ich brauche Zugriff SOFORT.** | Bei dringenden Fällen: IT-Admin (Thomas Zoller) direkt kontaktieren → manuelle Eskalation. |
| **Meine Rolle fehlt im Katalog.** | IT-Admin kontaktieren → neue Rolle definieren (Admin-Bereich). |
| **Passwort vergessen?** | Kein Passwort nötig — Azure AD SSO. Bei Problemen: IT-Helpdesk. |
| **Zugriff nach Austritt?** | Wird automatisch entfernt (30 Tage nach Austrittsdatum). |
| **Temporärer Zugriff?** | Rolle beantragen mit Enddatum im Begründungstext → Admin setzt Enddatum. |

---

## 8. Support & Kontakt

| Anliegen | Kontakt |
|----------|---------|
| Technische Probleme (Portal) | IT-Helpdesk: `it-support@vfb-bildung.de` / Ext. 123 |
| Genehmigungsfragen | Ihr direkter Vorgesetzter |
| Neue Rolle / Berechtigung | IT-Admin: Thomas Zoller (`thomas.zoller@vfb-bildung.de`) |
| Datenschutz / DSGVO | DSB: `datenschutz@vfb-bildung.de` |
| Notfall (Sicherheitsvorfall) | **Sofort:** `security@vfb-bildung.de` / Rufbereitschaft |

---

## 9. Glossar

| Begriff | Bedeutung |
|---------|-----------|
| **RBAC** | Role-Based Access Control — rollenbasierte Zugriffskontrolle |
| **Zero Trust** | Sicherheitsmodell: "Never Trust, Always Verify" |
| **GitHub Team** | Gruppe in GitHub, die Berechtigungen auf Repositories bündelt |
| **Provisioning** | Automatisches Einrichten der Rechte (hier: GitHub Team-Mitgliedschaft) |
| **Audit-Log** | Revisionssicheres Protokoll aller Änderungen |
| **Self-Service** | Nutzer stellen Anträge selbst, ohne IT-Ticket |
| **Eskalation** | Automatische Weiterleitung bei Fristüberschreitung |

---

## 10. Kurzanleitung (Cheat Sheet)

```
1. https://rbac.vfb-bildung.de öffnen
2. "Mit Azure AD anmelden" → VFB-Login
3. Dashboard → "+ Rolle beantragen"
4. Rolle wählen, Begründung schreiben → "Antrag stellen"
5. Warten auf Genehmigung (E-Mail + GitHub Notification)
6. Bei Genehmigung: Zugriff sofort aktiv
7. Status jederzeit unter "Meine Anträge" prüfbar
```

---

**Version:** 1.0 | **Gültig ab:** 01.11.2026 | **Nächste Revision:** 01.05.2027  
**Freigegeben durch:** IT-Administration (Thomas Zoller) & Datenschutzbeauftragter

---

*Ende Anhang A13. Für Administratoren siehe Anhang A9 (Entwicklerdokumentation) und A7 (Wireframes).*