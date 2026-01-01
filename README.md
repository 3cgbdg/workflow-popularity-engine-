Workflow Popularity Engine

Overview
Workflow Popularity Engine is a production-ready backend service that tracks and ranks popular n8n workflows across multiple platforms using real, verifiable popularity signals.

The system aggregates engagement data from sources such as YouTube, community forums, and search trends, normalizes it into a structured database, and exposes it through a clean, API-first interface suitable for automation and deployment.

This project is designed with data integrity, idempotency, and extensibility as first-class concerns.

Problem Statement
Identifying genuinely popular n8n workflows is difficult because relevant signals are fragmented across platforms such as tutorial videos on YouTube, discussions on community forums, and search interest over time. There is no unified, evidence-based view of workflow popularity.

Workflow Popularity Engine solves this by ingesting platform-specific signals, normalizing them, and making them accessible via a consistent REST API.

Key Capabilities
API-first backend built with FastAPI.
Normalized PostgreSQL data model.
Evidence-driven popularity metrics.
Idempotent ingestion pipelines.
Safe re-ingestion without duplication.
Designed for automation via scheduled jobs.

Implemented Features
REST API for querying workflow popularity.
PostgreSQL database with enforced uniqueness constraints.
YouTube ingestion pipeline that fetches workflow-related videos, stores views, likes, and comments, and computes engagement ratios.
Deduplication using (platform, source_id, country).
Idempotent updates on repeated ingestion runs.
Environment-safe secret management using .env.
Modular and maintainable codebase with clean Git history.

Planned Features
n8n forum ingestion using the Discourse API.
Google Trends ingestion.
Automated ingestion using cron jobs.
Ranking and pagination endpoints.
Expanded API documentation.

Data Model
Each workflow record stores evidence-backed popularity metrics including workflow name, platform, source identifier, country, views, likes, comments, like-to-view ratio, and comment-to-view ratio.

Uniqueness is enforced on the combination of platform, source_id, and country to guarantee consistency across ingestion runs.

Local Setup
Clone the repository using git clone https://github.com/Dhyan011/workflow-popularity-engine-.git and navigate into the project directory.

Create and activate a virtual environment using python3 -m venv .venv followed by source .venv/bin/activate.

Install dependencies with pip install -r backend/requirements.txt.

Create a .env file and set DATABASE_URL and YOUTUBE_API_KEY values.

Start the API server using uvicorn backend.app.main:app –reload.

The API will be available at http://127.0.0.1:8000 with interactive documentation at http://127.0.0.1:8000/docs.

YouTube Ingestion
Run the ingestion pipeline manually using python -m ingestion.youtube_ingest.

The ingestion process searches for n8n workflow content, fetches engagement metrics, inserts new records or updates existing ones, and prevents duplicates through enforced constraints.

Automation
Scheduled ingestion can be enabled using cron. An example daily job would execute python -m ingestion.youtube_ingest at a fixed time.

Example API Response
A typical response includes the workflow name, platform, country, views, likes, comments, and computed engagement ratios, providing a normalized and evidence-backed view of workflow popularity.

Project Status
Backend API is complete.
Database schema is complete.
YouTube ingestion is complete.
Deduplication logic is complete.
Forum ingestion is in progress.
Google Trends ingestion is planned.
Automation is planned.
Documentation is in progress.
