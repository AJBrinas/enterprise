from typing import List, Optional
from pydantic import BaseModel
# from pydantic import ValidationError
from datetime import date


# For showing Data
class HealthTable(BaseModel):
    id: int
    full_name: str
    date_of_birth: date
    address: str


class EmergencyContact(BaseModel):
    name: str
    relationship: str
    contact_number: str


# Create Medical History
class CreateMedicalHistory(BaseModel):
    allergy: str
    allergy_type: str
    allergy_severity: str
    chronic_condition: str
    chronic_diagnosis: date
    surgery: str
    surgery_date: str
    family_history_condition: str
    family_history_relation: str
    person_info: int  # Optional Palang


class VaccinationRecord(BaseModel):
    vaccine: str
    vaccinated_date: date
    dose: str
    person_info: int


class Medication(BaseModel):
    illness: str
    medicine: str
    dosage: str
    frequency: str
    diagnosed_date: date
    person_info: int


class HealthInformation(BaseModel):
    full_name: Optional[str]
    date_of_birth: Optional[str]
    gender: Optional[str]
    address: Optional[str]
    contact_number: Optional[str]


# Medication
# For Creating Data
class AddInfo(Medication):
    illness: str
    diagnosed: date
    person_info: int


# For Updating Data
class UpdateInfo(HealthInformation):
    pass


# For Viewing Data
class ViewInfo(BaseModel):
    pass
