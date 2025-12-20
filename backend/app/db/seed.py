from backend.app.db.database import SessionLocal
from backend.app.models.workflow import Workflow

db = SessionLocal()

dummy_data = [
    Workflow(
        workflow_name="Google Sheets → Slack Automation",
        platform="youtube",
        country="US",
        views=12500,
        likes=630,
        comments=88,
        like_to_view_ratio=630/12500,
        comment_to_view_ratio=88/12500
    ),
    Workflow(
        workflow_name="WhatsApp Reminder Workflow",
        platform="forum",
        country="IN",
        views=2500,
        likes=37,
        comments=48,
        like_to_view_ratio=37/2500,
        comment_to_view_ratio=48/2500
    ),
    Workflow(
        workflow_name="n8n Slack Integration",
        platform="google",
        country="US",
        views=3600,
        likes=0,
        comments=0,
        like_to_view_ratio=0,
        comment_to_view_ratio=0
    )
]

db.add_all(dummy_data)
db.commit()
db.close()

print("Dummy workflows inserted")