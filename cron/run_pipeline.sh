#!/bin/bash

cd /Users/dhyanpatel/cyberlab/workflow-popularity-engine-
source .venv/bin/activate

python -m backend.app.jobs.run_ingestion
