allergies = [
    {"type": "Pollen", "severity": "Moderate"},
    {"type": "Peanuts", "severity": "Severe"},
    {"type": "Dust Mites", "severity": "Mild"},
    {"type": "Shellfish", "severity": "Moderate"},
    {"type": "Cat Hair", "severity": "Severe"},
    {"type": "Penicillin", "severity": "Severe"},
    {"type": "Eggs", "severity": "Moderate"},
    {"type": "Mold", "severity": "Mild"},
    {"type": "Latex", "severity": "Moderate"},
    {"type": "Insect Stings", "severity": "Severe"},
]

# Separate into type and severity lists
types = [entry["type"] for entry in allergies]
severities = [entry["severity"] for entry in allergies]

print("Types:", types)
print("Severities:", severities)


# Chronic Conditions
chronic_conditions = [
    {"condition": "Hypertension", "diagnosis_date": "2021-02-15"},
    {"condition": "Diabetes Type 2", "diagnosis_date": "2020-07-10"},
    {"condition": "Asthma", "diagnosis_date": "2019-05-22"},
    {"condition": "Arthritis", "diagnosis_date": "2022-03-18"},
    {"condition": "Migraines", "diagnosis_date": "2023-01-05"},
]

# Separate into condition and diagnosis_date lists
conditions = [entry["condition"] for entry in chronic_conditions]
diagnosis_dates = [entry["diagnosis_date"] for entry in chronic_conditions]

print("Chronic Conditions:", conditions)
print("Diagnosis Dates:", diagnosis_dates)

# Surgeries
surgeries = [
    {"procedure": "Appendectomy", "date": "2018-08-30"},
    {"procedure": "Knee Replacement", "date": "2020-11-12"},
    {"procedure": "Gallbladder Removal", "date": "2019-04-05"},
    {"procedure": "Cataract Surgery", "date": "2022-07-25"},
    {"procedure": "Hip Replacement", "date": "2019-06-10"},
    {"procedure": "Gastric Bypass Surgery", "date": "2020-03-25"},
    {"procedure": "Coronary Artery Bypass Graft (CABG)", "date": "2018-12-15"},
    {"procedure": "Appendix Removal", "date": "2021-07-05"},
    {"procedure": "Total Knee Replacement", "date": "2019-10-20"},
    {"procedure": "Lumbar Fusion", "date": "2022-02-28"},
    {"procedure": "LASIK Eye Surgery", "date": "2021-01-12"},
    {"procedure": "Gallstone Removal", "date": "2022-08-17"},
    {"procedure": "Tonsillectomy", "date": "2020-09-08"},
    {"procedure": "Cornea Transplant", "date": "2019-04-30"},
    {"procedure": "Hernia Repair", "date": "2021-11-22"},
    {"procedure": "Prostatectomy", "date": "2020-05-18"},
    {"procedure": "Gynecologic Laparoscopy", "date": "2022-06-03"},
    {"procedure": "Rotator Cuff Repair", "date": "2019-08-14"},
    {"procedure": "Carotid Endarterectomy", "date": "2022-12-10"},
    {"procedure": "Laparoscopic Cholecystectomy", "date": "2020-02-05"},
    {"procedure": "Corneal Transplant", "date": "2021-04-17"},
    {"procedure": "Cervical Disc Replacement", "date": "2018-11-30"},
    {"procedure": "Cataract Surgery", "date": "2022-01-28"},
    {"procedure": "Colon Resection", "date": "2020-07-20"},
    {"procedure": "Bunion Surgery", "date": "2021-09-15"},
    {"procedure": "Aortic Valve Replacement", "date": "2019-03-02"},
    {"procedure": "Spinal Fusion", "date": "2022-05-12"},
    {"procedure": "Tummy Tuck", "date": "2020-10-08"},
    {"procedure": "Open Heart Surgery", "date": "2018-09-18"},
    {"procedure": "Lobectomy", "date": "2021-02-23"},
    {"procedure": "Vasectomy", "date": "2022-10-30"},
    {"procedure": "Nasal Polyp Removal", "date": "2019-12-07"},
    {"procedure": "Knee Arthroscopy", "date": "2020-04-14"},
    {"procedure": "Lung Transplant", "date": "2021-08-05"},
    {"procedure": "Thyroidectomy", "date": "2019-01-25"},
    {"procedure": "Gallbladder Surgery", "date": "2022-03-15"},
    {"procedure": "Wrist Fusion", "date": "2020-06-19"},
    {"procedure": "Jaw Surgery", "date": "2021-05-03"},
    {"procedure": "ACL Reconstruction", "date": "2018-10-12"},
    {"procedure": "Prostate Biopsy", "date": "2022-11-08"},
    {"procedure": "Umbilical Hernia Repair", "date": "2020-01-16"},
    {"procedure": "Ablation Therapy", "date": "2021-06-27"},
    {"procedure": "Esophagectomy", "date": "2019-09-10"},
    {"procedure": "Laparoscopic Hysterectomy", "date": "2020-11-03"},
    {"procedure": "Gastrointestinal Bypass", "date": "2021-12-20"},
    {"procedure": "Hip Arthroplasty", "date": "2019-07-15"},
    {"procedure": "Temporal Lobectomy", "date": "2022-04-02"},
    {"procedure": "Rhinoplasty", "date": "2020-08-24"},
    {"procedure": "Circumcision", "date": "2021-10-18"},
    {"procedure": "Myomectomy", "date": "2019-02-28"},
    {"procedure": "Thoracic Outlet Decompression", "date": "2022-01-08"},
    {"procedure": "Bypass Surgery", "date": "2020-04-30"},
    {"procedure": "Breast Reconstruction", "date": "2021-07-25"},
    {"procedure": "Hip Resurfacing", "date": "2019-11-12"},
    {"procedure": "Retinal Detachment Repair", "date": "2022-02-17"},
    {"procedure": "Mastectomy", "date": "2020-09-05"},
    {"procedure": "Nephrectomy", "date": "2021-12-10"},
]

