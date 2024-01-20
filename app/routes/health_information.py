from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/health-information",
                   tags=["Health Information"])

temp = Jinja2Templates(directory="app/templates")


@router.get("/")
def root():
    return {'message': 'Hello health info'}


@router.post("/health-input")
def add(request: Request,
        name: str = Form(...)):
    print(name)
    return RedirectResponse(url=router.url_path_for("root"))


@router.get("/health")
def addnew(request: Request):
    return temp.TemplateResponse("add_health_info.html",
                                 {"request": request})
