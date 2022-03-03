# Created by Kelvin_Clark on 3/3/2022, 4:58 PM
from src import database as db


class User(db.Model):
    __tablename__ = "users"
    username: str = db.Column(db.String(200).with_variant(db.Text, "sqlite"), unique=True, primary_key=True)
    email: str = db.Column(db.String(200).with_variant(db.Text, "sqlite"), unique=True, nullable=False)
    password: str = db.Column(db.String(500).with_variant(db.Text, "sqlite"), nullable=False)

    def __init__(self, username: str, email: str, password: str):
        self.email = email
        self.password = password
        self.username = username


class UserOut:
    def __init__(self, user: User):
        self.username = user.username
        self.email = user.email
