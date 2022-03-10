# Created by Kelvin_Clark on 3/10/22, 3:07 PM
import pytest
from flask import url_for


def test_login_fake_user(test_client):
    with test_client:
        response = test_client.post("/auth/login", data={
            "email": "hello@mail.com",
            "password": "singMeToSleep@____"
        })
        assert url_for("auth.login_route") in response.headers.get("Location")  # Redirects to login page


def test_login_registered_user(test_client, test_user):
    with test_client:
        response = test_client.post("/auth/login", data={
            "email": test_user.email,
            "password": "password"
        }, follow_redirects=True)
        assert url_for("main.main_index") in response.request.path


@pytest.mark.parametrize(argnames="login_data",
                         argvalues=[{"email": "kel@dkdk", "password": "kdkdkd", "confirm_password": "kdkdkd",
                                     "username": "kelo"},
                                    {"email": "kel@dkdk.com", "password": "kdkdkd", "confirm_password": "dddd",
                                     "username": "kelo"},
                                    {"email": "kel@dkdk", "password": "kdkdkd", "confirm_password": "dddd",
                                     "username": "kelo"}
                                    ])
def test_register_user_malformed_form_data(test_client, login_data):
    with test_client:
        response = test_client.post("/auth/register", data=login_data, follow_redirects=True)
        assert url_for("auth.register_route") in response.request.path


def test_register_user_correct_form_data(test_client):
    with test_client:
        response = test_client.post("/auth/register", data={
            "email": "hello@hello.com",
            "password": "password",
            "confirm_password": "password",
            "username": "test_user"
        }, follow_redirects=True)
        assert url_for("main.main_index") in response.request.path
