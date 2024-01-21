from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models import users, cbhi
from app.schemas import user_schema
# from ..auth.oauth2 import get_current_user
router = APIRouter(prefix="/health-information",
                   tags=["Health Information"])


temp = Jinja2Templates(directory="app/templates")


# @router.get("/")
# def get(db: db_dependency):
#     user = db.query(users.User).all()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="User not found")
#     return user


@router.get("/", response_model=user_schema.UserResponse)
def root(request: Request, db: db_dependency):
    user = db.query(cbhi.Health_Information).all()

    return temp.TemplateResponse("health_information.html",
                                 {"request": request,
                                  "users": user})


#  Home
@router.get("/health")
def add_health_info(request: Request):
    return temp.TemplateResponse("add_health_info.html",
                                 {"request": request})


# Creating a health Info
@router.post("/health-input", status_code=status.HTTP_201_CREATED)
def add(request: Request,
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
def edit(request: Request,  user_id: int,
         db: db_dependency):
    # Get the user from the database by its id
    user = db.query(users.User).filter(users.User.id == user_id).first()
    return temp.TemplateResponse("edit_health_info.html",
                                 {"request": request,
                                  "user": user})


@router.get('/health-list')
def get_list(db: db_dependency):

    health = db.query().all()
    return health
