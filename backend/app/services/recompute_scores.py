from backend.app.db.database import SessionLocal
from backend.app.services.scoring import recompute_all_scores


def main():
    db = SessionLocal()
    recompute_all_scores(db)
    db.close()


if __name__ == "__main__":
    main()
