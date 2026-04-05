from fastapi import FastAPI, HTTPException
from app.models import AuditRequest, AuditResponse
from app.scraper import scrape_page
from app.schema_generator import generate_schema
from app.utils import calculate_score

app = FastAPI(title="Mini GEO Audit API")

@app.post("/audit", response_model=AuditResponse)
def audit(request: AuditRequest):
    try:
        data = scrape_page(str(request.url))

        schema = generate_schema(
            data["title"],
            data["headings"],
            str(request.url)
        )

        score = calculate_score(
            data["title"],
            data["meta_description"],
            data["headings"],
            data["image"]
        )

        return AuditResponse(
            title=data["title"],
            meta_description=data["meta_description"],
            headings=data["headings"],
            image=data["image"],
            recommended_schema=schema,
            citation_readiness_score=score
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))