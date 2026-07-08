# Prüferfragen-Katalog: Zero-Trust-Sicherheitskonzept mit GitHub-Integration

## 50+ Fragen und Antworten für die mündliche IHK-Prüfung

---

## A) Projektinitiierung & Ausgangssituation (Fragen 1–8)

**1. Warum haben Sie sich für das Thema Zero-Trust entschieden?**
Der VFB hatte keine standardisierte Rechteverwaltung. Die manuelle Vergabe per E-Mail war fehleranfällig (8–12 % Fehlerquote) und zeitaufwändig (2,5–3,5 Tage pro Antrag). Zero Trust nach NIST SP 800-207 bot das passende Framework, um diese Probleme systematisch zu lösen.

**2. Welches konkrete Problem hat das Projekt gelöst?**
Medienbrüche bei der Rechtevergabe, unklare Verantwortlichkeiten, fehlende Audit-Fähigkeit und DSGVO-Risiken. Vor dem Projekt gab es 35 manuelle Anträge pro Woche, die durchschnittlich 3,2 Tage Bearbeitungszeit benötigten.

**3. Wie kamen Sie auf die Idee, GitHub als Plattform zu nutzen?**
GitHub war im Unternehmen bereits im Einsatz und bietet mit GitHub Actions eine leistungsfähige CI/CD-Plattform. Die REST API ermöglicht die Automatisierung von Team- und Repository-Zugriffen. Die Make-or-Buy-Analyse ergab, dass ein GitHub-Prototyp flexibler und wirtschaftlicher ist als ein Standard-IAM-System.

**4. Wer war der Auftraggeber des Projekts?**
Der VFB (Verein zur Förderung der Berufsbildung e.V.) als Ausbildungsbetrieb. Der Projektauftrag wurde mit der Geschäftsführung und der IT-Leitung abgestimmt.

**5. Wie haben Sie die Ist-Analyse durchgeführt?**
Methodenmix aus Stakeholder-Interviews (8 Personen), Prozessdokumentation, Systeminventur, Dokumentenanalyse und Log-Auswertung. Die Analyse dauerte ca. 5 Stunden und bildete die Grundlage für die Anforderungsdefinition.

**6. Welche Schwachstellen haben Sie in der Ist-Analyse identifiziert?**
Manuelle E-Mail-basierte Anträge, dezentrale Audit-Logs, keine standardisierten Prozesse für Rechteentzug, durchschnittlich 15 Nachbesserungen pro Monat, keine Self-Service-Funktionen.

**7. Wie haben Sie die SMART-Ziele definiert?**
Spezifisch (RBAC mit 10+ Rollen), Messbar (Bearbeitungszeit von 3,2 Tage auf <4 h), Akzeptiert (Pilot mit 15 Nutzern), Realistisch (70 h Aufwand im Rahmen der IHK-Vorgabe), Terminiert (01.11.2026).

**8. Was war die größte Herausforderung in der Initiierungsphase?**
Die realistische Einschätzung des Aufwands für die Schnittstellenentwicklung und Security-Validierung. Der ursprüngliche Zeitplan war zu optimistisch und musste angepasst werden.

---

## B) Projektplanung & Methodik (Fragen 9–18)

**9. Welches Vorgehensmodell haben Sie gewählt und warum?**
Ein hybrides Modell aus Wasserfall (für die Phasenplanung) und agilen Methoden (für die Umsetzung in Sprints). Dies kombiniert die Planungssicherheit des Wasserfallmodells mit der Flexibilität agiler Entwicklung.

**10. Wie kamen Sie auf 70 Stunden Gesamtaufwand?**
Die IHK-Vorgabe für die Projektarbeit sieht maximal 70 Stunden vor. Die Aufteilung erfolgte nach Phasen: Analyse (10 h), Konzeption (12 h), Entwurf (8 h), Umsetzung (20 h), Test (7 h), Einführung (3 h), Dokumentation (5 h) und Projektinitiierung (5 h).

**11. Beschreiben Sie Ihren Projektstrukturplan.**
15 Arbeitspakete von der Ist-Analyse bis zur Dokumentation. Jedes Paket hat einen festgelegten Verantwortlichen, Zeitrahmen und definierte Ergebnisse. Der PSP ist als Mermaid-Diagramm visualisiert.

