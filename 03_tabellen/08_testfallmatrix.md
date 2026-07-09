# Tabelle 8: Testfallmatrix

| ID | Testobjekt | Erwartet | Tatsaechlich | Status |
|---|---|---|---|---|
| TF01 | Rollenantrag | Antrag angenommen | Antrag angenommen, GitHub Team hinzugefuegt | bestanden |
| TF02 | Pflichtfelder | Validierungsfehler | Fehlermeldung: "Feld 'Rolle' ist Pflichtfeld" | bestanden |
| TF03 | Genehmigung | Workflow laeuft | Genehmigungsworkflow durchgefuehrt, Rolle vergeben | bestanden |
| TF04 | Ablehnung | keine Rechtevergabe | Antrag abgelehnt, keine Aenderung in GitHub | bestanden |
| TF05 | Policy OK | Pruefung bestanden | Policy-Check erfolgreich, keine Violations | bestanden |
| TF06 | Policy Fehler | Pruefung blockiert | Policy-Check fehlgeschlagen, Deployment gestoppt | bestanden |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | Team-Mitglied hinzugefuegt, PR auto-merged | bestanden |
| TF08 | Rechteentzug | Zugriff entfernt | Team-Mitglied entfernt, Zugriff widerrufen | bestanden |
| TF09 | Audit-Log | Eintrag vorhanden | JSON-Eintrag in audit.log mit Timestamp, User, Action | bestanden |
| TF10 | Secret-Scan | keine Secrets | Gitleaks Scan: 0 Findings | bestanden |
| TF11 | Audit-Export | Bericht erzeugt | CSV-Export mit 47 Eintraegen erzeugt | bestanden |
| TF12 | Benachrichtigung | Status erhalten | E-Mail + GitHub Notification versendet | bestanden |

**Testsumme:** 12 / 12 bestanden (100 %)
**Testdatum:** 15.10.2026
**Tester:** Daniel Massa
**Umgebung:** Ubuntu 22.04, GitHub Enterprise Cloud, Python 3.11

(End of file - total 22 lines)