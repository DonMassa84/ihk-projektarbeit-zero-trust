# Architektur – Zero-Trust Pilot

**Stand:** 10.07.2026  
**Status:** Prototypische Entwicklung (Vorbereitung, nicht freigegeben)

---

## Komponenten

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Backend                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │  Health  │  │   Pilot  │  │  Audit   │  │  User/  │ │
│  │   API    │  │   API    │  │   API    │  │ Role API│ │
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘ │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Policy  │  │  Audit   │  │Provision-│              │
│  │ Service  │  │  Chain   │  │ ing Svc  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │              SQLite / PostgreSQL                     ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────┐
│  GitHub (Dry-Run)   │
│  - Team-Zuordnung   │
│  - Simulation       │
└─────────────────────┘
```

## Datenmodell (6 Entitäten)

- **UserReference:** Externe Benutzer-Identität
- **Role:** Pilot-Rolle mit Risikostufe und GitHub-Team-Mapping
- **AccessRequest:** Antrag mit Status (DRAFT→SUBMITTED→APPROVED/REJECTED→PROVISIONED/FAILED)
- **ApprovalDecision:** Genehmigungsentscheidung (APPROVED/REJECTED)
- **AuditEvent:** Ereignis mit SHA-256-Hash-Verkettung
- **ProvisioningAttempt:** Provisionierungsversuch (DRY_RUN/TEST_API)

## API-Endpunkte (12)

| Methode | Pfad | Zweck |
|---------|------|-------|
| POST | /api/v1/users | Benutzer anlegen |
| GET | /api/v1/users | Benutzer auflisten |
| POST | /api/v1/roles | Rolle anlegen |
| GET | /api/v1/roles | Rollen auflisten |
| POST | /api/v1/access-requests | Antrag erstellen |
| GET | /api/v1/access-requests/{id} | Antrag abrufen |
| GET | /api/v1/access-requests | Anträge auflisten |
| POST | /api/v1/access-requests/{id}/submit | Antrag einreichen |
| POST | /api/v1/access-requests/{id}/approve | Genehmigen |
| POST | /api/v1/access-requests/{id}/reject | Ablehnen |
| POST | /api/v1/access-requests/{id}/provision | Provisionieren |
| GET | /api/v1/access-requests/{id}/attempts | Versuche abrufen |
| GET | /api/v1/audit/events | Audit-Ereignisse |
| GET | /api/v1/audit/verify | Kette verifizieren |
| GET | /api/v1/health | Health-Check |
| GET | /api/v1/ready | Readiness-Check |

## Audit-Hash-Kette

```
event_hash = SHA256(
    canonical_timestamp +
    event_type +
    actor_reference +
    object_type +
    object_id +
    canonical_payload +
    previous_hash
)
```

- Genesis-Ereignis: `previous_hash = None`
- Jeder Eintrag enthält den Hash des Vorgängers
- Verifikation: Alle Hashes werden neu berechnet und mit gespeicherten Werten verglichen
