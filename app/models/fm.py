from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class Financial(Base):
    __tablename__ = 'financial_management'

    id = Column(Integer, primary_key=True)
        
