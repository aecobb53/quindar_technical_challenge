#!/bin/bash

cd quindar_technical_challenge/

# For development with auto-reload
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000

# For production
# uvicorn main:app --workers 2 --host 0.0.0.0 --port 8000
