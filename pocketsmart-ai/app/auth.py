import base64, hashlib, hmac, secrets
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Request
from .config import settings
from .database import get_user

ALGORITHM = 'HS256'

def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 310_000)
    return 'pbkdf2_sha256$310000$%s$%s' % (base64.b64encode(salt).decode(), base64.b64encode(digest).decode())

def verify_password(password: str, stored: str) -> bool:
    try:
        _, iterations, salt_b64, digest_b64 = stored.split('$')
        salt = base64.b64decode(salt_b64)
        digest = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, int(iterations))
        return hmac.compare_digest(digest, base64.b64decode(digest_b64))
    except Exception:
        return False

def create_access_token(user_id: int, expires_minutes=60*24):
    now = datetime.now(timezone.utc)
    return jwt.encode({'sub': str(user_id), 'iat': now, 'exp': now + timedelta(minutes=expires_minutes)}, settings.secret_key, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])

def current_user(request: Request):
    token = request.session.get('access_token')
    if not token:
        return None
    try:
        payload = decode_token(token)
        return get_user(int(payload['sub']))
    except Exception:
        request.session.pop('access_token', None)
        return None

def bearer_user(request: Request):
    auth = request.headers.get('Authorization', '')
    if not auth.lower().startswith('bearer '):
        return None
    try:
        payload = decode_token(auth.split(' ', 1)[1].strip())
        return get_user(int(payload['sub']))
    except Exception:
        return None
