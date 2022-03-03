# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
from typing import Optional

from dotenv import load_dotenv
from flask import Flask

from src.config import config

load_dotenv()


def create_app(config_name: Optional[str] = "default") -> Flask:
    app = Flask(__name__)
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
    except KeyError:
        raise ValueError(
            f"The config name can be either default, development, production or testing not ${config_name}")

    return app
