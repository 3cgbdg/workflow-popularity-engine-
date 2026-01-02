import requests
from backend.app.logger import logger
from backend.app.db.database import SessionLocal
from backend.app.models.workflow import Workflow
from fastapi import HTTPException
from os import getenv

HTTPException


def fetch_latest_topics(page: int = 0):
    """
    Fetch latest topics from Discourse
    """

    url = f"{DISCOURSE_BASE_URL}/latest.json?page={page}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def ingest():
    logger.info("Starting Discourse ingestion")

    db = SessionLocal()

    data = fetch_latest_topics()
    topics = data.get("topic_list", {}).get("topics", [])

    logger.info(f"Fetched {len(topics)} topics")
    try:
        for topic in topics:
            topic_id = str(topic["id"])

            # Deduplication check
            exists = (
                db.query(Workflow)
                .filter(
                    Workflow.platform == "discourse",
                    Workflow.source_id == topic_id,
                    Workflow.country == "global",
                )
                .first()
            )

            if exists:
                logger.info("Skipping existing topic:", topic["title"])
                continue

            views = topic.get("views", 0)
            likes = topic.get("like_count", 0)
            comments = max(topic.get("posts_count", 1) - 1, 0)
            workflow_name = topic.get("title", "Unknown")
            workflow = Workflow(
                workflow_name=workflow_name,
                platform="discourse",
                source_id=topic_id,
                country="global",
                views=views,
                likes=likes,
                comments=comments,
                like_to_view_ratio=(likes / views) if views else 0,
                comment_to_view_ratio=(comments / views) if views else 0,
            )

            logger.info(
                f"Inserting: {workflow.workflow_name}", extra={"topic_id": topic_id}
            )
            db.add(workflow)

        db.commit()
        db.close()
    except Exception:
        logger.error("Failed to upload data into db", exc_info=True)
        raise h

    logger.info("Discourse ingestion completed")


if __name__ == "__main__":
    ingest()
