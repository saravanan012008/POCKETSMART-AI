@echo off
if not exist .venv py -3.14 -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if not exist .env copy .env.example .env
python -m uvicorn app.main:app --reload
