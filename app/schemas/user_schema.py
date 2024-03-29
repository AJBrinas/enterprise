from pydantic import BaseModel, EmailStr  # Input Validation
from typing import List, Optional
from datetime import datetime
from pydantic.types import conint


class UserValidate(BaseModel):
    id: int
    email: EmailStr
    password: str


class UserInput(BaseModel):
    email: EmailStr
    password: str


class Login(BaseModel):
    email: EmailStr
    password: str


class Create(UserInput):
    pass


# Authentication
class Token(BaseModel):
    access_token: str
    token_Type: str


class TokenData(BaseModel):
    id: Optional[str] = None