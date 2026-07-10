# MODEL_CATALOG_REPORT.md

Erstellt: 2026-07-10T02:50:48.418339

| Modell | Task | Lokale Eignung | Projektrolle |
|---|---|---|---|
| microsoft/codebert-base | Code + NL, Feature Extraction | Mittel | Code-/Security-Ausblick |
| microsoft/graphcodebert-base | Code mit Datenfluss | Schwer | optionaler Code-Ausblick |
| google/flan-t5-small | Instruction/Text2Text | Gut | Review-Hinweise |
| google-t5/t5-small | Text2Text, 60M | Gut | Testmodell |
| sentence-transformers/all-MiniLM-L6-v2 | Embeddings, Semantic Search | Sehr gut | Kapitelähnlichkeit |
| sshleifer/distilbart-cnn-12-6 | Summarization | Mittel | Kapitelzusammenfassungen |

## Empfehlung
Nur lokaler Cache. Kein Download ohne --allow-online.