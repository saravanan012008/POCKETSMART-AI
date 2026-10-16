import os
os.environ['DATABASE_PATH']='data/test_pocketsmart.db'
os.environ['SECRET_KEY']='test-secret'
from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_health():
    r=client.get('/health'); assert r.status_code==200; assert r.json()['status']=='ok'

def test_register_login_and_history():
    email='test@example.com'
    # unique-ish cleanup is not necessary for a fresh test DB
    r=client.post('/api/register',json={'name':'Test User','email':email,'password':'password123'})
    assert r.status_code==200
    assert r.json()['user']['email']==email
    r=client.get('/api/session-info'); assert r.json()['logged_in'] is True
    r=client.post('/generate-home',json={'budget':50000,'room_type':'Living Room','style':'Modern','items':'lights, fan','notes':''})
    assert r.status_code==200
    assert r.json()['budget']==50000
    r=client.get('/api/history'); assert r.status_code==200; assert len(r.json()['items'])>=1
