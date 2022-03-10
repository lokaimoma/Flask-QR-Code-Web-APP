# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"

    @staticmethod
    def init_app(app: Flask):
        pass


class Development(Config):
    DEBUG = True


class Production(Config):
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 1800
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URL"]
    SECRET_KEY = os.environ["SECRET_KEY"]


class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


config = {
    "production": Production,
    "development": Development,
    "testing": Test,
    "default": Development
}
