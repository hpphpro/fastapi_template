from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

def compare_password(password: str, confirm_password: str) -> bool:
    if password != confirm_password:
        return False
    return True

def get_password_hash(password: str) -> str:
    return pwd_cxt.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_cxt.verify(plain_password, hashed_password)

