# Created by Kelvin_Clark on 3/10/22, 2:45 PM
from flask import url_for


def test_no_user(test_client):
    with test_client:
        response = test_client.get("/app/")
        assert response.status_code == 302
        assert url_for("auth.login_route") in response.headers.get("Location")
