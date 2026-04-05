from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any, Optional

class AuditRequest(BaseModel):
    url: HttpUrl

class AuditResponse(BaseModel):
    title: str
    meta_description: str
    headings: List[str]
    image: Optional[str]
    recommended_schema: Dict[str, Any]
    citation_readiness_score: int