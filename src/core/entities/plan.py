from sqlalchemy import Column, Integer, String, Boolean, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import List, Dict

Base = declarative_base()

class Plan(Base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))
    price = Column(Float, nullable=False)
    is_free = Column(Boolean, default=False)
    project_limit = Column(Integer, default=-1)  # -1 means unlimited
    features = Column(JSON)

    # Relationship with users (assuming many-to-many)
    users = relationship("User", secondary="user_plans", back_populates="plans")

    def __init__(self, name: str, description: str, price: float, is_free: bool = False, 
                 project_limit: int = -1, features: List[str] = None):
        self.name = name
        self.description = description
        self.price = price
        self.is_free = is_free
        self.project_limit = project_limit
        self.features = features or []

    def has_feature(self, feature: str) -> bool:
        return feature in self.features

    def can_create_project(self, user_project_count: int) -> bool:
        if self.project_limit == -1:
            return True
        return user_project_count < self.project_limit

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_free': self.is_free,
            'project_limit': self.project_limit,
            'features': self.features
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Plan':
        plan = cls(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            is_free=data['is_free'],
            project_limit=data['project_limit'],
            features=data['features']
        )
        plan.id = data.get('id')
        return plan

    @staticmethod
    def create_free_plan() -> 'Plan':
        return Plan(
            name="Free Plan",
            description="Basic plan with limited features",
            price=0.0,
            is_free=True,
            project_limit=1,
            features=["backend", "admin_panel"]
        )

    @staticmethod
    def create_premium_plan() -> 'Plan':
        return Plan(
            name="Premium Plan",
            description="Full access to all features",
            price=19.99,
            is_free=False,
            project_limit=-1,
            features=["backend", "admin_panel", "frontend", "mobile_app"]
        )