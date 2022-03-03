# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
import os
from flask import Flask


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")

    @staticmethod
    def init_app(app: Flask):
        pass


class Development(Config):
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SECRET_KEY = os.environ["SECRET_KEY"]


class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///./test.sqlite3"


config = {
    "production": Production,
    "development": Development,
    "testing": Test,
    "default": Development
}
