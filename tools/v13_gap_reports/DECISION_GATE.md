# Decision Gate: V13 Golden Reference Integration

## Status Check

| Criterion | Result |
|-----------|--------|
| Local build exit 0 | ✅ |
| 63 PDF pages | ✅ |
| 0 missing assets | ✅ (all 14 artifacts + cover + source_cover) |
| 0 clipped content | ✅ |
| 0 unexplained text diffs | ✅ |
| Full page rendering | ✅ All 63 pages rendered |
| Existing pipeline unmodified | ✅ Pandoc/XeLaTeX untouched |
| Git diff documented | ✅ |

## Assessment

**Decision: `KEEP_PANDOC_USE_V13_AS_REFERENCE`**

### Rationale

1. **V13 builds locally and is reproducible** – the port is successful
2. **Text content is 100% identical** between local and sandbox builds
3. **Pandoc pipeline is not broken** – it remains the productive build path
4. **ReportLab approach couples content and layout** – hard to maintain for ongoing edits
5. **V13 quality practices can be extracted without full migration**

### Next Steps

| Priority | Action | Target |
|----------|--------|--------|
| 1 | Fix test case count in dokumentation.md (14→12 with honest status) | dokumentation.md §6.3 |
| 2 | Add Sperrvermerk, Zero-Trust-Prinzipien, RACI, Schnittstellen | dokumentation.md |
| 3 | Create automated figure/table caption extraction for pandoc build | quality_gate/ |
| 4 | Align appendix structure with V13 A1-A12 | dokumentation.md |
| 5 | Extract V13 diagram data structures into JSON/YAML for reuse | 08_assets/v13/ |

### Migration Readiness

ReportLab migration is **NOT RECOMMENDED** at this point because:

- Content is tightly coupled with Python code (hard to edit for non-developers)
- No separation of content, layout, and data
- Our Pandoc pipeline already produces valid IHK-compliant PDFs
- V13's value is in its **quality practices**, not its build technology

### Pipeline Strategy

```
Pandoc/XeLaTeX = produktiver Hauptbuild (unverändert)
ReportLab V13  = Golden Reference für Inhalte, Diagramme und Qualität
Hybrid         = empfohlen: automatische Verzeichnisse + Caption-Prüfung ins Gate
```

## Final Verdict

**BLOCKED für ReportLab-Migration. KEEP_PANDOC_USE_V13_AS_REFERENCE ist die empfohlene Entscheidung.**

V13 wird als Quality Benchmark genutzt, nicht als Build-Ersatz.
