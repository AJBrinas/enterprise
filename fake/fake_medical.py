from faker import Faker
from datetime import datetime, timedelta, timezone
import random
import json

fake = Faker()


# Generate random date within 2020-2024
def generate_random_date():
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


allergies = [
    {"type": "Pollen", "severity": "Moderate"},
    {"type": "Peanuts", "severity": "Severe"},
    {"type": "Dust Mites", "severity": "Mild"},
    {"type": "Shellfish", "severity": "Moderate"},
    {"type": "Cat Hair", "severity": "Severe"},
    {"type": "Penicillin", "severity": "Severe"},
    {"type": "Eggs", "severity": "Moderate"},
    {"type": "Mold", "severity": "Mild"},
    {"type": "Latex", "severity": "Moderate"},
    {"type": "Insect Stings", "severity": "Severe"},
]


# Chronic Conditions
chronic_conditions = [
    {"condition": "Hypertension", "diagnosis_date": "2021-02-15"},
    {"condition": "Diabetes Type 2", "diagnosis_date": "2020-07-10"},
    {"condition": "Asthma", "diagnosis_date": "2019-05-22"},
    {"condition": "Arthritis", "diagnosis_date": "2022-03-18"},
    {"condition": "Migraines", "diagnosis_date": "2023-01-05"},
]

# Surgeries
surgeries = [
    {"procedure": "Appendectomy", "date": "2018-08-30"},
    {"procedure": "Knee Replacement", "date": "2020-11-12"},
    {"procedure": "Gallbladder Removal", "date": "2019-04-05"},
    {"procedure": "Cataract Surgery", "date": "2022-07-25"},
]

# Family History
family_history = [
    {"condition": "Heart Disease", "relation": "Father"},
    {"condition": "Breast Cancer", "relation": "Mother"},
    {"condition": "Alzheimer's", "relation": "Grandparent"},
    {"condition": "Colon Cancer", "relation": "Sister"},
    {"condition": "Type 1 Diabetes", "relation": "Brother"},
]


# Generate random medical history data for the MedicalHistory model
for i in range(1, 61):
    allergies = json.dumps([allergies for _ in range(random.randint(0, 9))])
    chronic_conditions = json.dumps([chronic_conditions for _ in range(random.randint(0, 3))])
    surgeries = json.dumps([surgeries for _ in range(random.randint(0, 3))])
    family_history = json.dumps([family_history for _ in range(random.randint(0, 4))])
    person_info = random.randint(1, 100)  # Assuming health_information.id can be any integer between 1 and 100
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')

    insert_query = f"INSERT INTO medical_history (allergies, chronic_conditions, surgeries, family_history, person_info, created_at) " \
                   f"VALUES ('{allergies}', '{chronic_conditions}', '{surgeries}', '{family_history}', {person_info}, '{created_at}');"

    print(insert_query)
