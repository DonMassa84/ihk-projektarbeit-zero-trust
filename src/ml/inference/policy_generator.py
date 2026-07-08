import os
from typing import Dict, Any

MODEL_PATH = os.path.expanduser("~/.cache/zt-models/policy-generator")
_policy_model = None
_policy_tokenizer = None


def load_model():
    global _policy_model, _policy_tokenizer
    try:
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        import torch
        _policy_tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _policy_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)
        _policy_model.eval()
        return True
    except Exception as e:
        print(f"Policy model load failed: {e}")
        return False


def generate(requirement: str) -> Dict[str, Any]:
    if _policy_model is None:
        if not load_model():
            return {"policy": _template_policy(requirement), "model": "template"}

    try:
        import torch

        prompt = f"Generate OPA Rego policy for: {requirement}"
        inputs = _policy_tokenizer(prompt, return_tensors="pt", truncation=True, max_length=64)
        device = next(_policy_model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = _policy_model.generate(
                **inputs,
                max_new_tokens=128,
                do_sample=True,
                temperature=0.3,
            )
        generated = _policy_tokenizer.decode(outputs[0], skip_special_tokens=True)
        if generated and "ALLOW" in generated or "DENY" in generated:
            policy = _format_as_rego(generated, requirement)
            return {"policy": policy, "model": "flan-t5-small"}
    except Exception as e:
        print(f"Policy generation failed: {e}")

    return {"policy": _template_policy(requirement), "model": "template"}


def _format_as_rego(rule: str, requirement: str) -> str:
    parts = rule.split()
    effect = "allow"
    resource = "resource"
    access = "access"
    role = "user"

    if len(parts) >= 2:
        if parts[0] == "ALLOW":
            effect = "allow"
        elif parts[0] == "DENY":
            effect = "deny"
        if len(parts) >= 2:
            resource = parts[1].replace("/*", "/*")
        if "READ" in parts:
            access = "READ"
        elif "WRITE" in parts:
            access = "WRITE"
        elif "*" in parts:
            access = "*"
        if "role=" in rule:
            role = rule.split("role=")[-1].split(")")[0].strip()

    package_name = requirement.lower().replace(" ", "_").replace("-", "_")[:20]
    if effect == "allow" and resource == "*":
        return f"""package zero_trust.policies.{package_name}

default allow = false

allow {{
    input.user.role == "{role}"
}}"""
    elif effect == "deny":
        return f"""package zero_trust.policies.{package_name}

default allow = true

deny {{
    input.user.role == "{role}"
}}"""
    else:
        return f"""package zero_trust.policies.{package_name}

default allow = false

allow {{
    input.user.role == "{role}"
    input.request.resource == "{resource}"
    input.request.method == "{access}"
}}"""


def _template_policy(requirement: str) -> str:
    req_lower = requirement.lower()
    if "admin" in req_lower:
        return f"""package zero_trust.policies.admin

default allow = false

allow {{
    input.user.role == "admin"
    input.user.mfa_enabled == true
}}

trusted_networks = {{"10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"}}"""
    elif "read" in req_lower and "only" in req_lower:
        return f"""package zero_trust.policies.readonly

default allow = false

allow {{
    input.user.role == "viewer"
    input.request.method == "GET"
}}"""
    else:
        return f"""package zero_trust.policies.custom

default allow = false

allow {{
    input.user.role == "member"
    input.request.resource == "repository"
}}"""
