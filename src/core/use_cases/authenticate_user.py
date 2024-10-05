from typing import Optional
from pydantic import BaseModel
from src.core.entities.user import User
from src.core.interfaces.user_manager import IUserManager
from src.core.exceptions.user_exception import UserAuthenticationError, UserInactiveError

class AuthenticateUserInput(BaseModel):
    username: str
    password: str

class AuthenticateUserOutput(BaseModel):
    user_id: int
    username: str
    email: str
    is_active: bool
    access_token: str

class AuthenticateUser:
    """
    Use case for authenticating a user.
    """

    def __init__(self, user_manager: IUserManager, token_service: 'TokenService'):
        self.user_manager = user_manager
        self.token_service = token_service

    async def execute(self, input_data: AuthenticateUserInput) -> AuthenticateUserOutput:
        """
        Authenticate a user with the provided username and password.

        Args:
            input_data (AuthenticateUserInput): The input data containing username and password.

        Returns:
            AuthenticateUserOutput: The authenticated user data and access token.

        Raises:
            UserAuthenticationError: If the authentication fails.
            UserInactiveError: If the user account is inactive.

        Swagger Schema:
            operationId: authenticateUser
            summary: Authenticate a user
            description: Authenticate a user with the provided username and password
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/AuthenticateUserInput'
            responses:
                '200':
                    description: Successfully authenticated
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/AuthenticateUserOutput'
                '401':
                    description: Authentication failed
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
                '403':
                    description: User account is inactive
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
        """
        user = await self.user_manager.authenticate_user(input_data.username, input_data.password)
        
        if user is None:
            raise UserAuthenticationError("Invalid username or password.")
        
        if not user.is_active:
            raise UserInactiveError(user.id)

        access_token = self.token_service.create_access_token(user.id)

        return AuthenticateUserOutput(
            user_id=user.id,
            username=user.username,
            email=user.email,
            is_active=user.is_active,
            access_token=access_token
        )

# Swagger schema components
components_schema = {
    "AuthenticateUserInput": {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "password": {"type": "string", "format": "password"}
        },
        "required": ["username", "password"]
    },
    "AuthenticateUserOutput": {
        "type": "object",
        "properties": {
            "user_id": {"type": "integer"},
            "username": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "is_active": {"type": "boolean"},
            "access_token": {"type": "string"}
        }
    }
}