# Hugging Face Privacy Policy – Lokale Nutzung

## Grundsatz

Alle HF-Operationen erfolgen standardmäßig offline. Externe Zugriffe nur mit expliziter Freigabe.

## Lokale Sicherheitsregeln

1. `HF_HUB_OFFLINE=1` — kein HTTP zu huggingface.co
2. `HF_HUB_DISABLE_TELEMETRY=1` — keine Telemetrie
3. Kein `hf login` ohne Nutzer-Entscheidung
4. Tokens nur aus sicherer Umgebung (kein Hartcode)
5. Cache-Verzeichnis: `~/.cache/huggingface/` — nicht versioniert

## Was darf NICHT übertragen werden

- Prüflingsnummer
- Name, Adresse, Kontaktdaten
- PDF-Rohtexte
- Eidesstattliche Erklärung
- Interne Projektstruktur
- Secrets, Tokens, API-Keys
- Echte Audit-Logs

## Was darf lokal genutzt werden

- Offline-gespeicherte Modelle (aus Cache)
- Statische Kandidatenlisten
- Lokale Regex-/Heuristik-Checks
- Prompt-Templates (ohne Dateninhalt)

## Prüfungsfeste Formulierung

Die Verarbeitung personenbezogener Daten oder vertraulicher Projektdaten über externe Hugging-Face-Dienste erfolgt nicht. Alle Analysen werden lokal durchgeführt.
