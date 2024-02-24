from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DATE, Boolean
from sqlalchemy import TIMESTAMP, text
from app.config.database import Base


class EmergencyContact(Base):
    __tablename__ = 'emergency_contacts'

    id = Column(Integer, primary_key=True, index=True)
    contact_name = Column(String, index=True)
    relationship = Column(String)
    contact_number = Column(String)
    person_info = Column(Integer, ForeignKey('health_information.id',
                                             ondelete='CASCADE'))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True, index=True)


class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    id = Column(Integer, primary_key=True, index=True)
    allergy = Column(String)
    allergy_type = Column(String)
    allergy_severity = Column(String)
    chronic_condition = Column(String)
    chronic_diagnosis = Column(DATE)
    surgery = Column(String)
    surgery_date = Column(DATE)
    family_history_condition = Column(String)
    family_history_relation = Column(String)
    person_info = Column(Integer, ForeignKey('health_information.id',
                                             ondelete='CASCADE'))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True, index=True)


class VaccinationRecord(Base):
    __tablename__ = 'vaccination_records'

    id = Column(Integer, primary_key=True, index=True)
    vaccine = Column(String)
    vaccinated_date = Column(DATE)
    dose = Column(String)
    person_info = Column(Integer, ForeignKey('health_information.id',
                                             ondelete='CASCADE'))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True, index=True)


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, index=True)
    illness = Column(String)
    medicine = Column(String)
    dosage = Column(String)
    frequency = Column(String)
    diagnosed_date = Column(DATE)
    person_info = Column(Integer, ForeignKey('health_information.id',
                                             ondelete='CASCADE'))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True, index=True)


class HealthInformation(Base):
    __tablename__ = 'health_information'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(DATE, nullable=False)
    gender = Column(String)
    address = Column(String)
    contact_number = Column(String)
    is_dead = Column(Boolean, server_default=text('False'))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()'))
    created_by = Column(String,
                        nullable=False,
                        server_default=text("'admin'"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=True)
    updated_by = Column(String, nullable=True, index=True)
