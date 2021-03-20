#!/bin/sh

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
python3 app.py
# uvicorn src:app --host 0.0.0.0