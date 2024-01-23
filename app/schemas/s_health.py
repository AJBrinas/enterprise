from typing import List, Optional
from pydantic import BaseModel
from pydantic import BaseModel, ValidationError
from datetime import date

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
    barangay_id: Optional[str]


class HealthInformationAdd(HealthInformation):

    emergency_contact: EmergencyContact
    medical_history: MedicalHistory
    vaccination_record: VaccinationRecord
    current_medications: List[Medication] = []
    recent_health_events: List[str] = []
    health_habits: dict
    routine_checkups: dict
    health_insurance: dict
    health_screenings: dict
    mental_health: dict
    reproductive_health: dict
    weight_and_height: dict
    dental_health: dict
    vision_and_hearing: dict
