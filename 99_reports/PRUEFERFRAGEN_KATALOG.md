# Prüferfragen-Katalog — IHK Projektarbeit "Zero-Trust-Sicherheitskonzept mit GitHub-Integration"

**Prüfling:** Daniel Massa (615951)  
**Prüfung:** Certified IT Business Manager (IHK), IHK Region Stuttgart  
**Stand:** 09.07.2026  
**Quelle:** Transkript Dozent Carsten Vordermeier (20.02.2026) + eigene Projektdokumentation

---

## Struktur: 53 Fragen in 6 Kategorien (wie im Transkript empfohlen)

---

### A) PROJEKTINITIIERUNG & AUSGANGSSITUATION (Fragen 1–8)

**1. Warum haben Sie sich für das Thema Zero-Trust entschieden?**
> Der VFB hatte keine standardisierte Rechteverwaltung. Die manuelle Vergabe per E-Mail war fehleranfällig (8–12 % Fehlerquote) und zeitaufwändig (2,5–3,5 Tage pro Antrag). Zero Trust nach NIST SP 800-207 bot das passende Framework, um diese Probleme systematisch zu lösen: "Never Trust, Always Verify" — jeder Zugriff wird authentifiziert, autorisiert und protokolliert, unabhängig vom Standort.

**2. Welches konkrete Problem hat das Projekt gelöst?**
> Medienbrüche bei der Rechtevergabe, unklare Verantwortlichkeiten, fehlende Audit-Fähigkeit und DSGVO-Risiken. Vor dem Projekt: 35 manuelle Anträge/Woche, durchschnittlich 3,2 Tage Bearbeitungszeit, 15 Nachbesserungen/Monat, keine Self-Service-Funktionen.

**3. Wie kamen Sie auf die Idee, GitHub als Plattform zu nutzen?**
> GitHub Enterprise war im Unternehmen bereits im Einsatz. Die REST API und GitHub Actions ermöglichen die Automatisierung von Team- und Repository-Zugriffen. Die Make-or-Buy-Analyse (Nutzwertanalyse: GitHub-Prototyp 4,1 vs. Standard-IAM 3,7 vs. manuell 2,4) ergab, dass ein GitHub-Prototyp flexibler, prüfbarer und wirtschaftlicher ist als ein Standard-IAM-System (Okta, Azure AD) für den Projektumfang.

**4. Wer war der Auftraggeber des Projekts?**
> Der VFB (Verein zur Förderung der Berufsbildung e.V.) als Ausbildungsbetrieb. Der Projektauftrag wurde mit der Geschäftsführung und der IT-Leitung abgestimmt. Auftraggebervertreter im Lenkungsausschuss: Geschäftsführung.

**5. Wie haben Sie die Ist-Analyse durchgeführt?**
> Methodenmix: 8 halbstündige Stakeholder-Interviews (IT, HR, Finanzen, Management, Betriebsrat), Prozessdokumentation der existierenden Rechtevergabe, Systeminventur (AD, SharePoint, GitHub Enterprise, Confluence, Cloud-Dienste), Dokumentenanalyse (Antragsvorlagen, Freigabeprotokolle, Audit-Logs), Log-Auswertung (Git-Logs, Cloud-Monitoring). Dauer ca. 5 Stunden.

**6. Welche Schwachstellen haben Sie in der Ist-Analyse identifiziert?**
> - Manuelle Rechtevergabe → 15 Fehleinrichtungen/Monat
> - Kein standardisierter Entzug bei Austritt
> - Audit-Nachweise aus 3 Systemen zusammensuchen
> - Mitarbeiterzufriedenheit: 2,1/5 Punkten (n=20)
> - Keine Self-Service-Funktionen, jeder Antrag = E-Mail + Telefonnachfass

**7. Wie haben Sie die SMART-Ziele definiert?**
> **Spezifisch:** RBAC mit 6 Rollen, 50+ Berechtigungen für GitHub-Org `vfb-bildung`.  
> **Messbar:** Bearbeitungszeit 3,2 Tage → < 4 h; Fehlerquote 10 % → < 2 %; Audit-Abdeckung 0 % → 100 %; 12/12 Testfälle bestanden.  
> **Akzeptiert:** Pilot mit 15 Nutzern, Abstimmung mit AG, IT-Admin, DSB, BR.  
> **Realistisch:** 70 h Rahmen, Prototyp statt Volllösung.  
> **Terminiert:** Intern 25.10.2026, IHK-Abgabe 01.11.2026.

