# Style Guide — Zero-Trust IHK Projektarbeit

## 1. Schreibstil & Sprache

### Grundprinzipien
- **Sachlich, präzise, nachvollziehbar** — keine Marketing-Sprache
- **Aktiv statt Passiv** — "Ich habe analysiert" statt "Es wurde analysiert"
- **Konkret statt abstrakt** — Zahlen, Daten, Fakten statt "viele", "groß", "schnell"
- **Prüfungssicher** — Jede Behauptung belegbar (Quelle, Anhang, Screenshot, Testprotokoll)

### Personenbezug
- **Ich-Form** für Eigenleistung: "Ich habe das RBAC-Modell entworfen"
- **Wir-Form** für Team/Abstimmung: "Wir haben die Stakeholder interviewt"
- **Passiv** nur für Prozessergebnisse: "Der Workflow wurde getriggert"

### Zeitformen
- **Präteritum** für abgeschlossene Handlungen: "Ich führte die Interviews durch"
- **Perfekt** für Ergebnisse mit Gegenwartsbezug: "Die Analyse hat ergeben"
- **Präsens** für Beschreibung des Prototyps: "Das System prüft die Policy"

---

## 2. Fachterminologie (Glossar-Auszug)

| Begriff | Definition (kurz) | Verwendung |
|---------|-------------------|------------|
| **Zero Trust** | Sicherheitsmodell: "Never Trust, Always Verify" | Immer mit Verweis auf NIST SP 800-207 |
| **RBAC** | Role-Based Access Control — Berechtigungen über Rollen | Immer als "RBAC (Role-Based Access Control)" beim ersten Vorkommen |
| **GitHub Actions** | CI/CD-Plattform von GitHub für Workflow-Automatisierung | Immer "GitHub Actions" (nicht "GitHub Action") |
| **Policy-as-Code** | Sicherheitsrichtlinien als versionierter Code | Mit Bindestrich, nicht "Policy as Code" |
| **Self-Service** | Nutzer stellen Anträge selbst über Portal | Als Substantiv: "der Self-Service" |
| **Audit-Log** | Revisionssicheres Protokoll aller Aktionen | Als zusammengesetztes Substantiv: "Audit-Log" |
| **DPIA** | Datenschutz-Folgenabschätzung (Art. 35 DSGVO) | Abkürzung beim 1. Mal ausschreiben |
| **Muss-/Kann-Kriterium** | Anforderungspriorität nach MoSCoW | Immer mit Bindestrich: "Muss-Kriterium" |
| **Prototyp** | Technischer Machbarkeitsnachweis, nicht produktiv | Immer "prototypisch", "nicht produktiv freigegeben" |

---

## 3. Zahlen & Einheiten

| Regel | Beispiel |
|-------|----------|
| **Zahlen 1–12** als Wort | "fünf Interviews" |
| **Zahlen ab 13** als Ziffer | "35 Anträge pro Woche" |
| **Maßeinheiten** mit Leerzeichen | "70 Stunden", "3,2 Tage", "50 Mitarbeiter" |
| **Prozent** mit Leerzeichen | "8–12 %" |
| **Währung** mit Leerzeichen | "3.740 EUR" |
| **Datum** ISO / deutsch | "01.11.2026" oder "2026-11-01" |
| **Zeitraum** mit En-Dash | "14 Wochen", "15.08.–01.11.2026" |
| **Dezimaltrenner** | Komma (deutsch): "3,2 Tage" |

---

## 4. Abkürzungen

| Regel | Beispiel |
|-------|----------|
| **Beim 1. Vorkommen** ausschreiben | "Role-Based Access Control (RBAC)" |
| **Abkürzungsverzeichnis** pflegen | Alle Abkürzungen dort eintragen |
| **Keine Eigenabkürzungen** ohne Erklärung | "ZT" für Zero Trust → nicht ohne Definition |
| **SI-Einheiten** standardisiert | "h" für Stunden, "EUR" für Euro |

---

## 5. Strukturierungshilfen

### Überschriften
- **Max. 3 Ebenen** im Fließtext (1 / 1.1 / 1.1.1)
- **Kurz, aussagekräftig**, keine ganzen Sätze
- **Parallelismus** bei gleicher Ebene: alle Infinitiv oder alle Substantiv

### Listen
- **Aufzählungspunkte** (•) für gleichrangige Items ohne Reihenfolge
- **Nummerierung** (1., 2.) für sequenzielle Schritte / Prioritäten
- **Einrückung** max. 2 Ebenen
- **Parallelismus** bei Listeneinträgen

