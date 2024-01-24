from faker import Faker
# import random

fake = Faker()
Faker.seed(0)

# Generate 30 rows of data
for _ in range(200):
    full_name = fake.name()
    date_of_birth = fake.date_of_birth()
    gender = fake.random_element(elements=('Male', 'Female'))
    address = fake.address()
    contact_number = fake.phone_number()
    is_dead = fake.random_element(elements=(True, False))
# Assuming 1 to 100 are valid IDs in medications

    # Generate the INSERT INTO statement
    insert_statement = f"""
    INSERT INTO health_information (
        full_name, date_of_birth, gender, address, contact_number, is_dead)
        VALUES (
        '{full_name}',
        '{date_of_birth}', '{gender}',
        '{address}', '{contact_number}', '{is_dead}'
    );
    """

    # Print or execute the INSERT INTO statement as needed
    print(insert_statement)
