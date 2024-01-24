from faker import Faker
from datetime import datetime, timedelta, timezone
import random

fake = Faker()


# Generate random date within 2020-2024
def generate_random_date():
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    random_seconds = random.randint(
        0, int((end_date - start_date).total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


# Generate 60 rows of fake data for the BudgetTracking model
for i in range(1, 100):
    budget_name = fake.word()
    budget_amount = random.randint(1000, 100000)
    expenditure = random.randint(0, budget_amount)
    transaction_date = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')
    note = fake.sentence()
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')

    insert_query = f"""
    INSERT INTO budget_tracking ("BudgetName", "BudgetAmount",
    "Expenditure", "TransactionDate", "Note", "created_at")
    VALUES ('{budget_name}', {budget_amount}, {expenditure}, '{transaction_date}', '{note}', '{created_at}');"""

    print(insert_query)
