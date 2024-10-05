from abc import ABC, abstractmethod
from typing import Optional, List
from src.core.entities.user import User
from src.core.entities.plan import Plan

class IUserManager(ABC):
    @abstractmethod
    async def register_user(self, username: str, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            username (str): The username for the new user.
            email (str): The email address for the new user.
            password (str): The password for the new user.

        Returns:
            User: The newly created user.

        Raises:
            ValueError: If the username or email is already taken.
        """
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[User]: The requested user, or None if not found.
        """
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Retrieve a user by their username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            Optional[User]: The requested user, or None if not found.
        """
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email address of the user to retrieve.

        Returns:
            Optional[User]: The requested user, or None if not found.
        """
        pass

    @abstractmethod
    async def update_user(self, user: User) -> User:
        """
        Update an existing user's information.

        Args:
            user (User): The user object with updated information.

        Returns:
            User: The updated user.

        Raises:
            ValueError: If the user does not exist.
        """
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        pass

    @abstractmethod
    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user with their username and password.

        Args:
            username (str): The username of the user to authenticate.
            password (str): The password to check.

        Returns:
            Optional[User]: The authenticated user if successful, None otherwise.
        """
        pass

    @abstractmethod
    async def change_password(self, user_id: int, old_password: str, new_password: str) -> bool:
        """
        Change a user's password.

        Args:
            user_id (int): The ID of the user whose password to change.
            old_password (str): The user's current password.
            new_password (str): The new password to set.

        Returns:
            bool: True if the password was successfully changed, False otherwise.

        Raises:
            ValueError: If the old password is incorrect.
        """
        pass

    @abstractmethod
    async def get_user_plan(self, user_id: int) -> Plan:
        """
        Get the current subscription plan for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Plan: The user's current subscription plan.
        """
        pass

    @abstractmethod
    async def update_user_plan(self, user_id: int, plan_id: int) -> User:
        """
        Update a user's subscription plan.

        Args:
            user_id (int): The ID of the user.
            plan_id (int): The ID of the new plan.

        Returns:
            User: The updated user with the new plan.

        Raises:
            ValueError: If the user or plan does not exist.
        """
        pass

    @abstractmethod
    async def get_all_users(self, page: int = 1, per_page: int = 20) -> List[User]:
        """
        Retrieve a paginated list of all users.

        Args:
            page (int): The page number to retrieve (default: 1).
            per_page (int): The number of users per page (default: 20).

        Returns:
            List[User]: A list of users for the specified page.
        """
        pass

    @abstractmethod
    async def search_users(self, query: str, page: int = 1, per_page: int = 20) -> List[User]:
        """
        Search for users based on a query string.

        Args:
            query (str): The search query (matches against username or email).
            page (int): The page number to retrieve (default: 1).
            per_page (int): The number of users per page (default: 20).

        Returns:
            List[User]: A list of users matching the search query.
        """
        pass