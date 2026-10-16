from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..auth import current_user

templates=Jinja2Templates(directory='app/templates')
router=APIRouter()

@router.get('/', response_class=HTMLResponse)
def home(request: Request): return templates.TemplateResponse('index.html', {'request':request,'user':current_user(request)})
@router.get('/login', response_class=HTMLResponse)
def login(request: Request): return templates.TemplateResponse('login.html', {'request':request,'user':current_user(request)})
@router.get('/register', response_class=HTMLResponse)
def register(request: Request): return templates.TemplateResponse('register.html', {'request':request,'user':current_user(request)})
@router.get('/dashboard', response_class=HTMLResponse)
def dashboard(request: Request): return templates.TemplateResponse('dashboard.html', {'request':request,'user':current_user(request)})
@router.get('/planner/{planner}', response_class=HTMLResponse)
def planner(request: Request, planner: str):
    if planner not in {'home','party','jewelry'}: planner='home'
    return templates.TemplateResponse('planner.html', {'request':request,'user':current_user(request),'planner':planner})
@router.get('/history', response_class=HTMLResponse)
def history(request: Request): return templates.TemplateResponse('history.html', {'request':request,'user':current_user(request)})
