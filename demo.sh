#!/usr/bin/env bash
set -euo pipefail
# demo.sh – Nachweis der Funktionsfähigkeit des Zero-Trust-Prototyps
# Führt alle API-Endpunkte durch und zeigt Ergebnisse.

BASE="${1:-http://localhost:8000}"
PASS=0
FAIL=0

green() { echo -e "\e[32m✅ $1\e[0m"; }
red()   { echo -e "\e[31m❌ $1\e[0m"; }
step()  { echo -e "\n\e[36m━━━ $1 ━━━\e[0m"; }

check() {
  local desc="$1" method="$2" url="$3" data="$4" expect="$5"
  if [ -n "$data" ]; then
    resp=$(curl -s -o /tmp/demo_resp.json -w "%{http_code}" -X "$method" "$BASE$url" -H "Content-Type: application/json" -d "$data")
  else
    resp=$(curl -s -o /tmp/demo_resp.json -w "%{http_code}" -X "$method" "$BASE$url")
  fi
  if [ "$resp" = "$expect" ]; then
    green "$desc (HTTP $resp)"
    PASS=$((PASS+1))
  else
    red "$desc → erwartet $expect, erhalten $resp"
    cat /tmp/demo_resp.json 2>/dev/null | python3 -m json.tool 2>/dev/null || true
    FAIL=$((FAIL+1))
  fi
}

echo "╔══════════════════════════════════════════════════╗"
echo "║  Zero-Trust Prototype – API Functionality Demo   ║"
echo "╚══════════════════════════════════════════════════╝"
echo "Target: $BASE"

step "1. Health Check"
check "Health endpoint" GET "/api/v1/health" "" "200"

step "2. Authentication"
check "Login (success)" POST "/api/v1/auth/login" '{"username":"admin","password":"admin"}' "200"
check "Login (failure)" POST "/api/v1/auth/login" '{"username":"admin","password":"wrong"}' "401"
check "Current user" GET "/api/v1/auth/me" "" "200"

step "3. RBAC – Role Management"
check "List roles" GET "/api/v1/rbac/roles" "" "200"
check "Request role" POST "/api/v1/rbac/request" '{"user_id":1,"role_id":2,"justification":"Project access"}' "200"
check "List pending requests" GET "/api/v1/rbac/requests?status=pending" "" "200"
check "Get user roles" GET "/api/v1/rbac/users/1/roles" "" "200"
check "Approve request" POST "/api/v1/rbac/approve" '{"request_id":1,"reviewer_id":1,"comment":"OK"}' "200"
check "Reject request" POST "/api/v1/rbac/reject" '{"request_id":2,"reviewer_id":1,"reason":"Not authorized"}' "200"
check "Revoke role" POST "/api/v1/rbac/revoke" '{"user_id":1,"role_id":2,"revoked_by":1,"reason":"Access expired"}' "200"

step "4. Audit Logging"
check "Create audit log" POST "/api/v1/audit/log" '{"action":"test","resource":"api","user_id":1,"details":"Demo test"}' "200"
check "Query audit logs" GET "/api/v1/audit/logs" "" "200"
check "Audit statistics" GET "/api/v1/audit/stats" "" "200"

step "5. GitHub Integration"
check "Trigger workflow" POST "/api/v1/github/trigger" '{"user":"demo","role":"Developer","action":"grant"}' "200"
check "Workflow history" GET "/api/v1/github/history" "" "200"
check "Webhook handler" POST "/api/v1/github/webhook" "" "200"

step "6. ML Services (Simulated)"
check "Anomaly detection" POST "/api/v1/ml/anomaly" '{"event_type":"login","user_id":1,"resource":"/api/admin"}' "200"
check "Policy generation" POST "/api/v1/ml/policy" '{"context":"developer access to production"}' "200"
check "Embeddings" POST "/api/v1/ml/embed" '{"text":"role-based access control"}' "200"
check "Semantic search" POST "/api/v1/ml/search" '{"query":"access control","corpus":["RBAC","Zero Trust","VPN"],"top_k":2}' "200"

echo -e "\n╔══════════════════════════════════════════════════╗"
printf "║  Ergebnis: %3d passed, %d failed                ║\n" $PASS $FAIL
echo "╚══════════════════════════════════════════════════╝"
[ "$FAIL" -eq 0 ] && echo -e "\e[32m🎉 Alle Endpunkte funktionieren!\e[0m" || echo -e "\e[33m⚠  $FAIL Endpunkte fehlgeschlagen\e[0m"