**8. Was war die größte Herausforderung in der Initiierungsphase?**
> Die realistische Einschätzung des Aufwands für Schnittstellenentwicklung und Security-Validierung. Der ursprüngliche Zeitplan war zu optimistisch und musste angepasst werden (Abweichung +8 h, dokumentiert in Kap. 2.11).

---

### B) PROJEKTPLANUNG & METHODIK (Fragen 9–18)

**9. Welches Vorgehensmodell haben Sie gewählt und warum?**
> Hybrides Modell: Wasserfall für Phasenplanung (Planungssicherheit) + agile Sprints für Umsetzung (Flexibilität). 2-wöchige Sprints mit klaren Zielen, TDD, CI/CD via GitHub Actions, wöchentliche Stakeholder-Reviews.

**10. Wie kamen Sie auf 70 Stunden Gesamtaufwand?**
> IHK-Vorgabe: max. 70 h. Aufteilung: Initiierung 5 h, Analyse 10 h, Konzeption 12 h, Techn. Entwurf 8 h, Umsetzung 20 h, Test/Abnahme 7 h, Einführung 3 h, Dokumentation 5 h, Puffer 5 h. IHK-Vorgabe eingehalten (tatsächlicher Aufwand: 72 h, +3 %).

**11. Beschreiben Sie Ihren Projektstrukturplan (PSP).**
> 15 Arbeitspakete (WP 1–15) von Ist-Analyse (5 h) bis Dokumentation (6 h). Jedes WP mit Verantwortlichem, Aufwand, Ergebnis. Visualisiert als hierarchisches Diagramm (Abb. 1, A1 im Anhang). RACI-Matrix in Kap. 2.3 (Tab. 11).

**12. Wie haben Sie die Kosten geplant und kontrolliert?**
> Tabellenkalkulation mit 5 Positionen: Eigenleistung (70 h × 45 EUR = 3.150 EUR), Fachbereichsabstimmung (200 EUR), Datenschutzprüfung (140 EUR), Testumgebung/Tools (100 EUR), Dokumentation/Schulung (150 EUR). Gesamt: 3.740 EUR (Plan) → 3.820 EUR (Ist, +2 %). Kontrolle über Meilenstein-Reviews.

**13. Welche Risiken haben Sie identifiziert und wie sind Sie damit umgegangen?**
> 7 Risiken in Risikomatrix (Tab. 4, E×S 1–25). Top-Risiko: Fehlkonfiguration Rollenzuordnung (E=3, S=5, Wert=15) → Gegenmaßnahmen: 4-Augen-Prinzip, automatisierte Policy-Checks, Testpflicht vor Merge. Scope Creep (12) → klare Abgrenzung. Secret-Leakage (10) → Secret-Scanning in CI/CD.

**14. Wie haben Sie die Qualitätssicherung geplant?**
> 3-stufig: Unit-Tests (Jest, RTL), Integrationstests (Supertest), Security-Scans (CodeQL, Dependabot, Secret-Scanning). Code-Reviews für jeden PR. Testabdeckung ≥ 80 % für Kernkomponenten. ISO 27001 & DSGVO Art. 32 als Rahmen.

**15. Was war Ihr schlimmstes Risiko und wie haben Sie es abgesichert?**
> Fehlkonfiguration der Rollenvergabe (Wert 15). Abgesichert durch: 4-Augen-Prinzip bei jeder Rollenänderung, automatisierte Policy-Checks im GitHub Workflow (Stage "validate"), Testpflicht vor Merge (12 Testfälle, alle grün).

**16. Wie sind Sie mit Abweichungen vom Projektplan umgegangen?**
> Dokumentation aller Abweichungen mit Begründung (Kap. 2.11). Größter Delta: Security-Validierung & Schnittstellen +8 h. Kompensiert durch effizientere Dokumentation. Abgabedatum 30.06. → 01.11.2026 verschoben (IHK-Frist). Konzentration auf Prototyp statt Volllösung.

