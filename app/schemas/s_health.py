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


class MedicalHistory(BaseModel):
    allergies: List[str] = []
    chronic_conditions: List[str] = []
    surgeries: List[str] = []
    family_history: List[str] = []


class VaccinationRecord(BaseModel):
    vaccine: str
    date: date
    dose: str


class Medication(BaseModel):
    name: str
    dosage: str
    frequency: str

class HealthInformation(BaseModel):
    full_name: Optional[str]
    date_of_birth: Optional[str]
    gender: Optional[str]
    address: Optional[str]
    contact_number: Optional[str]


class HealthInformationAdd(HealthInformation):

    emergency_contact: Optional[EmergencyContact]
    medical_history: Optional[MedicalHistory]
    vaccination_record: Optional[VaccinationRecord]
    current_medications: Optional[Medication]


# Medication
# For Creating Data
class AddInfo(Medication):
    illness: str
    pass


# For Updating Data
class UpdateInfo(HealthInformation):
    pass


# For Viewing Data
class ViewInfo(BaseModel):
    pass
