from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from src.core.entities.user import User
from src.core.entities.plan import Plan
from src.core.interfaces.plan_manager import IPlanManager
from src.core.interfaces.user_manager import IUserManager
from src.infrastructure.external_services.payment_service import PaymentService
from src.core.exceptions.user_exception import UserNotFoundError
from src.core.exceptions.plan_exception import PlanNotFoundError, SubscriptionError

class SubscribeInput(BaseModel):
    plan_id: int

class ChangeSubscriptionInput(BaseModel):
    new_plan_id: int

class SubscriptionOutput(BaseModel):
    user_id: int
    plan_id: int
    plan_name: str
    subscription_status: str
    start_date: datetime
    end_date: Optional[datetime]
    is_active: bool

class ManageSubscriptions:
    """
    Use case for managing user subscriptions.
    """

    def __init__(self, plan_manager: IPlanManager, user_manager: IUserManager, payment_service: PaymentService):
        self.plan_manager = plan_manager
        self.user_manager = user_manager
        self.payment_service = payment_service

    async def subscribe(self, user: User, input_data: SubscribeInput) -> SubscriptionOutput:
        """
        Subscribe a user to a new plan.

        Args:
            user (User): The user subscribing to the plan.
            input_data (SubscribeInput): The input data containing the plan ID.

        Returns:
            SubscriptionOutput: The new subscription details.

        Raises:
            PlanNotFoundError: If the plan with the given ID doesn't exist.
            SubscriptionError: If there's an error during the subscription process.

        Swagger Schema:
            operationId: subscribeUser
            summary: Subscribe user to a plan
            description: Subscribe the authenticated user to a new plan
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/SubscribeInput'
            responses:
                '200':
                    description: Successfully subscribed to the plan
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/SubscriptionOutput'
                '404':
                    description: Plan not found
                '400':
                    description: Subscription error
        """
        plan = await self.plan_manager.get_plan(input_data.plan_id)
        if not plan:
            raise PlanNotFoundError(input_data.plan_id)

        try:
            if not plan.is_free:
                payment_successful = await self.payment_service.process_payment(user, plan)
                if not payment_successful:
                    raise SubscriptionError("Payment processing failed")

            updated_user = await self.plan_manager.assign_plan_to_user(user, plan)
            return self._create_subscription_output(updated_user, plan)
        except Exception as e:
            raise SubscriptionError(str(e))

    async def change_subscription(self, user: User, input_data: ChangeSubscriptionInput) -> SubscriptionOutput:
        """
        Change a user's subscription to a new plan.

        Args:
            user (User): The user changing the subscription.
            input_data (ChangeSubscriptionInput): The input data containing the new plan ID.

        Returns:
            SubscriptionOutput: The updated subscription details.

        Raises:
            PlanNotFoundError: If the new plan with the given ID doesn't exist.
            SubscriptionError: If there's an error during the subscription change process.

        Swagger Schema:
            operationId: changeUserSubscription
            summary: Change user's subscription
            description: Change the authenticated user's subscription to a new plan
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/ChangeSubscriptionInput'
            responses:
                '200':
                    description: Successfully changed the subscription
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/SubscriptionOutput'
                '404':
                    description: Plan not found
                '400':
                    description: Subscription change error
        """
        new_plan = await self.plan_manager.get_plan(input_data.new_plan_id)
        if not new_plan:
            raise PlanNotFoundError(input_data.new_plan_id)

        try:
            if not new_plan.is_free:
                payment_successful = await self.payment_service.update_subscription(user, new_plan)
                if not payment_successful:
                    raise SubscriptionError("Payment processing failed for the new plan")

            updated_user = await self.plan_manager.assign_plan_to_user(user, new_plan)
            return self._create_subscription_output(updated_user, new_plan)
        except Exception as e:
            raise SubscriptionError(str(e))

    async def cancel_subscription(self, user: User) -> SubscriptionOutput:
        """
        Cancel a user's current subscription.

        Args:
            user (User): The user cancelling the subscription.

        Returns:
            SubscriptionOutput: The updated subscription details (reverted to free plan).

        Raises:
            SubscriptionError: If there's an error during the cancellation process.

        Swagger Schema:
            operationId: cancelUserSubscription
            summary: Cancel user's subscription
            description: Cancel the authenticated user's current subscription
            responses:
                '200':
                    description: Successfully cancelled the subscription
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/SubscriptionOutput'
                '400':
                    description: Subscription cancellation error
        """
        try:
            await self.payment_service.cancel_subscription(user)
            free_plan = await self.plan_manager.get_free_plan()
            updated_user = await self.plan_manager.assign_plan_to_user(user, free_plan)
            return self._create_subscription_output(updated_user, free_plan)
        except Exception as e:
            raise SubscriptionError(str(e))

    async def get_current_subscription(self, user: User) -> SubscriptionOutput:
        """
        Get the current subscription details for a user.

        Args:
            user (User): The user whose subscription to retrieve.

        Returns:
            SubscriptionOutput: The current subscription details.

        Raises:
            UserNotFoundError: If the user is not found.

        Swagger Schema:
            operationId: getCurrentSubscription
            summary: Get user's current subscription
            description: Get the authenticated user's current subscription details
            responses:
                '200':
                    description: Successfully retrieved the subscription details
                    content:
                        application/json:
                            schema:
                                $ref: '#/components/schemas/SubscriptionOutput'
                '404':
                    description: User not found
        """
        if not user:
            raise UserNotFoundError()
        
        current_plan = await self.plan_manager.get_user_plan(user)
        return self._create_subscription_output(user, current_plan)

    def _create_subscription_output(self, user: User, plan: Plan) -> SubscriptionOutput:
        return SubscriptionOutput(
            user_id=user.id,
            plan_id=plan.id,
            plan_name=plan.name,
            subscription_status="active" if user.is_subscription_active() else "inactive",
            start_date=user.subscription_start_date,
            end_date=user.subscription_end_date,
            is_active=user.is_subscription_active()
        )

# Swagger schema components
components_schema = {
    "SubscribeInput": {
        "type": "object",
        "properties": {
            "plan_id": {"type": "integer"}
        },
        "required": ["plan_id"]
    },
    "ChangeSubscriptionInput": {
        "type": "object",
        "properties": {
            "new_plan_id": {"type": "integer"}
        },
        "required": ["new_plan_id"]
    },
    "SubscriptionOutput": {
        "type": "object",
        "properties": {
            "user_id": {"type": "integer"},
            "plan_id": {"type": "integer"},
            "plan_name": {"type": "string"},
            "subscription_status": {"type": "string"},
            "start_date": {"type": "string", "format": "date-time"},
            "end_date": {"type": "string", "format": "date-time", "nullable": true},
            "is_active": {"type": "boolean"}
        }
    }
}