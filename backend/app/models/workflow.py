from sqlalchemy import Column, Integer, String, Float, Index
from backend.app.db.database import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    # Core identity
    workflow_name = Column(String, nullable=False, index=True)
    platform = Column(String, nullable=False, index=True)      # youtube / discourse / etc
    source_id = Column(String, nullable=False, index=True)     # videoId, topicId
    country = Column(String, nullable=False, index=True)

    # Popularity metrics
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)

    like_to_view_ratio = Column(Float, default=0.0)
    comment_to_view_ratio = Column(Float, default=0.0)

    # Final computed ranking score
    popularity_score = Column(Float, default=0.0, index=True)

    __table_args__ = (
        Index(
            "uq_workflow_source",
            "platform",
            "source_id",
            "country",
            unique=True
        ),
    )