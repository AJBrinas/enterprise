from faker import Faker
import random

fake = Faker()
Faker.seed(0)

# Generate 30 rows of data
for _ in range(25):
    full_name = fake.name()
    date_of_birth = fake.date_of_birth()
    gender = fake.random_element(elements=('Male', 'Female'))
    address = fake.address()
    contact_number = fake.phone_number()
    barangay_id = fake.word()

    emergency_contact_id = random.randint(1, 64)  # Assuming 1 to 100 are valid IDs in emergency_contacts
    medical_history_id = random.randint(1, 12)  # Assuming 1 to 100 are valid IDs in medical_history
    vaccination_record_id = random.randint(1, 56)  # Assuming 1 to 100 are valid IDs in vaccination_records
    current_medications_id = random.randint(1, 20)  # Assuming 1 to 100 are valid IDs in medications

    # Generate the INSERT INTO statement
    insert_statement = f"""
    INSERT INTO health_information (
        full_name, date_of_birth, gender, address, contact_number, barangay_id,
        emergency_contact, medical_history, vaccination_record, current_medications
    ) VALUES (
        '{full_name}', '{date_of_birth}', '{gender}', '{address}', '{contact_number}', '{barangay_id}',
        {emergency_contact_id}, {medical_history_id}, {vaccination_record_id}, {current_medications_id}
    );
    """
    
    # Print or execute the INSERT INTO statement as needed
    print(insert_statement)