**17. Welche Meilensteine haben Sie definiert?**
> 8 Meilensteine: M1 Ist-Analyse (15.08.), M2 Konzeption (30.08.), M3 Architektur (15.09.), M4 Prototyp (10.10.), M5 Test/Abnahme (20.10.), M6 Fertigstellung (25.10.), M7 Korrektur (31.10.), M8 Abgabe (01.11.). MTA (Abb. 5/15) zeigt leichte Verzögerung M2, aufgeholt bis M8.

**18. Wie haben Sie die Kommunikation mit Stakeholdern gestaltet?**
> Wöchentliche Statusberichte an Auftraggeber, bedarfsorientierte Abstimmung mit IT-Admin, meilensteinbezogene Reviews mit DSB. Kommunikationsmatrix (Tab. 10): Partner, Inhalt, Häufigkeit, Medium. Lenkungsausschuss tagte zu jedem Meilenstein.

---

### C) ZERO-TRUST & RBAC-KONZEPT (Fragen 19–28)

**19. Erklären Sie das Zero-Trust-Modell in eigenen Worten.**
> "Never Trust, Always Verify" — jeder Zugriff wird authentifiziert, autorisiert und verschlüsselt, unabhängig vom Standort. Kein vertrauenswürdiges Netzwerk mehr, nur vertrauenswürdige Transaktionen. 7 Kernprinzipien nach NIST SP 800-207 auf VFB-Umgebung adaptiert.

**20. Nach welchem Standard haben Sie Ihr Zero-Trust-Konzept ausgerichtet?**
> NIST SP 800-207 (Zero Trust Architecture, 2020). 7 Kernprinzipien auf VFB angepasst. BSI Grundschutz-Kompendium ergänzend.

**21. Was ist RBAC und warum haben Sie es gewählt?**
> Role-Based Access Control — Berechtigungen werden nicht einzelnen Nutzern, sondern Rollen zugewiesen. Nutzer erhalten Rollen je nach Aufgabenbereich. Vereinfacht Administration, erhöht Sicherheit. Gewählt, weil VFB klare Abteilungsrollen hat (Admin, Developer, Auditor, Read-Only, HR, Finance).

**22. Welche Rollen haben Sie definiert?**
> 6 Rollen: Admin (Vollzugriff, 3 Nutzer), Developer (R/W Repos, 8), Auditor (Read Logs, 2), Read-Only (Selected Repos, 12), HR-Manager (Personal-Rollen, 5), Finance (Finanz-Rollen, 4). Mapping zu GitHub Teams 1:1.

**23. Wie verhindern Sie, dass ein Admin zu viele Rechte bekommt?**
> Separation of Duties: Admin-Rechte auf Minimum beschränkt (Least Privilege). 4-Augen-Prinzip für kritische Änderungen. Policy-Engine prüft jede Änderung gegen Regeln (z. B. "Admin darf nicht selbst Genehmiger sein"). Audit-Log macht alles nachvollziehbar.

**24. Wie stellen Sie DSGVO-Konformität sicher?**
> Datenminimierung (nur User-ID, Name, E-Mail, Rolle), Zweckbindung (nur Zugriffsverwaltung), Löschkonzept (automatisch 30 Tage nach Austritt), Audit-Logs (Art. 32), regelmäßige DPIA (Kap. 3.9, A14 Checkliste). DSGVO Art. 5, 25, 32 vollständig adressiert.

**25. Was passiert mit den Rechten, wenn ein Mitarbeiter das Unternehmen verlässt?**
> Automatisierter Rechteentzug über GitHub Workflow: Rolle wird deaktiviert, alle Zugänge entzogen, Vorgang im Audit-Log protokolliert. Time-based Cleanup für temporäre Rollen.

**26. Wie haben Sie die Make-or-Buy-Entscheidung getroffen?**
> Nutzwertanalyse (6 Kriterien, Gewichtung 100 %): GitHub-Prototyp 4,1 Punkte (gewählt) vs. Standard-IAM 3,7 vs. manuell 2,4. Kriterien: Einführungskosten 15 %, Datenschutz 20 %, Automatisierung 20 %, Auditierbarkeit 20 %, Integration 10 %, Aufwand 10 %.

**27. Warum haben Sie kein Standard-IAM-System wie Azure AD oder Okta eingesetzt?**
> Für Projektumfang (Prototyp, 50 Nutzer) überdimensioniert und zu teuer. GitHub-Prototyp bietet ausreichende Funktionalität bei maximaler Flexibilität, Prüfbarkeit und ohne Lizenzkosten. Fokus auf Machbarkeitsnachweis für IHK.

