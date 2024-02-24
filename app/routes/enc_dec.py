from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Encryption for Medication
def encrypt_medication(key, message):
    cipher = Fernet(key)
