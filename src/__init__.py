# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
import os
from typing import Optional

from flask import Flask, render_template
from flask_alembic import Alembic
from flask_sqlalchemy import SQLAlchemy

from src.config import config

src_path = os.path.abspath(os.path.dirname(__file__))
print(src_path)

database = SQLAlchemy()
alembic = Alembic()


def create_app(config_name: Optional[str] = "default") -> tuple[Flask, SQLAlchemy, Alembic]:
    app = Flask(__name__, static_folder=os.path.join(src_path, "static"),
                template_folder=os.path.join(src_path, "templates"))
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
        global database
        global alembic
        import src.models.entities.__all_models__
        database.init_app(app)
        alembic.init_app(app)
    except KeyError:
        raise ValueError(
            f"The config name can be either default, development, production or testing not ${config_name}")
    from src.routes.auth import auth_router
    from src.routes.main import main_router
    app.register_blueprint(auth_router, url_prefix="/auth")
    app.register_blueprint(main_router, url_prefix="/app")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app, database, alembic
