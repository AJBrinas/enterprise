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


# Generate 60 rows of fake data for the Announcement model
for i in range(1, 100):
    announcement_title = fake.sentence()
    announcement_content = fake.paragraph()
    announcement_date = generate_random_date().strftime('%Y-%m-%d %H:%M:%S')
    announcer = fake.name()
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S')

    insert_query = f"""
    INSERT INTO announcements ("AnnouncementTitle", "AnnouncementContent",
    "AnnouncementDate", "Announcer", "created_at")
    VALUES ('{announcement_title}', '{announcement_content}',
    '{announcement_date}', '{announcer}', '{created_at}');"""

    print(insert_query)
