from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class Community_Events_Announcements(Base):
    __tablename__ = 'c_events_announcments'

    id = Column(Integer,
                primary_key=True)
    event = Column(String)
