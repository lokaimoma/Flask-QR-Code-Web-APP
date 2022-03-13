# Created by Kelvin_Clark on 3/10/22, 2:45 PM
from flask import url_for
import pytest


@pytest.mark.parametrize(argnames='path', argvalues=["/app/", "/app/generateQrCode/"])
def test_login_required(test_client, path):
    with test_client:
        response = test_client.get(path)
        assert response.status_code == 302
        assert url_for("auth.login_route") in response.headers.get("Location")
