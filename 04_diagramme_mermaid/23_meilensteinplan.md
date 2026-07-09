# Mermaid: Meilensteinplan & Projektphasen (Gantt)

```mermaid
---
title: Meilensteinplan Zero-Trust-Projekt (6 Monate, 70h)
---
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %W.%m
    title       Projektphasen & Meilensteine

    section 1. Initialisierung & Analyse (Mai–Jun)
    M1: Projektauftrag freigegeben      :milestone, m1, 2026-05-15, 0d
    Ist-Analyse & Interviews            :active, a1, 2026-05-18, 10d
    Anforderungen & Lastenheft          :a2, after a1, 10d
    Stakeholder- & Risikoanalyse        :a3, after a2, 5d
    M2: Lastenheft / Fachkonzept fertig :milestone, m2, 2026-06-26, 0d

    section 2. Konzept & Architektur (Jul)
    Zero-Trust-Konzept & RBAC-Modell    :active, c1, 2026-07-01, 10d
    Make-or-Buy & Nutzwertanalyse       :c2, after c1, 5d
    Architektur & Pflichtenheft         :c3, after c2, 10d
    M3: Architektur & Pflichtenheft fg. :milestone, m3, 2026-08-07, 0d

    section 3. Umsetzung & GitHub-Integration (Aug–Sep)
    Dev-Setup & Datenmodell             :active, u1, 2026-08-10, 10d
    RBAC-Implementierung                :u2, after u1, 10d
    GitHub Actions Workflows            :u3, after u2, 10d
    Self-Service Portal (Frontend)      :u4, after u3, 10d
    Audit-Logging & Monitoring          :u5, after u4, 5d
    M4: Prototyp / Pilot implementiert  :milestone, m4, 2026-09-18, 0d

    section 4. Test & Abnahme (Sep–Okt)
    Funktionstests (Unit/Integration)   :active, t1, 2026-09-21, 10d
    Security-Tests (Bandit, Trivy, OWASP) :t2, after t1, 5d
    Datenschutzprüfung (DSB)            :t3, after t2, 5d
    User Acceptance Test (15 Pilot-User) :t4, after t3, 5d
    M5: Tests & Abnahme bestanden       :milestone, m5, 2026-10-16, 0d

    section 5. Einführung & Abschluss (Okt)
    Schulung & Dokumentation            :active, e1, 2026-10-19, 5d
    Pilotbetrieb & Hypercare            :e2, after e1, 5d
    Lessons Learned Workshop            :e3, after e2, 2d
    Projektdokumentation finalisieren   :e4, after e3, 5d
    M6: Projektdokumentation final      :milestone, m6, 2026-10-31, 0d
    Abgabe IHK (01.11.)                 :milestone, m7, 2026-11-01, 0d

    %% Critical Path Highlighting
    %% crit a1, a2, c1, c3, u1, u2, u3, u4, t1, t2, t3, t4, e4
```

| Meilenstein | Datum (KW) | Beschreibung | Abhängigkeit |
|-------------|------------|--------------|--------------|
| **M1** | 15.05.2026 (KW 20) | **Projektauftrag freigegeben** – Formeller Start durch Lenkungskreis | Genehmigung Projektantrag IHK |
| **M2** | 26.06.2026 (KW 26) | **Lastenheft / Fachkonzept fertig** – Anforderungen, Stakeholder, Risiken | Ist-Analyse, Interviews |
| **M3** | 07.08.2026 (KW 32) | **Architektur & Pflichtenheft freigegeben** – Zero-Trust-Konzept, RBAC, Make-or-Buy | M2 + Nutzwertanalyse |
| **M4** | 18.09.2026 (KW 38) | **Prototyp / Pilot implementiert** – RBAC, GitHub Actions, Self-Service, Audit-Log | M3 + 6 Wochen Dev |
| **M5** | 16.10.2026 (KW 42) | **Tests & Abnahme bestanden** – Funktion, Security, Datenschutz, UAT | M4 + 4 Wochen Test |
| **M6** | 31.10.2026 (KW 44) | **Projektdokumentation final** – Alle Kapitel, Anhang, Eidesstattliche Erklärung | M5 + 2 Wochen Doku |
| **M7** | **01.11.2026** | **Abgabe bei IHK Stuttgart** – Fristende alte PO | **Harter Termin!** |

**Abb. AA: Meilensteinplan mit kritischem Pfad (rot) – Puffer: 2 Wochen vor IHK-Frist**