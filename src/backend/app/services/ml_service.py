from typing import Optional, Dict, Any, List
import numpy as np
from app.core.config import settings
import structlog

logger = structlog.get_logger()


class MLService:
    def __init__(self):
        self.anomaly_model = None
        self.policy_model = None
        self.embedding_model = None
        self._initialized = False

    async def initialize(self):
        if self._initialized:
            return
        try:
            self.anomaly_model = await self._load_anomaly_model()
            self.policy_model = await self._load_policy_model()
            self.embedding_model = await self._load_embedding_model()
            self._initialized = True
            logger.info("ML models initialized successfully")
        except Exception as e:
            logger.warning("ML models not available, running in fallback mode", error=str(e))

    async def _load_anomaly_model(self):
        try:
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
            model_path = settings.ML_ANOMALY_MODEL_PATH
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForSequenceClassification.from_pretrained(model_path)
            return {"model": model, "tokenizer": tokenizer, "loaded": True}
        except Exception as e:
            logger.info("Anomaly model not loaded, using rule-based fallback", error=str(e))
            return None

    async def _load_policy_model(self):
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            model_path = settings.ML_POLICY_MODEL_PATH
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
            return {"model": model, "tokenizer": tokenizer, "loaded": True}
        except Exception as e:
            logger.info("Policy generator model not loaded", error=str(e))
            return None

    async def _load_embedding_model(self):
        try:
            from sentence_transformers import SentenceTransformer
            model = SentenceTransformer(settings.ML_EMBEDDING_MODEL)
            return {"model": model, "loaded": True}
        except Exception as e:
            logger.info("Embedding model not loaded", error=str(e))
            return None

    async def detect_anomaly(self, audit_entry: dict) -> float:
        if self.anomaly_model and self.anomaly_model.get("loaded"):
            try:
                model = self.anomaly_model["model"]
                tokenizer = self.anomaly_model["tokenizer"]
                text = f"{audit_entry.get('action', '')} {audit_entry.get('resource_type', '')} {audit_entry.get('result', '')}"
                inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
                outputs = model(**inputs)
                score = float(torch.sigmoid(outputs.logits).max().item())
                return round(score, 4)
            except Exception as e:
                logger.debug("ML anomaly detection failed, using fallback", error=str(e))

        return self._rule_based_anomaly_score(audit_entry)

    def _rule_based_anomaly_score(self, audit_entry: dict) -> float:
        score = 0.0
        flagged_actions = {"ROLE_ESCALATION", "MASS_REVOKE", "ADMIN_IMPERSONATE", "UNAUTHORIZED_ACCESS"}
        sensitive_resources = {"users", "roles", "policies", "github-token"}

        action = audit_entry.get("action", "")
        resource = audit_entry.get("resource_type", "")
        result = audit_entry.get("result", "")

        if action in flagged_actions:
            score += 0.4
        if resource in sensitive_resources:
            score += 0.3
        if result == "failure":
            score += 0.2
        if audit_entry.get("details", {}).get("privilege_escalation"):
            score += 0.3

        if "night" in audit_entry.get("details", {}).get("time", ""):
            score += 0.2
        if audit_entry.get("ip_address", "").startswith("10."):
            score += 0.1
        if audit_entry.get("details", {}).get("retry_count", 0) > 3:
            score += 0.2

        return round(min(score, 1.0), 4)

    async def generate_policy(self, requirement: str) -> str:
        if self.policy_model and self.policy_model.get("loaded"):
            try:
                model = self.policy_model["model"]
                tokenizer = self.policy_model["tokenizer"]
                prompt = f"""Generate an OPA Rego policy for: {requirement}

package zero_trust.policies

default allow = false

"""
                inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=512,
                    temperature=0.3,
                    do_sample=False,
                )
                generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
                return generated[len(prompt):]
            except Exception as e:
                logger.debug("ML policy generation failed, using template", error=str(e))

        return self._template_policy(requirement)

    def _template_policy(self, requirement: str) -> str:
        req_lower = requirement.lower()
        if "admin" in req_lower or "administrator" in req_lower:
            return f"""package zero_trust.policies.admin

default allow = false

allow {{
    input.user.role == "admin"
    input.user.mfa_enabled == true
    input.request.ip in trusted_networks
}}

trusted_networks = {{"10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"}}"""
        
        elif "read" in req_lower and "only" in req_lower:
            return f"""package zero_trust.policies.readonly

default allow = false

allow {{
    input.user.role == "viewer"
    input.request.method == "GET"
}}"""

        return f"""package zero_trust.policies.custom

default allow = false

allow {{
    input.user.role == "member"
    input.user.department == "{requirement.split('for ')[-1] if 'for ' in requirement else 'engineering'}"
    input.request.resource == "repository"
}}"""

    async def create_embedding(self, text: str) -> List[float]:
        if self.embedding_model and self.embedding_model.get("loaded"):
            try:
                model = self.embedding_model["model"]
                embedding = model.encode(text, normalize_embeddings=True)
                return embedding.tolist()
            except Exception as e:
                logger.debug("Embedding creation failed", error=str(e))
        return [0.0] * 384

    async def semantic_search(
        self,
        query: str,
        documents: List[Dict[str, Any]],
        top_k: int = 5,
        text_field: str = "text",
    ) -> List[dict]:
        if not documents:
            return []

        query_embedding = await self.create_embedding(query)
        if all(v == 0.0 for v in query_embedding):
            return documents[:top_k]

        doc_embeddings = []
        for doc in documents:
            text = doc.get(text_field, "")
            emb = await self.create_embedding(text)
            doc_embeddings.append(emb)

        query_vec = np.array(query_embedding)
        doc_vecs = np.array(doc_embeddings)
        scores = np.dot(doc_vecs, query_vec)

        top_indices = np.argsort(scores)[-top_k:][::-1]
        results = []
        for idx in top_indices:
            result = dict(documents[idx])
            result["similarity_score"] = float(scores[idx])
            results.append(result)

        return results