#!/bin/sh

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
python src/main.py
# uvicorn src:app --host 0.0.0.0