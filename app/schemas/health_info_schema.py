from pydantic import BaseModel, EmailStr  # Input Validation
from typing import List, Optional
from datetime import datetime, date

from pydantic.types import conint


# Input
class Health_Info(BaseModel):
    name = str
    illness: str


# List of Vaccination
class Vaccination(BaseModel):
    vaccine_name: str
    place: str
    date: date


# Fow showing data
class Show_Health_info(BaseModel):
    name: str
    illness: str
    is_vaccinated: bool
    vaccine_type: Optional(List[Vaccination])
