from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models import users, s_health
from app.schemas import user_schema, s_health as schema
from typing import List
from fastapi.encoders import jsonable_encoder
# from ..auth.oauth2 import get_current_user
router = APIRouter(prefix="/health-information",
                   tags=["Health Information"])


temp = Jinja2Templates(directory="app/templates")


fake_fb = {}

# @router.get("/")
# def get(db: db_dependency):
#     user = db.query(users.User).all()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="User not found")
#     return user


@router.get("/")
def root(request: Request, db: db_dependency):
    user = db.query(cbhi.Health_Information).all()

    return temp.TemplateResponse("health_information.html",
                                 {"request": request,
                                  "users": user})


#  Home
@router.get("/health")
def goto_health_info(request: Request):
    return temp.TemplateResponse("add_health_info.html",
                                 {"request": request})


# Creating a health Info
@router.post("/health-input", status_code=status.HTTP_201_CREATED)
def add_health_info(request: Request,
                    db: db_dependency,
                    f_name: str = Form(...),
                    l_name: str = Form(...)):
    user = cbhi.Health_Information(f_name=f_name, s_name=l_name)
    db.add(user)
    db.commit()
    return RedirectResponse(url=router.url_path_for("root"),
                            status_code=status.HTTP_303_SEE_OTHER)


# edit of health information
@router.put("/health-edit/{user_id}")
def edit_health_info(request: Request,  user_id: int,
                     db: db_dependency):
    # Get the user from the database by its id
    user = db.query(users.User).filter(users.User.id == user_id).first()
    return temp.TemplateResponse("edit_health_info.html",
                                 {"request": request,
                                  "user": user})


# @router.get('/health-list')
# def get_list(db: db_dependency):

#     health = db.query().all()
#     return health


# Vaccine
@router.get('/vaccine')
def get_vaccine(request: Request):

    return temp.TemplateResponse('health_vaccine.html',
                                 {'request': request})


# Get all data without html
@router.get("/all/{id}",
            response_class=ORJSONResponse, response_model=schema.HealthInformation)
async def read_item(id: int, db: db_dependency):
    health = db.query(s_health.HealthInformation
                      ).filter(s_health.HealthInformation.id == id
                               ).first()
    print(health)
    return {"health-data": health}


# Get all data without html
@router.get("/all", response_class=ORJSONResponse)
def read_items(db: db_dependency, limit: int = 10):
    health = db.query(s_health.HealthInformation).limit(limit).all()

    if not health:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No informations yet."
            )

    return {"health-data": health}


# Get all data without html
@router.get("/contacts")
def read_contacts(db: db_dependency, limit: int = 10):
    contacts = db.query(s_health.EmergencyContact).limit(limit)
    c = contacts.all()
    return {"health-data": c}


# Get all data without html
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
def get_vaccine(request: Request):

    return temp.TemplateResponse('disaster_response.html',
                                 {'request': request})