from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes.page_routes import router as pages
from .routes.auth_routes import router as auth
from .routes.planner_routes import router as planners

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db(); yield

init_db()
app=FastAPI(title='PocketSmart AI',version='1.0.0',lifespan=lifespan)
app.add_middleware(SessionMiddleware,secret_key=settings.secret_key,max_age=60*60*24*7 ,same_site='lax')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.mount('/static',StaticFiles(directory='app/static'),name='static')
app.include_router(pages); app.include_router(auth); app.include_router(planners)

@app.get('/health')
def health(): return {'status':'ok','app':'PocketSmart AI','model':settings.gemini_model,'gemini_configured':bool(settings.gemini_api_key)}

@app.get('/startup')
def startup(): return {'status':'ready','database':'sqlite','gemini_configured':bool(settings.gemini_api_key),'model':settings.gemini_model}

if __name__=='__main__':
    import uvicorn
    uvicorn.run('app.main:app',host='127.0.0.1',port=8000,reload=True)
