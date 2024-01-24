from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()


# Generate random date within 2020-2024
def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)


relationships = ['mother', 'father', 'sister', 'brother', 'wife',
                 'husband', 'niece', 'uncle', 'aunt']

# Generate 60 rows of fake data for the EmergencyContact model
for i in range(1, 61):
    contact_name = fake.name()
    relationship = random.choice(relationships)
    contact_number = fake.phone_number()
    person_info = random.randint(1, 200)
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S')

    insert_query = f"""
                INSERT INTO emergency_contacts (
                    contact_name, relationship, contact_number,
                    person_info, created_at)
                   VALUES (
                    '{contact_name}', '{relationship}',
                    '{contact_number}', {person_info}, '{created_at}');"""

    print(insert_query)
