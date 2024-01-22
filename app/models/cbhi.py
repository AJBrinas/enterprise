from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, TIMESTAMP, text
from app.config.database import Base


class Health_Information(Base):
    __tablename__ = 'c_health_information'

    id = Column(Integer,
                primary_key=True,
                nullable=False)
    f_name = Column(String)
    s_name = Column(String)
    gender = Column(String)
    Type = Column(String)
    gender = Column(String)
    civil_state = Column(String)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=(text('now()')))


class Vaccination(Base):
    __tablename__ = 'vaccination_history'

    id = Column(Integer, primary_key=True, nullable=False)
    health_id = Column(Integer,
                       ForeignKey("c_health_information.id",
                                  ondelete="CASCADE"),
                       nullable=True)
    vaccination_type = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=(text('now()')))


# class Medical(Base):
#     __tablename__ = "medical_history"

#     id = Column(Integer, primary_key=True)
#     health_id = Column(Integer, ForeignKey("c_health_information.id",
#                                            ondelete="CASCADE"),
#                        nullable=True)
#     type = Column(String, nullable=True)
#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False,
#                         server_default=(text('now()')))
