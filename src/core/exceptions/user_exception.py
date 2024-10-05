class UserException(Exception):
    """Base exception for user-related errors."""

class UserNotFoundError(UserException):
    """Raised when a user is not found."""
    def __init__(self, user_id: int = None, username: str = None, email: str = None):
        if user_id:
            super().__init__(f"User with ID {user_id} not found.")
        elif username:
            super().__init__(f"User with username '{username}' not found.")
        elif email:
            super().__init__(f"User with email '{email}' not found.")
        else:
            super().__init__("User not found.")

class UserCreationError(UserException):
    """Raised when there's an error creating a user."""
    def __init__(self, message: str):
        super().__init__(f"Error creating user: {message}")

class UserUpdateError(UserException):
    """Raised when there's an error updating a user."""
    def __init__(self, user_id: int, message: str):
        self.user_id = user_id
        super().__init__(f"Error updating user {user_id}: {message}")

class UserDeletionError(UserException):
    """Raised when there's an error deleting a user."""
    def __init__(self, user_id: int, message: str):
        self.user_id = user_id
        super().__init__(f"Error deleting user {user_id}: {message}")

class UserAuthenticationError(UserException):
    """Raised when there's an error authenticating a user."""
    def __init__(self, message: str = "Invalid username or password."):
        super().__init__(message)

class UserAlreadyExistsError(UserException):
    """Raised when trying to create a user with a username or email that already exists."""
    def __init__(self, username: str = None, email: str = None):
        if username and email:
            super().__init__(f"User with username '{username}' or email '{email}' already exists.")
        elif username:
            super().__init__(f"User with username '{username}' already exists.")
        elif email:
            super().__init__(f"User with email '{email}' already exists.")
        else:
            super().__init__("User already exists.")

class InvalidPasswordError(UserException):
    """Raised when a password doesn't meet the required criteria."""
    def __init__(self, message: str = "Password does not meet the required criteria."):
        super().__init__(message)

class EmailValidationError(UserException):
    """Raised when an email address is invalid."""
    def __init__(self, email: str):
        super().__init__(f"Invalid email address: {email}")

class UserInactiveError(UserException):
    """Raised when trying to authenticate an inactive user."""
    def __init__(self, user_id: int):
        super().__init__(f"User {user_id} is inactive.")

class UnauthorizedAccessError(UserException):
    """Raised when a user tries to access a resource they don't have permission for."""
    def __init__(self, user_id: int, resource: str):
        super().__init__(f"User {user_id} is not authorized to access {resource}.")

class PasswordChangeError(UserException):
    """Raised when there's an error changing a user's password."""
    def __init__(self, message: str = "Error changing password."):
        super().__init__(message)

class UserPlanUpdateError(UserException):
    """Raised when there's an error updating a user's subscription plan."""
    def __init__(self, user_id: int, plan_id: int, message: str):
        super().__init__(f"Error updating plan for user {user_id} to plan {plan_id}: {message}")