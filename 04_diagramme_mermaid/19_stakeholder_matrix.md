# Mermaid: Stakeholder-Matrix (Einfluss × Interesse / Power-Interest Grid)

```mermaid
---
title: Stakeholder-Matrix Zero-Trust-Projekt
---
%%{init: {'theme': 'base'}}%%
quadrantChart
    title Stakeholder-Einfluss vs. Interesse (Power-Interest Grid)
    x-axis Geringes Interesse --> Hohes Interesse
    y-axis Geringer Einfluss --> Hoher Einfluss
    quadrant-1 Latent (Informieren)
    quadrant-2 Schlüsselspieler (Eng managen)
    quadrant-3 Gleichgültig (Monitoren)
    quadrant-4 Subjektiv (Bedürfnisse berücksichtigen)

    "SH1: Geschäftsführung VFB\n(Auftraggeber)": [0.9, 0.9]
    "SH2: IT-Leitung\n(Disziplinarischer Vorgesetzter)": [0.8, 0.8]
    "SH3: Datenschutzbeauftragter\n(Compliance)": [0.7, 0.8]
    "SH4: Betriebsrat\n(Mitbestimmung)": [0.6, 0.7]
    "SH5: Projektleiter\n(Daniel Massa)": [0.9, 0.95]
    "SH6: Entwickler\n(Backend/Frontend)": [0.5, 0.8]
    "SH7: Security-Consultant\n(extern)": [0.4, 0.7]
    "SH8: IT-Administratoren\n(AD, GitHub, Netzwerk)": [0.6, 0.6]
    "SH9: Endanwender\n(Mitarbeiter, Azubis)": [0.3, 0.8]
    "SH10: IHK-Prüfungsausschuss\n(Externe Prüfer)": [0.8, 0.5]
    "SH11: Externe Auditoren\n(ISO 27001, DSGVO)": [0.5, 0.4]
```

| ID | Stakeholder | Rolle | Einfluss (1-5) | Interesse (1-5) | Kategorie | Kommunikationsstrategie | Frequenz | Verantwortlich |
|----|-------------|-------|----------------|-----------------|-----------|-------------------------|----------|----------------|
| SH1 | Geschäftsführung VFB | Auftraggeber, Budgetfreigabe | 5 | 5 | **Schlüsselspieler** | Eng managen, Lenkungskreis, Entscheidungsvorlagen | Monatlich (LK), Ad-hoc bei Entscheidungen | PL |
| SH2 | IT-Leitung | Disziplinarisch, Ressourcen | 4 | 4 | **Schlüsselspieler** | Eng managen, wöchentl. Jour-fixe, Eskalation | Wöchentlich | PL |
| SH3 | Datenschutzbeauftragter | Compliance, DPIA, DSB | 4 | 5 | **Schlüsselspieler** | Eng managen, früh einbinden, Freigabe DPIA | 2-wöchentlich, Meilensteine | PL |
| SH4 | Betriebsrat | Mitbestimmung §87 BetrVG | 3 | 4 | **Subjektiv** | Bedürfnisse berücksichtigen, früh informieren | Bei Meilensteinen, Änderungen | PL |
| SH5 | Projektleiter (Daniel Massa) | Gesamtverantwortung | 5 | 5 | **Schlüsselspieler** | Selbstmanagement, Reporting nach oben | Täglich operativ | – |
| SH6 | Entwickler | Technische Umsetzung | 3 | 4 | **Subjektiv** | Bedürfnisse berücksichtigen, Code-Reviews | Täglich (Standup) | PL |
| SH7 | Security-Consultant (extern) | Security-Review, Pen-Test | 2 | 3 | **Latent** | Informieren, Ergebnisse einfordern | Meilensteine M3, M5 | PL |
| SH8 | IT-Administratoren | AD, GitHub, Netzwerk, DB | 3 | 3 | **Gleichgültig** | Monitoren, Schnittstellen abstimmen | Bei Bedarf | Dev |
| SH9 | Endanwender (Mitarbeiter, Azubis) | Nutzer Self-Service | 2 | 4 | **Subjektiv** | Bedürfnisse berücksichtigen, UAT, Schulung | Pilotphase, Schulung | PL/Dev |
| SH10 | IHK-Prüfungsausschuss | Externe Prüfung, Note | 4 | 3 | **Latent** | Informieren, formale Vorgaben einhalten | Abgabe, Präsentation | PL |
| SH11 | Externe Auditoren (ISO/DSGVO) | Zertifizierung, Audit | 3 | 2 | **Gleichgültig** | Monitoren, Audit-Trails bereitstellen | Jährlich / Ad-hoc | DSB |

**Abb. X: Stakeholder-Matrix mit Kommunikationsplan – SH1–SH4 & SH5, SH10 als Schlüsselspieler (rote Zone) mit höchster Priorität**