# Separate into procedure and date lists
procedures = [entry["procedure"] for entry in surgeries]
surgery_dates = [entry["date"] for entry in surgeries]

print("\nSurgeries:", procedures)
print("Surgery Dates:", surgery_dates)

# Family History
family_history = [
    {"condition": "High Cholesterol", "relation": "Uncle"},
    {"condition": "Ovarian Cancer", "relation": "Aunt"},
    {"condition": "Parkinson's Disease", "relation": "Grandparent"},
    {"condition": "Lung Cancer", "relation": "Cousin"},
    {"condition": "Rheumatoid Arthritis", "relation": "Mother-in-law"},
    {"condition": "Stroke", "relation": "Grandmother"},
    {"condition": "Prostate Cancer", "relation": "Father-in-law"},
    {"condition": "Multiple Sclerosis", "relation": "Cousin"},
    {"condition": "Thyroid Cancer", "relation": "Aunt"},
    {"condition": "Leukemia", "relation": "Uncle"},
    {"condition": "Osteoporosis", "relation": "Mother"},
    {"condition": "Lupus", "relation": "Sister"},
    {"condition": "Hemophilia", "relation": "Brother"},
    {"condition": "Liver Disease", "relation": "Grandfather"},
    {"condition": "Gastric Cancer", "relation": "Aunt"},
    {"condition": "Cystic Fibrosis", "relation": "Cousin"},
    {"condition": "Psoriasis", "relation": "Father"},
    {"condition": "Sickle Cell Anemia", "relation": "Uncle"},
    {"condition": "Kidney Stones", "relation": "Sister-in-law"},
    {"condition": "Amyotrophic Lateral Sclerosis (ALS)", "relation": "Grandparent"},
    {"condition": "Anxiety Disorder", "relation": "Cousin"},
    {"condition": "Thalassemia", "relation": "Aunt"},
    {"condition": "Gout", "relation": "Father-in-law"},
    {"condition": "Chronic Fatigue Syndrome", "relation": "Mother-in-law"},
    {"condition": "Skin Cancer", "relation": "Uncle"},
    {"condition": "Fibromyalgia", "relation": "Sister"},
    {"condition": "Myasthenia Gravis", "relation": "Cousin"},
    {"condition": "Hodgkin's Lymphoma", "relation": "Grandparent"},
    {"condition": "Polycystic Kidney Disease", "relation": "Brother"},
    {"condition": "Inflammatory Bowel Disease (IBD)", "relation": "Aunt"},
    {"condition": "Endometriosis", "relation": "Mother"},
    {"condition": "Pancreatitis", "relation": "Uncle"},
    {"condition": "Hypothyroidism", "relation": "Sister-in-law"},
    {"condition": "Chronic Obstructive Pulmonary Disease (COPD)", "relation": "Father"},
    {"condition": "Rheumatic Heart Disease", "relation": "Cousin"},
    {"condition": "Interstitial Cystitis", "relation": "Mother-in-law"},
    {"condition": "Hemochromatosis", "relation": "Grandfather"},
    {"condition": "Bipolar Disorder", "relation": "Sister"},
    {"condition": "Tourette Syndrome", "relation": "Uncle"},
    {"condition": "Gastritis", "relation": "Aunt"},
    {"condition": "Obsessive-Compulsive Disorder (OCD)", "relation": "Brother"},
    {"condition": "Celiac Disease", "relation": "Cousin"},
    {"condition": "Bladder Cancer", "relation": "Grandfather"},
    {"condition": "Epilepsy", "relation": "Aunt"},
    {"condition": "Pancreatic Cancer", "relation": "Uncle"},
    {"condition": "Huntington's Disease", "relation": "Sister-in-law"},
    {"condition": "Ovarian Cancer", "relation": "Cousin"},
    {"condition": "Parkinson's Disease", "relation": "Grandparent"},
    {"condition": "Lung Cancer", "relation": "Cousin"},
    {"condition": "Rheumatoid Arthritis", "relation": "Mother-in-law"},
    {"condition": "Stroke", "relation": "Grandmother"},
    {"condition": "Prostate Cancer", "relation": "Father-in-law"},
    {"condition": "Multiple Sclerosis", "relation": "Cousin"},
    {"condition": "Thyroid Cancer", "relation": "Aunt"},
    {"condition": "Leukemia", "relation": "Uncle"},
    {"condition": "Celiac Disease", "relation": "Cousin"},
    {"condition": "Bladder Cancer", "relation": "Grandfather"},
    {"condition": "Epilepsy", "relation": "Aunt"},
    {"condition": "Pancreatic Cancer", "relation": "Uncle"},
    {"condition": "Huntington's Disease", "relation": "Sister-in-law"},
]

# Separate into condition and relation lists
family_conditions = [entry["condition"] for entry in family_history]
relations = [entry["relation"] for entry in family_history]

print("\nFamily History Conditions:", family_conditions)
print("Relations:", relations)
