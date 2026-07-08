import gradio as gr
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src", "ml", "inference"))
from policy_generator import generate

TITLE = "Zero-Trust Policy Generator"
DESCRIPTION = """
IHK-Projekt: Zero-Trust-Sicherheitskonzept mit GitHub-Integration  
**ML-basierte Policy-Generierung** (Rego/OPA) auf Basis von flan-t5
"""

EXAMPLES = [
    "Restrict admin access to users with MFA enabled",
    "Allow read-only access for viewer role",
    "Grant write access to engineering repository",
    "Deny access outside business hours",
    "Require approval for role escalation",
]


def generate_policy(requirement: str) -> str:
    if not requirement.strip():
        return "Please enter a policy requirement."

    result = generate(requirement)
    model_label = "ML Model (flan-t5)" if result["model"] == "flan-t5" else "Template Fallback"

    escaped = result["policy"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    output = f"""## Generated Policy

**Requirement:** {requirement}

**Source:** {model_label}

```rego
{result["policy"]}
```
"""
    return output


with gr.Blocks(title=TITLE, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {TITLE}\n{DESCRIPTION}")

    with gr.Row():
        with gr.Column(scale=2):
            req_input = gr.Textbox(
                label="Policy Requirement",
                placeholder="e.g., Restrict admin access to users with MFA enabled",
                lines=3,
            )
            example_btns = gr.Dataset(
                components=[req_input],
                samples=[[e] for e in EXAMPLES],
                label="Examples",
            )
            generate_btn = gr.Button("Generate Policy", variant="primary", size="lg")

        with gr.Column(scale=3):
            output = gr.Markdown(label="Generated Policy")

    generate_btn.click(generate_policy, inputs=[req_input], outputs=[output])

    gr.Markdown("---\n*Zero-Trust Security Concept · IHK Projektarbeit · Daniel Massa*")


if __name__ == "__main__":
    demo.launch()
