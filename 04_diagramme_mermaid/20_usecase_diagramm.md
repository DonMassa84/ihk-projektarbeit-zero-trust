# Mermaid: Use-Case-Diagramm Zero-Trust-Rechtevergabe

```mermaid
useCaseDiagram
    package "Zero-Trust-Rechteverwaltung" {
        actor "Mitarbeiter\n(Antragsteller)" as MA
        actor "Vorgesetzter\n(Genehmiger)" as VG
        actor "IT-Admin /\nProjektleiter" as PL
        actor "Datenschutz-\nbeauftragter" as DSB
        actor "GitHub Actions\n(Automatisierung)" as GH
        actor "Monitoring /\nAudit-System" as MON

        usecase "UC1: Rechteantrag\nstellen (Self-Service)" as UC1
        usecase "UC2: Antrag\nprüfen & genehmigen" as UC2
        usecase "UC3: Rolle &\nBerechtigung zuweisen" as UC3
        usecase "UC4: GitHub Team\n& Repo-Zugriff syncen" as UC4
        usecase "UC5: Audit-Log\nschreiben" as UC5
        usecase "UC6: Compliance-\nReport generieren" as UC6
        usecase "UC7: Rechte\nentziehen (Offboarding)" as UC7
        usecase "UC8: Notfall-\nzugriff (Break-Glass)" as UC8
        usecase "UC9: Rollen-\nverwaltung (CRUD)" as UC9
        usecase "UC10: Dashboard &\nMonitoring anzeigen" as UC10

        MA --> UC1
        VG --> UC2
        PL --> UC3
        PL --> UC9
        DSB --> UC6
        GH --> UC4
        GH --> UC5
        MON --> UC5
        MON --> UC10
        PL --> UC7
        PL --> UC8
        MA --> UC10 : "Eigenen Status prüfen"
        VG --> UC10 : "Team-Status prüfen"
```

**Abb. X: Use-Case-Diagramm – 10 Use Cases, 6 Akteure (inkl. technische Akteure GitHub Actions & Monitoring). Beziehungen: <<include>> UC1→UC5, UC3→UC4→UC5, UC7→UC5, UC8→UC5**