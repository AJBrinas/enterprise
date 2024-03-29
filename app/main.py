from fastapi import FastAPI, Request

from app.routes import health_information, disaster_plan, financial_management
from app.routes import auth, user, about
from app.routes import events_announcement, population_commision

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Enterprise"
)

temp = Jinja2Templates(directory="app/templates")
app.mount("/app/static", StaticFiles(directory='app/static/'), name="static")


@app.get("/tac")
def root(Request: Request):
    return temp.TemplateResponse("landing.html",
                                 {"request": Request}
                                 )


@app.get("/service")
def services(Request: Request):
    return temp.TemplateResponse("enterprise_services.html",
                                 {"request": Request}
                                 )


@app.get("/s")
def here(Request: Request):
    return {"msg": "hello"}


app.include_router(health_information.router)
app.include_router(disaster_plan.router)
app.include_router(financial_management.router)
app.include_router(auth.router)
app.include_router(events_announcement.router)
app.include_router(population_commision.router)
app.include_router(about.router)
