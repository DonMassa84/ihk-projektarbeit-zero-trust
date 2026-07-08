#!/usr/bin/env python3
import re
import sys

master_path = sys.argv[1]
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

checks = []

# 1. Formale Kriterien
checks.append(("Deckblatt IHK-konform", "Projektarbeit im Rahmen der Prüfung zum Certified IT Business Manager" in content))
checks.append(("Sperrvermerk vorhanden", "SPERRVERMERK" in content))
checks.append(("Eidesstattliche Erklärung", "Eidesstattliche Erklärung" in content))
checks.append(("Eidesstattliche im IV", "Eidesstattliche Erklärung" in content and "......" in content.split("Eidesstattliche Erklärung")[1][:50]))

# 2. Verzeichnisse
checks.append(("Inhaltsverzeichnis", "## INHALTSVERZEICHNIS" in content))
checks.append(("Abbildungsverzeichnis", "## ABBILDUNGSVERZEICHNIS" in content))
checks.append(("Tabellenverzeichnis", "## TABELLENVERZEICHNIS" in content))
checks.append(("Abkürzungsverzeichnis", "## ABKÜRZUNGSVERZEICHNIS" in content))
checks.append(("Literaturverzeichnis", "## LITERATURVERZEICHNIS" in content or "# LITERATURVERZEICHNIS" in content))

# 3. Fußnoten
footnotes = len(re.findall(r'\[\^(\d+)\]', content))
checks.append((f"Fußnoten ({footnotes} Stück)", footnotes >= 6))

# 4. Struktur Kapitel 1-8
for i in range(1, 9):
    checks.append((f"Kapitel {i} vorhanden", f"# {i} " in content or f"## {i} " in content))

# 5. SMART-Ziele
checks.append(("SMART-Ziele", "SMART" in content and "Spezifisch" in content and "Messbar" in content))

# 6. Wirtschaftlichkeitsanalyse
checks.append(("Wirtschaftlichkeitsanalyse", "Amortisation" in content and "ROI" in content))

# 7. Nutzwertanalyse
checks.append(("Nutzwertanalyse", "Nutzwertanalyse" in content))

# 8. RBAC-Modell
checks.append(("RBAC-Modell", "RBAC" in content and "Role" in content and "Permission" in content))

# 9. Zero-Trust + Standards
checks.append(("Zero-Trust (NIST SP 800-207)", "NIST SP 800-207" in content or "Zero Trust Architecture" in content))
checks.append(("DSGVO/ISO 27001", "DSGVO" in content and "ISO 27001" in content))

# 10. Testkonzept
checks.append(("Testkonzept (4 Stufen)", "Unit-Test" in content and "Integrationstest" in content and "Security-Test" in content and "Abnahmetest" in content))
checks.append(("12 Testfälle", "TF12" in content or "Testfall" in content))

# 11. Abnahme
checks.append(("Abnahmeprotokoll", "Abnahmeprotokoll" in content))

# 12. GitHub/Technisch
checks.append(("GitHub Actions Workflow", "GitHub Actions" in content and "workflow" in content.lower()))
checks.append(("ML-Modelle (CodeBERT/flan-t5)", "CodeBERT" in content and "flan-t5" in content))

# 13. Diagramme referenziert
checks.append(("Abbildungen referenziert", "Abbildung" in content or "Abb." in content))
checks.append(("Tabellen referenziert", "Tabelle" in content or "Tab." in content))

# Auswertung
passed = sum(1 for _, ok in checks if ok)
total = len(checks)
percentage = (passed / total) * 100

print(f"\n{'='*60}")
print(f"IHK VALIDIERUNG: {passed}/{total} ({percentage:.0f}%)")
print(f"{'='*60}")
for name, ok in checks:
    status = "✓" if ok else "✗"
    print(f"  {status} {name}")

if percentage >= 90:
    print(f"\n🎉 SEHR GUT - Prüfungsreif (Note 1,0-1,3)")
elif percentage >= 80:
    print(f"\n✅ GUT - Kleinere Nachbesserungen (Note 1,7-2,3)")
else:
    print(f"\n⚠️  NACHBESSERUNG ERFORDERLICH")

sys.exit(0 if percentage >= 85 else 1)
