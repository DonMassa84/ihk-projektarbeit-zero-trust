import gradio as gr
import json, random
import sys, os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src", "ml", "inference"))
from anomaly_detector import predict

TITLE = "Zero-Trust Audit Explorer"
DESCRIPTION = """
IHK-Projekt: Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**Durchsuche und analysiere Audit-Logs** mit semantischer Suche
"""

SAMPLE_LOGS = [
    {"timestamp": (datetime.now() - timedelta(minutes=5)).isoformat(), "action": "ROLE_REQUESTED", "user": "alice@example.com", "resource": "write-access", "result": "success"},
    {"timestamp": (datetime.now() - timedelta(hours=1)).isoformat(), "action": "ROLE_APPROVED", "user": "bob@example.com", "resource": "admin-role", "result": "success"},
    {"timestamp": (datetime.now() - timedelta(hours=2)).isoformat(), "action": "MASS_ROLE_REVOKE", "user": "attacker_001", "resource": "all-roles", "result": "failure"},
    {"timestamp": (datetime.now() - timedelta(hours=3)).isoformat(), "action": "UNAUTHORIZED_ACCESS", "user": "unknown", "resource": "admin-panel", "result": "failure"},
    {"timestamp": (datetime.now() - timedelta(hours=5)).isoformat(), "action": "ROLE_REQUESTED", "user": "carol@example.com", "resource": "read-only", "result": "success"},
    {"timestamp": (datetime.now() - timedelta(hours=6)).isoformat(), "action": "ADMIN_IMPERSONATE", "user": "suspicious_conn", "resource": "super-admin-role", "result": "failure"},
    {"timestamp": (datetime.now() - timedelta(hours=8)).isoformat(), "action": "PRIVILEGE_ESCALATION", "user": "dev_user", "resource": "production/secrets", "result": "failure"},
    {"timestamp": (datetime.now() - timedelta(hours=12)).isoformat(), "action": "ROLE_REQUESTED", "user": "dave@example.com", "resource": "deploy-access", "result": "success"},
]


def search_logs(query: str, threshold: float) -> str:
    if not query.strip():
        lines = []
        for log in SAMPLE_LOGS:
            result = predict(log)
            anomaly_flag = "🔴" if result["is_anomaly"] else "🟢"
            score = result["score"]
            lines.append(f"| {log['timestamp'][:19]} | {log['action']} | {log['user']} | {anomaly_flag} {score:.0%} |")
        header = "## All Audit Events\n\n| Timestamp | Action | User | Score |\n|-----------|--------|------|-------|\n"
        return header + "\n".join(lines)

    query_lower = query.lower()
    results = []
    for log in SAMPLE_LOGS:
        text = f"{log['action']} {log['user']} {log['resource']}"
        if query_lower in text.lower():
            anomaly = predict(log)
            score = anomaly["score"]
            if score >= threshold:
                results.append((log, score))

    if not results:
        return f"No results found for '{query}' (threshold: {threshold:.0%})"

    lines = []
    for log, score in results:
        flag = "🔴" if score > 0.5 else "🟢"
        lines.append(f"| {log['timestamp'][:19]} | {log['action']} | {log['user']} | {log['resource']} | {flag} {score:.0%} |")

    header = f"## Search Results for '{query}'\n\n| Timestamp | Action | User | Resource | Anomaly Score |\n|-----------|--------|------|----------|---------------|\n"
    return header + "\n".join(lines)


with gr.Blocks(title=TITLE, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {TITLE}\n{DESCRIPTION}")

    with gr.Row():
        with gr.Column(scale=2):
            search_input = gr.Textbox(
                label="Search Query",
                placeholder="Search logs by action, user, or resource...",
            )
            threshold = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.0,
                step=0.05,
                label="Min. Anomaly Threshold",
            )
            search_btn = gr.Button("Search", variant="primary", size="lg")
        with gr.Column(scale=3):
            output = gr.Markdown(label="Results")

    search_btn.click(search_logs, inputs=[search_input, threshold], outputs=[output])

    gr.Markdown("---\n*Zero-Trust Security Concept · IHK Projektarbeit · Daniel Massa*")


if __name__ == "__main__":
    demo.launch()
