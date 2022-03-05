# Created by Kelvin_Clark on 3/5/2022, 6:32 PM
from passlib.context import CryptContext

pwd_context: CryptContext = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
