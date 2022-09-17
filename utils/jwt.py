from typing import Optional
import jwt
import os
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from db.models import User
from cruds.users import get_user_by_email,generate_password_hash
from sqlalchemy.orm.session import Session

SECRET = os.environ.get('SECRET', 'jwt_secret')

def generate_token(db: Session, email:str, password: str) -> str:
    user:User = get_user_by_email(db,email)
    password_hash = generate_password_hash(password)
    if user.password_hash != password_hash:
        raise HTTPException(status_code=401, detail='authentication failed')
    
    exp_datetime = datetime.now() + timedelta(10)
    jwt_payload = {
        "exp": exp_datetime.timestamp(),
        "user_id": user.user_id
    }

    encode_jwt = jwt.encode(jwt_payload,SECRET,algorithm='HS256')

    return encode_jwt

def decode_token(token: str) -> str:
    user_dict = jwt.decode(token, SECRET, algorithms=['HS256'])
    user_id = user_dict["user_id"]
    return user_id

def get_current_user(jwt_token: str = Header(None)) -> Optional[str]:
    print('authorization: ', jwt_token)
    if jwt_token.find("Bearer ") != 0:
        raise HTTPException(status_code=400, detail="jwt_token is invarid")
    try: 
        token = jwt_token.split(' ')[1]
        user_id = decode_token(token)
        return user_id
    except:
        return None
