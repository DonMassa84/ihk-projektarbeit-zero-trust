# Anhang A3 — Use-Case-Diagramm

**Projekt:** Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Version:** 1.0  
**Datum:** 01.11.2026  
**Autor:** Daniel Massa (Prüfling 615951)

---

## Use-Case-Diagramm (Mermaid)

```mermaid
useCaseDiagram
    actor "Mitarbeiter" as MA
    actor "Vorgesetzter" as VG
    actor "IT-Admin" as ADM
    actor "System (GitHub Actions)" as SYS
    actor "Datenschutzbeauftragter" as DSB

    package "Self-Service-Portal" {
        usecase "UC-01: Rolle beantragen" as UC1
        usecase "UC-02: Antragsstatus prüfen" as UC2
        usecase "UC-03: Eigene Rollen einsehen" as UC3
    }

    package "Genehmigungsprozess" {
        usecase "UC-04: Antrag genehmigen" as UC4
        usecase "UC-05: Antrag ablehnen" as UC5
        usecase "UC-06: Eskalation nach 48h" as UC6
    }

    package "Automatisierte Rechtevergabe" {
        usecase "UC-07: GitHub Team zuordnen" as UC7
        usecase "UC-08: Audit-Log erstellen" as UC8
        usecase "UC-09: Benachrichtigung senden" as UC9
    }

    package "Rechteentzug & Audit" {
        usecase "UC-10: Rechte entziehen" as UC10
        usecase "UC-11: Audit-Export erstellen" as UC11
        usecase "UC-12: Compliance-Prüfung" as UC12
    }

    MA --> UC1
    MA --> UC2
    MA --> UC3
    VG --> UC4
    VG --> UC5
    SYS --> UC6
    SYS --> UC7
    SYS --> UC8
    SYS --> UC9
    SYS --> UC10
    ADM --> UC11
    ADM --> UC12
    DSB --> UC12

    UC1 ..> UC4 : «include»
    UC1 ..> UC8 : «include»
    UC4 ..> UC7 : «include»
    UC7 ..> UC9 : «include»
    UC10 ..> UC8 : «include»
```

---

## Use-Case-Beschreibungen (Kurz)

| UC-ID | Name | Akteur | Beschreibung | Vorbedingung | Nachbedingung |
|-------|------|--------|--------------|--------------|---------------|
| UC-01 | Rolle beantragen | Mitarbeiter | Mitarbeiter wählt Rolle, füllt Formular aus, sendet ab | Angemeldet im Portal | Antrag erstellt, Status "offen", Workflow getriggert |
| UC-02 | Antragsstatus prüfen | Mitarbeiter | Mitarbeiter sieht eigenen Antragsverlauf | Angemeldet | Statusliste angezeigt |
| UC-03 | Eigene Rollen einsehen | Mitarbeiter | Aktuelle Rollen & Berechtigungen anzeigen | Angemeldet | Rollenliste angezeigt |
| UC-04 | Antrag genehmigen | Vorgesetzter | Prüft Antrag, klickt "Genehmigen" | Antrag Status "offen", Vorgesetzter zuständig | Status "genehmigt", Workflow Provisioning |
| UC-05 | Antrag ablehnen | Vorgesetzter | Prüft Antrag, klickt "Ablehnen" mit Begründung | Antrag Status "offen" | Status "abgelehnt", keine Rechtevergabe |
| UC-06 | Eskalation | System | Nach 48h ohne Entscheidung | Antrag "offen", 48h verstrichen | Benachrichtigung IT-Admin, erneute Aufforderung |
| UC-07 | GitHub Team zuordnen | System | API-Call an GitHub (Team-Membership) | Genehmigung erfolgt | Mitgliedschaft erstellt/aktualisiert |
| UC-08 | Audit-Log erstellen | System | Schreibt Eintrag in Append-Only DB | Jede relevante Aktion | Log-Eintrag mit Hash-Chain |
| UC-09 | Benachrichtigung senden | System | E-Mail + GitHub Notification | Aktion abgeschlossen | Empfänger informiert |
| UC-10 | Rechte entziehen | System / Admin | Entfernt Team-Membership, loggt | Austritt / Rollenwechsel / Admin-Aktion | Mitgliedschaft entfernt, Log-Eintrag |
| UC-11 | Audit-Export | IT-Admin | Erzeugt CSV/JSON mit Filtern | Admin-Bereich, Export angefordert | Datei zum Download |
| UC-12 | Compliance-Prüfung | DSB / Admin | Prüft DSGVO-Checkliste, DPIA | Regelmäßig / Anlassbezogen | Prüfbericht, Maßnahmen |

---

## Erweiterungen & Varianten

| UC-ID | Erweiterung | Beschreibung |
|-------|-------------|--------------|
| UC-01 | Policy-Violation | System prüft 4-Augen-Prinzip, Kompetenzmatrix; blockiert bei Verstoß |
| UC-04 | Delegation | Vorgesetzter kann Stellvertreter benennen (Konfiguration) |
| UC-06 | Auto-Eskalation | Nach 48h → IT-Admin, nach weiteren 24h → Geschäftsführung |
| UC-07 | Rollback | Bei Fehler im Provisioning → automatischer Rollback + Alert |
| UC-10 | Time-based | Temporäre Rollen (z.B. Projekt) laufen nach Ablauf automatisch aus |

---

## Nicht-funktionale Anforderungen an Use-Cases

| UC-ID | Performance | Sicherheit | Verfügbarkeit |
|-------|-------------|------------|---------------|
| UC-01 | < 2 s Formular-Ladezeit | Validierung client+server | 99,5 % |
| UC-04 | < 1 s Genehmigungs-Response | 4-Augen-Prinzip erzwungen | 99,5 % |
| UC-07 | < 3 s GitHub API-Call | PAT mit minimalen Rechten | 99,9 % (GitHub SLA) |
| UC-08 | < 100 ms DB-Write | Append-Only, Hash-Chain | 99,99 % |
| UC-11 | < 5 s Export-Generierung | Nur für Admin, TLS | On-Demand |

---

## Traceability Matrix

| UC-ID | Anforderung (Lastenheft) | Testfall | Kapitel |
|-------|--------------------------|----------|---------|
| UC-01 | MU-02 | TF01, TF02 | 6.2 |
| UC-04 | MU-03 | TF03 | 6.2 |
| UC-05 | MU-03 | TF04 | 6.2 |
| UC-07 | MU-04 | TF07 | 6.2 |
| UC-08 | MU-05 | TF09 | 6.2 |
| UC-10 | MU-06 | TF08 | 6.2 |
| UC-11 | MU-05 | TF11 | 6.2 |
| UC-12 | MU-07 | A14 Checkliste | 3.9, 6.5 |

---

*Ende Anhang A3. Mermaid-Code rendert als SVG/PDF. Vgl. Kapitel 3.3 der Projektarbeit.*