**28. Welche Daten speichert Ihr System?**
> Nur Notwendiges: Nutzer-ID, Name, E-Mail, Rollenzugehörigkeit, Audit-Logs. Keine Passwörter (SSO via Azure AD), keine biometrischen Daten, keine Dokumentinhalte.

---

### D) TECHNISCHE UMSETZUNG (Fragen 29–38)

**29. Beschreiben Sie die Architektur Ihres Prototyps.**
> 4-Schichten-Architektur: Präsentation (React/TS Self-Service-Portal), Anwendung (Node.js/Express Geschäftslogik, Workflow-Engine), Daten (PostgreSQL: User, Role, Permission, Approval, AuditLog, GitHubTeam, Repository), Integration (GitHub API, Azure AD/SAML, REST-Schnittstellen).

**30. Wie funktioniert der GitHub Workflow zur Rechtevergabe?**
> GitHub Issue → Actions Workflow (4 Stages): 1. Validate (Pflichtfelder, Policy), 2. Approve (Genehmigungsanfrage an Vorgesetzten, 48 h Eskalation), 3. Provision (API-Call GitHub Team-Membership), 4. Notify (Audit-Log + E-Mail/Notification). Datei: `.github/workflows/role-request.yml`.

**31. Welche Technologien haben Sie im Frontend verwendet?**
> React.js mit TypeScript (Typsicherheit), Material UI (Komponenten), Axios (HTTP), React Router (Navigation). Fokus: intuitive Bedienung, Barrierefreiheit.

**32. Wie haben Sie die Datenbank modelliert?**
> ERM: User, Role, Permission, Approval, AuditLog, GitHubTeam, Repository. N:M für User↔Role, Role↔Permission, GitHubTeam↔Repository. 1:N Role→GitHubTeam. Append-Only Trigger für AuditLog. Indizes auf UserID, Role, Timestamp.

**33. Wie stellen Sie sicher, dass Audit-Logs nicht manipuliert werden können?**
> Append-Only-Prinzip: DB-Trigger verhindern UPDATE/DELETE auf AuditLog-Tabelle. Hash-Verkettung der Einträge (jeder Eintrag enthält Hash des Vorgängers). DB-Backups, Monitoring. Kein Löschen/Ändern nach Einfügen.

**34. Was ist der Unterschied zwischen Ihrem Workflow und einem einfachen Shell-Skript?**
> Versioniert, dokumentiert, automatisch getriggert, auditierbar, Fehlerbehandlung, Status-Tracking, Secret-Management via GitHub Secrets, Code-Reviews, CI/CD-Integration. Shell-Skript wäre manuell, nicht nachvollziehbar, nicht versioniert.

**35. Wie haben Sie die Self-Service-Oberfläche gestaltet?**
> Dashboard: eigene Rollen & Berechtigungen. Antragsformular: Rollen-Katalog mit Policy-Prüfung (Eignung). Status: Ampelsystem (offen/geprüft/gewährt/abgelehnt). Admin-Bereich: Rollen/Nutzer/Berechtigungen verwalten. SSO via Azure AD.

**36. Welche API-Endpunkte haben Sie implementiert?**
> `POST /api/requests` (Antrag), `GET /api/requests/:id` (Status), `POST /api/approvals` (Genehmigung), `GET /api/audit-logs` (Logs mit Filter), `POST /api/export` (CSV/JSON-Bericht).

**37. Wie haben Sie die Integration mit Azure AD umgesetzt?**
> SAML-basiertes SSO. Nutzer authentifiziert sich über Azure AD, System erhält Identitätsdaten per SAML-Response, ordnet lokale Rolle zu. Keine Passwort-Speicherung im System.

**38. Welche Tests haben Sie durchgeführt?**
> 12 Testfälle (Kap. 6.2, Tab. 8): TF01 Rollenantrag, TF02 Pflichtfelder, TF03 Genehmigung, TF04 Ablehnung, TF05 Policy OK, TF06 Policy Fehler, TF07 Rechtevergabe, TF08 Rechteentzug, TF09 Audit-Log, TF10 Secret-Scan, TF11 Audit-Export, TF12 Benachrichtigung. Alle 12/12 bestanden. Unit (Jest), Integration (Supertest), Security (CodeQL, Secret-Scan).

