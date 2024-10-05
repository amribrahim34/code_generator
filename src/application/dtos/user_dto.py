from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserDTO(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    is_active: bool
    is_subscribed: bool
    plan_name: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "created_at": "2023-09-21T14:30:00Z",
                "is_active": True,
                "is_subscribed": True,
                "plan_name": "Premium"
            }
        }

class UserCreateDTO(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserUpdateDTO(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class UserLoginDTO(BaseModel):
    username: str
    password: str

class UserPasswordChangeDTO(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=8)

class UserListDTO(BaseModel):
    users: List[UserDTO]
    total: int
    page: int
    per_page: int

class UserProfileDTO(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    is_subscribed: bool
    plan_name: Optional[str] = None
    project_count: int
    last_login: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john.doe@example.com",
                "created_at": "2023-09-21T14:30:00Z",
                "is_subscribed": True,
                "plan_name": "Premium",
                "project_count": 5,
                "last_login": "2023-09-22T10:15:00Z"
            }
        }