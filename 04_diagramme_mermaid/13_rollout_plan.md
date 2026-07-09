# Mermaid: Rollout-Plan

```mermaid
gantt
    title Rollout-Plan Zero-Trust RBAC
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m.
    todayMarker stroke-width:2,stroke:red

    section Pilotphase (Woche 1-2)
    Pilot-User aufsetzen     :a1, 2026-10-20, 3d
    Schulung Pilot-User      :a2, after a1, 2d
    Pilot-Betrieb            :a3, after a2, 10d
    Feedback sammeln         :a4, after a3, 3d

    section Rollout Phase 1 (Woche 3-4)
    HR & Finanzen einbinden  :b1, after a4, 5d
    Schulung Phase 1         :b2, after b1, 3d
    Produktivbetrieb Phase 1 :b3, after b2, 10d

    section Vollausbau (ab Woche 5)
    Organisationweit aktivieren :c1, after b3, 5d
    Manuelle Prozesse abschalten :c2, after c1, 2d
    Monitoring & Optimierung   :c3, after c2, 20d

    section Meilensteine
    M4: Prototyp fertig      :milestone, m4, 2026-10-10, 0d
    M5: Test/Abnahme         :milestone, m5, 2026-10-20, 0d
    M6: Dokumentation fertig :milestone, m6, 2026-10-25, 0d
    M8: IHK Abgabe           :milestone, m8, 2026-11-01, 0d
```