### Tabellen vs. Listen
| Inhalt | Format |
|--------|--------|
| Vergleich, Matrix, viele Spalten | Tabelle |
| Einfache Aufzählung, < 5 Items | Liste |
| Schrittfolge, Prozedur | Nummerierte Liste |

---

## 6. Abbildungen & Tabellen im Text

### Einbindung
```
Siehe Abbildung 3: GitHub Workflow für automatisierte Rechtevergabe.

[Abb. 3: GitHub Workflow ...]

Wie in Tabelle 5 dargestellt, erreicht der GitHub-Prototyp 4,1 Punkte.
```

### Beschriftung
- **Über der Tabelle**, **unter der Abbildung**
- **Titel** fett, **Nr.** normal: **Tab. 5:** Nutzwertanalyse
- **Quelle/Hinweis** darunter in 9 pt Kursiv

### Querverweise
- Im Text: "Abb. 3", "Tab. 5", "Kap. 3.8", "Gleichung (2)"
- Nie: "die obige Tabelle", "die folgende Abbildung"

---

## 7. Zitierweise

### Im Text (numerisch)
- **Eckige Klammern:** "...laut NIST SP 800-207 [5]..."
- **Mehrere Quellen:** "[5, 8, 12]"
- **Seitenangabe:** "[5, S. 12]"

### Literaturverzeichnis (APA-ähnlich, numerisch)
```
[5] Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). Zero Trust Architecture.
    NIST Special Publication 800-207. National Institute of Standards and Technology.
    https://doi.org/10.6028/NIST.SP.800-207 (Abruf: 01.10.2026)
```

### Online-Quellen
- **Immer** mit Abrufdatum und URL
- **DOI** wenn vorhanden
- **Archiv-URL** (Web Archive) für kritische Quellen empfohlen

---

## 8. Code & Konfiguration im Text

### Inline-Code
- **Backticks** für: Dateinamen, Befehle, Variablen, Keys, kurze Snippets
- Beispiel: `role-request.yml`, `POST /api/requests`, `user_id`

### Code-Blöcke
- **Sprache angeben:** ```yaml, ```bash, ```python, ```json
- **Kommentare** im Code für Erklärung
- **Keine echten Secrets** — Platzhalter: `{{GITHUB_TOKEN}}`, `<YOUR_TENANT_ID>`

### Konfigurationsdateien
- **YAML** für GitHub Actions, Docker Compose
- **JSON** für API-Beispiele
- **SQL** für DDL/DML

---

## 9. Besondere Hinweise für IHK

### Projektleiter-Leistung sichtbar machen
- **Ich-Form** bei: Analyse, Konzeption, Umsetzung, Test, Dokumentation
- **Abgrenzung** zu Fremdleistung (DSB, IT-Admin, externe Berater) klar benennen
- **Stunden** pro Arbeitspaket im PSP nachvollziehbar

### Prototyp-Charakter wahren
- **Keine** Aussagen wie "Das System ist produktiv"
- **Immer:** "prototypisch umgesetzt", "in Testumgebung validiert", "Konzeptnachweis"
- **Screenshots** als "Simulationsplatzhalter" kennzeichnen, falls nicht echt

### Wirtschaftlichkeit
- **Kosten** realistisch (Eigenleistung × Stundensatz + externe Kosten)
- **Nutzen** quantifiziert (Zeitersparnis × Stundensatz × Frequenz)
- **Amortisation** in Monaten berechnet
- **ROI** über 3 Jahre

---

## 10. Checkliste pro Kapitel

| Prüfung | Kapitel 1 | Kapitel 2 | Kapitel 3 | Kapitel 4 | Kapitel 5 | Kapitel 6 | Kapitel 7 | Kapitel 8 |
|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| SMART-Ziele | ✅ | | | | | | | |
| PSP vollständig | | ✅ | | | | | | |
| Stakeholder komplett | | | ✅ | | | | | |
| Make-or-Buy belegt | | | ✅ | | | | | |
| Nutzwertanalyse | | | ✅ | | | | | |
| Architektur skizziert | | | | ✅ | | | | |
| Workflow-YAML | | | | ✅ | | | | |
| Datenmodell (ERD) | | | | ✅ | | | | |
| Code-Beispiele | | | | | ✅ | | | |
| Testfallmatrix 12/12 | | | | | | ✅ | | |
| Abnahmeprotokoll | | | | | | ✅ | | |
| Pilot / Schulung | | | | | | | ✅ | |
| Lessons Learned | | | | | | | | ✅ |

---

*Ende Style Guide. Bei Unklarheiten: IHK-Rahmenprüfungsordnung & PMBOK 7. Ed. konsultieren.*