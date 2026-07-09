# Anhang A7 — Oberflächenentwürfe (Wireframes)

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Tool:** Figma / Balsamiq / Handskizze (Export als PNG, 300 DPI)  
**Version:** 1.0 | **Datum:** 09.07.2026

---

## 1. Dashboard (Startseite nach Login)

```
┌─────────────────────────────────────────────────────────────────┐
│  VFB Zero-Trust RBAC                                    [Profil] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Meine Rollen │  │ Offene Anträge│  │ Letzte Akt.  │          │
│  │     (3)      │  │     (1)      │  │    (5)       │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Schnellaktion: [+ Rolle beantragen]  [Meine Berechtigungen]│  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Aktuelle Rollen                                          │  │
│  ├────────┬──────────────────┬────────────┬────────────────┤  │
│  │ Rolle  │ Berechtigungen   │ Seit       │ Status         │  │
│  ├────────┼──────────────────┼────────────┼────────────────┤  │
│  │ Developer│ repo.read/write │ 15.03.2026 │ ✅ Aktiv      │  │
│  │ Read-Only│ repo.read       │ 01.01.2026 │ ✅ Aktiv      │  │
│  └────────┴──────────────────┴────────────┴────────────────┘  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Rollenantrag (Self-Service-Formular)

```
┌─────────────────────────────────────────────────────────────────┐
│  Rolle beantragen                                      [Abbrechen]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Gewünschte Rolle *                                       │  │
│  │  ▼ Developer                                    [?] Hilfe │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Begründung *                                             │  │
│  │  ══════════════════════════════════════════════════════════  │  │
│  │  Brauche Schreibzugriff auf repo:vfb-bildung/frontend    │  │
│  │  für Sprint 23 (Feature: User-Dashboard)                  │  │
│  │                                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Ressource (optional)                                     │  │
│  │  ▼ vfb-bildung/frontend                                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ℹ️  Die Anfrage wird an Ihren Vorgesetzten (Max Mustermann)    │
│      zur Genehmigung weitergeleitet. Frist: 48 Stunden.        │
│                                                                 │
│  [Zurück]                                    [Antrag stellen]  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Antragsstatus (Tracking)

```
┌─────────────────────────────────────────────────────────────────┐
│  Meine Anträge                                        [Filtern] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────┬────────────┬───────────┬──────────┬────────┬────────┐  │
│  │ #  │ Rolle      │ Beantragt │ Status   │ Fortsch│ Aktionen│  │
│  ├────┼────────────┼───────────┼──────────┼────────┼────────┤  │
│  │ 12 │ Developer  │ 08.07.2026│ 🟡 Prüfung│ 2/4    │ [Details]│
│  │ 11 │ Read-Only  │ 05.07.2026│ ✅ Gewährt│ 4/4    │ [Details]│
│  │ 10 │ Admin      │ 01.07.2026│ 🔴 Abgelehnt│ 2/4   │ [Details]│
│  └────┴────────────┴───────────┴──────────┴────────┴────────┘  │
│                                                                 │
│  Legende: 🟢 Genehmigt  🟡 In Prüfung  🔴 Abgelehnt  ⚫ Eskaliert │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Admin-Bereich: Rollenverwaltung

```
┌─────────────────────────────────────────────────────────────────┐
│  Administration > Rollen                              [+ Neu]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [🔍 Suchen...]  [Filter: Alle ▼]  [Export CSV]                 │
│                                                                 │
│  ┌────┬────────────┬──────────────────┬────────┬───────┬─────┐ │
│  │ #  │ Name       │ Beschreibung     │ System │ Nutzer│ Akt.│ │
│  ├────┼────────────┼──────────────────┼────────┼───────┼─────┤ │
│  │ 1  │ Admin      │ Vollzugriff      │ ✅     │ 3     │ [✏️]│ │
│  │ 2  │ Developer  │ R/W Repos        │        │ 8     │ [✏️]│ │
│  │ 3  │ Auditor    │ Read Logs        │        │ 2     │ [✏️]│ │
│  │ 4  │ Read-Only  │ Read Selected    │        │ 12    │ [✏️]│ │
│  │ 5  │ HR-Manager │ HR-System        │        │ 5     │ [✏️]│ │
│  │ 6  │ Finance    │ Finanz-System    │        │ 4     │ [✏️]│ │
│  └────┴────────────┴──────────────────┴────────┴───────┴─────┘ │
│                                                                 │
│  [Rollen berechtigen]  [Berechtigungen matrix]  [GitHub Sync]   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Admin: Berechtigungsmatrix

