from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from .settings import settings as s
from typing import Annotated


URL_DATABASE = f"postgresql://{
    s.database_username}:{
        s.database_password}@{
            s.database_hostname}:{s.database_port}/{s.database_name}"


engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#  Getting the Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Short for Session = Depends(get_db)
db_dependency = Annotated[Session, Depends(get_db)]