**12. Wie haben Sie die Kosten geplant und kontrolliert?**
Tabellenkalkulation mit 5 Positionen: Eigenleistung (70 h × 45 EUR = 3.150 EUR), Fachbereichsabstimmung (200 EUR), Datenschutzprüfung (140 EUR), Tools (100 EUR) und Dokumentation (150 EUR). Gesamt: 3.740 EUR.

**13. Welche Risiken haben Sie identifiziert und wie sind Sie damit umgegangen?**
Sieben Risiken in der Risikomatrix, darunter Fehlkonfiguration (Wert 15), DSGVO-Verstoß (10) und Secret-Leakage (10). Maßnahmen: 4-Augen-Prinzip, Datenminimierung, automatisiertes Secret-Scanning.

**14. Wie haben Sie die Qualitätssicherung geplant?**
Dreistufig: Unit-Tests (Jest, React Testing Library), Integrationstests und Security-Scans (CodeQL, Dependabot). Zusätzlich Code-Reviews für jeden Pull Request.

**15. Was war Ihr schlimmstes Risiko und wie haben Sie es abgesichert?**
Fehlkonfiguration der Rollenvergabe (Eintrittswahrsch. 3/5, Schaden 5/5 → Wert 15). Abgesichert durch 4-Augen-Prinzip bei jeder Rollenänderung, automatisierte Policy-Checks und Testpflicht vor Merge.

**16. Wie sind Sie mit Abweichungen vom Projektplan umgegangen?**
Dokumentation aller Abweichungen mit Begründung. Der größte Delta war die umfangreichere Security-Validierung (+8 h). Kompensiert durch effizientere Dokumentation.

**17. Welche Meilensteine haben Sie definiert?**
Acht Meilensteine von M1 (Ist-Analyse abgeschlossen, 15.08.2026) bis M8 (Abgabe, 01.11.2026). Visualisiert als Meilensteintrendanalyse (MTA).

**18. Wie haben Sie die Kommunikation mit Stakeholdern gestaltet?**
Wöchentliche Statusberichte an Auftraggeber, bedarfsorientierte Abstimmung mit IT-Admin, meilensteinbezogene Reviews mit Datenschutz. Dokumentiert in der Kommunikationsmatrix.

---

## C) Zero-Trust & RBAC-Konzept (Fragen 19–28)

**19. Erklären Sie das Zero-Trust-Modell in eigenen Worten.**
"Never Trust, Always Verify" – jeder Zugriff wird authentifiziert, autorisiert und verschlüsselt, unabhängig vom Standort des Nutzers. Es gibt kein vertrauenswürdiges Netzwerk mehr, nur noch vertrauenswürdige Transaktionen.

**20. Nach welchem Standard haben Sie Ihr Zero-Trust-Konzept ausgerichtet?**
NIST SP 800-207 (Zero Trust Architecture, 2020). Die sieben Kernprinzipien wurden auf die VFB-Umgebung angepasst.

**21. Was ist RBAC und warum haben Sie es gewählt?**
Role-Based Access Control – Berechtigungen werden nicht einzelnen Nutzern, sondern Rollen zugewiesen. Nutzer erhalten Rollen je nach Aufgabenbereich. Dies vereinfacht die Administration und erhöht die Sicherheit.

**22. Welche Rollen haben Sie definiert?**
Admin, Developer, Auditor, Read-Only, HR-Manager, Finance. Jede Rolle hat spezifische Berechtigungen in definierten Systemen.

**23. Wie verhindern Sie, dass ein Admin zu viele Rechte bekommt?**
Trennung von Rollen (Separation of Duties): Admin-Rechte sind auf das notwendige Minimum beschränkt (Least Privilege). Zusätzlich 4-Augen-Prinzip für kritische Änderungen.

**24. Wie stellen Sie DSGVO-Konformität sicher?**
Datenminimierung, Zweckbindung, Löschkonzepte, revisionssichere Audit-Logs, regelmäßige Datenschutzprüfungen. Die DPIA wurde durchgeführt und dokumentiert.

**25. Was passiert mit den Rechten, wenn ein Mitarbeiter das Unternehmen verlässt?**
Automatisierter Rechteentzug über den GitHub-Workflow. Die Rolle wird deaktiviert, alle Zugänge werden entzogen. Der Vorgang wird im Audit-Log protokolliert.

