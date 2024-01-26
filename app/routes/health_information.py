from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status, Depends
from fastapi.responses import RedirectResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models.s_health import EmergencyContact as ec, MedicalHistory as mh, VaccinationRecord as vr, Medication as m, HealthInformation as hi
from app.schemas import s_health as schema
from app.models import s_health as models
from typing import List
from fastapi.encoders import jsonable_encoder
from datetime import date
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
        return RedirectResponse(url='http://127.0.0.1:8000/login',
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
    person = db.query(hi.full_name).filter(hi.id == id).first()
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


@router.get("/gender-all")
async def gender_all(db: db_dependency):
    genders = db.query(hi.gender,
                       func.count(hi.gender).label('total')
                       ).group_by(hi.gender).all()
    result = [{"gender": gender, "total": total} for gender, total in genders]
    return result


@router.get('/add')
def add_form(request: Request):
    return temp.TemplateResponse("try.html", {'request': request})


# From the Html FORM
@router.post("/create", status_code=201)
def create_information(db: db_dependency, id: int,
                       illness: str = Form(...),
                       medicine: str = Form(...),
                       dosage: str = Form(...),
                       frequency: str = Form(...),
                       diagnosed: date = Form(...),
                       person_info: str = Form(...)):
    # TODO: Implement the function to save information into database
    new = m(
        illness=illness,
        medicine=medicine,
        dosage=dosage,
        frequency=frequency,
        diagnosed=diagnosed,
        person_info=person_info
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.post("/update")
def put_information(name: str = Form(), id: str = Form()):
    # TODO: Implement the function to save information into database

    return {'name': name, 'id': id}

@router.put("/delete")
def delete_information(db: db_dependency, id: int):
    # TODO: Implement the function to save information into database
    pass
