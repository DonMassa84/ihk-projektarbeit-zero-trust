#!/usr/bin/env python3
import re
import sys

master_path = sys.argv[1]
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Finde INHALTSVERZEICHNIS Bereich
iv_start = content.find("## INHALTSVERZEICHNIS")
if iv_start == -1:
    print("INHALTSVERZEICHNIS nicht gefunden")
    sys.exit(1)

iv_end = content.find("---", iv_start)
if iv_end == -1:
    iv_end = content.find("## ", iv_start + 1)

iv_block = content[iv_start:iv_end]

# Parse Einträge
lines = iv_block.split('\n')
new_lines = []
page_counter = 1
in_roman_main = False
in_roman_appendix = False
roman_main_pages = []
arabic_pages = []
roman_appendix_pages = []

# Logik: Vorwort = römisch I-V, Kapitel 1-8 = arabisch 1-70, Anhang + Literatur = römisch i-x
# Wir schätzen Seitenzahlen basierend auf Einträgen

roman_main_entries = [
    "Vorwort", "Einleitung", "Projektumfeld", "Meine Tätigkeiten", "Allgemeine Informationen",
    "SPERRVERMERK", "ABBILDUNGSVERZEICHNIS", "TABELLENVERZEICHNIS", "ABKÜRZUNGSVERZEICHNIS"
]

arabic_entries = [
    "1 Projektinitiierung", "1.1 Projektumfeld", "1.2 Ausgangssituation", "1.3 Ist-Analyse",
    "1.4 Problemstellung", "1.5 Soll-Konzept", "1.6 Projektziele nach SMART",
    "1.7 Projektbegründung", "1.8 Projektabgrenzung", "1.9 Projektschnittstellen",
    "1.10 Projektauftrag",
    "2 Projektplanung", "2.1 Vorgehensmodell", "2.2 Projektphasen", "2.3 Projektstrukturplan",
    "2.4 Arbeitspakete", "2.5 Meilensteinplanung", "2.6 Ressourcenplanung",
    "2.7 Kostenplanung", "2.8 Kommunikationsplanung", "2.9 Risikoanalyse",
    "2.10 Qualitätsplanung", "2.11 Abweichungen vom Projektantrag",
    "3 Analyse und Konzeption", "3.1 Anforderungsanalyse", "3.2 Lastenheft / Fachkonzept",
    "3.3 Stakeholderanalyse", "3.4 Make-or-Buy-Entscheidung", "3.5 Wirtschaftlichkeitsanalyse",
    "3.6 Nutzwertanalyse", "3.7 Zero-Trust-Konzept", "3.8 RBAC-Modell",
    "3.9 Datenschutz- und Sicherheitskonzept",
    "4 Technischer Entwurf", "4.1 Zielplattform", "4.2 Architekturdesign",
    "4.3 GitHub-Workflow-Integration", "4.4 Self-Service-Prozess", "4.5 Datenmodell",
    "4.6 Geschäftslogik", "4.7 Audit-Logging", "4.8 Schnittstellen",
    "4.9 Maßnahmen zur Qualitätssicherung", "4.10 Pflichtenheft / Datenverarbeitungskonzept",
    "5 Umsetzung", "5.1 Aufbau der Entwicklungsumgebung", "5.2 Implementierung der Datenstrukturen",
    "5.3 Implementierung des RBAC-Modells", "5.4 Implementierung der Benutzeroberfläche",
    "5.5 Implementierung der GitHub-Automatisierung", "5.6 Implementierung der Geschäftslogik",
    "5.7 Implementierung der Audit-Protokollierung", "5.8 Implementierung der Qualitätssicherung",
    "5.9 Entwicklerdokumentation",
    "6 Test und Abnahme", "6.1 Testkonzept", "6.2 Funktionstests", "6.3 Integrationstests",
    "6.4 Security-Tests", "6.5 Datenschutzprüfung", "6.6 Testfallmatrix",
    "6.7 Fehleranalyse", "6.8 Soll-Ist-Vergleich", "6.9 Abnahme",
    "7 Einführung und Dokumentation", "7.1 Einführungskonzept", "7.2 Pilotbetrieb",
    "7.3 Schulung", "7.4 Change Management", "7.5 Benutzerdokumentation",
    "7.6 Betriebsdokumentation", "7.7 Übergabe",
    "8 Projektabschluss", "8.1 Projektergebnis", "8.2 Soll-Ist-Vergleich",
    "8.3 Wirtschaftliche Bewertung", "8.4 Lessons Learned", "8.5 Risiken nach Projektabschluss",
    "8.6 Ausblick", "8.7 Persönliches Fazit"
]

roman_appendix_entries = [
    "Literaturverzeichnis", "Abkürzungsverzeichnis", "Abbildungsverzeichnis",
    "Tabellenverzeichnis", "Anhang", "A1 Detaillierte Zeitplanung", "A2 Lastenheft-Auszug",
    "A3 Use-Case-Diagramm", "A4 Pflichtenheft-Auszug", "A5 Datenmodell",
    "A6 EPK-Prozessbeschreibung", "A7 Oberflächenentwürfe", "A8 Screenshots der Anwendung",
    "A9 Entwicklerdokumentation", "A10 Testfall Konsole", "A11 Schnittstellenübersicht",
    "A12 Klassendiagramm", "A13 Benutzerdokumentation", "A14 Datenschutz-Checkliste",
    "A15 Abnahmeprotokoll", "Eidesstattliche Erklärung"
]

def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i, v in enumerate(val):
        while n >= v:
            res += syms[i]
            n -= v
    return res

def to_roman_lower(n):
    return to_roman(n).lower()

# Neue IV bauen
new_iv = "## INHALTSVERZEICHNIS\n\n"

# Römisch groß (I, II, III...) für Vorwort/Verzeichnisse
page = 1
for entry in roman_main_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {to_roman(page)}\n"
    page += 1

# Arabisch (1, 2, 3...) für Kapitel 1-8
page = 1
for entry in arabic_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {page}\n"
    page += 1

# Römisch klein (i, ii, iii...) für Anhang
page = 1
for entry in roman_appendix_entries:
    dots = "." * (60 - len(entry))
    new_iv += f"{entry} {dots} {to_roman_lower(page)}\n"
    page += 1

new_iv += "\n---\n"

# Ersetzen
new_content = content[:iv_start] + new_iv + content[iv_end:]

with open(master_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("IV korrigiert: römisch groß (Vorwort), arabisch (Kapitel), römisch klein (Anhang)")
