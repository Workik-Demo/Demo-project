import pytest
from src.app.auth import create_token, token_required
from src.app.main import app

def test_create_token():
    token = create_token(1)
    assert isinstance(token, str)
    assert len(token) > 0

def test_invalid_token():
    with app.test_client() as client:
        response = client.get('/protected', headers={
            'Authorization': 'invalid_token'
        })
        assert response.status_code == 401