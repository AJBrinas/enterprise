from pydantic import BaseModel, EmailStr  # Input Validation
from typing import List, Optional
from datetime import datetime
from pydantic.types import conint


# input
class Health_Info(BaseModel):
    
