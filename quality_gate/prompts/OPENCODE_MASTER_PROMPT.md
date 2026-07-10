# OpenCode-Masterprompt: IHK-Projektarbeit bis zum internen 90/100-Gate

Arbeite ausschließlich im aktuellen Repository.

## Ziel
Optimiere die kanonische Markdown-Masterdatei so lange iterativ, bis
`python3 quality_gate/ihk_gate.py --build`
mit `IHK_GATE=GREEN` und mindestens 90/100 endet.

Der Score ist ein internes Qualitätsgate und keine offizielle IHK-Punktzusage.

## Unverhandelbare Regeln
1. Keine direkte PDF-Manipulation. Änderungen ausschließlich in Markdown, Build-Konfiguration, Tabellen- oder Diagrammquellen.
2. Keine Tatsachen erfinden: keine Personen, Rollen, Unterschriften, Abnahmen, Nutzerzahlen, Commit-Hashes, Laufzeiten, Testergebnisse, Einsparungen oder Produktivdaten.
3. Unbelegte Aussagen entweder mit realem Nachweis belegen oder als Plan/Ist kennzeichnen.
4. Keine Eidesstattliche Erklärung ändern oder simulieren.
5. Alle Änderungen dokumentieren.
6. Der manuelle Review-Score in `quality_gate/manual_review.json` wird unabhängig durch einen menschlichen Prüfer eingetragen.

## Build Pipeline
1. `python3 quality_gate/ihk_gate.py --build` (baut PDF + führt statische Prüfung)
2. Ergebnis: `quality_gate/reports/gate.md`
3. Manueller Score eintragen in `quality_gate/manual_review.json`
4. Wiederholen bis Gate=GREEN und Score≥90

## Erlaubte Änderungen
- Dokumentationstext in der Markdown-Masterdatei
- Tabellen/Diagramme in `docs/`
- Build-Konfiguration in `quality_gate/config/gate.json`
- `quality_gate/manual_review.json` (nur manuell durch Menschen)
