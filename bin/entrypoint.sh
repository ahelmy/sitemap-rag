#!/bin/bash
if [ -f /app/requirements.txt ]; then
    pip install -r /app/requirements.extra.txt
fi

gunicorn -w 4 -b "0.0.0.0:8000" --preload main:app