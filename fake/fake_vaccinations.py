from faker import Faker
from datetime import datetime, timedelta, timezone
import random

fake = Faker()

# Generate random date within 2020-2024
def generate_random_date():
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


vaccinations = [
  "Hepatitis B Vaccine",
  "Polio Vaccine",
  "DTaP Vaccine (Diphtheria, Tetanus, Pertussis)",
  "Hib Vaccine (Haemophilus influenzae type b)",
  "MMR Vaccine (Measles, Mumps, Rubella)",
  "Varicella Vaccine (Chickenpox)",
  "Hepatitis A Vaccine",
  "Rotavirus Vaccine",
  "Pneumococcal Conjugate Vaccine",
  "Meningococcal Vaccine",
  "HPV Vaccine (Human Papillomavirus)",
  "Influenza Vaccine",
  "Tdap Vaccine (Tetanus, Diphtheria, Pertussis)",
  "Shingles Vaccine",
  "Typhoid Vaccine",
  "Japanese Encephalitis Vaccine",
  "Yellow Fever Vaccine",
  "Rabies Vaccine",
  "Malaria Vaccine",
  "Cholera Vaccine",
  "Tuberculosis (BCG) Vaccine",
  "RotaTeq (Rotavirus) Vaccine",
  "MenB (Meningococcal B) Vaccine",
  "Meningococcal ACWY Vaccine",
  "H1N1 Influenza Vaccine",
  "Dengue Fever Vaccine",
  "Ebola Vaccine",
  "Pertussis Booster (Tdap) for Adolescents and Adults",
  "COVID-19 Vaccine (e.g., Pfizer-BioNTech, Moderna, Johnson & Johnson, AstraZeneca, Sinovac, Sinopharm, Covaxin)",
  "Novavax COVID-19 Vaccine",
  "Sputnik V COVID-19 Vaccine"
]


doses = [
    "1st dose", "2nd dose", "3rd dose", "4th dose", "5th dose"
]


# Generate random vaccination records for the VaccinationRecord model
for i in range(1, 151):
    vaccine = random.choice(vaccinations)
    vaccinated_date = generate_random_date().strftime('%Y-%m-%d')
    dose = random.choice(doses)
    person_info = random.randint(1, 100)  # Assuming health_information.id can be any integer between 1 and 100
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')

    insert_query = f"INSERT INTO vaccination_records (vaccine, vaccinated_date, dose, person_info, created_at) " \
                   f"VALUES ('{vaccine}', '{vaccinated_date}', '{dose}', {person_info}, '{created_at}');"
    
    print(insert_query)
