from sqlalchemy import Column, Text, DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base
# from datetime import datetime


class CommunityEvent(Base):
    __tablename__ = "community_events"

    EventID = Column(Integer, primary_key=True, index=True)
    EventName = Column(String, index=True, nullable=False)
    EventType = Column(String, index=True)
    EventDate = Column(DateTime)
    EventLocation = Column(String)
    Organizer = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'),
                        index=True
                        )
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"),
                        index=True
                        )
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True,
                        index=True
                        )
    updated_by = Column(String, nullable=True, index=True)


class Announcement(Base):
    __tablename__ = "announcements"

    AnnouncementID = Column(Integer, primary_key=True, index=True)
    AnnouncementTitle = Column(String, index=True, nullable=False)
    AnnouncementContent = Column(Text)
    AnnouncementDate = Column(DateTime, server_default=text('now()'))
    Announcer = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'),
                        index=True
                        )
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"),
                        index=True
                        )
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True,
                        index=True
                        )
    updated_by = Column(String, nullable=True, index=True)
