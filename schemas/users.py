from pydantic import BaseModel, EmailStr

class SignUpPayload(BaseModel):
    name: str
    email: EmailStr
    password: str

class SignInPayload(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    user_id: str
    name: str
    email: EmailStr

    class Config :
        orm_mode = True


class AuthInfo(BaseModel):
    jwt: str




