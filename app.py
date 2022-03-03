# Created by Kelvin_Clark on 3/3/2022, 11:06 AM
from src import create_app

(app, database, alembic) = create_app("development")

if __name__ == "__main__":
    app.run()
