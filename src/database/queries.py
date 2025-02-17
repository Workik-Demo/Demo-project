from sqlalchemy.orm import Session
from src.app.models import User
from src.database.db import get_db

def get_all_users():
    db = next(get_db())
    return db.query(User).all()

def get_user_by_id(user_id: int):
    db = next(get_db())
    return db.query(User).filter(User.id == user_id).first()