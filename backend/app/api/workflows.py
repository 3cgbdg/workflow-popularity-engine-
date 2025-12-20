from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.db.deps import get_db
from backend.app.models.workflow import Workflow

router = APIRouter(prefix="/workflows", tags=["workflows"])

@router.get("/")
def list_workflows(
    platform: str | None = Query(None),
    country: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Workflow)

    if platform:
        query = query.filter(Workflow.platform == platform)

    if country:
        query = query.filter(Workflow.country == country)

    return query.all()
