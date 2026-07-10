---
title: "DSGVO-Checkliste (Art. 5, 25, 32)"
---

| Art. DSGVO | Prüfpunkt | Status | Nachweis / Verweis |
|------------|-----------|--------|-------------------|
| **Art. 5** | **Grundsätze** | | |
| 5(1)a | Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz | ✅ | Kap. 3.5, 3.6 |
| 5(1)b | Zweckbindung | ✅ | Kap. 1.3.5, 3.6 |
| 5(1)c | Datenminimierung | ✅ | Kap. 3.5, 3.6, A14 |
| 5(1)d | Richtigkeit | ✅ | Kap. 3.5, 4.7 |
| 5(1)e | Speicherbegrenzung | ✅ | Kap. 3.6, A14 |
| 5(1)f | Integrität & Vertraulichkeit | ✅ | Kap. 3.6, 4.7 |
| 5(2) | Rechenschaftspflicht | ✅ | Kap. 3.6, 4.7, A14 |
| **Art. 25** | **Datenschutz durch Technikgestaltung & Standard** | | |
| 25(1) | Technische & organisatorische Maßnahmen | ✅ | Kap. 3.5, 4.7, A14 |
| 25(2) | Datenschutzfreundliche Voreinstellungen | ✅ | Kap. 3.5, 3.6 |
| **Art. 32** | **Sicherheit der Verarbeitung** | | |
| 32(1)a | Pseudonymisierung & Verschlüsselung | ✅ | TLS 1.3, DB at Rest, Kap. 3.6 |
| 32(1)b | Vertraulichkeit, Integrität, Verfügbarkeit | ✅ | RBAC, Least Privilege, Kap. 3.6 |
| 32(1)c | Verfahren zur Wiederherstellung | ✅ | Backup, Recovery, Kap. 3.6 |
| 32(1)d | Regelmäßige Überprüfung | ✅ | Monitoring, Alerting, Kap. 3.6 |
| 32(2) | Risikobeurteilung | ✅ | DPIA, Kap. 3.6, A14 |

---

### Technische & Organisatorische Maßnahmen (TOMs, Art. 32)

| Maßnahme | Implementierung | Status |
|----------|----------------|--------|
| Verschlüsselung | TLS 1.3 (Transport), DB at Rest Encryption | ✅ |
| Vertraulichkeit | RBAC, Least Privilege, Need-to-know | ✅ |
| Integrität | Append-only Audit-Log, Hash-Chain | ✅ |
| Verfügbarkeit | Docker Compose, Backup, Monitoring | ✅ |
| Belastbarkeit | Prometheus/Grafana Alerting, Health-Checks | ✅ |

---

### DPIA (Datenschutz-Folgenabschätzung)

| Aspekt | Status |
|--------|--------|
| Erforderlichkeit geprüft | ✅ Ja (Art. 35) |
| DPIA durchgeführt | ✅ In Kap. 3.6 dokumentiert |
| DSB beteiligt | ✅ 4h Beratung |
| Risiken bewertet | ✅ Risikomatrix Kap. 2.6 |