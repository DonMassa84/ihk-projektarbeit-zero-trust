# API Inventory – Zero-Trust Pilot

**Stand:** 10.07.2026

| Endpoint | Methode | Status | Beschreibung |
|----------|---------|--------|--------------|
| /api/v1/health | GET | ✅ | Health-Check |
| /api/v1/ready | GET | ✅ | Readiness (DB + Audit) |
| /api/v1/users | POST | ✅ | User anlegen |
| /api/v1/users | GET | ✅ | User auflisten |
| /api/v1/roles | POST | ✅ | Rolle anlegen |
| /api/v1/roles | GET | ✅ | Rollen auflisten |
| /api/v1/access-requests | POST | ✅ | Antrag erstellen |
| /api/v1/access-requests/{id} | GET | ✅ | Antrag abrufen |
| /api/v1/access-requests | GET | ✅ | Anträge filtern/suchen |
| /api/v1/access-requests/{id}/submit | POST | ✅ | Antrag einreichen |
| /api/v1/access-requests/{id}/approve | POST | ✅ | Genehmigen |
| /api/v1/access-requests/{id}/reject | POST | ✅ | Ablehnen |
| /api/v1/access-requests/{id}/provision | POST | ✅ | Provisionieren (DRY_RUN/TEST_API) |
| /api/v1/access-requests/{id}/attempts | GET | ✅ | Provisionierungsversuche |
| /api/v1/audit/events | GET | ✅ | Audit-Ereignisse |
| /api/v1/audit/verify | GET | ✅ | Kettenverifikation |

**Gesamt:** 16 Endpunkte, alle implementiert und getestet.
