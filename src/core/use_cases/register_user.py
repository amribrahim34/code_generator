from pydantic import BaseModel, EmailStr, Field
from src.core.entities.user import User
from src.core.interfaces.user_manager import IUserManager
from src.core.interfaces.plan_manager import IPlanManager
from src.core.exceptions.user_exception import UserCreationError, UserAlreadyExistsError
from src.core.exceptions.plan_exception import PlanNotFoundError
from src.infrastructure.external_services.email_service import EmailService

class RegisterUserInput(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=1, max_length=100)

class RegisterUserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    is_active: bool
    plan_name: str

class RegisterUser:
    """
    Use case for registering a new user.
    """

    def __init__(self, user_manager: IUserManager, plan_manager: IPlanManager, email_service: EmailService):
        self.user_manager = user_manager
        self.plan_manager = plan_manager
        self.email_service = email_service

    async def execute(self, input_data: RegisterUserInput) -> RegisterUserOutput:
        """
        Register a new user with the provided information.

        Args:
            input_data (RegisterUserInput): The input data for user registration.

        Returns:
            RegisterUserOutput: The created user's information.

        Raises:
            UserAlreadyExistsError: If a user with the same username or email already exists.
            UserCreationError: If there's an error during user creation.
            PlanNotFoundError: If the default free plan is not found.

        Swagger Schema:
            operationId: registerUser
            summary: Register a new user
            description: Create a new user account with the provided information
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/RegisterUserInput'
            responses:
                '201':
                    description: User successfully registered
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/RegisterUserOutput'
                '400':
                    description: Invalid input or user already exists
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
                '500':
                    description: Server error during user registration
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    error:
                                        type: string
        """
        try:
            # Check if user already exists
            if await self.user_manager.get_user_by_username(input_data.username):
                raise UserAlreadyExistsError(username=input_data.username)
            if await self.user_manager.get_user_by_email(input_data.email):
                raise UserAlreadyExistsError(email=input_data.email)

            # Create the user
            user = await self.user_manager.register_user(
                username=input_data.username,
                email=input_data.email,
                password=input_data.password,
                full_name=input_data.full_name
            )

            # Assign the default free plan
            free_plan = await self.plan_manager.get_free_plan()
            if not free_plan:
                raise PlanNotFoundError("Default free plan not found")

            user = await self.plan_manager.assign_plan_to_user(user, free_plan)

            # Send welcome email
            await self.email_service.send_welcome_email(user.email, user.full_name)

            return RegisterUserOutput(
                id=user.id,
                username=user.username,
                email=user.email,
                full_name=user.full_name,
                is_active=user.is_active,
                plan_name=free_plan.name
            )

        except (UserAlreadyExistsError, PlanNotFoundError) as e:
            raise e
        except Exception as e:
            raise UserCreationError(str(e))

# Swagger schema components
components_schema = {
    "RegisterUserInput": {
        "type": "object",
        "properties": {
            "username": {"type": "string", "minLength": 3, "maxLength": 50},
            "email": {"type": "string", "format": "email"},
            "password": {"type": "string", "minLength": 8},
            "full_name": {"type": "string", "minLength": 1, "maxLength": 100}
        },
        "required": ["username", "email", "password", "full_name"]
    },
    "RegisterUserOutput": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "username": {"type": "string"},
            "email": {"type": "string", "format": "email"},
            "full_name": {"type": "string"},
            "is_active": {"type": "boolean"},
            "plan_name": {"type": "string"}
        }
    }
}