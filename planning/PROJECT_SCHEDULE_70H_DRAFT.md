# PROJECT SCHEDULE – 70-Stunden-Plan (Entwurf)

> **Status:** ENTWURF – noch nicht freigegeben  
> **Hinweis:** Alle Zeiten sind PLAN-Werte. Keine Ist-Zeiten eingetragen.  
> **Prüfung:** 4+6+5+8+8+9+8+8+5+9 = 70 ✓

---

## Zeitplan (Kalenderwochen basierend auf tatsächlichem Startdatum)

| Woche | AP | Bezeichnung | Plan (h) | Kumuliert |
|:-----:|:--:|-------------|---------:|----------:|
| 1 | 1 | Projektauftrag und Kick-off | 4 | 4 |
| 1 | 2 | Ist-Analyse und Anforderungen | 6 | 10 |
| 2 | 3 | Variantenbewertung und Lösungsentscheidung | 5 | 15 |
| 2 | 4 | Architektur, Rollen- und Datenmodell | 8 | 23 |
| 3 | 5 | Backend-Grundstruktur und Datenhaltung | 8 | 31 |
| 3 | 6 | Antrags-, Policy- und Genehmigungsworkflow (Teil 1) | 4 | 35 |
| 4 | 6 | Antrags-, Policy- und Genehmigungsworkflow (Teil 2) | 5 | 40 |
| 4 | 7 | GitHub-Integration und Audit-Verkettung | 8 | 48 |
| 5 | 8 | Tests, CI und Fehlerkorrektur | 8 | 56 |
| 5 | 9 | Pilotreview, Schulung und Abnahme | 5 | 61 |
| 6 | 10 | Soll-Ist-Auswertung und Abschlussdokumentation | 9 | 70 |

---

## Meilensteine

| MS | Bezeichnung | KW | Abnahmekriterium |
|----|-------------|:--:|------------------|
| M1 | Projekt freigegeben | W1 | Projektauftrag unterschrieben |
| M2 | Planung abgeschlossen | W2 | Architektur-Review bestanden |
| M3 | Backend funktional | W3 | Health-Endpoint → 200 |
| M4 | Workflow vollständig | W4 | Antrag→Genehmigung→Provisionierung getestet |
| M5 | CI etabliert | W5 | CI-Pipeline läuft erfolgreich |
| M6 | Pilot abgenommen | W5 | Abnahmeprotokoll unterschrieben |
| M7 | Dokumentation final | W6 | PDF liegt vor (alle Claims VERIFIED) |

---

## Puffer

| AP | Risikopuffer | Begründung |
|----|:------------:|------------|
| 6 | ±2 h | Policy-Integration unerwartet komplex |
| 7 | ±2 h | GitHub-API-Integration |
| 8 | ±2 h | CI-Konfiguration |
| **Gesamtpuffer** | **6 h** | entspricht ~9 % des Gesamtbudgets |