**26. Wie haben Sie die Make-or-Buy-Entscheidung getroffen?**
Nutzwertanalyse mit 6 Kriterien (Einführungskosten, Datenschutz, Automatisierung, Auditierbarkeit, Integration, Aufwand). Ergebnis: GitHub-Prototyp (4,1 Punkte) vs. Standard-IAM (3,7 Punkte) vs. manuell (2,4 Punkte).

**27. Warum haben Sie kein Standard-IAM-System wie Azure AD oder Okta eingesetzt?**
Für den Projektumfang (Prototyp, 50 Nutzer) wäre ein Standard-IAM überdimensioniert und zu teuer. Der GitHub-Prototyp bietet ausreichende Funktionalität bei maximaler Flexibilität und Prüfbarkeit.

**28. Welche Daten speichert Ihr System?**
Nur notwendige Daten: Nutzer-ID, Name, E-Mail, Rollenzugehörigkeit, Audit-Logs. Keine Passwörter, keine biometrischen Daten, keine Inhalte von Dokumenten.

---

## D) Technische Umsetzung (Fragen 29–38)

**29. Beschreiben Sie die Architektur Ihres Prototyps.**
Vier-Schichten-Architektur: Präsentation (React), Anwendung (Node.js/Express), Daten (PostgreSQL), Integration (GitHub API, Azure AD). Kommunikation über REST-APIs.

**30. Wie funktioniert der GitHub Workflow zur Rechtevergabe?**
GitHub Issue → Actions Workflow → Pflichtfeld-Prüfung → Policy-Check → Genehmigungsanfrage → API-Aufruf → Audit-Log → Benachrichtigung. Vier Stages: validate, approve, provision, notify.

**31. Welche Technologien haben Sie im Frontend verwendet?**
React.js mit TypeScript für Typsicherheit. Material UI als Komponentenbibliothek. Axios für HTTP-Requests. React Router für Navigation.

**32. Wie haben Sie die Datenbank modelliert?**
ERM mit Entitäten: User, Role, Permission, Approval, AuditLog, GitHubTeam, Repository. Viele-zu-Viele-Beziehungen für Rollen-Berechtigungen und Nutzer-Rollen. Append-Only für Audit-Logs.

**33. Wie stellen Sie sicher, dass Audit-Logs nicht manipuliert werden können?**
Append-Only-Prinzip: Log-Einträge können nur hinzugefügt, nicht gelöscht oder verändert werden. Datenbank-Trigger verhindern UPDATE/DELETE auf der Audit-Log-Tabelle. Zusätzlich Hash-Verkettung der Einträge.

**34. Was ist der Unterschied zwischen Ihrem Workflow und einem einfachen Shell-Skript?**
Der GitHub Actions Workflow ist versioniert, dokumentiert, automatisch getriggert, auditierbar, hat Fehlerbehandlung und Status-Tracking. Ein Shell-Skript wäre manuell auszuführen und nicht nachvollziehbar.

**35. Wie haben Sie die Self-Service-Oberfläche gestaltet?**
Dashboard mit Rollenübersicht, Antragsformular mit Auswahlmenü, Statusanzeige mit Ampelfarben. Fokus auf intuitive Bedienung und Barrierefreiheit.

**36. Welche API-Endpunkte haben Sie implementiert?**
POST /api/requests (Antrag), GET /api/requests/:id (Status), POST /api/approvals (Genehmigung), GET /api/audit-logs (Logs), POST /api/export (Bericht).

**37. Wie haben Sie die Integration mit Azure AD umgesetzt?**
SAML-basiertes SSO. Der Nutzer authentifiziert sich über Azure AD, das System erhält die Identitätsdaten per SAML-Response und ordnet die lokale Rolle zu.

**38. Welche Tests haben Sie durchgeführt?**
12 Testfälle in der Testfallmatrix, abgedeckt: Unit-Tests (Jest), Integrationstests (Supertest), Security-Scans (CodeQL), manuelle Abnahmetests.

---

## E) Testen & Abnahme (Fragen 39–45)

