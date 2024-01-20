from fastapi import FastAPI, Request
from .routes import health_information
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Enterprise"
)

temp = Jinja2Templates(directory="app/templates")


@app.get("/")
def root(Request: Request):
    return temp.TemplateResponse("health_information.html",
                                 {"request": Request,
                                  'message': 'Hello World'}
                                 )


app.include_router(health_information.router)