```
┌─────────────────────────────────────────────────────────────────┐
│  Berechtigungsmatrix                                    [Speichern]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────┬─────────┬─────────┬─────────┬─────────┬──────┐ │
│  │ Berechtig. │ Admin   │ Developer│ Auditor │ Read-Only│ HR  │ │
│  ├────────────┼─────────┼─────────┼─────────┼─────────┼──────┤ │
│  │ repo.admin │ ✅      │          │         │         │      │ │
│  │ repo.write │ ✅      │ ✅       │         │         │      │ │
│  │ repo.read  │ ✅      │ ✅       │ ✅      │ ✅      │      │ │
│  │ team.manage│ ✅      │          │         │         │      │ │
│  │ audit.read │ ✅      │          │ ✅      │         │      │ │
│  │ user.manage│ ✅      │          │         │         │ ✅   │ │
│  └────────────┴─────────┴─────────┴─────────┴─────────┴──────┘ │
│                                                                 │
│  [+ Berechtigung]  [+ Rolle]  [GitHub Sync prüfen]              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Audit-Log-Ansicht (Admin)

```
┌─────────────────────────────────────────────────────────────────┐
│  Audit-Log                                    [Export CSV] [🔍] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Zeitraum: [Letzte 7 Tage ▼]  User: [Alle ▼]  Aktion: [Alle ▼] │
│                                                                 │
│  ┌──────┬────────────┬────────┬──────────┬────────┬──────────┐ │
│  │ Zeit │ Nutzer     │ Aktion │ Ressource│ Ergebnis│ Details │ │
│  ├──────┼────────────┼────────┼──────────┼────────┼──────────┤ │
│  │ 10:23│ M. Muster  │ GRANT  │ Dev Team │ ✅     │ user:dm  │ │
│  │ 10:22│ System     │ APPROVE│ Req #12  │ ✅     │ by:MM    │ │
│  │ 10:15│ D. Massa   │ REQUEST│ Dev Role │ 🟡     │ reason:..│ │
│  │ 09:45│ A. Schmidt │ REVOKE │ Fin Role │ ✅     │ user:AS  │ │
│  │ 09:30│ System     │ SYNC   │ GitHub   │ ✅     │ 6 teams  │ │
│  └──────┴────────────┴────────┴──────────┴────────┴──────────┘ │
│                                                                 │
│  [⬅ Seite 1 von 12]  [Filter zurücksetzen]                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Mobile-Ansicht (Responsive)

```
┌─────────────────┐
│ ☰ VFB RBAC      │
├─────────────────┤
│ Meine Rollen (3)│
│ ┌─────────────┐ │
│ │ Developer   │ │
│ │ Read-Only   │ │
│ │ HR-Manager  │ │
│ └─────────────┘ │
│                 │
│ [+ Beantragen]  │
│ [Anträge (1)]   │
│ [Audit-Log]     │
│                 │
│ [Abmelden]      │
└─────────────────┘
```

---

## 8. Fehler- & Leere Zustände

### Validierungsfehler
```
┌────────────────────────────────────────┐
│ ⚠️  Bitte füllen Sie alle Pflichtfelder │
│    aus:                                 │
│    • Gewünschte Rolle                   │
│    • Begründung (min. 10 Zeichen)      │
└────────────────────────────────────────┘
```

### Keine Anträge
```
┌────────────────────────────────────────┐
│                                         │
│       📋  Noch keine Anträge            │
│                                         │
│    [+ Erste Rolle beantragen]           │
│                                         │
└────────────────────────────────────────┘
```

### API-Fehler (Provisioning)
```
┌────────────────────────────────────────┐
│ ❌  Berechtigung konnte nicht vergeben  │
│                                         │
│    GitHub API: Rate Limit erreicht      │
│    Bitte in 5 Min. erneut versuchen     │
│    oder IT-Admin kontaktieren           │
│                                         │
│    [Erneut versuchen] [Admin kontaktieren]│
└────────────────────────────────────────┘
```

---

## 9. Export-Spezifikation

| Wireframe | Dateiname | Format | DPI | Zweck |
|-----------|-----------|--------|-----|-------|
| Dashboard | `A7_01_Dashboard.png` | PNG | 300 | Anhang A7 |
| Antrag | `A7_02_Antrag.png` | PNG | 300 | Anhang A7 |
| Status | `A7_03_Status.png` | PNG | 300 | Anhang A7 |
| Admin-Rollen | `A7_04_AdminRollen.png` | PNG | 300 | Anhang A7 |
| Berechtigungsmatrix | `A7_05_Matrix.png` | PNG | 300 | Anhang A7 |
| Audit-Log | `A7_06_AuditLog.png` | PNG | 300 | Anhang A7 |
| Mobile | `A7_07_Mobile.png` | PNG | 300 | Anhang A7 |
| Fehlerszenarien | `A7_08_Fehler.png` | PNG | 300 | Anhang A7 |

---

*Ende Anhang A7. Wireframes als PNG (300 DPI) in Anhang A7. Quelle: Figma-Projekt "VFB Zero-Trust RBAC".*