# DATASET_SCOUT.md

## Zweck
Recherche-Dokumentation für mögliche spätere ML-Nutzung.
Nicht Teil des finalen IHK-Prototyps.

## Regeln
- Keine personenbezogenen Echtdaten verwenden
- Keine neuen Behauptungen in finale PDF übernehmen
- Lizenzprüfung erforderlich vor Nutzung
- Kein automatischer Download

## Kandidaten

### SIEM/Security Logs
- **Zweck:** Training für Anomalieerkennung in Security-Events
- **Suchbegriffe:** wazuh alerts, siem logs, security event, intrusion detection
- **Lizenz:** Prüfung erforderlich (CC-BY, MIT, proprietär)
- **Risiko:** Kann personenbezogene IPs/Hostnames enthalten

### Wazuh Alerts
- **Zweck:** Klassifikation von Sicherheitsalerts
- **Suchbegriffe:** wazuh, ossec, alert classification
- **Lizenz:** Apache 2.0 (Wazuh selbst), Datasets variieren
- **Risiko:** Echte Alert-Daten können sensibel sein

### GitHub Issues mit CVE-Bezug
- **Zweck:** Analyse von Schwachstellen-Meldungen
- **Suchbegriffe:** github issues CVE, vulnerability disclosure, security advisory
- **Lizenz:** GitHub Terms, Open Data
- **Risiko:** Niedrig — öffentliche Daten

### Code Vulnerability Detection
- **Zweck:** Training für automatische Code-Schwachstellen-Erkennung
- **Suchbegriffe:** code vulnerability, SAST dataset, security code review
- **Lizenz:** Variiert — Einzelfallprüfung
- **Risiko:** Möglicherweise urheberrechtlich geschützter Code

### Security Event Classification
- **Zweck:** Klassifikation nach MITRE ATT&CK Framework
- **Suchbegriffe:** security event classification, MITRE ATT&CK dataset, threat intelligence
- **Lizenz:** MITRE ATT&CK ist öffentlich
- **Risiko:** Niedrig

### Audit Log Anomaly Detection
- **Zweck:** Erkennung von Anomalien in Audit-Logs
- **Suchbegriffe:** audit log anomaly, log analysis dataset, anomaly detection logs
- **Lizenz:** Prüfung erforderlich
- **Risiko:** Kann echte Benutzeraktivitäten enthalten

## Empfehlung
Für die vorliegende Projektarbeit: Keine produktive ML-Integration.
HF dient nur als Recherche-Plattform für mögliche Erweiterungen.

## Nächste Schritte
1. Lizenz jedes Datensatzes einzeln prüfen
2. Anonymisierung vor任何 Training
3. Keine echten Produktionsdaten verwenden