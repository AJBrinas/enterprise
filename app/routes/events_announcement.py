from fastapi import APIRouter, Request, Form
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.config.database import db_dependency


router = APIRouter(prefix="/events-and-announcements",
                   tags=["Events and Announcements"])

temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root(request: Request):

    return temp.TemplateResponse("events_and_announcements.html",
                                 {"request": request})
