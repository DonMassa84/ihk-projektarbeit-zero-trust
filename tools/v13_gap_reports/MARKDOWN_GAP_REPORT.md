# Markdown Gap Report: dokumentation.md vs V13 Reference

## Methodology

| Status     | Meaning                                  |
|------------|------------------------------------------|
| IDENTISCH  | Content exists in both, structurally similar |
| FEHLT_IM_MARKDOWN | Present in V13 but missing from dokumentation.md |
| FEHLT_IN_V13 | Present in dokumentation.md but not in V13 |
| WIDERSPRUCH | Both have content but they disagree |
| NUR_LAYOUT | Formatting/cosmetics only, not content |

## Chapter-by-Chapter

| Bereich | dokumentation.md | V13 (63p) | Status | Anmerkung |
|---------|-----------------|-----------|--------|-----------|
| **Deckblatt** | vorhanden | vorhanden | IDENTISCH | Beide mit IHK-Logo, Stammdaten |
| **Sperrvermerk** | nicht explizit | vorhanden | FEHLT_IM_MARKDOWN | Sollte ergänzt werden |
| **Management Summary** | Kap. 0 | separater Abschnitt | IDENTISCH | Gleiche Kernaussagen |
| **1 Projektinfo** | Kap. 1 | Kap. 1 | IDENTISCH | Gleicher Inhalt, ähnlich tief |
| 1.1 Umfeld | 1.1-1.2 | 1.1 | IDENTISCH | |
| 1.2 Problemstellung | 1.3 | 1.2 | IDENTISCH | |
| 1.3 Ziel | 1.4 | 1.3 | IDENTISCH | |
| 1.4 Begründung | — | 1.4 | FEHLT_IM_MARKDOWN | Neue Sektion in V13 |
| 1.5 Abgrenzung | 1.5 | 1.5 | IDENTISCH | |
| 1.6 Rahmenbedingungen | — | 1.6 | FEHLT_IM_MARKDOWN | V13 erwähnt DSGVO/TOM |
| 1.7 Projektauftrag | 1.6 | 1.7 | IDENTISCH | |
| 1.8 Eigenleistung | 1.7 | 1.8 | IDENTISCH | Ähnliche Beschreibung |

| **2 Projektmanagement** | Kap. 2 | Kap. 2 | ERWEITERT | V13 hat mehr Sub-Chapters |
| 2.1 Kick-off | — | 2.1 | FEHLT_IM_MARKDOWN | V13 mit Agenda-Tabelle |
| 2.2 Vorgehensmodell | 2.1 | 2.2 | IDENTISCH | |
| 2.3 PSP | 2.2 | 2.3 | IDENTISCH | |
| 2.4 Zeitplanung | 2.3 | 2.4 | IDENTISCH | |
| 2.5 Ressourcen | 2.4 | 2.5 | IDENTISCH | |
| 2.6 Kosten | 2.5 | 2.6 | IDENTISCH | |
| 2.7 Stakeholder | 2.6 | 2.7 | IDENTISCH | |
| 2.8 Risiko | 2.8 | 2.8 | IDENTISCH | |
| 2.9 Qualität | 2.9 | (in 2.8) | IDENTISCH | |
| 2.10 Meilensteine | 2.10 | 2.9 | IDENTISCH | |
| 2.11 RACI | — | 2.10 | FEHLT_IM_MARKDOWN | V13 mit voller Matrix |
| 2.12 Change | 2.11 | 2.11 | IDENTISCH | |
| 2.13 Marketing | — | 2.12 | FEHLT_IM_MARKDOWN | V13 beschreibt Akzeptanz |

| **3 Spezifikation** | Kap. 3 | Kap. 3 | ERWEITERT | |
| 3.1 Ist-Analyse | 3.1 | 3.1 | IDENTISCH | |
| 3.2 Anforderungen | 3.2 | 3.2 | IDENTISCH | |
| 3.3 Zero-Trust-Prinzipien | — | 3.3 | FEHLT_IM_MARKDOWN | Neue Sektion |
| 3.4 Variantenvergleich | 3.3-3.5 | 3.4 | IDENTISCH | |
| 3.5 Datenschutz | 3.6 | 3.5 | IDENTISCH | |
| 3.6 Budget | (in 2.5) | 3.6 | FEHLT_IN_V13 | |
| 3.7 Bedrohungsmodell | — | 3.7 | FEHLT_IM_MARKDOWN | Neue Sektion |
| 3.8 Datenfeldbewertung | — | 3.8 | FEHLT_IM_MARKDOWN | DSGVO-Feldebene |
| 3.9 Abnahmekriterien | 3.8 | 3.9 | IDENTISCH | |
| 3.10 Nachkalkulation | — | 3.10 | FEHLT_IM_MARKDOWN | Neue Sektion |

