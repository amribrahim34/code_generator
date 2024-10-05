from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import List

Base = declarative_base()

class PlanModel(Base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(500))
    price = Column(Float, nullable=False)
    billing_cycle = Column(String(20), default='monthly')  # 'monthly', 'yearly', etc.
    is_active = Column(Boolean, default=True)
    features = Column(JSON)
    limitations = Column(JSON)
    stripe_price_id = Column(String(100))  # For integration with Stripe

    # Relationship
    users = relationship("UserModel", back_populates="plan")

    def __init__(self, name: str, price: float, description: str = None):
        self.name = name
        self.price = price
        self.description = description
        self.features = []
        self.limitations = {}

    def add_feature(self, feature: str):
        if feature not in self.features:
            self.features.append(feature)

    def remove_feature(self, feature: str):
        if feature in self.features:
            self.features.remove(feature)

    def set_limitation(self, key: str, value: int):
        self.limitations[key] = value

    def get_limitation(self, key: str) -> int:
        return self.limitations.get(key, 0)

    def is_feature_available(self, feature: str) -> bool:
        return feature in self.features

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'billing_cycle': self.billing_cycle,
            'is_active': self.is_active,
            'features': self.features,
            'limitations': self.limitations,
            'stripe_price_id': self.stripe_price_id
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'PlanModel':
        plan = cls(
            name=data['name'],
            price=data['price'],
            description=data.get('description')
        )
        plan.id = data.get('id')
        plan.billing_cycle = data.get('billing_cycle', 'monthly')
        plan.is_active = data.get('is_active', True)
        plan.features = data.get('features', [])
        plan.limitations = data.get('limitations', {})
        plan.stripe_price_id = data.get('stripe_price_id')
        return plan

    def __eq__(self, other: 'PlanModel') -> bool:
        if not isinstance(other, PlanModel):
            return False
        return self.id == other.id

    def __lt__(self, other: 'PlanModel') -> bool:
        if not isinstance(other, PlanModel):
            return False
        return self.price < other.price

    def __gt__(self, other: 'PlanModel') -> bool:
        if not isinstance(other, PlanModel):
            return False
        return self.price > other.price