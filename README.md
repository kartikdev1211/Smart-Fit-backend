# Smart Fit Backend

## Overview
Production-ready backend for Smart Fit, built with Python.

## Setup
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your environment variables.

## Running Locally
```bash
uvicorn app.main:app --reload
```

## Running in Production
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Testing
```bash
pytest
```

## Linting
```bash
flake8
black --check .
isort --check-only .
```

## API Documentation
- See `/docs` endpoint when running the server.

## Environment Variables
See `.env.example` for required variables. 