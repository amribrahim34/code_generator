from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.plan import Plan
from src.core.entities.user import User

class IPlanManager(ABC):
    @abstractmethod
    async def create_plan(self, name: str, description: str, price: float, is_free: bool,
                          project_limit: int, features: List[str]) -> Plan:
        """
        Create a new subscription plan.

        Args:
            name (str): The name of the plan.
            description (str): A brief description of the plan.
            price (float): The price of the plan.
            is_free (bool): Whether this is a free plan.
            project_limit (int): The maximum number of projects allowed (-1 for unlimited).
            features (List[str]): A list of features included in the plan.

        Returns:
            Plan: The newly created plan.

        Raises:
            ValueError: If a plan with the same name already exists.
        """
        pass

    @abstractmethod
    async def get_plan(self, plan_id: int) -> Optional[Plan]:
        """
        Retrieve a plan by its ID.

        Args:
            plan_id (int): The ID of the plan to retrieve.

        Returns:
            Optional[Plan]: The requested plan, or None if not found.
        """
        pass

    @abstractmethod
    async def get_plan_by_name(self, name: str) -> Optional[Plan]:
        """
        Retrieve a plan by its name.

        Args:
            name (str): The name of the plan to retrieve.

        Returns:
            Optional[Plan]: The requested plan, or None if not found.
        """
        pass

    @abstractmethod
    async def update_plan(self, plan: Plan) -> Plan:
        """
        Update an existing plan.

        Args:
            plan (Plan): The plan object with updated information.

        Returns:
            Plan: The updated plan.

        Raises:
            ValueError: If the plan does not exist.
        """
        pass

    @abstractmethod
    async def delete_plan(self, plan_id: int) -> bool:
        """
        Delete a plan by its ID.

        Args:
            plan_id (int): The ID of the plan to delete.

        Returns:
            bool: True if the plan was successfully deleted, False otherwise.

        Raises:
            ValueError: If the plan is currently assigned to users.
        """
        pass

    @abstractmethod
    async def get_all_plans(self) -> List[Plan]:
        """
        Retrieve all available plans.

        Returns:
            List[Plan]: A list of all available plans.
        """
        pass

    @abstractmethod
    async def assign_plan_to_user(self, user: User, plan: Plan) -> User:
        """
        Assign a plan to a user.

        Args:
            user (User): The user to assign the plan to.
            plan (Plan): The plan to assign.

        Returns:
            User: The updated user with the new plan assigned.

        Raises:
            ValueError: If the user or plan does not exist.
        """
        pass

    @abstractmethod
    async def get_user_plan(self, user: User) -> Plan:
        """
        Get the current plan for a user.

        Args:
            user (User): The user whose plan to retrieve.

        Returns:
            Plan: The user's current plan.

        Raises:
            ValueError: If the user does not exist or has no assigned plan.
        """
        pass

    @abstractmethod
    async def can_user_access_feature(self, user: User, feature: str) -> bool:
        """
        Check if a user's plan allows access to a specific feature.

        Args:
            user (User): The user to check.
            feature (str): The feature to check access for.

        Returns:
            bool: True if the user's plan includes the feature, False otherwise.
        """
        pass

    @abstractmethod
    async def can_user_create_project(self, user: User) -> bool:
        """
        Check if a user can create a new project based on their plan's limits.

        Args:
            user (User): The user to check.

        Returns:
            bool: True if the user can create a new project, False otherwise.
        """
        pass

    @abstractmethod
    async def get_plan_usage(self, user: User) -> dict:
        """
        Get the current usage statistics for a user's plan.

        Args:
            user (User): The user to check.

        Returns:
            dict: A dictionary containing usage statistics (e.g., projects created, storage used).
        """
        pass