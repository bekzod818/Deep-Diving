import pytest
from app import DolphinApp


@pytest.fixture
def app():
    return DolphinApp()


@pytest.fixture
def test_client(app):
    return app.test_session()
