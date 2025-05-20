#!/bin/bash

# Run FastAPI backend
uvicorn app.api:app --reload &

# Run Streamlit frontend
streamlit run app/main.py