**39. Wie haben Sie getestet, ob Ihr System funktioniert?**
12 definierte Testfälle: Rollenantrag, Pflichtfelder, Genehmigung, Ablehnung, Policy OK, Policy Fehler, Rechtevergabe, Rechteentzug, Audit-Log, Secret-Scan, Audit-Export, Benachrichtigung. Alle bestanden.

**40. Was war der schwierigste Testfall?**
TF06 (Policy Fehler) – die korrekte Erkennung unzulässiger Anträge bei gleichzeitiger Vermeidung von False Positives. Die Policy-Engine musste mehrfach angepasst werden.

**41. Wie haben Sie die Security getestet?**
GitHub Advanced Security (CodeQL, Secret-Scanning). Prüfung auf offene Secrets, SQL-Injection, XSS und unsichere Konfigurationen. Keine kritischen Funde.

**42. Wer hat die Abnahme durchgeführt?**
Der Auftraggeber (VFB) auf Basis des Abnahmeprotokolls. Alle Muss-Kriterien wurden als erfüllt bewertet.

**43. Gab es Abweichungen zwischen Soll und Ist?**
Geringfügige Abweichungen: Gesamtaufwand 72 h statt 70 h (+3 %), Kosten 3.820 EUR statt 3.740 EUR (+2 %). Funktionale Ziele vollständig erreicht.

**44. Wie haben Sie die DSGVO-Konformität nachgewiesen?**
DSGVO-Checkliste (Art. 5, 25, 32) abgearbeitet, DPIA durchgeführt, Audit-Log-Funktion vorgeführt, Löschkonzept präsentiert.

**45. Was würden Sie beim nächsten Projekt in der Testphase anders machen?**
Mehr Endnutzer im Pilot (20 statt 15), früherer Start der Security-Tests, automatisierte Lasttests für das Audit-Logging.

---

## F) Wirtschaftlichkeit & Fazit (Fragen 46–53)

**46. Hat sich das Projekt wirtschaftlich gelohnt?**
Ja. Investition: 3.820 EUR. Jährliche Einsparung: ca. 13.000 EUR. Amortisation: ca. 3,5 Monate. ROI (3 Jahre): ca. 340 %.

**47. Wie berechnen Sie die Einsparungen?**
Reduktion der Bearbeitungszeit von 20 Min auf 2 Min pro Antrag (35 Anträge/Woche). Wegfall von Nachbesserungen (15 Fälle/Monat à 30 Min). Reduzierter Audit-Aufwand (−50 %).

**48. Was haben Sie aus dem Projekt gelernt?**
Iterative Entwicklung und frühzeitige Einbindung von Stakeholdern sind erfolgskritisch. Die Zeitplanung war zu optimistisch – in Zukunft größere Puffer einplanen.

**49. Was würden Sie beim nächsten Projekt anders machen?**
Externe Security-Partner früher einbinden, Pilotphase ausweiten, realistischere Aufwandsschätzung für Schnittstellen.

**50. Wie geht es mit dem Projekt weiter?**
Schrittweise Integration in weitere Geschäftsbereiche (HR, Verwaltung) ab 2027. Geplant: KI-basierte Anomalieerkennung, erweiterte Dashboard-Funktionen.

**51. Was war Ihre Eigenleistung im Projekt?**
Ich habe die Ist-Analyse durchgeführt, Anforderungen aufgenommen, das RBAC-Modell entwickelt, den GitHub-Workflow konzipiert, den Prototyp umgesetzt und die Dokumentation erstellt. Externe Berater (Datenschutz, Security) wurden nur punktuell eingebunden.

**52. Welche Alternativen haben Sie verworfen?**
Standard-IAM-Systeme (Okta, Azure AD) wegen zu hoher Kosten und mangelnder Flexibilität. Manuelle Prozesse wegen Fehleranfälligkeit. LLaVA-KI-Analyse (ursprüngliche Idee) wegen fehlender Passung zum Business-Manager-Profil.

**53. Wie beurteilen Sie den Erfolg des Projekts?**
Positiv. Alle SMART-Ziele wurden erreicht, der Prototyp ist funktionsfähig und die Wirtschaftlichkeitsrechnung zeigt einen klaren Nutzen. Der größte Erfolg ist die vollständige Auditierbarkeit und DSGVO-Konformität der Rechtevergabe.
