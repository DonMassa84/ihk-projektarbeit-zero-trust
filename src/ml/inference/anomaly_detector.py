import os, json
import numpy as np
from typing import Dict, Any, List, Optional

MODEL_PATH = os.path.expanduser("~/.cache/zt-models/anomaly-detector")
RULE_BASED_FALLBACK = True

_anomaly_model = None
_anomaly_tokenizer = None


def load_model():
    global _anomaly_model, _anomaly_tokenizer
    try:
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        _anomaly_tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        _anomaly_model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
        _anomaly_model.eval()
        return True
    except Exception as e:
        print(f"Anomaly model load failed: {e}")
        return False


def predict(audit_entry: Dict[str, Any]) -> Dict[str, Any]:
    if _anomaly_model is None:
        if not load_model():
            return rule_based_fallback(audit_entry)

    text = f"Action: {audit_entry.get('action', '')} | User: {audit_entry.get('user', '')} | Resource: {audit_entry.get('resource', '')} | Result: {audit_entry.get('result', 'success')}"
    inputs = _anomaly_tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    import torch
    with torch.no_grad():
        outputs = _anomaly_model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        score = float(probs[0][1].item())
    return {
        "is_anomaly": score > 0.5,
        "score": round(score, 4),
        "model": "codebert",
    }


FLAGGED_ACTIONS = {"MASS_ROLE_REVOKE", "ADMIN_IMPERSONATE", "UNAUTHORIZED_ACCESS", "PRIVILEGE_ESCALATION", "BRUTE_FORCE_LOGIN", "DATA_EXFILTRATION", "ROLE_ESCALATION", "SECRET_LEAKAGE", "SUSPICIOUS_API_CALL"}
SENSITIVE_RESOURCES = {"admin/panel", "super-admin-role", "all-roles", "production/secrets", "admin", "root"}
SUSPICIOUS_USERS = {"unknown_user", "attacker_001", "suspicious_conn", "root_external", "unknown", "attacker"}


def rule_based_fallback(entry: Dict[str, Any]) -> Dict[str, Any]:
    score = 0.0
    reasons = []
    action = entry.get("action", "")
    user = entry.get("user", "")
    resource = entry.get("resource", "")
    result = entry.get("result", "success")

    if action in FLAGGED_ACTIONS:
        score += 0.6; reasons.append(f"high-risk action: {action}")
    if resource in SENSITIVE_RESOURCES:
        score += 0.3; reasons.append(f"sensitive resource: {resource}")
    if user in SUSPICIOUS_USERS:
        score += 0.3; reasons.append(f"suspicious user: {user}")
    if result == "failure":
        score += 0.15; reasons.append("failed operation")
    score = min(score, 1.0)

    return {"is_anomaly": score > 0.5, "score": round(score, 4), "reasons": reasons, "model": "rule-based"}


def batch_predict(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [predict(e) for e in entries]
