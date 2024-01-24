from fastapi import HTTPException, Depends
from fastapi import status, APIRouter
from sqlalchemy.orm import Session
from typing import Annotated  # , List

from ..config.database import get_db
from app.models import users as u
from app.schemas import user_schema as us
from app.auth import utils, oauth2

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Short for Session = Depends(get_db)
db_dependency = Annotated[Session, Depends(get_db)]


# Creating Users
@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=us.UserValidate)
def create_user(user: us.Create,
                db: db_dependency):
    # Check if username already exists 6
    exists = db.query(u).filter(u.email == user.email).first()

    if not exists:
        hsh = utils.hash(user.password)
        user.password = hsh

        new_user = u.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    else:
        raise HTTPException(status_code=status.HTTP_302_FOUND,
                            detail="Already Used!")



# Getting one users
@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            response_model=us.UserValidate)
def get_user(id: int, db: db_dependency,
             current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(u.User).filter(u.User.id == id).first()
    if user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User found")

    return user
