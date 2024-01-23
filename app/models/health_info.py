from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class User_Health(Base):
    __tablename__ = 'health_information'

    user_health_id = Column(Integer,
                            primary_key=True,
                            nullable=False)
    f_name = Column(String, nullable=False)
    s_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    # birthday = Column('birthdate', TIMESTAMP)  # type: ignore

