from sqlalchemy import Column, Integer, String, DateTime
from src.database.db import Base
import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
