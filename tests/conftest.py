# Created by Kelvin_Clark on 3/10/22, 2:35 PM
from pytest import fixture


@fixture()
def app():
    from src import create_app
    (app, db, alembic) = create_app(config_name="testing")
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield app


@fixture()
def test_client(app):
    return app.test_client()


@fixture()
def test_user(app):
    with app.app_context():
        from src import database
        from src.models.entities.user import User
        from src.utils.security.password_util import hash_password
        user = User(username="tester1", email="test@qrweb.com", password=hash_password(password="password"))
        database.session.add(user)
        database.session.commit()
        database.session.refresh(user)
    return user