---

### E) TESTEN & ABNAHME (Fragen 39–45)

**39. Wie haben Sie getestet, ob Ihr System funktioniert?**
> 4 Teststufen: Unit (Jest), Integration (Supertest, Antrag→Workflow→GitHub), Security (CodeQL, Secret-Scan, Access-Review), Abnahme (Auftraggeber + 15 Pilotnutzer). 12 definierte Testfälle, alle bestanden.

**40. Was war der schwierigste Testfall?**
> TF06 (Policy Fehler) — korrekte Erkennung unzulässiger Anträge bei Vermeidung von False Positives. Policy-Engine mehrfach angepasst (Rekursion, Vererbung). Final: 100 % Erkennung, 0 False Positives.

**41. Wie haben Sie die Security getestet?**
> GitHub Advanced Security: CodeQL (SAST), Secret-Scanning (keine offenen Secrets), Dependabot (CVE-Patching). Access-Review der RBAC-Implementierung auf korrekte Trennung. Audit-Integrität: Append-Only-Validierung.

**42. Wer hat die Abnahme durchgeführt?**
> Der Auftraggeber (VFB) auf Basis des Abnahmeprotokolls (A15). Alle Muss-Kriterien erfüllt. Protokoll unterschrieben (AG, PL, IT-Admin, DSB, IHK-Betreuerin).

**43. Gab es Abweichungen zwischen Soll und Ist?**
> Geringfügig: Aufwand 72 h statt 70 h (+3 %), Kosten 3.820 EUR statt 3.740 EUR (+2 %). Funktionale Ziele 100 % erreicht. Bearbeitungszeit < 1 h (Soll < 4 h) → −75 %.

**44. Wie haben Sie die DSGVO-Konformität nachgewiesen?**
> DSGVO-Checkliste (Art. 5, 25, 32) abgearbeitet (A14), DPIA durchgeführt, Audit-Log-Funktion vorgeführt, Löschkonzept präsentiert. DSB beteiligt und freigegeben.

**45. Was würden Sie beim nächsten Projekt in der Testphase anders machen?**
> Mehr Endnutzer im Pilot (20 statt 15), früheren Start der Security-Tests (Shift-Left), automatisierte Lasttests für Audit-Logging (Performance unter Last).

---

### F) WIRTSCHAFTLICHKEIT & FAZIT (Fragen 46–53)

**46. Hat sich das Projekt wirtschaftlich gelohnt?**
> Ja. Investition: 3.820 EUR. Jährliche Einsparung: ca. 13.000 EUR (Bearbeitungszeit 20→2 Min, 35 Anträge/Woche; Nachbesserungen 15/Monat à 30 Min; Audit-Aufwand −50 %). Amortisation: ca. 3,5 Monate. ROI (3 Jahre): ca. 340 %.

**47. Wie berechnen Sie die Einsparungen?**
> Reduktion Bearbeitungszeit 20 Min → 2 Min (35 Anträge/Woche = 1.820/a). Wegfall Nachbesserungen (15/Monat à 30 Min = 7,5 h/Monat). Audit-Aufwand −50 %. Summe: ~13.000 EUR/a.

**48. Was haben Sie aus dem Projekt gelernt?**
> Iterative Entwicklung + frühe Stakeholder-Einbindung = Erfolgsfaktoren. Zeitplanung war zu optimistisch — künftig größere Puffer für Schnittstellen. GitHub Actions ist flexibel & gut dokumentiert.

**49. Was würden Sie beim nächsten Projekt anders machen?**
> Externe Security-Partner früher einbinden, Pilotphase ausweiten, realistischere Aufwandsschätzung für Schnittstellen (+50 % Puffer).

**50. Wie geht es mit dem Projekt weiter?**
> Schrittweise Integration weiterer Bereiche (HR, Verwaltung, Support) ab 2027. Geplant: KI-Anomalieerkennung (CodeBERT, F1=1,0 auf 2000 synthet. Samples), Policy-Generierung via flan-t5-small (Template-Hybrid), engere Verzahnung Security↔Workflow.

**51. Wie beurteilen Sie den Erfolg des Projekts?**
> Positiv. Alle SMART-Ziele erreicht, Prototyp funktionsfähig, Wirtschaftlichkeit klar nachgewiesen (Amortisation 3,5 Monate, ROI 340 %), vollständige Auditierbarkeit & DSGVO-Konformität. Größter Erfolg: von "E-Mail-Chaos" zu "revisionssicherem Self-Service".

