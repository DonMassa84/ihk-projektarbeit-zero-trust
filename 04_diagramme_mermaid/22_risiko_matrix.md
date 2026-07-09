# Mermaid: Risiko-Matrix (Eintrittswahrscheinlichkeit × Schadensausmaß)

```mermaid
---
title: Risiko-Matrix Zero-Trust-Projekt
---
quadrantChart
    title Risiko-Bewertung: Eintrittswahrscheinlichkeit vs. Schadensausmaß
    x-axis Geringe Eintrittswahrscheinlichkeit --> Hohe Eintrittswahrscheinlichkeit
    y-axis Geringes Schadensausmaß --> Hohes Schadensausmaß
    quadrant-1 "Überwachen\n(Mittel)"
    quadrant-2 "Kritisch\n(Sofort handeln)"
    quadrant-3 "Akzeptabel\n(Niedrig)"
    quadrant-4 "Reduzieren\n(Hoch)"

    "R1: Scope Creep\n(Anforderungswachstum)": [0.7, 0.6]
    "R2: Ressourcen-Engpass\n(Entwickler krank/abwesend)": [0.5, 0.7]
    "R3: GitHub API-Änderungen\n(Breaking Changes)": [0.4, 0.5]
    "R4: DSGVO-Nachweise\nnicht prüfungssicher": [0.3, 0.9]
    "R5: Sicherheitslücke\nim Prototyp (RCE/IDOR)": [0.2, 1.0]
    "R6: Betriebsrat blockiert\n(Mitbestimmung §87 BetrVG)": [0.25, 0.8]
    "R7: IHK-Formale Mängel\n(Seitenzahl, Eidesstattl.)": [0.15, 0.85]
    "R8: Budget-Überschreitung\n(>10%)": [0.3, 0.5]
    "R9: Terminverzug\n(Abgabe > 01.11.)": [0.2, 0.95]
    "R10: Know-how-Verlust\n(Entwickler geht)": [0.25, 0.65]
```

| ID | Risiko | Kategorie | Eintrittsw. | Schaden | Risikowert | Maßnahme | Verantwortlich | Status |
|----|--------|-----------|-------------|---------|------------|----------|----------------|--------|
| R1 | Scope Creep | Projektmgmt | Hoch (70%) | Mittel (6) | **42** | Change-Control-Prozess, wöchentl. Scope-Review | PL | 🟢 Überwacht |
| R2 | Ressourcen-Engpass | Personal | Mittel (50%) | Hoch (7) | **35** | Puffer 20%, Knowledge Sharing, Backup-Dev | PL/IT-Leitung | 🟢 Puffer geplant |
| R3 | GitHub API-Änderungen | Technisch | Mittel (40%) | Mittel (5) | **20** | Version Pinning, Tests gegen Preview-API | Dev | 🟢 Getestet |
| R4 | DSGVO-Nachweise unzureichend | Compliance | Gering (30%) | **Sehr hoch (9)** | **27** | Audit-Log-Design von Start an, DSB involviert | PL/DSB | 🟢 Design Review |
| R5 | Sicherheitslücke im Prototyp | Sicherheit | **Sehr gering (20%)** | **Kritisch (10)** | **20** | Security-Review, Bandit/Trivy in CI, Pentest | Sec-Consultant | 🟢 CI integriert |
| R6 | Betriebsrat blockiert | Organisatorisch | Gering (25%) | Hoch (8) | **20** | Frühzeitige Einbindung, Betriebsvereinbarung | PL/GF | 🟢 Eingebunden |
| R7 | IHK-Formale Mängel | Formal | Sehr gering (15%) | Hoch (8.5) | **12.75** | Checkliste (40 Seiten, Eidesstattl., Sperrvermerk) | PL | 🟢 Checkliste |
| R8 | Budget-Überschreitung | Finanziell | Mittel (30%) | Mittel (5) | **15** | Monatliches Controlling, Eskalation >10% | PL/GF | 🟢 Im Rahmen |
| R9 | Terminverzug (Abgabe) | Termin | Gering (20%) | **Kritisch (9.5)** | **19** | Puffer 2 Wochen, interne Deadline 15.10. | PL | 🟢 Puffer |
| R10 | Know-how-Verlust | Personal | Gering (25%) | Mittel (6.5) | **16.25** | Dokumentation, Pair Programming, Bus-Factor 2 | PL/Dev | 🟢 Dokumentiert |

**Abb. Z: Risiko-Matrix mit quantitativer Bewertung (FMEA-ähnlich) – Maßnahmen & Status**