# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
import os
from src import create_app

tmp_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "tmp")
(app, database, alembic) = create_app("development")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
