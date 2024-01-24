from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models import s_health
from app.schemas import user_schema, s_health as schema
from typing import List
from fastapi.encoders import jsonable_encoder
import datetime
from sqlalchemy import func
# from ..auth.oauth2 import get_current_user
router = APIRouter(prefix="/health-information",
                   tags=["Health Information"])


temp = Jinja2Templates(directory="app/templates")


# WITHOUT HTML
# Get data  without html
@router.get("/all/{id}",
            response_class=ORJSONResponse)
async def read_item(id: int, db: db_dependency):
    health = db.query(s_health.HealthInformation
                      ).filter(s_health.HealthInformation.id == id
                               ).first()
    return {"health-data": health}


# Get all HEALTH INFORMATION without HTML
@router.get("/all", response_model=List[schema.HealthTable])
def read_items(db: db_dependency, limit: int = 10):
    health = db.query(s_health.HealthInformation).limit(limit).all()

    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    return {"health-data": health}


# Get all CONTACTS data without html
@router.get("/contacts", status_code=status.HTTP_200_OK)
def read_contacts(db: db_dependency, limit: int = 10):
    contacts = db.query(s_health.EmergencyContact).limit(limit)
    c = contacts.all()
    if not c:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )
    return {"health-data": c}


# WITH HTML
# Get all data with html
@router.get("/infos", response_class=ORJSONResponse)
def read_health(request: Request, db: db_dependency):
    health = db.query(s_health.HealthInformation).all()
    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    return temp.TemplateResponse('health_records.html', {'request': request,
                                                         "health": health})


# Eventd
@router.get('/events')
def get_vaccine(request: Request):

    return temp.TemplateResponse('events.html',
                                 {'request': request})


# Disaster Plan
@router.get('/disaster_response')
def get_disaster(request: Request):

    return temp.TemplateResponse('disaster_response.html',
                                 {'request': request})



# Get Health data without Contact Information with html
@router.get("/infos/all/{id}")
def read_all_health(db: db_dependency, id: int):
    health = db.query(s_health.HealthInformation
                      ).filter(s_health.HealthInformation.id == id
                               ).first()
    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    emergency_contact = health.emergency_contact
    contact = db.query(s_health.EmergencyContact
                       ).filter(
                           s_health.EmergencyContact.id == emergency_contact
                                ).first()
    return {"information": health,
            "contact": contact}
