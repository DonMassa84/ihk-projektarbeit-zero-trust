# Hugging Face Model Candidates – PDF Review / Security / Semantic Search

## Entscheidung

Modelle werden nicht als Wahrheitsquelle genutzt. Sie können höchstens lokale Reviews, Zusammenfassungen, Embeddings oder Code-/Textanalysen unterstützen.

## Kandidaten

| Modell | Quelle | Zweck | Lokale Eignung | Projektrolle |
|---|---|---|---|---|
| microsoft/codebert-base | https://huggingface.co/microsoft/codebert-base | Code + Natural Language, CodeSearchNet, Feature Extraction | Mittel | Code-/Security-Ausblick |
| microsoft/graphcodebert-base | https://huggingface.co/microsoft/graphcodebert-base | Code-Repräsentationen mit Datenfluss | Mittel bis schwerer | optionaler Code-Ausblick |
| google/flan-t5-small | https://huggingface.co/google/flan-t5-small | kleine Instruction-/Text2Text-Aufgaben | Gut lokal möglich | kurze Review-Hinweise, nicht final |
| google-t5/t5-small | https://huggingface.co/google-t5/t5-small | Text2Text-Modell, 60M Parameter | Gut lokal möglich | Testmodell |
| sentence-transformers/all-MiniLM-L6-v2 | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 | Embeddings, 384-d Vektorraum, Semantic Search | Sehr gut lokal möglich | Kapitelähnlichkeit, Duplikate |
| sshleifer/distilbart-cnn-12-6 | https://huggingface.co/sshleifer/distilbart-cnn-12-6 | Summarization | Mittel | Kapitelzusammenfassungen |

## Empfohlene lokale Nutzung

1. all-MiniLM-L6-v2:
   - Kapitel-Embedding
   - Dubletten finden
   - semantische Nähe zwischen Zielen, Anforderungen, Tests, Abnahme prüfen

2. flan-t5-small / t5-small:
   - kurze Review-Hinweise
   - keine langen finalen Textpassagen blind übernehmen

3. CodeBERT:
   - Code-/Security-Ausblick
   - keine Behauptung über produktive Anomalieerkennung ohne Evaluation

## Nicht erlaubte Nutzung

- Keine automatische Änderung der finalen PDF.
- Keine eidesstattlichen Aussagen generieren.
- Keine personenbezogenen Daten an Modelle/API geben.
- Keine Bewertung „Bachelor-ready" allein durch Modell.
