from typing import List, Optional
from pydantic import BaseModel, Field
from src.core.entities.project import Project
from src.core.entities.user import User
from src.core.interfaces.project_manager import IProjectManager
from src.core.interfaces.plan_manager import IPlanManager
from src.core.exceptions.project_exception import ProjectCreationError, ProjectLimitExceededError

class ModelDTO(BaseModel):
    name: str
    attributes: List[dict]
    relationships: List[dict]

class ConfigDTO(BaseModel):
    framework: str
    database: str
    features: List[str]

class CreateProjectInput(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=500)
    models: List[ModelDTO]
    backend_config: ConfigDTO
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]

class CreateProjectOutput(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    status: str
    backend_config: dict
    frontend_config: Optional[dict]
    mobile_config: Optional[dict]
    admin_panel_config: Optional[dict]

class CreateProject:
    """
    Use case for creating a new project.
    """

    def __init__(self, project_manager: IProjectManager, plan_manager: IPlanManager):
        self.project_manager = project_manager
        self.plan_manager = plan_manager

    async def execute(self, user: User, input_data: CreateProjectInput) -> CreateProjectOutput:
        """
        Create a new project for the given user.

        Args:
            user (User): The user creating the project.
            input_data (CreateProjectInput): The input data for creating the project.

        Returns:
            CreateProjectOutput: The created project data.

        Raises:
            ProjectLimitExceededError: If the user has reached their project limit.
            ProjectCreationError: If there's an error during project creation.

        Swagger Schema:
            operationId: createProject
            summary: Create a new project
            description: Create a new project for the authenticated user
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/CreateProjectInput'
            responses:
                '201':
                    description: Project created successfully
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/CreateProjectOutput'
                '400':
                    description: Invalid input or project limit exceeded
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
                '500':
                    description: Server error during project creation
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
        """
        # Check if user can create a new project
        can_create = await self.plan_manager.can_user_create_project(user)
        if not can_create:
            raise ProjectLimitExceededError(user.id, await self.plan_manager.get_project_limit(user))

        try:
            # Create the project
            project = await self.project_manager.create_project(
                user=user,
                name=input_data.name,
                description=input_data.description
            )

            # Add models to the project
            for model in input_data.models:
                await self.project_manager.add_model_to_project(project, model.dict())

            # Update project configurations
            await self.project_manager.update_project_config(project, 'backend', input_data.backend_config.dict())
            if input_data.frontend_config:
                await self.project_manager.update_project_config(project, 'frontend', input_data.frontend_config.dict())
            if input_data.mobile_config:
                await self.project_manager.update_project_config(project, 'mobile', input_data.mobile_config.dict())
            if input_data.admin_panel_config:
                await self.project_manager.update_project_config(project, 'admin_panel', input_data.admin_panel_config.dict())

            return CreateProjectOutput(
                id=project.id,
                name=project.name,
                description=project.description,
                user_id=project.user_id,
                status=project.status,
                backend_config=project.backend_config,
                frontend_config=project.frontend_config,
                mobile_config=project.mobile_config,
                admin_panel_config=project.admin_panel_config
            )

        except Exception as e:
            raise ProjectCreationError(str(e))

# Swagger schema components
components_schema = {
    "CreateProjectInput": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "minLength": 3, "maxLength": 50},
            "description": {"type": "string", "maxLength": 500},
            "models": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "attributes": {"type": "array", "items": {"type": "object"}},
                        "relationships": {"type": "array", "items": {"type": "object"}}
                    }
                }
            },
            "backend_config": {
                "type": "object",
                "properties": {
                    "framework": {"type": "string"},
                    "database": {"type": "string"},
                    "features": {"type": "array", "items": {"type": "string"}}
                }
            },
            "frontend_config": {
                "type": "object",
                "properties": {
                    "framework": {"type": "string"},
                    "features": {"type": "array", "items": {"type": "string"}}
                }
            },
            "mobile_config": {
                "type": "object",
                "properties": {
                    "framework": {"type": "string"},
                    "features": {"type": "array", "items": {"type": "string"}}
                }
            },
            "admin_panel_config": {
                "type": "object",
                "properties": {
                    "framework": {"type": "string"},
                    "features": {"type": "array", "items": {"type": "string"}}
                }
            }
        },
        "required": ["name", "description", "models", "backend_config"]
    },
    "CreateProjectOutput": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "description": {"type": "string"},
            "user_id": {"type": "integer"},
            "status": {"type": "string"},
            "backend_config": {"type": "object"},
            "frontend_config": {"type": "object"},
            "mobile_config": {"type": "object"},
            "admin_panel_config": {"type": "object"}
        }
    }
}