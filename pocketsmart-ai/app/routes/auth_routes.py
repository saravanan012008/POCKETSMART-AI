from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from ..models.schemas import RegisterRequest, LoginRequest
from ..database import create_user, get_user_by_email
from ..auth import hash_password, verify_password, create_access_token, current_user, bearer_user

router=APIRouter(prefix='/api')

def user_json(user): return {'id':user['id'],'name':user['name'],'email':user['email']}

@router.post('/register')
def register(data:RegisterRequest, request:Request):
    if get_user_by_email(data.email): raise HTTPException(409,'An account with this email already exists.')
    uid=create_user(data.email,data.name.strip(),hash_password(data.password))
    token=create_access_token(uid); request.session['access_token']=token
    return {'message':'Account created','user':{'id':uid,'name':data.name.strip(),'email':data.email}}

@router.post('/login')
def login(data:LoginRequest, request:Request):
    user=get_user_by_email(data.email)
    if not user or not verify_password(data.password,user['password_hash']): raise HTTPException(401,'Invalid email or password.')
    request.session['access_token']=create_access_token(user['id'])
    return {'message':'Logged in','user':user_json(user)}

@router.post('/logout')
def logout(request:Request):
    request.session.clear(); return {'message':'Logged out'}

@router.post('/token')
def token(data:LoginRequest):
    user=get_user_by_email(data.email)
    if not user or not verify_password(data.password,user['password_hash']): raise HTTPException(401,'Invalid credentials.')
    return {'access_token':create_access_token(user['id']),'token_type':'bearer'}

@router.get('/session-info')
def session_info(request:Request):
    user=current_user(request); return {'logged_in':bool(user),'user':user_json(user) if user else None}

@router.get('/session-data')
def session_data(request:Request):
    user=current_user(request) or bearer_user(request)
    if not user: raise HTTPException(401,'Authentication required.')
    return {'user':user_json(user),'session_active':True}
