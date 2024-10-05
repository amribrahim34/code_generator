from typing import List, Optional
from decimal import Decimal
from datetime import datetime
from src.core.interfaces.plan_manager import IPlanManager
from src.core.entities.plan import Plan
from src.core.entities.user import User
from src.infrastructure.persistence.repositories.plan_repository import PlanRepository
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.application.dtos.plan_dtos import PlanDTO, PlanCreateDTO, PlanUpdateDTO, UserPlanDTO, PlanListDTO, PlanComparisonDTO, FeatureDTO

class PlanService(IPlanManager):
    def __init__(self, plan_repository: PlanRepository, user_repository: UserRepository):
        self.plan_repository = plan_repository
        self.user_repository = user_repository

    async def create_plan(self, name: str, description: str, price: float, is_free: bool,
                          project_limit: int, features: List[str]) -> Plan:
        existing_plan = await self.get_plan_by_name(name)
        if existing_plan:
            raise ValueError(f"A plan with the name '{name}' already exists.")
        
        new_plan = Plan(name=name, description=description, price=Decimal(price),
                        is_free=is_free, project_limit=project_limit, features=features)
        return await self.plan_repository.create(new_plan)

    async def get_plan(self, plan_id: int) -> Optional[Plan]:
        return await self.plan_repository.get_by_id(plan_id)

    async def get_plan_by_name(self, name: str) -> Optional[Plan]:
        return await self.plan_repository.get_by_name(name)

    async def update_plan(self, plan: Plan) -> Plan:
        existing_plan = await self.get_plan(plan.id)
        if not existing_plan:
            raise ValueError(f"Plan with id {plan.id} does not exist.")
        return await self.plan_repository.update(plan)

    async def delete_plan(self, plan_id: int) -> bool:
        plan = await self.get_plan(plan_id)
        if not plan:
            return False
        
        users_with_plan = await self.user_repository.get_users_by_plan(plan_id)
        if users_with_plan:
            raise ValueError("Cannot delete a plan that is currently assigned to users.")
        
        return await self.plan_repository.delete(plan_id)

    async def get_all_plans(self) -> List[Plan]:
        return await self.plan_repository.get_all()

    async def assign_plan_to_user(self, user: User, plan: Plan) -> User:
        if not user or not plan:
            raise ValueError("User and plan must be valid.")
        
        user.plan = plan
        user.subscription_start_date = datetime.utcnow()
        user.subscription_end_date = None if plan.is_free else datetime.utcnow().replace(year=datetime.utcnow().year + 1)
        return await self.user_repository.update(user)

    async def get_user_plan(self, user: User) -> Plan:
        if not user:
            raise ValueError("User must be valid.")
        
        if not user.plan:
            raise ValueError("User has no assigned plan.")
        
        return user.plan

    async def can_user_access_feature(self, user: User, feature: str) -> bool:
        if not user or not user.plan:
            return False
        return feature in user.plan.features

    async def can_user_create_project(self, user: User) -> bool:
        if not user or not user.plan:
            return False
        
        if user.plan.project_limit == -1:
            return True
        
        user_projects = await self.user_repository.get_user_projects(user.id)
        return len(user_projects) < user.plan.project_limit

    async def get_plan_usage(self, user: User) -> dict:
        if not user:
            raise ValueError("User must be valid.")
        
        user_projects = await self.user_repository.get_user_projects(user.id)
        return {
            "projects_created": len(user_projects),
            "project_limit": user.plan.project_limit if user.plan else 0,
            "storage_used": sum(project.storage_used for project in user_projects),
            "storage_limit": user.plan.storage_limit if user.plan else 0
        }

    # Helper methods to convert between entities and DTOs
    def _plan_to_dto(self, plan: Plan) -> PlanDTO:
        return PlanDTO(
            id=plan.id,
            name=plan.name,
            description=plan.description,
            price=plan.price,
            is_free=plan.is_free,
            project_limit=plan.project_limit,
            features=[FeatureDTO(name=f, description=f, is_available=True) for f in plan.features]
        )

    def _dto_to_plan(self, dto: PlanCreateDTO) -> Plan:
        return Plan(
            name=dto.name,
            description=dto.description,
            price=dto.price,
            is_free=dto.is_free,
            project_limit=dto.project_limit,
            features=dto.features
        )

    # Additional methods to handle DTOs
    async def create_plan_from_dto(self, dto: PlanCreateDTO) -> PlanDTO:
        plan = self._dto_to_plan(dto)
        created_plan = await self.create_plan(
            plan.name, plan.description, float(plan.price), plan.is_free,
            plan.project_limit, plan.features
        )
        return self._plan_to_dto(created_plan)

    async def update_plan_from_dto(self, plan_id: int, dto: PlanUpdateDTO) -> PlanDTO:
        plan = await self.get_plan(plan_id)
        if not plan:
            raise ValueError(f"Plan with id {plan_id} does not exist.")
        
        for field, value in dto.dict(exclude_unset=True).items():
            setattr(plan, field, value)
        
        updated_plan = await self.update_plan(plan)
        return self._plan_to_dto(updated_plan)

    async def get_all_plans_dto(self) -> PlanListDTO:
        plans = await self.get_all_plans()
        return PlanListDTO(
            plans=[self._plan_to_dto(plan) for plan in plans],
            total=len(plans)
        )

    async def get_user_plan_dto(self, user: User) -> UserPlanDTO:
        plan = await self.get_user_plan(user)
        user_projects = await self.user_repository.get_user_projects(user.id)
        return UserPlanDTO(
            plan=self._plan_to_dto(plan),
            current_project_count=len(user_projects),
            subscription_start_date=user.subscription_start_date.isoformat() if user.subscription_start_date else None,
            subscription_end_date=user.subscription_end_date.isoformat() if user.subscription_end_date else None,
            is_active=user.is_subscription_active()
        )

    async def get_plan_comparison(self) -> PlanComparisonDTO:
        plans = await self.get_all_plans()
        all_features = set()
        for plan in plans:
            all_features.update(plan.features)
        
        return PlanComparisonDTO(
            plans=[self._plan_to_dto(plan) for plan in plans],
            features=list(all_features)
        )