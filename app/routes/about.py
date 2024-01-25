from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency


router = APIRouter(prefix="/about",
                   tags=["About"])

temp = Jinja2Templates(directory="app/templates")


@router.get("/faqs")
def get_faqs(Request: Request):
    return temp.TemplateResponse("faqs.html",
                                 {"request": Request}
                                 )


@router.get("/privacy")
def get_privacy(Request: Request):
    return temp.TemplateResponse("privacy.html",
                                 {"request": Request}
                                 )


@router.get("/terms-and-conditions")
def get_terms_and_condition(Request: Request):
    return temp.TemplateResponse("terms_conditions.html",
                                 {"request": Request}
                                 )
