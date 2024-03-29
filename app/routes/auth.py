from fastapi import APIRouter, Depends, Form, Cookie, Header, Request
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
    print(user_credentials)
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
def login(request: Request, db: Session = Depends(get_db),
          user_credentials: OAuth2PasswordRequestForm = Depends(), username: str = Form(...), password: str = Form(...)):
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
    print(access_token)
    red = f"http://127.0.0.1:8000/health-information/infos?at={access_token}&token_type=bearer"
    return RedirectResponse(url=red)
    # return temp.TemplateResponse('health_records.html',
    #                              {'request': request,
    #                               'access_token': access_token,
    #                               'token_type': 'bearer'})


@router.get("/")
def log(request: Request):
    return temp.TemplateResponse('login.html', {'request': request})


@router.get("/login/au")
def logs(request: Request, username: str = Form(...), password: str = Form(...)):
    return RedirectResponse(url='/health-information/infos')
