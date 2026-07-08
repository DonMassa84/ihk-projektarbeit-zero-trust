# A14 DSGVO-Checkliste – Zero-Trust-Sicherheitskonzept mit GitHub-Integration

## Prüfungsdatum: 08.07.2026
## Geprüft von: Daniel Massa (Projektleiter) / DSB VFB

---

### Art. 5 DSGVO – Grundsätze der Datenverarbeitung

| # | Anforderung | Status | Nachweis |
|---|-------------|--------|----------|
| 1 | Datenminimierung: Nur notwendige Daten verarbeitet | ✓ | User-ID, Name, E-Mail, Rollenzugehörigkeit – keine Passwörter, keine biometrischen Daten |
| 2 | Zweckbindung: Daten nur für Rechtevergabe genutzt | ✓ | Keine Weiterverarbeitung, kein Tracking, keine Profilerstellung |
| 3 | Richtigkeit: Daten aktuell und korrekt | ✓ | Synchronisation mit Azure AD, regelmäßige Abgleiche |
| 4 | Speicherbegrenzung: Löschfristen definiert | ✓ | Automatisierte Löschung bei Austritt, Aufbewahrung Audit-Logs: 3 Jahre |
| 5 | Integrität und Vertraulichkeit | ✓ | Verschlüsselung (TLS), Zugriffsschutz, Audit-Trail |

### Art. 25 DSGVO – Data Protection by Design & Default

| # | Anforderung | Status | Nachweis |
|---|-------------|--------|----------|
| 6 | Datenschutz durch Technikgestaltung | ✓ | RBAC, Least-Privilege, Append-Only-Audit-Logs |
| 7 | Datenschutz durch Voreinstellungen | ✓ | Standardrolle: Read-Only, keine unnötigen Berechtigungen |
| 8 | Pseudonymisierung geprüft | ✓ | Pseudonyme User-IDs statt Klarnamen in Logs |
| 9 | Verschlüsselung (Transport + Ruhend) | ✓ | TLS 1.3 für API, PostgreSQL-Verschlüsselung |

### Art. 32 DSGVO – Sicherheit der Datenverarbeitung

| # | Anforderung | Status | Nachweis |
|---|-------------|--------|----------|
| 10 | Pseudonymisierung und Verschlüsselung | ✓ | TLS, PostgreSQL-Encryption-at-Rest |
| 11 | Vertraulichkeit (Zugriffskontrolle) | ✓ | RBAC, 4-Augen-Prinzip, Self-Service mit Genehmigung |
| 12 | Integrität (Protokollierung) | ✓ | Append-Only Audit-Logs, Hash-Verkettung |
| 13 | Verfügbarkeit und Belastbarkeit | ✓ | Docker-Compose, Health-Checks, Monitoring |
| 14 | Verfahren zur regelmäßigen Überprüfung | ✓ | Jährliche Audits, wöchentliche Reports |

### Zusätzliche Maßnahmen

| # | Maßnahme | Status | Beschreibung |
|---|----------|--------|--------------|
| 15 | DPIA durchgeführt | ✓ | Datenschutz-Folgenabschätzung liegt vor |
| 16 | Auftragsverarbeitung geprüft | ✓ | GitHub Enterprise DPA vorhanden |
| 17 | Löschkonzept | ✓ | Automatisierter Rechteentzug bei Austritt |
| 18 | Betroffenenrechte | ✓ | Auskunft, Berichtigung, Löschung via Self-Service |
| 19 | Data Breach Procedure | ✓ | Benachrichtigungskette definiert (DSB → Aufsicht) |
| 20 | Mitarbeiterschulung | ✓ | Datenschutzunterweisung im Pilot enthalten |

---

**Status:** VOLLSTÄNDIG – Alle DSGVO-Anforderungen erfüllt.
**Nächste Überprüfung:** Januar 2027 oder bei wesentlichen Systemänderungen.
