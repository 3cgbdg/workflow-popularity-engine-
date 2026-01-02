from backend.app.db.database import SessionLocal

from ingestion.youtube_ingest import ingest as ingest_youtube
from ingestion.discourse_ingest import ingest as ingest_discourse
from ingestion.trends_ingest import ingest as ingest_trends
from backend.app.logger import logger
from backend.app.services.scoring import recompute_all_scores


def run_pipeline():
    logger.info("Starting full ingestion pipeline")

    ingest_youtube("US")
    ingest_youtube("IN")

    ingest_discourse()

    ingest_trends("US")
    ingest_trends("IN")

    db = SessionLocal()
    try:
        recompute_all_scores(db)
    finally:
        db.close()

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
