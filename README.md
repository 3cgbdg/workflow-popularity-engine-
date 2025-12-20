Workflow Popularity Engine

A production-ready backend system that tracks and ranks popular n8n workflows across multiple platforms (YouTube, community forums, and search trends) using real, verifiable popularity signals.

This project is designed to be API-first, automatable, and evidence-driven, suitable for immediate deployment.

⸻

🎯 Problem Statement

Discovering which n8n workflows are actually popular is difficult because data is scattered across:
	•	YouTube tutorials
	•	Community forum discussions
	•	Search trends

This system aggregates those signals into a single normalized database and exposes them via a REST API.

⸻

🧠 Core Features

✅ Implemented
	•	FastAPI backend with REST endpoints
	•	PostgreSQL database with normalized schema
	•	YouTube ingestion pipeline
	•	Fetches workflow-related videos
	•	Stores views, likes, comments
	•	Calculates engagement ratios
	•	Deduplicates using (platform, source_id, country)
	•	Idempotent ingestion
	•	Re-running ingestion updates metrics instead of inserting duplicates
	•	API endpoints
	•	List workflows
	•	Filter by platform and country
	•	Environment-safe secrets handling
	•	API keys stored in .env
	•	Clean Git history & modular architecture

🚧 In Progress / Planned
	•	n8n Forum (Discourse) ingestion
	•	Google Trends ingestion
	•	Cron-based automation
	•	Pagination & ranking endpoints
	•	Expanded documentation

⸻

🏗️ Architecture Overview

workflow-popularity-engine/
│
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── db/           # Database session & utilities
│   │   ├── models/       # SQLAlchemy models
│   │   └── main.py       # FastAPI entrypoint
│
├── ingestion/
│   ├── youtube_ingest.py # YouTube ingestion pipeline
│   ├── forum_ingest.py   # (planned) Discourse ingestion
│   └── trends_ingest.py  # (planned) Google Trends ingestion
│
├── cron/
│   └── crontab.txt       # Scheduled ingestion jobs
│
├── docs/
│   └── architecture.md  # Design notes
│
├── .env                 # Environment variables (not committed)
├── README.md
└── .gitignore


⸻

🗄️ Database Schema (Workflows)

Each workflow entry stores evidence-backed popularity metrics.

Field	Description
workflow_name	Workflow title or keyword
platform	youtube, forum, or google
source_id	Platform-specific identifier
country	Country code (US / IN)
views	View count
likes	Like/upvote count
comments	Comment/reply count
like_to_view_ratio	Engagement metric
comment_to_view_ratio	Engagement metric

Uniqueness enforced on:
(platform, source_id, country)

⸻

🚀 Getting Started (Local Setup)

1. Clone the repository

git clone https://github.com/Dhyan011/workflow-popularity-engine-.git
cd workflow-popularity-engine-

2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r backend/requirements.txt

4. Set environment variables

Create a .env file:

DATABASE_URL=postgresql://localhost/workflow_popularity
YOUTUBE_API_KEY=your_api_key_here

5. Start the API

uvicorn backend.app.main:app --reload

API available at:
👉 http://127.0.0.1:8000
👉 Swagger UI: http://127.0.0.1:8000/docs

⸻

📡 YouTube Ingestion

Run manually:

python -m ingestion.youtube_ingest

What it does:
	•	Searches for n8n workflow videos
	•	Fetches statistics
	•	Inserts or updates records
	•	Ensures no duplicates

⸻

🔄 Automation (Cron – Planned)

Example cron job:

0 2 * * * python -m ingestion.youtube_ingest

This enables fully automated daily updates.

⸻

📊 API Example Response

{
  "workflow_name": "Google Sheets → Slack Automation",
  "platform": "youtube",
  "country": "US",
  "views": 12500,
  "likes": 630,
  "comments": 88,
  "like_to_view_ratio": 0.05,
  "comment_to_view_ratio": 0.007
}


⸻

🧪 Current Project Status

Component	Status
Backend API	✅ Complete
Database schema	✅ Complete
YouTube ingestion	✅ Complete
Deduplication	✅ Complete
Forum ingestion	🚧 Pending
Google Trends ingestion	🚧 Pending
Cron automation	🚧 Pending
Documentation	🚧 In progress


⸻

🧩 Why This Project Matters

This is not a demo app.

It demonstrates:
	•	Real API integration
	•	Data engineering fundamentals
	•	Backend system design
	•	Production-ready thinking
	•	Automation mindset

⸻

📌 Next Steps
	•	Implement Discourse (n8n forum) ingestion
	•	Add Google Trends data
	•	Enable cron scheduling
	•	Add ranking & pagination endpoints
	•	Finalize documentation

⸻

📄 License

MIT

⸻


Once this README is live, your repo will look like a serious backend/data engineering project, not a student experiment.

When you’re ready, we’ll attack Discourse ingestion next.
