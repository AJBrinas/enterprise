from fastapi import APIRouter, Depends, Form
from fastapi import status, HTTPException, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.auth import utils, oauth2
from app.models import users as u
from app.schemas import user_schema as us
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter(tags=['Authentication'])

temp = Jinja2Templates(directory="app/templates")


@router.post('/verify', status_code=status.HTTP_202_ACCEPTED)
def verify(user_credentials: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):

    user = db.query(u.User).filter(
        u.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials")

    # Checking the password using hashed passwords method
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials!")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login/auth', status_code=status.HTTP_100_CONTINUE)
def login(db: Session = Depends(get_db), user_credentials: OAuth2PasswordRequestForm = Depends()
          , username: str = Form(...), password: str = Form(...)):
    user_credentials.username = username
    user_credentials.password = password
    user = db.query(u.User).filter(
        u.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials")

    # Checking the password using hashed passwords method
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials!")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    for_url = f"/health-information/infos?access_token={access_token}&bearer_token=bearer"
    response = RedirectResponse(url=for_url)
    return response


@router.get("/")
def log(request: Request):
    return temp.TemplateResponse('login.html', {'request': request})


@router.get("/login/au")
def logs(request: Request, username: str = Form(), password: str = Form()):
    user = username
    passw = password
    return temp.TemplateResponse('health_records.html', {'request': request, 'user': user, 'pass': passw},
                                 status_code=201)
