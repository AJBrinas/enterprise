from faker import Faker
from datetime import datetime, timedelta, timezone
import random

fake = Faker()


# Generate random date within 2020-2024
def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)


# with timezone
def generate_random_date_tz():
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    random_seconds = random.randint(
        0, int((end_date - start_date).total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


# Generate 60 rows of fake data
for i in range(1, 150):
    event_name = fake.word() + ' ' + fake.word()
    event_type = fake.word()
    event_date = generate_random_date().strftime('%Y-%m-%d %H:%M:%S')
    event_location = fake.word() + ' ' + fake.word()
    organizer = fake.company()
    created_at = generate_random_date_tz().strftime('%Y-%m-%d %H:%M:%S %z')

    insert_query = f"""INSERT INTO community_events ("EventName", "EventType", "EventDate", "EventLocation", "Organizer", "created_at")
    VALUES ('{event_name}', '{event_type}', '{event_date}', '{event_location}', '{organizer}', '{created_at}');"""

    print(insert_query)
