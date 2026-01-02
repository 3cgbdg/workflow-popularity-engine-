from backend.app.db.database import SessionLocal
from backend.app.services.scoring import recompute_all_scores
from backend.app.logger import logger
from fastapi import HTTPException
def main():
    db = SessionLocal()
    try:
        recompute_all_scores(db)
    except Exception:
        logger.error("Failed to recompute all scores",exc_info=True)
        raise HTTPException(status_code=500)
        
    finally:
        db.close()
        


if __name__ == "__main__":
    main()