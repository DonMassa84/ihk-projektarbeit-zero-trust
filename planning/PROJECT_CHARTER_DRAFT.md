# PROJEKTAUFTRAG (Entwurf)

> **Status:** ENTWURF – noch nicht freigegeben  
> **Hinweis:** Dieser Auftrag ist noch nicht erteilt. Die Felder für Auftraggeber, Daten und Unterschriften sind offen.

---

## 1. Projekttitel

**Zero-Trust-Sicherheitskonzept mit GitHub-Integration – Pilot eines rollenbasierten Berechtigungsworkflows**

---

## 2. Auftraggeber

| Feld | Eintrag |
|------|---------|
| **Name** | [Offen – einzutragen] |
| **Funktion** | [Offen – einzutragen] |
| **Organisation** | [Offen – einzutragen] |

---

## 3. Projektleiter

| Feld | Eintrag |
|------|---------|
| **Name** | Daniel Massa |
| **Funktion** | Projektleiter und technischer Umsetzer |

---

## 4. Projektumfeld

Der **Verein zur Förderung der Berufsbildung (VFB)** bietet als gemeinnütziger Bildungsträger IHK- und IT-Qualifizierungen an. Die Berechtigungsverwaltung erfolgt aktuell manuell und ist fehleranfällig. Der Pilot adressiert diesen Bereich mit einem automatisierten, rollenbasierten Workflow.

---

## 5. Ausgangslage

- Manuelle Rechtevergabe ohne Dokumentation
- Keine zentrale Audit-Trail-fähige Berechtigungsverwaltung
- Medienbrüche zwischen Antrag, Genehmigung und Umsetzung
- Erhöhter Prüfaufwand bei Compliance-Fragen

---

## 6. Problemstellung

Fehlende Automatisierung und Nachvollziehbarkeit der Berechtigungsvergabe führt zu Sicherheitsrisiken, hohem manuellem Aufwand und unzureichender Audit-Fähigkeit.

---

## 7. Projektziel

Bis zum vereinbarten Abgabetermin wird ein prototypischer, rollenbasierter Berechtigungsworkflow auf Basis von FastAPI und GitHub-Integration implementiert, der die manuelle Rechtevergabe durch einen automatisierten Antrags-, Prüf- und Genehmigungsprozess ersetzt.

---

## 8. Messbare Erfolgskriterien

| Kriterium | Zielwert |
|-----------|----------|
| Funktionierender Antrags-Workflow | Antrag → Prüfung → Genehmigung/Ablehnung |
| Policy-basierte Validierung | Nicht berechtigte Rollenanträge werden abgewiesen |
| Audit-Log mit Hash-Verkettung | Jeder Eintrag enthält SHA-256 des vorherigen |
| Automatisierte Tests | CI-Pipeline mit Test-Report |
| Dokumentierter Fehler- und Retestfall | Fehler gefunden → korrigiert → erneut getestet |
| Abnahmeprotokoll | Durch Auftraggeber bestätigt |

---

## 9. Liefergegenstände

1. FastAPI-Backend mit REST-API
2. Datenmodell (Rollen, Anträge, Audit-Logs)
3. Policy-Engine für Berechtigungsprüfung
4. GitHub-Integration (Team-Zuordnung)
5. Audit-Log mit SHA-256-Hash-Verkettung
6. CI-Pipeline (GitHub Actions)
7. Test- und Coverage-Reports
8. Abnahmeprotokoll
9. Projektdokumentation (IHK-Format)

---

## 10. Projektumfang

Siehe `planning/PILOT_SCOPE_DRAFT.md` – MUSS-Umfang (M1–M15).

---

## 11. Nicht-Ziele

Siehe `planning/PILOT_SCOPE_DRAFT.md` – NICHT im Projekt (N1–N8).

---

## 12. Projektzeitraum

| Feld | Eintrag |
|------|---------|
| **Geplanter Start** | [Offen – nach Freigabe einzutragen] |
| **Geplantes Ende** | [Offen – nach Freigabe einzutragen] |
| **Planaufwand** | 70 aktive Stunden |

---

## 13. Planaufwand

| AP | Bezeichnung | Plan (h) |
|----|-------------|---------:|
| 1 | Projektauftrag und Kick-off | 4 |
| 2 | Ist-Analyse und Anforderungen | 6 |
| 3 | Variantenbewertung und Lösungsentscheidung | 5 |
| 4 | Architektur, Rollen- und Datenmodell | 8 |
| 5 | Backend-Grundstruktur und Datenhaltung | 8 |
| 6 | Antrags-, Policy- und Genehmigungsworkflow | 9 |
| 7 | GitHub-Integration und Audit-Verkettung | 8 |
| 8 | Tests, CI und Fehlerkorrektur | 8 |
| 9 | Pilotreview, Schulung und Abnahme | 5 |
| 10 | Soll-Ist-Auswertung und Abschlussdokumentation | 9 |
| **Gesamt** | | **70** |

