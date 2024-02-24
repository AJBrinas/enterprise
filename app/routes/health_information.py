from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status, Depends
from fastapi.responses import RedirectResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models.s_health import EmergencyContact as ec, MedicalHistory as mh, VaccinationRecord as vr, Medication as m, HealthInformation as hi
from app.schemas import s_health as schema
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
@router.get("/all")
def read_items(db: db_dependency, limit: int = 10):
    health = db.query(hi).limit(limit).all()

    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    print(len(health))
    return {'healthdata': health}


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
@router.get("/infoss", response_model=schema.HealthTable)
def read_health(request: Request, db: db_dependency, get_user: int = Depends(get_current_user)):
    if not get_user:
        raise HTTPException(RedirectResponse(url='/'),
                            status_code=status.HTTP_401_UNAUTHORIZED)
    health = db.query(hi).all()
    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    return temp.TemplateResponse('health_records.html', {'request': request,
                                                         "health": health})


# Get all data with html COPYYYYY
@router.get("/infos", response_model=schema.HealthTable)
def reads_health(request: Request, db: db_dependency):
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


# Health View -------------------
# Goto HTML
@router.get('/view/{id}', status_code=200)
def view_form(request: Request, db: db_dependency, id: int):
    person = db.query(hi).filter(hi.id == id).first()
    contact = db.query(ec).filter(ec.person_info == id).all()
    medical = db.query(m).filter(m.person_info == id).all()
    vaccine = db.query(vr).filter(vr.person_info == id).all()
    return temp.TemplateResponse("view_health_info.html", {'request': request,
                                                           'person': person,
                                                           'contact': contact,
                                                           'medical': medical,
                                                           'vaccine': vaccine})


# Get Person info
@router.get('/views/{id}', status_code=200)
def add_form(id: int, db: db_dependency):
    person = db.query(hi).filter(hi.id == id).first()

    return {'person': person}
# ------------------------


# From the Html FORM CRUD for MEDICATION -----------------------
# Form
@router.get("/add/medication")
def try_form(request: Request):
    return temp.TemplateResponse('try.html', {"request": request})


# Create Medication
@router.post("/create", status_code=201)
def create_information(db: db_dependency,
                       illness: str = Form(...),
                       medicine: str = Form(...),
                       dosage: str = Form(...),
                       frequency: str = Form(...),
                       diagnosed: date = Form(...),
                       person_info: str = Form(...)):
    # TODO: Implement the function to save information into database
    try:
        new = m(
            illness=illness,
            medicine=medicine,
            dosage=dosage,
            frequency=frequency,
            diagnosed_date=diagnosed,
            person_info=person_info
        )   
        db.add(new)
        db.commit()
        db.refresh(new)
        return new
    except Exception as e:
        print(e)


# Update Medication
@router.post("/update")
def put_information(illness: str = Form(...),
                    medicine: str = Form(...),
                    dosage: str = Form(...),
                    frequency: str = Form(...),
                    diagnosed: date = Form(...),
                    person_info: str = Form(...)):
    # TODO: Implement the function to save information into database

    return {'medicine': medicine,
            'dosages': dosage,
            'illness': illness,
            'diagnosed': diagnosed,
            'frequency': frequency,
            'person_info': person_info}


# Delete Medication
@router.put("/delete")
def delete_information(db: db_dependency, id: int):
    # TODO: Implement the function to save information into database
    pass


# VIEWING and GETTING DATA ----------------------
# For Line GRAPH ILLNESSES
@router.get('/graphs/illnesses')
async def get_all_illnesses(request: Request, db: db_dependency):
    illnesses = db.query(m.illness, func.count(m.illness).label('total')).group_by(m.illness).all()
    result = [{"illness": illness, "total": total} for illness, total in illnesses]
    return {'ill': result}


# for donut Chart Gender
@router.get("/gender-all")
async def gender_all(db: db_dependency):
    genders = db.query(hi.gender,
                       func.count(hi.gender).label('total')
                       ).group_by(hi.gender).all()
    result = [{"gender": gender, "total": total} for gender, total in genders]
    return {'gender': result}


# From the Html FORM CRUD for MEDICATION HISTORY -----------------------
# Go to Medical History Form
@router.get("/form-medical-history/")
def medical_history(request: Request):
    return temp.TemplateResponse('<>.html', {'request': request})


# Create Medical History
@router.post("/create-medical-history")
def create_medical_history(db: db_dependency,
                           allergy: str = Form(),
                           allergy_type: str = Form(),
                           allergy_severity: str = Form(),
                           chronic_condition: str = Form(),
                           chronic_diagnosis: date = Form(),
                           surgery: str = Form(),
                           surgery_date: str = Form(),
                           family_history_condition: str = Form(),
                           family_history_relation: str = Form(),
                           person_info: int = Form(),):

    try:
        new = mh(
            allergy=allergy,
            allergy_type=allergy_type,
            allergy_severity=allergy_severity,
            chronic_condition=chronic_condition,
            chronic_diagnosis=chronic_diagnosis,
            surgery=surgery,
            surgery_date=surgery_date,
            family_history_condition=family_history_condition,
            family_history_relationship=family_history_relation,
            patient_id=person_info)
        db.add(new)
        db.commit()
        pass
    except Exception as e:
        db.rollback()
        print("Error in adding medical history: ", e)
        raise HTTPException(status_code=500, detail="Failed to add medical history.")

    pass


# Return the newly created object (with id)
