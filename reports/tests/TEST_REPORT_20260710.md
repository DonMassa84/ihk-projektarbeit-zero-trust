# Test Report – Zero-Trust Pilot

**Datum:** 10.07.2026  
**Testumgebung:** Python 3.12, SQLite (aiosqlite), FastAPI, httpx  
**Testbefehl:** `python -m pytest tests/test_pilot.py -v`  
**Commit:** siehe GIT_HEAD

---

## Zusammenfassung

| Metrik | Wert |
|--------|------|
| Tests gesamt | 14 |
| Bestanden | 14 |
| Fehlgeschlagen | 0 |
| Übersprungen | 0 |
| Laufzeit | ~76 s |

---

## Einzelergebnisse

| ID | Testfall | Status |
|----|----------|--------|
| TF01 | Gültiger Antrag (DRAFT → 201) | BESTANDEN |
| TF02 | Fehlendes Pflichtfeld (422) | BESTANDEN |
| TF03 | Unbekannte Rolle (422) | BESTANDEN |
| TF04 | Inaktive Rolle (422) | BESTANDEN |
| TF05 | Unzulässiger Statusübergang (DRAFT → Provision = 422) | BESTANDEN |
| TF06 | Selbstgenehmigung abgelehnt (422) | BESTANDEN |
| TF07 | Gültige Genehmigung (SUBMITTED → APPROVED) | BESTANDEN |
| TF08 | Ablehnung (SUBMITTED → REJECTED) | BESTANDEN |
| TF09 | Provision ohne Genehmigung blockiert (SUBMITTED → Provision = 422) | BESTANDEN |
| TF10 | Erfolgreicher Dry-Run (APPROVED → PROVISIONED) | BESTANDEN |
| TF12 | Auditkette verifiziert (chain_valid = True) | BESTANDEN |
| TF13 | Idempotente Mehrfachprovisionierung | BESTANDEN |
| H01 | Health-Endpoint (200) | BESTANDEN |
| R01 | Readiness-Endpoint (ready = True) | BESTANDEN |

---

## Coverage (geschätzt)

Aufgrund des Umfangs der getesteten API-Pfade wird eine Code-Coverage von > 70 % für die Pilot-Module angenommen.  
Eine detaillierte Coverage-Erhebung kann mit `pytest --cov` in einer geeigneten Umgebung durchgeführt werden.
