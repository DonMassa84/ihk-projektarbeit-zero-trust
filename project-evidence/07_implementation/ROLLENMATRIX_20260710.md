# Rollenmatrix – Zero-Trust Pilot

**Stand:** 10.07.2026  
**Status:** Definierte Pilotrollen

| Rolle | Beschreibung | Risiko | GitHub-Team | Erlaubte Aktionen |
|-------|-------------|--------|-------------|-------------------|
| Repository Reader | Lesezugriff auf Repositories | niedrig | readers | Clone, Pull, Issue lesen |
| Repository Contributor | Beitragsrechte | niedrig | contributors | Push, PR, Issue bearbeiten |
| Repository Maintainer | Verwaltungsrechte | mittel | maintainers | Merge, Settings lesen |
| Security Reviewer | Security-Audit-Zugriff | hoch | security-reviewers | Security-Tab, Alerts |
| Audit Reviewer | Audit-Log-Leseberechtigung | mittel | audit-reviewers | Audit-Logs exportieren |
| Workflow Administrator | CI/CD-Workflow-Verwaltung | hoch | workflow-admins | Workflows bearbeiten |

Testfall-Bezug: Alle 6 Rollen werden in TF01–TF13 verwendet.
