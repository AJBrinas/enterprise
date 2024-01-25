from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency


router = APIRouter(prefix="/population-commission")

temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root(request: Request):

    return temp.TemplateResponse("population_commission.html",
                                 {"request": request})
