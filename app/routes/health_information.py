from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status, Depends
from fastapi.responses import RedirectResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models.s_health import EmergencyContact as ec, MedicalHistory as mh, VaccinationRecord as vr, Medication as m, HealthInformation as hi
from app.schemas import user_schema, s_health as schema
from typing import List
from fastapi.encoders import jsonable_encoder
import datetime
from sqlalchemy import func
from ..auth.oauth2 import get_current_user
router = APIRouter(prefix="/health-information",
                   tags=["Health Information"])


temp = Jinja2Templates(directory="app/templates")


# WITHOUT HTML
# Get data  without html
@router.get("/all/{id}", status_code=status.HTTP_302_FOUND)
async def read_item(id: int, db: db_dependency,
                    active: int = Depends(get_current_user)):
    if not active:
        return RedirectResponse('http://127.0.0.1:8000/login',
                                status_code=status.HTTP_401_UNAUTHORIZED)

    health = db.query(hi).filter(hi.id == id).first()
    return {"health-data": health}


# Get all HEALTH INFORMATION without HTML
@router.get("/all", response_model=List[schema.HealthTable])
def read_items(db: db_dependency, limit: int = 10):
    health = db.query(hi).limit(limit).all()

    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    return {"health-data": health}


# Getting all vaccines related to the person
@router.get("/info/vac/{id}")
def read_person_vaccines(id: int, db: db_dependency):
    person = db.query(hi).filter(hi.id == id).first()
    vaccines = db.query(vr).filter(vr.person_info == id).all()
    # vac = vaccines.
    return {'person': person, 'vaccines': vaccines}


# Getting all related to the person
@router.get("/info/all-vac/")
def read_person_infos(db: db_dependency, limit: int = 2):
    person = db.query(hi).join(vr).filter(vr.person_info == hi.id).limit(limit).all()
    # vac = vaccines.
    return {'person': person}


# Get all CONTACTS data without html
@router.get("/contacts", status_code=status.HTTP_200_OK)
def read_contacts(db: db_dependency, limit: int = 10):
    contacts = db.query(ec).limit(limit)
    c = contacts.all()
    if not c:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )
    return {"health-data": c}


# WITH HTML
# Get all data with html
@router.get("/infos", response_model=schema.HealthTable)
def read_health(request: Request, db: db_dependency):
    health = db.query(hi).all()
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
    health = db.query(hi
                      ).filter(hi.id == id
                               ).first()
    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )
    emergency_contact = health.emergency_contact
    contact = db.query(ec
                       ).filter(
                           ec.id == emergency_contact
                                ).first()
    return {"information": health,
            "contact": contact}