Alle Zeiten sind Plan-Werte. Ist-Werte werden während der Durchführung erfasst.

---

## 14. Stakeholder

| Stakeholder | Rolle | Erwartung |
|-------------|-------|-----------|
| Auftraggeber | Entscheider, Abnehmer | Funktionaler Pilot, Einhaltung des Zeitrahmens |
| Projektleiter | Umsetzung, Steuerung | Erfolgreicher Projektabschluss |
| Technischer Reviewer | Qualitätssicherung | Code-Qualität, Architektur |
| Pilotnutzer | Testnutzer | Funktionierender Workflow |
| IHK-Prüfer | Bewertung | Nachvollziehbare, evidenzbasierte Dokumentation |

---

## 15. Rollen und Verantwortlichkeiten

| Rolle | Verantwortlich | Aufgabe |
|-------|----------------|---------|
| Auftraggeber | [Offen] | Projektfreigabe, Scope-Entscheidung, Abnahme |
| Projektleiter | Daniel Massa | Gesamtsteuerung, Implementierung, Dokumentation |
| Technischer Reviewer | [Offen] | Code-Reviews, Architektur-Review |
| Pilotnutzer | [Offen] | Funktionstest, Feedback |

---

## 16. Risiken

| Risiko | Eintrittsw'keit | Auswirkung | Gegenmaßnahme |
|--------|:---------------:|:----------:|---------------|
| Auftraggeber nicht verfügbar | Mittel | Hoch | Frühzeitig Termin sichern |
| Technische Komplexität | Mittel | Mittel | Puffer einplanen, Scope reduzieren |
| CI-Konfiguration zeitaufwändig | Mittel | Mittel | Templates verwenden |
| GitHub-API-Rate-Limits | Gering | Mittel | Mock-Fallback vorbereiten |
| Pilotnutzer nicht verfügbar | Mittel | Hoch | Alternativnutzer definieren |

---

## 17. Kommunikationswege

| Anlass | Frequenz | Beteiligte | Medium |
|--------|----------|------------|--------|
| Status-Update | Wöchentlich | Auftraggeber, Projektleiter | E-Mail / Kurz-Protokoll |
| Code-Review | Nach Bedarf | Projektleiter, Reviewer | GitHub PR |
| Abnahme | Einmalig | Auftraggeber, Projektleiter | Persönlich / Video |

---

## 18. Entscheidungs- und Eskalationsweg

| Ebene | Entscheider | Themen |
|-------|-------------|--------|
| Operativ | Projektleiter | Technische Umsetzung |
| Taktisch | Auftraggeber | Scope-Änderungen, Ressourcen |
| Strategisch | Auftraggeber | Budget, Abbruch |

---

## 19. Abnahmeverfahren

1. Projektleiter stellt vollständigen Lieferumfang bereit.
2. Auftraggeber prüft anhand der Abnahmekriterien.
3. Ergebnis wird im Abnahmeprotokoll dokumentiert.
4. Bei Mängeln: Nachbesserung innerhalb vereinbarter Frist.
5. Abschließende Freigabe durch Unterschrift des Auftraggebers.

---

## 20. Voraussetzungen

- [ ] Python 3.11+ auf Entwicklungsrechner
- [ ] GitHub-Zugang (Test-Organisation oder Mock)
- [ ] SQLite (lokal) oder PostgreSQL (wenn verfügbar)
- [ ] Keine produktiven personenbezogenen Daten

---

## 21. Datenschutz und Vertraulichkeit

- Es werden keine realen personenbezogenen Daten verarbeitet.
- Alle Testdaten sind anonymisiert.
- Secrets und Tokens werden nicht im Repository abgelegt.
- Screenshots werden vor Ablage auf sensible Inhalte geprüft.

---

## 22. Freigabe

| Rolle | Name | Datum | Unterschrift |
|-------|------|-------|--------------|
| **Auftraggeber** | ________________ | ________ | ____________________________ |
| **Projektleiter** | Daniel Massa | ________ | ____________________________ |
| **Projektcoach** | ________________ | ________ | ____________________________ |

> Die Unterschriften werden manuell oder durch reale elektronische Bestätigung erzeugt.
