from typing import List, Optional
from pydantic import BaseModel, Field
from decimal import Decimal

class FeatureDTO(BaseModel):
    name: str
    description: str
    is_available: bool

class PlanDTO(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal = Field(..., ge=0)
    is_free: bool
    project_limit: int = Field(..., description="Number of projects allowed. -1 for unlimited.")
    features: List[FeatureDTO]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Premium Plan",
                "description": "Full access to all features",
                "price": 19.99,
                "is_free": False,
                "project_limit": -1,
                "features": [
                    {"name": "Backend Generation", "description": "Generate backend code", "is_available": True},
                    {"name": "Frontend Generation", "description": "Generate frontend code", "is_available": True},
                    {"name": "Mobile App Generation", "description": "Generate mobile app code", "is_available": True},
                    {"name": "Admin Panel Generation", "description": "Generate admin panel", "is_available": True}
                ]
            }
        }

class PlanCreateDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=200)
    price: Decimal = Field(..., ge=0)
    is_free: bool
    project_limit: int = Field(..., ge=-1)
    features: List[str]

class PlanUpdateDTO(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    price: Optional[Decimal] = Field(None, ge=0)
    is_free: Optional[bool] = None
    project_limit: Optional[int] = Field(None, ge=-1)
    features: Optional[List[str]] = None

class PlanListDTO(BaseModel):
    plans: List[PlanDTO]
    total: int

class UserPlanDTO(BaseModel):
    plan: PlanDTO
    current_project_count: int
    subscription_start_date: Optional[str] = None
    subscription_end_date: Optional[str] = None
    is_active: bool

    class Config:
        schema_extra = {
            "example": {
                "plan": {
                    "id": 1,
                    "name": "Premium Plan",
                    "description": "Full access to all features",
                    "price": 19.99,
                    "is_free": False,
                    "project_limit": -1,
                    "features": [
                        {"name": "Backend Generation", "description": "Generate backend code", "is_available": True},
                        {"name": "Frontend Generation", "description": "Generate frontend code", "is_available": True},
                        {"name": "Mobile App Generation", "description": "Generate mobile app code", "is_available": True},
                        {"name": "Admin Panel Generation", "description": "Generate admin panel", "is_available": True}
                    ]
                },
                "current_project_count": 3,
                "subscription_start_date": "2023-09-01",
                "subscription_end_date": "2024-08-31",
                "is_active": True
            }
        }

class PlanComparisonDTO(BaseModel):
    plans: List[PlanDTO]
    features: List[str]