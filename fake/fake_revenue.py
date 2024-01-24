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


philippineCompanies = [
  "Manila Metro Health Services",
  "Davao City Agricultural Solutions",
  "Cebu Tech Hub",
  "Makati Financial Advisors",
  "Quezon City Realty Group",
  "Taguig Global Logistics",
  "Cagayan de Oro Tourism Ventures",
  "Bacolod Food Innovations",
  "Iloilo Sustainable Energy",
  "Pampanga Manufacturing Co.",
  "Zamboanga Maritime Technologies",
  "Subic Bay Electronics",
  "Iligan City Construction",
  "Cavite Pharma Solutions",
  "Baguio Educational Systems",
  "Dagupan Hospitality Enterprises",
  "Ormoc City Real Estate",
  "Naga City Software Development",
  "Tacloban Renewable Resources",
  "Puerto Princesa Eco-Tourism",
  "Lapu-Lapu City Shipping Services",
  "Angeles City Automotive Solutions",
  "Lucena City Real Estate Developers",
  "Butuan City Financial Consultants",
  "General Santos Agribusiness",
  "Legazpi City Health Innovations",
  "Sorsogon City Manufacturing",
  "Cotabato City Tech Solutions",
  "Batangas City Hospitality Group",
  "Caloocan City Retail Ventures",
  "Malolos City Construction Co.",
  "San Juan City Telecommunications",
  "Roxas City Food Industries",
  "Mandaue City Real Estate",
  "Marikina City Educational Systems",
  "Olongapo City Logistics",
  "Tarlac City Pharmaceutical",
  "Valenzuela City Maritime Solutions",
  "Dipolog City Automotive Services",
  "Kidapawan City Renewable Energy",
  "Bayawan City Manufacturing Co.",
  "Laoag City Tourism Ventures",
]

# Generate random revenue collection data for the RevenueCollection model
for i in range(1, 150):
    source_name = random.choice(philippineCompanies)
    collection_amount = random.randint(1000, 10000)
    collection_date = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')
    note = fake.text()
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')

    insert_query = f"""INSERT INTO revenue_collection ("SourceName", "CollectionAmount", "CollectionDate", "Note", "created_at") VALUES ('{source_name}', {collection_amount}, '{collection_date}', '{note}', '{created_at}');"""

    print(insert_query)
