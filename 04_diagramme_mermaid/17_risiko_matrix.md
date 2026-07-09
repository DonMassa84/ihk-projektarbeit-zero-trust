# Mermaid: Risiko-Matrix (Eintrittswahrscheinlichkeit × Schadensausmaß)

```mermaid
---
title: Risiko-Matrix Zero-Trust-Projekt
---
%%{init: {'theme': 'base'}}%%
quadrantChart
    title Risikobewertung: Wahrscheinlichkeit × Auswirkung
    x-axis Niedrige Wahrscheinlichkeit --> Hohe Wahrscheinlichkeit
    y-axis Geringe Auswirkung --> Hohe Auswirkung
    quadrant-1 Überwachen
    quadrant-2 Handeln (Priorität)
    quadrant-3 Akzeptieren
    quadrant-4 Reduzieren

    "R1: Scope Creep\n(Anforderungswachstum)": [0.7, 0.6]
    "R2: Zeitverzug durch\nberufsbegleitende Arbeit": [0.8, 0.5]
    "R3: Technische Schulden\n(schneller Prototyp)": [0.6, 0.7]
    "R4: GitHub API-Limits\n(Rate Limiting)": [0.4, 0.4]
    "R5: Datenschutz-\nverstöße (DSGVO)": [0.3, 0.9]
    "R6: Fehlende Akzeptanz\n(Self-Service)": [0.5, 0.6]
    "R7: Sicherheitslücken\nim Prototyp": [0.4, 0.8]
    "R8: Budgetüberschreitung\n(Consultant-Kosten)": [0.3, 0.5]
    "R9: Key-Person-Risk\n(Projektleiter)": [0.2, 0.7]
    "R10: IHK-Änderungen\n(Prüfungsordnung)": [0.1, 0.6]
```

| ID | Risiko | Eintrittsw. | Auswirkung | Risikowert | Maßnahme | Verantwortlich | Status |
|----|--------|-------------|------------|------------|----------|----------------|--------|
| R1 | Scope Creep | Hoch (0,7) | Mittel (0,6) | 0,42 | Change Control Board, strikte Abgrenzung | PL | Überwachen |
| R2 | Zeitverzug | Hoch (0,8) | Mittel (0,5) | 0,40 | Puffer 20%, wöchentliche Meilenstein-Prüfung | PL | Reduzieren |
| R3 | Technische Schulden | Mittel (0,6) | Hoch (0,7) | 0,42 | Code-Reviews, Refactoring-Sprints, DoD | Dev | Reduzieren |
| R4 | GitHub API Limits | Mittel (0,4) | Mittel (0,4) | 0,16 | Caching, Batch-Requests, Backoff | Dev | Überwachen |
| R5 | DSGVO-Verstoß | Niedrig (0,3) | Sehr hoch (0,9) | 0,27 | Privacy by Design, DPIA, DSB früh einbinden | DSB/PL | Handeln |
| R6 | Geringe Akzeptanz | Mittel (0,5) | Mittel (0,6) | 0,30 | User-Tests, Schulung, Change Mgmt | PL | Reduzieren |
| R7 | Sicherheitslücken | Mittel (0,4) | Hoch (0,8) | 0,32 | Sec-Consultant, Bandit/Trivy in CI, Pen-Test | Sec-Consultant | Handeln |
| R8 | Budgetüberschreitung | Niedrig (0,3) | Mittel (0,5) | 0,15 | Monatliches Controlling, Fixpreis-Consultant | PL | Überwachen |
| R9 | Key-Person-Risk | Niedrig (0,2) | Hoch (0,7) | 0,14 | Wissensdoku, Pair Programming, Stellvertreter | PL | Reduzieren |
| R10 | IHK-Änderungen | Sehr niedrig (0,1) | Mittel (0,6) | 0,06 | Monitoring IHK-Newsletter, Dozenten-Kontakt | PL | Akzeptieren |

**Abb. X: Risiko-Matrix mit quantitativer Bewertung und Maßnahmen**