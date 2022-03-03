# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
from typing import Optional, Tuple
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from src.config import config

database = SQLAlchemy()
alembic = Alembic()


def create_app(config_name: Optional[str] = "default") -> tuple[Flask, SQLAlchemy, Alembic]:
    app = Flask(__name__)
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
        global database
        global alembic
        database.init_app(app)
        alembic.init_app(app)
    except KeyError:
        raise ValueError(
            f"The config name can be either default, development, production or testing not ${config_name}")
    return app, database, alembic
