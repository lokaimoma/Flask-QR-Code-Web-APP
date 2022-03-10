# Created by Kelvin_Clark on 3/10/22, 2:35 PM
from pytest import fixture


@fixture()
def app():
    from src import create_app
    (app, db, alembic) = create_app(config_name="testing")
    db.create_all()
    yield app
    db.drop_all()


@fixture()
def test_client(app):
    return app.test_client()
