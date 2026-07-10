# PROJECT START GATE (Entwurf)

> **Status:** ENTWURF – noch nicht freigegeben  
> **Zweck:** Definiert die Bedingungen, die erfüllt sein müssen, bevor das Projekt als real gestartet markiert wird.  
> **Hinweis:** Das Startgate gilt erst als bestanden, wenn alle untenstehenden Kriterien durch reale Artefakte belegt sind.

---

## Startgate-Kriterien

| # | Kriterium | Nachweis | Status |
|---|-----------|----------|--------|
| SG1 | Projektauftrag bestätigt | Unterschriebener Projektauftrag in `project-evidence/01_project_order/` | 🔴 OFFEN |
| SG2 | Projekttitel mit IHK-Zielvereinbarung abgeglichen | Bestätigungs-E-Mail oder Protokoll | 🔴 OFFEN |
| SG3 | Auftraggeber benannt | Name und Rolle im Projektauftrag | 🔴 OFFEN |
| SG4 | Projektleiter benannt | Name im Projektauftrag | 🔴 OFFEN |
| SG5 | Tatsächliches Startdatum vereinbart | Datum im Projektauftrag | 🔴 OFFEN |
| SG6 | Scope freigegeben | Freigegebener PILOT_SCOPE_DRAFT.md | 🔴 OFFEN |
| SG7 | 70-Stunden-Plan freigegeben | Freigegebener WORK_BREAKDOWN_STRUCTURE_DRAFT.md | 🔴 OFFEN |
| SG8 | Abnahmeverantwortlicher bestimmt | Name im Projektauftrag | 🔴 OFFEN |
| SG9 | Testumgebung verfügbar | Bestätigung (Rechner, Python, GitHub-Zugang) | 🔴 OFFEN |
| SG10 | Datenschutzanforderungen geklärt | Datenschutz-Check (keine PII im Pilot) | 🔴 OFFEN |
| SG11 | Repository-Baseline dokumentiert | `99_AUDIT_BASELINE_*/` vorhanden | ✅ BASELINE VORHANDEN |

---

## Startgate-Entscheidung

| Entscheidung | Voraussetzung |
|-------------|---------------|
| 🟢 **Start freigegeben** | Alle 11 Kriterien erfüllt |
| 🟡 **Bedingt gestartet** | SG1–SG8 erfüllt, SG9–SG10 mit Risikoakzeptanz |
| 🔴 **Nicht gestartet** | SG1 nicht erfüllt |

---

## Nach bestandenem Startgate

Erst nach Freigabe darf folgender Tag gesetzt werden:

```
project-start-<YYYYMMDD>
```

Beispiel: `project-start-20260714`

Dieser Tag markiert den Beginn der Zeiterfassung und der technischen Implementierung. Alle vorherigen Planungsarbeiten sind dem Vorbereitungszeitraum zuzuordnen.

---

## Konsequenzen bei Nichtbestehen

- Kein Tag `project-start-*` setzen.
- Keine technische Implementierung beginnen.
- Keine Zeiterfassung starten.
- Keine Ist-Daten erzeugen.
- Option D (neues Projektthema) prüfen.

---

## Aktueller Status

**DATUM:** 10.07.2026  
**STATUS:** 🔴 NOCH NICHT BESTANDEN – Projektstart nicht freigegeben

Es fehlen: Auftraggeber-Bestätigung, Startdatum, Scope-Freigabe, Abnahmeverantwortlicher.
