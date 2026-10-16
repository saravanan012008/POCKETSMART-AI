import json
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Form
from ..auth import current_user, bearer_user
from ..database import save_recommendation, get_history, get_recommendation
from ..models.schemas import HomeRequest, PartyRequest
from ..services.gemini_utils import generate_text, generate_jewelry

router=APIRouter()

def require_user(request):
    return current_user(request) or bearer_user(request)

def save(user, planner, data, result):
    return save_recommendation(user['id'],planner,float(data['budget']),data,result)

@router.post('/generate-home')
def generate_home(data:HomeRequest, request:Request):
    user=require_user(request)
    if not user: raise HTTPException(401,'Please log in to use the planner.')
    payload=data.model_dump(); result=generate_text('home',payload); rid=save(user,'home',payload,result); result['id']=rid; return result

@router.post('/generate-party')
def generate_party(data:PartyRequest, request:Request):
    user=require_user(request)
    if not user: raise HTTPException(401,'Please log in to use the planner.')
    payload=data.model_dump(); result=generate_text('party',payload); rid=save(user,'party',payload,result); result['id']=rid; return result

@router.post('/generate-jewelry')
async def generate_jewelry_route(request:Request, budget:float=Form(...), occasion:str=Form(...), style:str=Form('Elegant'), metal:str=Form('Any'), notes:str=Form(''), outfit:UploadFile|None=File(None)):
    user=require_user(request)
    if not user: raise HTTPException(401,'Please log in to use the planner.')
    if budget<=0: raise HTTPException(422,'Budget must be greater than zero.')
    image_bytes=None; mime=None
    if outfit:
        if not outfit.content_type or not outfit.content_type.startswith('image/'): raise HTTPException(400,'Outfit must be an image file.')
        image_bytes=await outfit.read()
        if len(image_bytes)>5*1024*1024: raise HTTPException(413,'Image must be 5 MB or smaller.')
        mime=outfit.content_type
    payload={'budget':budget,'occasion':occasion,'style':style,'metal':metal,'notes':notes}
    result=generate_jewelry(payload,image_bytes,mime); rid=save(user,'jewelry',payload,result); result['id']=rid; return result

@router.get('/history')
@router.get('/api/history')
def history(request:Request):
    user=require_user(request)
    if not user: raise HTTPException(401,'Authentication required.')
    rows=get_history(user['id'])
    for r in rows: r['input_json']=json.loads(r['input_json']); r['result_json']=json.loads(r['result_json'])
    return {'items':rows}

@router.get('/recommendations-details/{rec_id}')
def details(rec_id:int, request:Request):
    user=require_user(request)
    if not user: raise HTTPException(401,'Authentication required.')
    row=get_recommendation(user['id'],rec_id)
    if not row: raise HTTPException(404,'Recommendation not found.')
    row['input_json']=json.loads(row['input_json']); row['result_json']=json.loads(row['result_json']); return row
