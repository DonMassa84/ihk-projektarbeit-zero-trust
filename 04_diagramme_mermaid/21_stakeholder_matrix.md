# Mermaid: Stakeholder-Matrix (Macht/Interesse)

```mermaid
---
title: Stakeholder-Matrix Zero-Trust-Projekt
---
quadrantChart
    title Macht vs. Interesse
    x-axis Geringes Interesse --> Hohes Interesse
    y-axis Geringe Macht --> Hohe Macht
    quadrant-1 "Schlüsselspieler\n(Eng einbinden)"
    quadrant-2 "Kontextsetzer\n(Regelmäßig informieren)"
    quadrant-3 "Zuschauer\n(Minimal informieren)"
    quadrant-4 "Gefährliche Spieler\n(Engmaschig managen)"

    "Projektleiter\nDaniel Massa": [0.95, 0.95]
    "IT-Leitung\nCarsten Vordermeier": [0.9, 0.85]
    "Geschäftsführung": [0.95, 0.7]
    "Datenschutzbeauftragter": [0.8, 0.9]
    "Entwickler": [0.7, 0.9]
    "Betriebsrat": [0.6, 0.8]
    "Externer Security Consultant": [0.5, 0.85]
    "IHK Prüfer": [0.9, 0.5]
    "Mitarbeiter (Endanwender)": [0.3, 0.7]
    "GitHub Support": [0.2, 0.3]
```

**Abb. Y: Stakeholder-Matrix – Einordnung nach Macht und Interesse (RZ-Vorbild)**

| Stakeholder | Macht | Interesse | Kategorie | Maßnahmen |
|-------------|-------|-----------|-----------|-----------|
| Projektleiter Daniel Massa | Sehr hoch | Sehr hoch | **Schlüsselspieler** | Tägliche Steuerung, volle Verantwortung |
| IT-Leitung Carsten Vordermeier | Sehr hoch | Hoch | **Schlüsselspieler** | Lenkungskreis, technische Freigaben |
| Geschäftsführung | Sehr hoch | Mittel | **Kontextsetzer** | Budget, strategische Entscheidungen |
| Datenschutzbeauftragter | Hoch | Sehr hoch | **Schlüsselspieler** | DSGVO-Prüfung, TOM-Freigabe |
| Entwickler | Mittel | Sehr hoch | **Schlüsselspieler** | Operative Umsetzung, tägliche Syncs |
| Betriebsrat | Mittel | Hoch | **Kontextsetzer** | Mitbestimmung §87 BetrVG, anhören |
| Ext. Security Consultant | Mittel | Hoch | **Kontextsetzer** | Reviews, Pen-Test, Beratung |
| IHK Prüfer | Sehr hoch | Gering | **Gefährlicher Spieler** | Formale Kriterien prüfen, keine Überraschungen |
| Mitarbeiter (Endanwender) | Gering | Mittel | **Zuschauer** | Pilot-User, Feedback, Schulung |
| GitHub Support | Gering | Gering | **Zuschauer** | Nur bei Störungen kontaktieren |