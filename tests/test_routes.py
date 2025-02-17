import pytest
from src.app.main import app
from src.database.db import get_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# tests/test_models.py
from src.app.models import User

def test_user_creation():
    user = User(username="test_user", email="test@example.com")
    assert user.username == "test_user"
    assert user.email == "test@example.com"