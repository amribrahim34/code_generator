from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.project import Project
from src.core.entities.user import User

class IProjectManager(ABC):
    @abstractmethod
    async def create_project(self, user: User, name: str, description: str) -> Project:
        """
        Create a new project for the given user.

        Args:
            user (User): The user creating the project.
            name (str): The name of the project.
            description (str): A brief description of the project.

        Returns:
            Project: The newly created project.

        Raises:
            ValueError: If the user has reached their project limit.
        """
        pass

    @abstractmethod
    async def get_project(self, project_id: int) -> Optional[Project]:
        """
        Retrieve a project by its ID.

        Args:
            project_id (int): The ID of the project to retrieve.

        Returns:
            Optional[Project]: The requested project, or None if not found.
        """
        pass

    @abstractmethod
    async def get_user_projects(self, user: User) -> List[Project]:
        """
        Retrieve all projects for a given user.

        Args:
            user (User): The user whose projects to retrieve.

        Returns:
            List[Project]: A list of projects belonging to the user.
        """
        pass

    @abstractmethod
    async def update_project(self, project: Project) -> Project:
        """
        Update an existing project.

        Args:
            project (Project): The project with updated information.

        Returns:
            Project: The updated project.

        Raises:
            ValueError: If the project does not exist.
        """
        pass

    @abstractmethod
    async def delete_project(self, project_id: int) -> bool:
        """
        Delete a project by its ID.

        Args:
            project_id (int): The ID of the project to delete.

        Returns:
            bool: True if the project was successfully deleted, False otherwise.
        """
        pass

    @abstractmethod
    async def add_model_to_project(self, project: Project, model_data: dict) -> Project:
        """
        Add a new model to an existing project.

        Args:
            project (Project): The project to add the model to.
            model_data (dict): The data representing the new model.

        Returns:
            Project: The updated project with the new model added.
        """
        pass

    @abstractmethod
    async def update_project_config(self, project: Project, part: str, config: dict) -> Project:
        """
        Update the configuration for a specific part of the project.

        Args:
            project (Project): The project to update.
            part (str): The part of the project to update (e.g., 'backend', 'frontend').
            config (dict): The new configuration data.

        Returns:
            Project: The updated project with the new configuration.
        """
        pass

    @abstractmethod
    async def generate_project(self, project: Project) -> bool:
        """
        Initiate the project generation process.

        Args:
            project (Project): The project to generate.

        Returns:
            bool: True if the generation process was successfully initiated, False otherwise.
        """
        pass

    @abstractmethod
    async def get_project_status(self, project_id: int) -> str:
        """
        Get the current status of a project's generation process.

        Args:
            project_id (int): The ID of the project to check.

        Returns:
            str: The current status of the project (e.g., 'queued', 'generating', 'completed', 'failed').
        """
        pass

    @abstractmethod
    async def get_generated_files(self, project_id: int) -> List[str]:
        """
        Get a list of generated files for a project.

        Args:
            project_id (int): The ID of the project.

        Returns:
            List[str]: A list of file paths for the generated project files.
        """
        pass