# PocketSmart AI — pocketnewai(fresh)

A complete FastAPI + Jinja2 + JavaScript Generative AI budget recommendation assistant based on the supplied PocketSmart AI documentation.

## What is included
- Home Interior Planner
- Party Budget Planner
- Jewelry Planner with optional outfit image analysis
- Registration, login, logout and JWT token endpoint
- SQLite persistence for users and recommendation history
- Session personalization
- Gemini integration through Google's current `google-genai` SDK
- Demo fallback mode when no API key is configured
- Mock/simulated marketplace links for Amazon, IKEA, Flipkart, Swiggy, Zomato and OYO, matching the documentation's mock/simulated API requirement
- Responsive professional UI
- Automated API tests

## Important model note
The supplied document names Gemini 1.5 Flash Pro / Gemini 1.5 Flash. That model family was shut down by Google in 2025, so it cannot be used for a genuinely working October 2026 application. This implementation uses the current supported `GEMINI_MODEL` value from `.env` (default: `gemini-3.8-flash`) while keeping the same planner prompts and multimodal behavior described in the document. Change the variable if your Google account supports another current model.

## VS Code setup — Windows
1. Open this folder in VS Code.
2. Install Python 3.14.7.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:
   `py -3.14 -m venv .venv`
5. Activate it:
   `.venv\\Scripts\\activate`
6. Upgrade pip:
   `python -m pip install --upgrade pip`
7. Install dependencies:
   `pip install -r requirements.txt`
8. Create `.env` from `.env.example` and add your Gemini API key.
9. Start the server:
   `python -m uvicorn app.main:app --reload`
10. Open http://127.0.0.1:8000

### Demo mode
If `GEMINI_API_KEY` is empty, the application still runs and uses safe deterministic demo recommendations. This lets you test the UI, auth, database, routing and all three planners before configuring Gemini.

## Testing
Run:
`python -m pytest -q`

Or test the health endpoint in a browser:
http://127.0.0.1:8000/health

## API endpoints
- GET `/`
- GET `/login`
- GET `/register`
- POST `/api/register`
- POST `/api/login`
- POST `/api/logout`
- POST `/api/token`
- GET `/api/session-info`
- GET `/api/session-data`
- POST `/generate-home`
- POST `/generate-party`
- POST `/generate-jewelry`
- GET `/recommendations-details/{id}`
- GET `/history`
- GET `/startup`
- GET `/health`

## Deployment
The application is ready for deployment on any Python host that supports ASGI (Render, Railway, Fly.io, a VPS, etc.).

Production checklist:
1. Set a strong `SECRET_KEY`.
2. Set `GEMINI_API_KEY` as a secret/environment variable.
3. Set `GEMINI_MODEL` to a model available to your API project.
4. Use a persistent volume for `data/pocketsmart.db`, or replace SQLite with a managed database for multi-instance production.
5. Run `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
6. Do not commit `.env`.

For Render-style hosts, the start command is:
`uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Project structure
```text
pocketnewai(fresh)/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── auth.py
│   ├── models/
│   │   └── schemas.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── planner_routes.py
│   │   └── page_routes.py
│   ├── services/
│   │   ├── gemini_utils.py
│   │   └── recommendations.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── planner.html
│   │   └── history.html
│   └── static/
│       ├── css/style.css
│       └── js/app.js
├── data/
├── tests/
│   └── test_app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
