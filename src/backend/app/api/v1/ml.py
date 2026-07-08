from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

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
    score = 0.15
    is_anomaly = score > 0.7
    return AnomalyResponse(
        is_anomaly=is_anomaly,
        score=score,
        reason=None if not is_anomaly else "Unusual access pattern detected",
    )

@router.post("/policy", response_model=PolicyResponse)
async def generate_policy(body: PolicyRequest):
    return PolicyResponse(
        policy=f"policy_allow_{body.context[:20].replace(' ', '_')}",
        source="template",
    )

@router.post("/embed", response_model=EmbedResponse)
async def create_embedding(body: EmbedRequest):
    mock_embedding = [0.1] * 384
    return EmbedResponse(embedding=mock_embedding, dimension=384)

@router.post("/search", response_model=SearchResponse)
async def semantic_search(body: SearchRequest):
    results = [
        {"text": t, "score": 0.95 - i * 0.1}
        for i, t in enumerate(body.corpus[:body.top_k])
    ]
    return SearchResponse(results=results)