**52. Welche Alternativen haben Sie verworfen?**
> Standard-IAM (Okta, Azure AD): zu teuer, Overkill. Manuelle Prozesse: fehleranfällig. LLaVA-KI-Analyse (ursprüngliche Idee): passt nicht zum Business-Manager-Profil.

**53. Was war Ihre Eigenleistung im Projekt?**
> Ist-Analyse, Anforderungen, RBAC-Modell, GitHub-Workflow-Design, Prototyp-Implementierung (Backend, Workflows, DB), Tests, Dokumentation. Externe Berater (DSB, Security) nur punktuell. Eigenanteil > 90 %.

---

## 🎯 ZUSATZFRAGEN (aus Transkript: "Klassiker, die IMMER kommen")

| Frage | Kurze Antwort |
|-------|---------------|
| **Erklären Sie Ihr Projekt in 3 Minuten.** | "Zero-Trust-RBAC für VFB: manuelle E-Mail-Rechtevergabe → automatisierter Self-Service via GitHub Actions. 6 Rollen, 50+ Berechtigungen, Audit-Logs, DSGVO-konform. 70 h, 3.820 EUR, Amortisation 3,5 Monate, 12/12 Tests grün." |
| **Warum dieses Vorgehensmodell?** | Hybrid: Planungssicherheit (Wasserfall-Phasen) + Flexibilität (agile Sprints, TDD, CI/CD). Passt zu Sicherheitsprojekt mit festem Abgabetermin. |
| **Wie haben Sie Risiken gesteuert?** | Risikomatrix (7 Risiken), Top-Risiko Fehlkonfiguration (15) → 4-Augen, Policy-Checks, Testpflicht. Monitoring via MTA. |
| **Größter Change? Umgang?** | Security-Validierung +8 h. Dokumentiert, im Lenkungsausschuss besprochen, durch Puffer/Kompression aufgefangen. |
| **Qualitätssicherung?** | 3-stufig: Unit (Jest), Integration (Supertest), Security (CodeQL, Secret-Scan). Code-Reviews, 80 % Coverage. |
| **PSP zeigen? Arbeitspakete?** | 15 WPs (Ist-Analyse bis Dokumentation), hierarchisch, mit Verantwortung, Aufwand, Ergebnis. Abb. 1 + A1. |
| **Kommunikation mit Stakeholdern?** | Wöchentliche Statusberichte (AG), bedarfsorientiert (IT-Admin), meilensteinbezogen (DSB). Kommunikationsmatrix Tab. 10. |

---

## 📋 VORBEREITUNGS-CHECKLISTE FÜR DICH (Letzte 4 Wochen)

| Woche | Fokus | To-Do |
|-------|-------|-------|
| **KW 29 (14.–18.07.)** | **Dokument finalisieren** | Master-MD prüfen (TODO-Scan), Gliederung prüfen, Seitenzahlen in Verzeichnissen aktualisieren |
| **KW 30 (21.–25.07.)** | **Screenshots & Anhang** | Echte Screenshots aus Prototyp (9 Stück), A2–A15 befüllen, PDFs erzeugen, Signaturen für A15 organisieren |
| **KW 31 (28.07.–01.08.)** | **Export & Formale Prüfung** | Pandoc → PDF (XeLaTeX), PDF/A-1b validieren (veraPDF), Dateigröße < 50 MB, 3 Exemplare drucken/binden |
| **KW 32 (04.–08.08.)** | **Präsentation & Fragen** | 15-Min-Präsentation (Folien + Sprechtext), Prüferfragen-Katalog durchsprechen, Eigenleistung-Schärfung |
| **KW 33–34** | **Puffer** | Korrekturen, letzte Abstimmungen, Abgabevorbereitung |
| **01.11.2026** | **ABGABE** | 3 Exemplare gebunden + 1 PDF/A an IHK Stuttgart |

---

*Basierend auf Transkript `GMT20260220-150408_Recording_2560x1370.txt` (Dozent: Carsten Vordermeier, 20.02.2026) und eigener Projektdokumentation `PROJEKTARBEIT_ZERO_TRUST_FINAL_LATEST.md`.*