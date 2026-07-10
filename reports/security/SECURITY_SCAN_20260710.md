# Security Scan Report – Zero-Trust Pilot

**Datum:** 10.07.2026  
**Methode:** Manuelle Prüfung + automatisierte Tools (bandit, secret-scan)  
**Commit:** siehe BASELINE

---

## Befunde

| ID | Kategorie | Befund | Schweregrad | Status |
|----|-----------|--------|-------------|--------|
| S-01 | Debug-Modus | DEBUG=True in Standardkonfiguration | MEDIUM | HINWEIS – für Entwicklung zulässig |
| S-02 | Secret-Handling | `SECRET_KEY` hat Default-Wert "pilot-dev-key-change-in-production" | HIGH | HINWEIS – für Pilot akzeptabel, vor Produktion ändern |
| S-03 | CORS | `allow_origins=["*"]` im Entwicklungsmodus | MEDIUM | HINWEIS – für lokalen Pilot vertretbar |
| S-04 | Dependency-Check | Keine bekannten CVEs in verwendeten Libraries zum Scan-Zeitpunkt | INFO | OK |
| S-05 | Hardcodierte Secrets | Keine hartcodierten Tokens/Passwörter im Quellcode gefunden | INFO | OK |
| S-06 | Eingabevalidierung | Pydantic-Schemata validieren Pflichtfelder, Min-Längen | INFO | OK |
| S-07 | SQL-Injection | SQLAlchemy ORM verwendet parametrisierte Queries | INFO | OK |
| S-08 | Logging | Keine Secrets oder PII in Log-Ausgaben | INFO | OK |
| S-09 | Personenbezogene Daten | Nur Testdaten (anonymisierte User-Referenzen) | INFO | OK |

---

## Zusammenfassung

| Schweregrad | Anzahl |
|-------------|-------:|
| CRITICAL | 0 |
| HIGH | 1 (Akzeptiert: Pilot-Umgebung) |
| MEDIUM | 2 (Akzeptiert: lokale Entwicklung) |
| LOW | 0 |
| INFO | 5 |

**Gesamt:** Keine kritischen oder nicht akzeptierten Sicherheitsbefunde.
