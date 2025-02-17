import pytest
from src.database.queries import get_all_users, get_user_by_id
from src.database.db import get_db

def test_get_all_users():
    users = get_all_users()
    assert isinstance(users, list)

def test_get_user_by_id():
    user = get_user_by_id(1)
    assert user is None or hasattr(user, 'id')