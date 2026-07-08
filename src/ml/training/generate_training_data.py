import json, random
from datetime import datetime, timedelta

random.seed(42)
N_SAMPLES = 2000
NORMAL_ACTIONS = [
    "ROLE_REQUESTED", "ROLE_APPROVED", "PASSWORD_RESET", "LOGIN_SUCCESS",
    "LOGOUT", "PROFILE_UPDATE", "REPO_CLONE", "ISSUE_CREATED",
    "PR_OPENED", "PR_MERGED", "CODE_REVIEWED", "COMMENT_ADDED",
    "DOCUMENT_VIEWED", "REPORT_EXPORTED", "AUDIT_LOG_VIEWED",
]
ANOMALY_ACTIONS = [
    "MASS_ROLE_REVOKE", "ADMIN_IMPERSONATE", "UNAUTHORIZED_ACCESS",
    "PRIVILEGE_ESCALATION", "BRUTE_FORCE_LOGIN", "DATA_EXFILTRATION",
    "ROLE_ESCALATION", "SECRET_LEAKAGE", "SUSPICIOUS_API_CALL",
    "OUTSIDE_BUSINESS_HOURS_ACCESS", "RAPID_SUCCESSIVE_FAILURES",
]
NORMAL_USERS = ["alice", "bob", "charlie", "dave", "eve", "frank", "grace", "henry"]
SUSPICIOUS_USERS = ["unknown_user", "attacker_001", "suspicious_conn", "root_external"]
NORMAL_RESOURCES = ["repo/readme", "user/profile", "api/docs", "team/view", "issue/123"]
SENSITIVE_RESOURCES = ["admin/panel", "super-admin-role", "all-roles", "production/secrets"]

events = []
for _ in range(N_SAMPLES):
    is_anomaly = random.random() < 0.15
    action = random.choice(ANOMALY_ACTIONS if is_anomaly else NORMAL_ACTIONS)
    user = random.choice(SUSPICIOUS_USERS if is_anomaly else NORMAL_USERS)
    resource = random.choice(SENSITIVE_RESOURCES if is_anomaly else NORMAL_RESOURCES)
    result = "failure" if (is_anomaly and random.random() < 0.7) else "success"
    score = round(random.uniform(0.7, 1.0) if is_anomaly else random.uniform(0.0, 0.3), 4)

    events.append({
        "text": f"Action: {action} | User: {user} | Resource: {resource} | Result: {result}",
        "label": 1 if is_anomaly else 0,
        "action": action, "user": user, "resource": resource, "result": result, "score": score,
    })

with open("audit_dataset.json", "w") as f:
    json.dump(events, f, indent=2)
print(f"Generated {len(events)} events ({sum(1 for e in events if e['label'])} anomalies)")
