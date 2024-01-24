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


Types = ['Pollen', 'Peanuts', 'Dust Mites', 'Shellfish', 'Cat Hair', 'Penicillin', 'Eggs', 'Mold', 'Latex', 'Insect Stings']
Severities = ['Moderate', 'Severe', 'Mild', 'Moderate', 'Severe', 'Severe', 'Moderate', 'Mild', 'Moderate', 'Severe']
Chronic_Conditions = ['Hypertension', 'Diabetes Type 2', 'Asthma', 'Arthritis', 'Migraines']

Surgeries = ['Appendectomy', 'Knee Replacement', 'Gallbladder Removal', 'Cataract Surgery', 'Hip Replacement', 'Gastric Bypass Surgery', 'Coronary Artery Bypass Graft (CABG)',
             'Appendix Removal', 'Total Knee Replacement', 'Lumbar Fusion', 'LASIK Eye Surgery', 'Gallstone Removal', 'Tonsillectomy', 'Cornea Transplant', 'Hernia Repair',
             'Prostatectomy', 'Gynecologic Laparoscopy', 'Rotator Cuff Repair', 'Carotid Endarterectomy', 'Laparoscopic Cholecystectomy', 'Corneal Transplant', 'Cervical Disc Replacement',
             'Cataract Surgery', 'Colon Resection', 'Bunion Surgery', 'Aortic Valve Replacement', 'Spinal Fusion', 'Tummy Tuck', 'Open Heart Surgery', 'Lobectomy', 'Vasectomy',
             'Nasal Polyp Removal', 'Knee Arthroscopy', 'Lung Transplant', 'Thyroidectomy', 'Gallbladder Surgery', 'Wrist Fusion', 'Jaw Surgery', 'ACL Reconstruction',
             'Prostate Biopsy', 'Umbilical Hernia Repair', 'Ablation Therapy', 'Esophagectomy', 'Laparoscopic Hysterectomy', 'Gastrointestinal Bypass', 'Hip Arthroplasty',
             'Temporal Lobectomy', 'Rhinoplasty', 'Circumcision', 'Myomectomy', 'Thoracic Outlet Decompression', 'Bypass Surgery', 'Breast Reconstruction', 'Hip Resurfacing',
             'Retinal Detachment Repair', 'Mastectomy', 'Nephrectomy']
Surgery_Dates = ['2018-08-30', '2020-11-12', '2019-04-05', '2022-07-25']

Family_History_Conditions = ['Heart Disease', 'Breast Cancer', "Alzheimers", 'Colon Cancer', 'Type 1 Diabetes', 'High Cholesterol', 'Ovarian Cancer',
                             "Parkinsons Disease", 'Lung Cancer', 'Rheumatoid Arthritis', 'Stroke', 'Prostate Cancer', 'Multiple Sclerosis', 'Thyroid Cancer',
                             'Leukemia', 'Osteoporosis', 'Lupus', 'Hemophilia', 'Liver Disease', 'Gastric Cancer', 'Cystic Fibrosis', 'Psoriasis', 'Sickle Cell Anemia',
                             'Kidney Stones', 'Amyotrophic Lateral Sclerosis (ALS)', 'Anxiety Disorder', 'Thalassemia', 'Gout', 'Chronic Fatigue Syndrome', 'Skin Cancer',
                             'Fibromyalgia', 'Myasthenia Gravis', "Hodgkins Lymphoma", 'Polycystic Kidney Disease', 'Inflammatory Bowel Disease (IBD)', 'Endometriosis',
                             'Pancreatitis', 'Hypothyroidism', 'Chronic Obstructive Pulmonary Disease (COPD)', 'Rheumatic Heart Disease', 'Interstitial Cystitis',
                             'Hemochromatosis', 'Bipolar Disorder', 'Tourette Syndrome', 'Gastritis', 'Obsessive-Compulsive Disorder (OCD)', 'Celiac Disease',
                             'Bladder Cancer', 'Epilepsy', 'Pancreatic Cancer', "Huntingtons Disease", 'Ovarian Cancer', "Parkinsons Disease", 'Lung Cancer',
                             'Rheumatoid Arthritis', 'Stroke', 'Prostate Cancer', 'Multiple Sclerosis', 'Thyroid Cancer', 'Leukemia', 'Celiac Disease', 'Bladder Cancer',
                             'Epilepsy', 'Pancreatic Cancer', "Huntingtons Disease"]
Relations = ['Father', 'Mother', 'GrandMother', 'Sister', 'Brother', 'GrandFather']


# Generate random medical history data for the MedicalHistory model
for i in range(1, 61):
    allergies = [{"type": random.choice(Types), "severity": random.choice(Severities)} for _ in range(random.randint(0, 5))]
    chronic_conditions = [{"condition": random.choice(Chronic_Conditions), "diagnosis_date": generate_random_date().strftime('%Y-%m-%d')} for _ in range(random.randint(0, 3))]
    surgeries = [{"procedure": random.choice(Surgeries), "date": generate_random_date().strftime('%Y-%m-%d')} for _ in range(random.randint(0, 2))]
    family_history = [{"condition": random.choice(Family_History_Conditions), "relation": random.choice(Relations)} for _ in range(random.randint(0, 2))]
    person_info = random.randint(1, 200)  # Assuming health_information.id can be any integer between 1 and 100
    created_at = generate_random_date().strftime('%Y-%m-%d %H:%M:%S %z')

    allergies_str = json.dumps(allergies)
    chronic_conditions_str = json.dumps(chronic_conditions)
    surgeries_str = json.dumps(surgeries)
    family_history_str = json.dumps(family_history)

    insert_query = f"INSERT INTO medical_history (allergies, chronic_conditions, surgeries, family_history, person_info, created_at) " \
                   f"VALUES ('{allergies_str}', '{chronic_conditions_str}', '{surgeries_str}', '{family_history_str}', {person_info}, '{created_at}');"

    print(insert_query)
