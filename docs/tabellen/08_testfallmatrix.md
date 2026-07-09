# Tabelle 8: Testfallmatrix

| ID | Testobjekt | Erwartet | Tatsaechlich | Status |
|---|---|---|---|---|
| TF01 | Rollenantrag | Antrag angenommen | Antrag via Self-Service-Portal erstellt, ID zurueckgegeben | bestanden |
| TF02 | Pflichtfelder | Validierungsfehler | Pydantic-Validierung meldet Fehlende Pflichtfelder (400) | bestanden |
| TF03 | Genehmigung | Workflow laeuft | GitHub Action `rbac-workflow.yml` ausgeloest, Genehmigung erfasst | bestanden |
| TF04 | Ablehnung | keine Rechtevergabe | Bei Ablehnung kein API-Call, Audit-Log "REJECTED" | bestanden |
| TF05 | Policy OK | Pruefung bestanden | OPA-Policy erlaubt Konfiguration, Validierung grün | bestanden |
| TF06 | Policy Fehler | Pruefung blockiert | OPA blockiert nicht konforme Anfrage, HTTP 403 | bestanden |
| TF07 | Rechtevergabe | GitHub-Team aktualisiert | `addCollaborator` fuehrt Rolle im Team aus | bestanden |
| TF08 | Rechteentzug | Zugriff entfernt | `removeCollaborator` entzieht Berechtigung sofort | bestanden |
| TF09 | Audit-Log | Eintrag vorhanden | PostgreSQL-Eintrag mit User, Aktion, Zeitstempel vorhanden | bestanden |
| TF10 | Secret-Scan | keine Secrets | gitleaks-Scan im CI sauber, keine Treffer | bestanden |
| TF11 | Audit-Export | Bericht erzeugt | CSV-/JSON-Export ueber API erzeugt | bestanden |
| TF12 | Benachrichtigung | Status erhalten | E-Mail/Webhook-Benachrichtigung an Antragsteller gesendet | bestanden |
