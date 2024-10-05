class ProjectException(Exception):
    """Base exception for project-related errors."""

class ProjectNotFoundError(ProjectException):
    """Raised when a project is not found."""
    def __init__(self, project_id: int):
        self.project_id = project_id
        super().__init__(f"Project with ID {project_id} not found.")

class ProjectCreationError(ProjectException):
    """Raised when there's an error creating a project."""
    def __init__(self, message: str):
        super().__init__(f"Error creating project: {message}")

class ProjectUpdateError(ProjectException):
    """Raised when there's an error updating a project."""
    def __init__(self, project_id: int, message: str):
        self.project_id = project_id
        super().__init__(f"Error updating project {project_id}: {message}")

class ProjectDeletionError(ProjectException):
    """Raised when there's an error deleting a project."""
    def __init__(self, project_id: int, message: str):
        self.project_id = project_id
        super().__init__(f"Error deleting project {project_id}: {message}")

class ProjectLimitExceededError(ProjectException):
    """Raised when a user tries to create a project but has reached their limit."""
    def __init__(self, user_id: int, limit: int):
        self.user_id = user_id
        self.limit = limit
        super().__init__(f"User {user_id} has reached the project limit of {limit}.")

class InvalidProjectConfigurationError(ProjectException):
    """Raised when a project configuration is invalid."""
    def __init__(self, project_id: int, message: str):
        self.project_id = project_id
        super().__init__(f"Invalid configuration for project {project_id}: {message}")

class ProjectGenerationError(ProjectException):
    """Raised when there's an error during project generation."""
    def __init__(self, project_id: int, message: str):
        self.project_id = project_id
        super().__init__(f"Error generating project {project_id}: {message}")

class ModelValidationError(ProjectException):
    """Raised when there's an error validating a model in a project."""
    def __init__(self, project_id: int, model_name: str, message: str):
        self.project_id = project_id
        self.model_name = model_name
        super().__init__(f"Model validation error in project {project_id}, model {model_name}: {message}")

class UnauthorizedProjectAccessError(ProjectException):
    """Raised when a user tries to access a project they don't have permission for."""
    def __init__(self, user_id: int, project_id: int):
        self.user_id = user_id
        self.project_id = project_id
        super().__init__(f"User {user_id} is not authorized to access project {project_id}.")

class ProjectNameExistsError(ProjectException):
    """Raised when trying to create a project with a name that already exists for the user."""
    def __init__(self, user_id: int, project_name: str):
        self.user_id = user_id
        self.project_name = project_name
        super().__init__(f"Project name '{project_name}' already exists for user {user_id}.")