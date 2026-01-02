from pydantic import BaseModel


class PopularityMetrics(BaseModel):
    views: int
    likes: int
    comments: int
    like_to_view_ratio: float
    comment_to_view_ratio: float
    popularity_score: float


class WorkflowOut(BaseModel):
    workflow: str
    platform: str
    country: str
    popularity_metrics: PopularityMetrics

    class Config:
        from_attributes = True