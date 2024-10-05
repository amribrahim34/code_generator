from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class ModelDTO(BaseModel):
    id: str
    name: str
    attributes: List[Dict[str, str]]
    relationships: List[Dict[str, str]]

class ConfigDTO(BaseModel):
    framework: str
    database: str
    authentication: str
    features: List[str]

class ProjectDTO(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    created_at: datetime
    updated_at: datetime
    status: str = Field(..., description="Current status of the project (e.g., 'new', 'generating', 'completed')")
    models: List[ModelDTO]
    backend_config: ConfigDTO
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]
    generation_path: Optional[str] = Field(None, description="Path to the generated project files")
    is_free_plan: bool = Field(..., description="Indicates if the project is on a free plan")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "E-commerce Platform",
                "description": "An online marketplace for buying and selling products",
                "user_id": 42,
                "created_at": "2023-09-21T14:30:00Z",
                "updated_at": "2023-09-21T15:45:00Z",
                "status": "completed",
                "models": [
                    {
                        "id": "1",
                        "name": "Product",
                        "attributes": [
                            {"name": "title", "type": "string"},
                            {"name": "price", "type": "decimal"},
                            {"name": "description", "type": "text"}
                        ],
                        "relationships": [
                            {"name": "category", "type": "belongs_to"},
                            {"name": "reviews", "type": "has_many"}
                        ]
                    }
                ],
                "backend_config": {
                    "framework": "Laravel",
                    "database": "MySQL",
                    "authentication": "JWT",
                    "features": ["RESTful API", "Database Migrations"]
                },
                "frontend_config": {
                    "framework": "Vue.js",
                    "features": ["Vuex State Management", "Vue Router"]
                },
                "mobile_config": None,
                "admin_panel_config": {
                    "framework": "Laravel Nova",
                    "features": ["CRUD Operations", "Dashboard"]
                },
                "generation_path": "/projects/42/e-commerce-platform",
                "is_free_plan": False
            }
        }

class ProjectCreateDTO(BaseModel):
    name: str
    description: str
    models: List[ModelDTO]
    backend_config: ConfigDTO
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]

class ProjectUpdateDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    models: Optional[List[ModelDTO]]
    backend_config: Optional[ConfigDTO]
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]

class ProjectListDTO(BaseModel):
    projects: List[ProjectDTO]
    total: int
    page: int
    per_page: int