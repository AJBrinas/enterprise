from pydantic import BaseModel, EmailStr  # Input Validation
from typing import List, Optional
from datetime import datetime
from pydantic.types import conint


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    password: str
