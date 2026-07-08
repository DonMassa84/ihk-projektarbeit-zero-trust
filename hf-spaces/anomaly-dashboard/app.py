import gradio as gr
import json, sys, os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src", "ml", "inference"))
from anomaly_detector import predict, batch_predict

TITLE = "Zero-Trust Audit Anomaly Detector"
DESCRIPTION = """
IHK-Projekt: Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**ML-basierte Anomalieerkennung** (CodeBERT) für Audit-Logs
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

    result = predict(event)
    score = result["score"]
    model_name = result["model"]

    if score >= 0.7:
        severity = "CRITICAL"
        icon = "🔴"
    elif score >= 0.4:
        severity = "SUSPICIOUS"
        icon = "🟡"
    else:
        severity = "NORMAL"
        icon = "🟢"

    reasons_str = ""
    if "reasons" in result:
        reasons_str = ", ".join(result["reasons"])

    output = f"""## Analysis Result: {icon} {severity}

### Anomaly Score: **{score:.2%}**
**Model:** {model_name}
**Risk Factors:** {reasons_str if reasons_str else 'None detected'}

### Event Details
| Field | Value |
|-------|-------|
| Action | `{event['action']}` |
| User | `{event['user']}` |
| Resource | `{event['resource']}` |
| Result | `{event['result']}` |
"""
    return output


def analyze_batch() -> str:
    results = batch_predict(SAMPLE_EVENTS)
    lines = []
    for event, result in zip(SAMPLE_EVENTS, results):
        score = result["score"]
        icon = "🔴" if score >= 0.5 else "🟢"
        lines.append(f"| {event['action']} | {event['user']} | {icon} {score:.0%} |")

    header = "## Batch Analysis - 6 Sample Events\n\n| Action | User | Anomaly Score |\n|--------|------|---------------|\n"
    return header + "\n".join(lines)


def generate_report() -> str:
    scores = [predict(e)["score"] for e in SAMPLE_EVENTS]
    anomaly_count = sum(1 for s in scores if s > 0.5)
    total_count = len(SAMPLE_EVENTS)
    avg_score = sum(scores) / len(scores)

    if avg_score > 0.7:
        status = "CRITICAL"
        icon = "🔴"
    elif avg_score > 0.4:
        status = "WARNING"
        icon = "🟡"
    else:
        status = "HEALTHY"
        icon = "🟢"

    now = datetime.now()
    lines = ""
    for i, (event, score) in enumerate(zip(SAMPLE_EVENTS, scores)):
        timestamp = (now - timedelta(hours=i * 2)).strftime("%Y-%m-%d %H:%M")
        icon = "🔴" if score >= 0.5 else "🟢"
        lines += f"| {timestamp} | {event['action']} | {event['user']} | {icon} {score:.0%} |\n"

    return f"""## Zero-Trust Security Report
**Generated:** {now.strftime('%Y-%m-%d %H:%M UTC')}

### Overall Security Status: {icon} {status}

### Key Metrics
| Metric | Value |
|--------|-------|
| Analyzed Events | {total_count} |
| Anomalies Detected | {anomaly_count} |
| Avg. Anomaly Score | {avg_score:.1%} |
| Detection Model | CodeBERT (fine-tuned) |

### Event Analysis
| Time | Action | User | Score |
|------|--------|------|-------|
{lines}"""


with gr.Blocks(title=TITLE, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {TITLE}\n{DESCRIPTION}")

    with gr.Tabs():
        with gr.Tab("Single Event Analysis"):
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
                    analyze_btn = gr.Button("Analyze Event", variant="primary", size="lg")
                with gr.Column(scale=3):
                    output = gr.Markdown(label="Analysis Result")

            example_dropdown.change(
                lambda x: json.loads(x) if isinstance(x, str) else x,
                inputs=[example_dropdown],
                outputs=[event_input],
            )
            analyze_btn.click(analyze_event, inputs=[event_input], outputs=[output])

        with gr.Tab("Batch Analysis"):
            batch_btn = gr.Button("Run Batch Analysis", variant="primary")
            batch_output = gr.Markdown()
            batch_btn.click(analyze_batch, outputs=[batch_output])

        with gr.Tab("Security Report"):
            report_btn = gr.Button("Generate Report", variant="primary")
            report_output = gr.Markdown()
            report_btn.click(generate_report, outputs=[report_output])

    gr.Markdown("---\n*Zero-Trust Security Concept · IHK Projektarbeit · Daniel Massa*")


if __name__ == "__main__":
    demo.launch()
