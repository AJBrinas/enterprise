from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency


router = APIRouter(prefix="/financial-management",
                   tags=["Financial Management"])

temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root(request: Request):
    return temp.TemplateResponse("financial_management.html",
                                 {"request": request})
temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root(request: Request):
    return temp.TemplateResponse("financial_management.html",
                                 {"request": request})
