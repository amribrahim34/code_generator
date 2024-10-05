from pydantic import BaseModel
from src.core.entities.user import User
from src.core.interfaces.project_manager import IProjectManager
from src.core.exceptions.project_exception import ProjectNotFoundError, ProjectDeletionError, UnauthorizedProjectAccessError

class DeleteProjectInput(BaseModel):
    project_id: int

class DeleteProjectOutput(BaseModel):
    success: bool
    message: str

class DeleteProject:
    """
    Use case for deleting an existing project.
    """

    def __init__(self, project_manager: IProjectManager):
        self.project_manager = project_manager

    async def execute(self, user: User, input_data: DeleteProjectInput) -> DeleteProjectOutput:
        """
        Delete an existing project for the given user.

        Args:
            user (User): The user requesting the project deletion.
            input_data (DeleteProjectInput): The input data containing the project ID to delete.

        Returns:
            DeleteProjectOutput: The result of the deletion operation.

        Raises:
            ProjectNotFoundError: If the project with the given ID doesn't exist.
            UnauthorizedProjectAccessError: If the user doesn't have permission to delete the project.
            ProjectDeletionError: If there's an error during project deletion.

        Swagger Schema:
            operationId: deleteProject
            summary: Delete an existing project
            description: Delete a project for the authenticated user
            parameters:
              - in: path
                name: project_id
                required: true
                schema:
                    type: integer
                description: The ID of the project to delete
            responses:
                '200':
                    description: Project deleted successfully
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/DeleteProjectOutput'
                '404':
                    description: Project not found
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
                '403':
                    description: Unauthorized access to the project
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
                '500':
                    description: Server error during project deletion
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
        """
        try:
            # Check if the project exists
            project = await self.project_manager.get_project(input_data.project_id)
            if not project:
                raise ProjectNotFoundError(input_data.project_id)

            # Check if the user has permission to delete the project
            if project.user_id != user.id:
                raise UnauthorizedProjectAccessError(user.id, input_data.project_id)

            # Perform the deletion
            success = await self.project_manager.delete_project(input_data.project_id)
            
            if success:
                return DeleteProjectOutput(
                    success=True,
                    message=f"Project {input_data.project_id} has been successfully deleted."
                )
            else:
                raise ProjectDeletionError(input_data.project_id, "Failed to delete the project for unknown reasons.")

        except ProjectNotFoundError as e:
            raise e
        except UnauthorizedProjectAccessError as e:
            raise e
        except Exception as e:
            raise ProjectDeletionError(input_data.project_id, str(e))

# Swagger schema components
components_schema = {
    "DeleteProjectInput": {
        "type": "object",
        "properties": {
            "project_id": {"type": "integer"}
        },
        "required": ["project_id"]
    },
    "DeleteProjectOutput": {
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "message": {"type": "string"}
        }
    }
}