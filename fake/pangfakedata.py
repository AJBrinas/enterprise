from faker import Faker
from datetime import datetime, timedelta
import random
# import random

fake = Faker()
Faker.seed(0)


def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)


# Generate 30 rows of data
for _ in range(200):
    full_name = fake.name()
    date_of_birth = fake.date_of_birth()
    gender = fake.random_element(elements=('Male', 'Female'))
    address = fake.address()
    contact_number = fake.phone_number()
    is_dead = fake.random_element(elements=(True, False))
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S')

# Assuming 1 to 100 are valid IDs in medications

    # Generate the INSERT INTO statement
    insert_statement = f"""
    INSERT INTO health_information (
        full_name, date_of_birth, gender, address, contact_number, is_dead, created_at)
        VALUES ('{full_name}', '{date_of_birth}', '{gender}', '{address}', '{contact_number}', '{is_dead}', '{created_at}');"""

    # Print or execute the INSERT INTO statement as needed
    print(insert_statement)
