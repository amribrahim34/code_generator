from pydantic import BaseModel, Field
from typing import List, Optional
from src.core.entities.user import User
from src.core.entities.project import Project
from src.core.interfaces.project_manager import IProjectManager
from src.core.exceptions.project_exception import ProjectNotFoundError, UnauthorizedProjectAccessError, ProjectUpdateError

class ModelDTO(BaseModel):
    id: Optional[str]
    name: str
    attributes: List[dict]
    relationships: List[dict]

class ConfigDTO(BaseModel):
    framework: str
    database: str
    features: List[str]

class UpdateProjectInput(BaseModel):
    project_id: int
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    models: Optional[List[ModelDTO]]
    backend_config: Optional[ConfigDTO]
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]

class UpdateProjectOutput(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    status: str
    models: List[ModelDTO]
    backend_config: ConfigDTO
    frontend_config: Optional[ConfigDTO]
    mobile_config: Optional[ConfigDTO]
    admin_panel_config: Optional[ConfigDTO]

class UpdateProject:
    """
    Use case for updating an existing project.
    """

    def __init__(self, project_manager: IProjectManager):
        self.project_manager = project_manager

    async def execute(self, user: User, input_data: UpdateProjectInput) -> UpdateProjectOutput:
        """
        Update an existing project with the provided information.

        Args:
            user (User): The user updating the project.
            input_data (UpdateProjectInput): The input data for project update.

        Returns:
            UpdateProjectOutput: The updated project information.

        Raises:
            ProjectNotFoundError: If the project with the given ID doesn't exist.
            UnauthorizedProjectAccessError: If the user doesn't have permission to update the project.
            ProjectUpdateError: If there's an error during project update.

        Swagger Schema:
            operationId: updateProject
            summary: Update an existing project
            description: Update an existing project with new information
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/UpdateProjectInput'
            responses:
                '200':
                    description: Project successfully updated
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/UpdateProjectOutput'
                '404':
                    description: Project not found
                '403':
                    description: Unauthorized access to the project
                '400':
                    description: Invalid input or update error
                '500':
                    description: Server error during project update
        """
        try:
            # Fetch the existing project
            project = await self.project_manager.get_project(input_data.project_id)
            if not project:
                raise ProjectNotFoundError(input_data.project_id)

            # Check if the user has permission to update the project
            if project.user_id != user.id:
                raise UnauthorizedProjectAccessError(user.id, input_data.project_id)

            # Update project fields
            if input_data.name:
                project.name = input_data.name
            if input_data.description:
                project.description = input_data.description

            # Update models
            if input_data.models is not None:
                project.models = [model.dict() for model in input_data.models]

            # Update configurations
            if input_data.backend_config:
                project = await self.project_manager.update_project_config(project, 'backend', input_data.backend_config.dict())
            if input_data.frontend_config:
                project = await self.project_manager.update_project_config(project, 'frontend', input_data.frontend_config.dict())
            if input_data.mobile_config:
                project = await self.project_manager.update_project_config(project, 'mobile', input_data.mobile_config.dict())
            if input_data.admin_panel_config:
                project = await self.project_manager.update_project_config(project, 'admin_panel', input_data.admin_panel_config.dict())

            # Save the updated project
            updated_project = await self.project_manager.update_project(project)

            return UpdateProjectOutput(
                id=updated_project.id,
                name=updated_project.name,
                description=updated_project.description,
                user_id=updated_project.user_id,
                status=updated_project.status,
                models=[ModelDTO(**model) for model in updated_project.models],
                backend_config=ConfigDTO(**updated_project.backend_config),
                frontend_config=ConfigDTO(**updated_project.frontend_config) if updated_project.frontend_config else None,
                mobile_config=ConfigDTO(**updated_project.mobile_config) if updated_project.mobile_config else None,
                admin_panel_config=ConfigDTO(**updated_project.admin_panel_config) if updated_project.admin_panel_config else None
            )

        except (ProjectNotFoundError, UnauthorizedProjectAccessError) as e:
            raise e
        except Exception as e:
            raise ProjectUpdateError(str(e))

# Swagger schema components
components_schema = {
    "UpdateProjectInput": {
        "type": "object",
        "properties": {
            "project_id": {"type": "integer"},
            "name": {"type": "string", "minLength": 3, "maxLength": 50},
            "description": {"type": "string", "maxLength": 500},
            "models": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
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
        "required": ["project_id"]
    },
    "UpdateProjectOutput": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "description": {"type": "string"},
            "user_id": {"type": "integer"},
            "status": {"type": "string"},
            "models": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
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
        }
    }
}