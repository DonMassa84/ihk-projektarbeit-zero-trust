# Präsentation: Zero-Trust-Sicherheitskonzept mit GitHub-Integration

## 15 Minuten – Vollständiger Sprechtext mit Folienbeschreibung

---

## FOLIE 1: Titel (0:00–1:00)

**Inhalt:**
- Zero-Trust-Sicherheitskonzept mit GitHub-Integration
- Certified IT Business Manager (IHK) – Sommer 2026
- Daniel Massa (Prüflingsnummer 615951)

**Sprechtext:**
"Guten Tag, mein Name ist Daniel Massa. Meine Projektarbeit trägt den Titel 'Zero-Trust-Sicherheitskonzept mit GitHub-Integration'. Ich habe einen Prototyp entwickelt, der die automatisierte Rechtevergabe im Verein zur Förderung der Berufsbildung in Ludwigsburg ermöglicht. Die Präsentation gibt einen Überblick über Ausgangssituation, Konzept, Umsetzung und Ergebnisse."

---

## FOLIE 2: Ausgangssituation und Problem (1:00–2:30)

**Inhalt:**
- Manuelle Rechtevergabe per E-Mail
- 35 Anträge/Woche, 3,2 Tage Bearbeitungszeit
- 8–12 % Fehlerquote
- Dezentrale Audit-Logs
- Keine Self-Service-Funktionen

**Sprechtext:**
"Vor dem Projekt wurden Zugriffsrechte manuell per E-Mail vergeben. Ein Antrag durchlief 3 bis 4 Stationen und benötigte durchschnittlich 3,2 Tage. Die Fehlerquote lag zwischen 8 und 12 Prozent, was zu 15 Nachbesserungen pro Monat führte. Audit-Logs waren über mehrere Systeme verteilt, und Self-Service-Funktionen existierten nicht."

---

## FOLIE 3: Projektziele (2:30–4:00)

**Inhalt:**
- SMART-Ziele
- RBAC-Modell mit 10+ Rollen
- Reduktion Bearbeitungszeit auf <4 h
- Fehlerquote <2 %
- 100 % Audit-Abdeckung
- Abgabe: 01.11.2026

**Sprechtext:**
"Die Ziele wurden nach SMART definiert: Spezifisch die Einführung eines RBAC-Modells mit zehn Rollen und 50 Berechtigungen. Messbar die Reduktion der Bearbeitungszeit auf unter vier Stunden und der Fehlerquote auf unter zwei Prozent. Terminiert bis zum 1. November 2026."

---

## FOLIE 4: Projektplanung (4:00–5:30)

**Inhalt:**
- 70 Stunden Aufwand
- 3.740 EUR Budget
- 7 Risiken identifiziert
- 8 Meilensteine
- Hybrides Vorgehensmodell

**Sprechtext:**
"Der Gesamtaufwand betrug 70 Stunden bei einem Budget von 3.740 Euro. Ich habe sieben Risiken identifiziert und mit Gegenmaßnahmen abgesichert. Acht Meilensteine strukturierten den Projektverlauf von der Ist-Analyse bis zur Abgabe."

---

## FOLIE 5: Zero-Trust- und RBAC-Konzept (5:30–7:00)

**Inhalt:**
- NIST SP 800-207 Zero Trust Architecture
- "Never Trust, Always Verify"
- 6 Rollen definiert
- Least-Privilege-Prinzip
- DSGVO-Konformität

**Sprechtext:**
"Das Zero-Trust-Konzept basiert auf NIST SP 800-207 und folgt dem Prinzip 'Never Trust, Always Verify'. Ich habe sechs Rollen definiert: Admin, Developer, Auditor, Read-Only, HR-Manager und Finance. Jede Rolle hat nur die Berechtigungen, die für die Aufgabenerfüllung notwendig sind – das Least-Privilege-Prinzip."

---

## FOLIE 6: GitHub-Workflow (7:00–9:00)

**Inhalt:**
- Automatisierter Workflow mit 4 Stages
- Antrag → Validate → Approve → Provision
- YAML-basierte Pipeline
- Audit-Log nach jedem Schritt
- Fehlerbehandlung integriert

**Sprechtext:**
"Der GitHub-Workflow automatisiert die Rechtevergabe in vier Stufen: Validate prüft Pflichtfelder und Policy-Konformität. Approve leitet die Genehmigungsanfrage an den Vorgesetzten. Provision führt die Rechtevergabe über die GitHub API aus. Notify benachrichtigt den Antragsteller. Jeder Schritt wird im Audit-Log protokolliert."

---

## FOLIE 7: Prototyp-Umsetzung (9:00–10:30)

**Inhalt:**
- React-Frontend (Self-Service-Portal)
- Node.js/Express-Backend
- PostgreSQL-Datenbank
- GitHub-API-Integration
- 12 Testfälle bestanden

**Sprechtext:**
"Der Prototyp besteht aus einem React-Frontend für das Self-Service-Portal, einem Node.js-Backend und einer PostgreSQL-Datenbank. Die GitHub-API steuert die Rechtevergabe. Alle zwölf Testfälle wurden bestanden."

---

## FOLIE 8: Test und Abnahme (10:30–12:00)

**Inhalt:**
- 12 Testfälle (alle bestanden)
- Funktionstests, Security-Tests
- DSGVO-Prüfung
- Abnahmeprotokoll unterzeichnet
- Keine offenen Fehler

**Sprechtext:**
"Die Testmatrix umfasst 12 Testfälle von der Rollenbeantragung bis zum Audit-Export. Alle wurden bestanden. Security-Tests durch GitHub CodeQL und Secret-Scanning verliefen ohne kritische Funde. Die DSGVO-Prüfung wurde dokumentiert. Das Abnahmeprotokoll ist unterzeichnet."

---

## FOLIE 9: Wirtschaftlichkeit (12:00–13:30)

**Inhalt:**
- Investition: 3.820 EUR
- Jährliche Einsparung: 13.000 EUR
- Amortisation: 3,5 Monate
- ROI (3 Jahre): 340 %
- Make-or-Buy: GitHub-Prototyp gewählt

**Sprechtext:**
"Das Projekt kostete 3.820 Euro bei 72 Stunden Aufwand. Die jährlichen Einsparungen betragen rund 13.000 Euro – durch schnellere Bearbeitung, weniger Fehler und reduzierten Audit-Aufwand. Die Amortisation liegt bei 3,5 Monaten, der ROI nach drei Jahren bei 340 Prozent."

---

## FOLIE 10: Lessons Learned und Ausblick (13:30–15:00)

**Inhalt:**
- Iterative Entwicklung als Erfolgsfaktor
- Zeitplanung war zu optimistisch
- Ausblick: KI-basierte Anomalieerkennung
- Integration weiterer Bereiche ab 2027
- Fragen?

**Sprechtext:**
"Die iterative Entwicklung mit kurzen Feedback-Zyklen war ein Erfolgsfaktor. Die Zeitplanung war anfangs zu optimistisch – in Zukunft würde ich größere Puffer einplanen. Das Konzept lässt sich für weitere Bereiche adaptieren. Geplant sind KI-basierte Anomalieerkennung und die Integration von HR und Verwaltung ab 2027. Ich bedanke mich für Ihre Aufmerksamkeit – Fragen?"
