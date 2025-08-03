# tests/conftest.py
import pytest
from project import create_app, db

@pytest.fixture(scope='module')
def test_app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", # Use in-memory DB for tests
        "JWT_SECRET_KEY": "test-secret-key"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(test_app):
    """A test client for the app."""
    return test_app.test_client()