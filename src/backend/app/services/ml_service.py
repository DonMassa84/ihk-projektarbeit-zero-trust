from typing import Optional, Dict, Any, List
import numpy as np
import sys, os, torch
from app.core.config import settings
import structlog

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "ml", "inference"))

logger = structlog.get_logger()


class MLService:
    def __init__(self):
        self._initialized = False
        self.anomaly_detector = None
        self.policy_generator = None
        self.embedding_model_obj = None

    async def initialize(self):
        if self._initialized:
            return
        try:
            from anomaly_detector import predict as ad_predict, load_model as ad_load
            if ad_load():
                self.anomaly_detector = ad_predict
                logger.info("Anomaly detector loaded")
            else:
                logger.warning("Anomaly detector not available, will use rule-based fallback")
                self.anomaly_detector = None
        except Exception as e:
            logger.warning("Anomaly detector import failed", error=str(e))
            self.anomaly_detector = None

        try:
            from policy_generator import generate as pg_generate, load_model as pg_load
            if pg_load():
                self.policy_generator = pg_generate
                logger.info("Policy generator loaded")
            else:
                logger.warning("Policy generator not available, will use template fallback")
                self.policy_generator = None
        except Exception as e:
            logger.warning("Policy generator import failed", error=str(e))
            self.policy_generator = None

        try:
            from sentence_transformers import SentenceTransformer
            self.embedding_model_obj = SentenceTransformer(settings.ML_EMBEDDING_MODEL)
            logger.info("Embedding model loaded")
        except Exception as e:
            logger.warning("Embedding model not loaded", error=str(e))
            self.embedding_model_obj = None

        self._initialized = True

    async def detect_anomaly(self, audit_entry: dict) -> float:
        if self.anomaly_detector:
            try:
                result = self.anomaly_detector(audit_entry)
                return result.get("score", 0.0)
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
        if self.policy_generator:
            try:
                result = self.policy_generator(requirement)
                if "package" in result.get("policy", ""):
                    return result["policy"]
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
        if self.embedding_model_obj:
            try:
                embedding = self.embedding_model_obj.encode(text, normalize_embeddings=True)
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
