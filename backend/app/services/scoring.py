from sqlalchemy.orm import Session
from backend.app.models.workflow import Workflow


def recompute_all_scores(db: Session):
    workflows = db.query(Workflow).all()
    print(f"Recomputing scores for {len(workflows)} workflows")

    for wf in workflows:
        wf.popularity_score = (
            wf.views
            + (wf.likes * 2)
            + (wf.comments * 3)
        )

    db.commit()
    print("Popularity scores updated successfully")