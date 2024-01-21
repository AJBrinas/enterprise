from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    # admin = Column(Boolean, default=False)
    # created_at = Column(TIMESTAMP(timezone=True),
    #                     nullable=False,
    #                     server_default=text('now()'),
    #                     index=True
    #                     )