| **4 Technik** | Kap. 4 | Kap. 4 | ERWEITERT | |
| 4.1 Architektur | 4.1 | 4.1 | IDENTISCH | |
| 4.2 Workflow | 4.3 | 4.2 | IDENTISCH | |
| 4.3 Rollen | 4.2 | 4.3 | IDENTISCH | |
| 4.4 Datenmodell | 4.4 | 4.4 | IDENTISCH | |
| 4.5 Audit | 4.8 | 4.5 | IDENTISCH | |
| 4.6 Schnittstellen | — | 4.6 | FEHLT_IM_MARKDOWN | Tabelle |
| 4.7 Sicherheitsmaßnahmen | 4.6 | 4.7 | IDENTISCH | |
| 4.8 API-Vertrag | 4.5 | 4.8 | IDENTISCH | |
| 4.9 Deployment | 4.10 | 4.9 | IDENTISCH | |
| 4.10 Fehler/Retry | 4.9 | 4.10 | IDENTISCH | |
| 4.11 Logging/Monitoring | 4.10 | 4.11 | IDENTISCH | |

| **5 Durchführung** | Kap. 5 | Kap. 5 | IDENTISCH | |
| 5.1 Entwicklung | 5.1 | 5.1 | IDENTISCH | |
| 5.2 Backend | 5.2 | 5.2 | IDENTISCH | |
| 5.3 Self-Service | 5.3 | (in 5.2) | IDENTISCH | |
| 5.4 GitHub | 5.7 | 5.4 | IDENTISCH | |
| 5.5 Audit | 5.7 | 5.5 | IDENTISCH | |
| 5.6 Qualität | 5.8 | 5.6 | IDENTISCH | |
| 5.7 Abweichungen | 5.9 | 5.7 | IDENTISCH | |
| 5.8 Entscheidungen | 5.9 | 5.8 | IDENTISCH | |
| 5.9 Repo-Struktur | — | 5.9 | FEHLT_IM_MARKDOWN | Tabelle |

| **6 Test** | Kap. 6 | Kap. 6 | ERWEITERT | |
| 6.1 Strategie | 6.1 | 6.1 | IDENTISCH | |
| 6.2 Testfälle | 6.3 | 6.2 | IDENTISCH | |
| 6.3 Fehleranalyse | 6.5 | 6.3 | IDENTISCH | |
| 6.4 Soll-Ist | 8.2 | 6.4 | FEHLT_IN_V13 | |
| 6.5 Abnahme | 7.4 | 6.5 | IDENTISCH | |
| 6.6 Evidenz | — | 6.6 | FEHLT_IM_MARKDOWN | |
| 6.7 Restpunkte | 7.6 | 6.7 | IDENTISCH | |
| 6.8 Statusbericht | — | 6.8 | FEHLT_IM_MARKDOWN | |

| **7 Rollout** | Kap. 7 | Kap. 7 | IDENTISCH | |
| 7.1 Pilotbetrieb | — | 7.1 | FEHLT_IM_MARKDOWN | |
| 7.2 Schulung | — | 7.2 | FEHLT_IM_MARKDOWN | |
| 7.3 Übergabe | 7.1-7.3 | 7.3 | IDENTISCH | |
| 7.4 Roadmap | — | 7.4 | FEHLT_IM_MARKDOWN | (unser Kap. 7 enthält teilweise) |
| 7.5 Betriebsmodell | — | 7.5 | FEHLT_IM_MARKDOWN | |

