from sqlalchemy import Boolean, Column
# from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    admin = Column(Boolean, server_default=text('False'))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True)
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    deleted_by = Column(String, nullable=True)
