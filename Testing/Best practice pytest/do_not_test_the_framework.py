import pytest

from django.contrib.auth.models import User


# 🚨 Bad
@pytest.mark.django_db
def test_django_authentication():
    user = User.objects.create_user(username="testuser", password="testpassword")
    authenticated = user.check_password("testpassword")
    assert authenticated


from flask import Flask


def test_flask_error_handling():
    app = Flask(__name__)

    with app.test_client() as client:
        response = client.get("/nonexistent-route")
        assert response.status_code == 404
        assert "Not Found" in response.get_data(as_text=True)