| **8 Abschluss** | Kap. 8 | Kap. 8 | IDENTISCH | |
| 8.1 Ergebnis | 8.1 | 8.1 | IDENTISCH | |
| 8.2 Kosten/Nutzen | 8.4/8.6 | 8.2 | IDENTISCH | |
| 8.3 Lessons Learned | 8.8 | 8.3 | IDENTISCH | |
| 8.4 Restrisiken | 8.7 | 8.4 | IDENTISCH | |
| 8.5 Fazit | 8.9 | 8.5 | IDENTISCH | |
| 8.6 Mag. Dreieck | — | 8.6 | FEHLT_IM_MARKDOWN | |

| **9 Quellen** | Kap. 9 | Kap. 9 | IDENTISCH | |
| 9.1 Quellen | 9 (Quellen) | 9.1 | IDENTISCH | |
| 9.2 KI-Transparenz | 9 (Hilfsmittel) | 9.2 | IDENTISCH | |

| **Anhang** | Anhang A-F | A1-A12 | ERWEITERT | |
| Testprotokoll | A | A7 | IDENTISCH | |
| Security | B | (in A7) | FEHLT_IN_V13 | |
| Claim-Matrix | C | (in A6) | FEHLT_IN_V13 | |
| Sign-Off | D | (A8) | IDENTISCH | |
| Fehler/Retest | E | (A7) | FEHLT_IN_V13 | |
| KI-Transparenz | F | — | FEHLT_IN_V13 | |
| Projektstammdaten | — | A1 | FEHLT_IM_MARKDOWN | |
| PSP (Anhang) | — | A2 | FEHLT_IM_MARKDOWN | |
| Risikoanalyse | — | A3 | FEHLT_IM_MARKDOWN | |
| Architektur (Detail) | — | A4 | FEHLT_IM_MARKDOWN | |
| Datenmodell (Detail) | — | A5 | FEHLT_IM_MARKDOWN | |
| Anforderungsnachweis | — | A6 | FEHLT_IM_MARKDOWN | |
| Abnahmevorlage | 7.4 | A8 | IDENTISCH | |
| Budget/Nachkalk. | — | A9 | FEHLT_IM_MARKDOWN | |
| Roadmap | — | A10 | FEHLT_IM_MARKDOWN | |
| Kick-off-Protokoll | — | A11 | FEHLT_IM_MARKDOWN | |
| Statusbericht | — | A12 | FEHLT_IM_MARKDOWN | |

## Zahlen/Kennzahlen Konflikte

| Kennzahl | dokumentation.md | V13 | Widerspruch? |
|----------|-----------------|-----|--------------|
| Projektstunden | 70 h | 70 h | Keiner |
| Budget | 50.000 EUR | 50.000 EUR | Keiner |
| Testfälle | 14 (14/14 bestanden) | 12 (12 dokumentiert) | **WIDERSPRUCH** – 14 vs 12 |
| Pilotrollen | 6 | 6 | Keiner |
| PDF-Seiten | 21 | 63 | V13 ist voller |

## Critical Findings

1. **Testfall-Anzahl: 14 vs 12** – dokumentation.md behauptet 14 Testfälle mit 14/14 bestanden. V13 zeigt 12 Testfälle ehrlich mit `Commit/Version: offen` und `Laufzeit: offen`.

2. **Anhangsstruktur** – V13 hat strukturierte Anhänge A1-A12; dokumentation.md hat A-F als lose Sektionen.

3. **Fehlende Sektionen in dokumentation.md (sollten übernommen werden):**
   - Sperrvermerk
   - Zero-Trust-Leitprinzipien (3.3)
   - Bedrohungsmodell (3.7)
   - Datenfeldbewertung (3.8)
   - Nachkalkulation (3.10)
   - RACI-Matrix (2.10)
   - Schnittstellentabelle (4.6)
   - Evidenzkonzept (6.6)
   - Betriebsmodell (7.5)

4. **In dokumentation.md vorhanden, aber nicht in V13:**
   - Detaillierte Security-Ergebnisse
   - Claim-Evidence-Matrix (strukturierter)
   - KI-Transparenzdokumentation (Anhang F)

## Recommendation

Priorität 1: Testfall-Anzahl korrigieren (14→12) – das ist ein fachlicher Widerspruch.
Priorität 2: Sperrvermerk, Zero-Trust-Prinzipien, RACI, Schnittstellen übernehmen.
Priorität 3: Anhangsstruktur an V13 A1-A12 angleichen.
