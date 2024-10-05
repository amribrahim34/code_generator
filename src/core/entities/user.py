from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_subscribed = Column(Boolean, default=False)

    # Relationship with projects (assuming one-to-many)
    projects = relationship("Project", back_populates="user")

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def subscribe(self):
        self.is_subscribed = True

    def unsubscribe(self):
        self.is_subscribed = False

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def can_create_project(self) -> bool:
        if self.is_subscribed:
            return True
        return self.projects.count() < 1  # Free users can create only one project

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active,
            'is_subscribed': self.is_subscribed
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        user = cls(
            username=data['username'],
            email=data['email']
        )
        user.id = data.get('id')
        user.created_at = datetime.fromisoformat(data['created_at'])
        user.is_active = data['is_active']
        user.is_subscribed = data['is_subscribed']
        return user