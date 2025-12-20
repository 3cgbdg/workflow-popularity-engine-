from sqlalchemy.orm import Session

from backend.app.models.workflow import Workflow


def compute_popularity_score(workflow: Workflow) -> float:
    """
    Platform-agnostic popularity score.
    Works for YouTube, Discourse, etc.
    """

    views = workflow.views or 0
    likes = workflow.likes or 0
    comments = workflow.comments or 0

    # Core idea:
    # - Views = reach
    # - Likes = approval
    # - Comments = engagement (weighted higher)

    score = (
        views * 0.5 +
        likes * 2.0 +
        comments * 3.0
    )

    return round(score, 2)


def recompute_all_scores(db: Session):
    """
    Recompute popularity_score for all workflows.
    """

    workflows = db.query(Workflow).all()

    print(f"Recomputing scores for {len(workflows)} workflows")

    for wf in workflows:
        wf.popularity_score = compute_popularity_score(wf)

    db.commit()
    print("Popularity scores updated successfully")
