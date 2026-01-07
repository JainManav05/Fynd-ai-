# Quick Start Commands

## Setup
```bash
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

## Configure
1. Copy `.env.example` to `.env`
2. Add your `GEMINI_API_KEY`
3. Update `DATABASE_URL` with MySQL credentials

## Run
**Terminal 1 - Backend:**
```bash
python -m uvicorn task2.backend.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd task2/frontend
reflex run
```

## Access
- User Dashboard: http://localhost:3000
- Admin Dashboard: http://localhost:3000/admin
- API Docs: http://localhost:8000/docs
