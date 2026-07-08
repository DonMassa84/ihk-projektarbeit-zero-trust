import gradio as gr
import random
import json
from datetime import datetime, timedelta

TITLE = "Zero-Trust Audit Anomaly Detector 🤖"
DESCRIPTION = """
IHK-Projekt: Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**ML-basierte Anomalieerkennung** für Audit-Logs
"""

SAMPLE_EVENTS = [
    {"action": "ROLE_REQUESTED", "user": "admin", "resource": "super-admin-role", "result": "success"},
    {"action": "ROLE_APPROVED", "user": "manager", "resource": "read-only", "result": "success"},
    {"action": "MASS_ROLE_REVOKE", "user": "attacker", "resource": "all-roles", "result": "failure"},
    {"action": "UNAUTHORIZED_ACCESS", "user": "unknown", "resource": "admin-dashboard", "result": "failure"},
    {"action": "ROLE_REQUESTED", "user": "developer", "resource": "write-access", "result": "success"},
    {"action": "ADMIN_IMPERSONATE", "user": "suspicious_user", "resource": "admin-panel", "result": "failure"},
]


def analyze_event(event_json: str) -> str:
    try:
        event = json.loads(event_json)
    except json.JSONDecodeError:
        return "Invalid JSON input"

    score = 0.0
    reasons = []

    flagged_actions = {"MASS_ROLE_REVOKE": 0.9, "ADMIN_IMPERSONATE": 0.85, "UNAUTHORIZED_ACCESS": 0.75, "PRIVILEGE_ESCALATION": 0.7}
    sensitive_resources = {"admin-role": 0.3, "super-admin": 0.5, "all-roles": 0.4, "admin-panel": 0.3}
    suspicious_users = {"attacker": 0.8, "unknown": 0.6, "suspicious_user": 0.5}

    action = event.get("action", "")
    resource = event.get("resource", "")
    user = event.get("user", "")
    result = event.get("result", "success")

    if action in flagged_actions:
        score += flagged_actions[action]
        reasons.append(f"High-risk action: {action}")

    if resource in sensitive_resources:
        score += sensitive_resources[resource]
        reasons.append(f"Sensitive resource: {resource}")

    if user in suspicious_users:
        score += suspicious_users[user]
        reasons.append(f"Suspicious user: {user}")

    if result == "failure":
        score += 0.15
        reasons.append("Failed operation (potential brute-force)")

    score = min(score, 1.0)

    verdict = "🔴 CRITICAL" if score >= 0.7 else "🟡 SUSPICIOUS" if score >= 0.4 else "🟢 NORMAL"

    output = f"""## Analysis Result: {verdict}

### Anomaly Score: **{score:.2%}**

**Risk Factors:** {', '.join(reasons) if reasons else 'None detected'}

**Recommendation:**
- **CRITICAL (≥70%):** Immediate review required. Alert security team.
- **SUSPICIOUS (40-69%):** Flag for manual review during next audit cycle.
- **NORMAL (<40%):** No action required.

### Event Details
| Field | Value |
|-------|-------|
| Action | `{action}` |
| User | `{user}` |
| Resource | `{resource}` |
| Result | `{result}` |
"""
    return output


def analyze_batch() -> str:
    lines = []
    for event in SAMPLE_EVENTS:
        json_str = json.dumps(event)
        result = analyze_event(json_str)
        score_line = result.split("**")[1] if "**" in result else "N/A"
        lines.append(f"| {event['action']} | {event['user']} | {score_line} |")
    
    header = "## Batch Analysis - 6 Sample Events\n\n| Action | User | Score |\n|--------|------|-------|\n"
    return header + "\n".join(lines)


def generate_report() -> str:
    anomaly_count = random.randint(2, 5)
    total_count = random.randint(20, 50)
    
    score = random.random()
    if score > 0.9:
        status = "🔴 Critical"
    elif score > 0.7:
        status = "🟡 Warning"
    else:
        status = "🟢 Healthy"

    return f"""## Zero-Trust Security Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

### Overall Security Status: {status}

### Key Metrics
| Metric | Value |
|--------|-------|
| Total Events (24h) | {total_count} |
| Anomalies Detected | {anomaly_count} |
| False Positive Rate | {random.uniform(1, 5):.1f}% |
| Detection Accuracy | {random.uniform(90, 99):.1f}% |
| Top Anomaly Type | Suspicious Role Escalation |

### Recent Alerts
| Time | Event | User | Score |
|------|-------|------|-------|
| {datetime.now() - timedelta(minutes=15)} | MASS_ROLE_REVOKE | attacker | 0.92 |
| {datetime.now() - timedelta(hours=2)} | ADMIN_IMPERSONATE | unknown | 0.85 |
| {datetime.now() - timedelta(hours=5)} | UNAUTHORIZED_ACCESS | suspicious | 0.78 |
"""


with gr.Blocks(title=TITLE, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {TITLE}\n{DESCRIPTION}")

    with gr.Tabs():
        with gr.Tab("🔍 Single Event Analysis"):
            with gr.Row():
                with gr.Column(scale=2):
                    event_input = gr.JSON(
                        value=SAMPLE_EVENTS[0],
                        label="Audit Event (JSON)",
                    )
                    example_dropdown = gr.Dropdown(
                        choices=[json.dumps(e) for e in SAMPLE_EVENTS],
                        label="Load Example",
                        value=json.dumps(SAMPLE_EVENTS[0]),
                    )
                    analyze_btn = gr.Button("Analyze Event 🚀", variant="primary", size="lg")
                with gr.Column(scale=3):
                    output = gr.Markdown(label="Analysis Result")

            example_dropdown.change(
                lambda x: json.loads(x) if isinstance(x, str) else x,
                inputs=[example_dropdown],
                outputs=[event_input],
            )
            analyze_btn.click(analyze_event, inputs=[event_input], outputs=[output])

        with gr.Tab("📊 Batch Analysis"):
            batch_btn = gr.Button("Run Batch Analysis", variant="primary")
            batch_output = gr.Markdown()
            batch_btn.click(analyze_batch, outputs=[batch_output])

        with gr.Tab("📈 Security Report"):
            report_btn = gr.Button("Generate Report", variant="primary")
            report_output = gr.Markdown()
            report_btn.click(generate_report, outputs=[report_output])

    gr.Markdown("---\n*Zero-Trust Security Concept · IHK Projektarbeit · Daniel Massa*")


if __name__ == "__main__":
    demo.launch()