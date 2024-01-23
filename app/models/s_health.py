from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DATE

from app.config.database import Base


class EmergencyContact(Base):
    __tablename__ = 'emergency_contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    relationship = Column(String)
    contact_number = Column(String)


class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    id = Column(Integer, primary_key=True, index=True)
    allergies = Column(JSON)
    chronic_conditions = Column(JSON)
    surgeries = Column(JSON)
    family_history = Column(JSON)


class VaccinationRecord(Base):
    __tablename__ = 'vaccination_records'

    id = Column(Integer, primary_key=True, index=True)
    vaccine = Column(String)
    date = Column(DATE)
    dose = Column(String)


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    dosage = Column(String)
    frequency = Column(String)


class HealthInformation(Base):
    __tablename__ = 'health_information'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    date_of_birth = Column(String)
    gender = Column(String)
    address = Column(String)
    contact_number = Column(String)
    barangay_id = Column(String)

    emergency_contact = Column(Integer, ForeignKey('emergency_contacts.id'))
    medical_history = Column(Integer, ForeignKey('medical_history.id'))
    vaccination_record = Column(Integer, ForeignKey('vaccination_records.id'))
    current_medications = Column(Integer, ForeignKey('medications.id'))
