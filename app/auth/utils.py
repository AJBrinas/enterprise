from passlib.context import CryptContext
p_sswr_d = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return p_sswr_d.hash(password)


def verify(plain_pass, hashed_pass):
    return p_sswr_d.verify(plain_pass, hashed_pass)
