from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency
from app.models import users
from app.schemas import user_schema
# from ..auth.oauth2 import get_current_user
router = APIRouter(prefix="/disaster-plan",
                   tags=["Disaster Plan"])


temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root(request: Request):
    return temp.TemplateResponse("disaster_plan.html",
                                 {"request": request})
