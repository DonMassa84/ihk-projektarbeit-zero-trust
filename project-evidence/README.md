# Project Evidence – Zero-Trust-Pilot

**Zweck:** Zentrale Ablage aller während des realen Projekts erzeugten Nachweise.

## Regeln

1. **Nur tatsächlich entstandene Artefakte ablegen.** Keine konstruierten oder rückdateirten Dokumente.
2. **Keine Rückdatierung.** Jede Datei erhält das tatsächliche Erstellungsdatum.
3. **Plan- und Ist-Werte strikt trennen.** Plan-Dokumente gehören in `planning/`, Ist-Dokumente in `project-evidence/`.
4. **Jede Datei enthält Metadaten:** Erstellungsdatum, Autor, Bezug zum Arbeitspaket.
5. **Änderungen werden über Git nachvollzogen.** Jeder neue Nachweis ist ein Commit.
6. **Personenbezogene Daten nur soweit erforderlich.** Anonymisierung wo möglich.
7. **Keine Secrets, Token oder Passwörter ablegen.** Einsatz von Umgebungsvariablen oder Secret-Stores.
8. **Screenshots müssen sensible Informationen schwärzen.** Vor Ablage prüfen.
9. **Unterschriften werden ausschließlich manuell oder durch reale elektronische Bestätigung erzeugt.** Keine simulierten Unterschriften.
10. **Jeder Ordner enthält eine INDEX.md** mit Auflistung des Inhalts und Erstellungsdatum.

## Ordnerstruktur

| Ordner | Inhalt |
|--------|--------|
| `01_project_order/` | Projektauftrag, Scope-Vereinbarung, IHK-Zielvereinbarung |
| `02_kickoff/` | Kick-Off-Protokoll, Präsentation, Teilnehmerliste |
| `03_time_tracking/` | Tägliche Timesheets, Stunden-Nachweise |
| `04_decisions/` | Entscheidungsprotokolle (ADRs) |
| `05_changes/` | Änderungsanträge, Scope-Änderungen |
| `06_costs/` | Kostenbelege, Rechnungen, Plan/Ist-Vergleiche |
| `07_implementation/` | Code-Reviews, Architektur-Dokumente |
| `08_tests/` | Testläufe, Test-Reports, Coverage |
| `09_reviews/` | Code-Reviews, Architektur-Reviews |
| `10_training/` | Schulungsprotokolle, Anleitungen |
| `11_acceptance/` | Abnahmeprotokolle, Bestätigungen |
| `12_communication/` | Statusberichte, Meeting-Protokolle |
| `13_screenshots/` | Echte Screenshots (geschwärzt) |

## Dateibenennung

```
YYYYMMDD_KURZBESCHREIBUNG.<ext>
```

Beispiel: `20260714_kickoff_protokoll.md`
