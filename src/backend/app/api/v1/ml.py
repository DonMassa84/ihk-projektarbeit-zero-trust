from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.services.ml_service import MLService
from app.core.config import settings

router = APIRouter(prefix="/ml", tags=["Machine Learning"])
ml_service = MLService()

class AnomalyRequest(BaseModel):
    event_type: str
    user_id: int
    resource: str
    details: Optional[str] = None

class AnomalyResponse(BaseModel):
    is_anomaly: bool
    score: float
    reason: Optional[str] = None

class PolicyRequest(BaseModel):
    context: str

class PolicyResponse(BaseModel):
    policy: str
    source: str

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: List[float]
    dimension: int

class SearchRequest(BaseModel):
    query: str
    corpus: List[str]
    top_k: int = 3

class SearchResponse(BaseModel):
    results: List[dict]

@router.post("/anomaly", response_model=AnomalyResponse)
async def detect_anomaly(body: AnomalyRequest):
    audit_entry = {
        "action": body.event_type,
        "user": str(body.user_id),
        "resource": body.resource,
        "result": "success",
    }
    score = await ml_service.detect_anomaly(audit_entry)
    is_anomaly = score > 0.5
    return AnomalyResponse(
        is_anomaly=is_anomaly,
        score=score,
        reason="Unusual access pattern detected" if is_anomaly else None,
    )

@router.post("/policy", response_model=PolicyResponse)
async def generate_policy(body: PolicyRequest):
    result = await ml_service.generate_policy(body.context)
    if "package" in result:
        source = "ml-model"
    else:
        source = "template"
    return PolicyResponse(policy=result, source=source)

@router.post("/embed", response_model=EmbedResponse)
async def create_embedding(body: EmbedRequest):
    embedding = await ml_service.create_embedding(body.text)
    return EmbedResponse(embedding=embedding, dimension=len(embedding))

@router.post("/search", response_model=SearchResponse)
async def semantic_search(body: SearchRequest):
    documents = [{"text": t} for t in body.corpus]
    results = await ml_service.semantic_search(body.query, documents, top_k=body.top_k)
    return SearchResponse(results=results)
