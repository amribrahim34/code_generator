from typing import List, Optional
from sqlalchemy.orm import Session
from src.core.entities.plan import Plan
from src.core.interfaces.plan_manager import IPlanManager
from src.infrastructure.persistence.models.plan_model import PlanModel

class PlanRepository(IPlanManager):
    def __init__(self, session: Session):
        self.session = session

    def create_plan(self, plan: Plan) -> Plan:
        plan_model = PlanModel(
            id=plan.id,
            name=plan.name,
            description=plan.description,
            price=plan.price,
            duration_days=plan.duration_days,
            max_projects=plan.max_projects,
            features=plan.features,
            is_active=plan.is_active,
            created_at=plan.created_at,
            updated_at=plan.updated_at
        )
        self.session.add(plan_model)
        self.session.commit()
        return plan

    def get_plan_by_id(self, plan_id: str) -> Optional[Plan]:
        plan_model = self.session.query(PlanModel).filter(PlanModel.id == plan_id).first()
        if plan_model:
            return Plan.from_dict(plan_model.__dict__)
        return None

    def get_plan_by_name(self, name: str) -> Optional[Plan]:
        plan_model = self.session.query(PlanModel).filter(PlanModel.name == name).first()
        if plan_model:
            return Plan.from_dict(plan_model.__dict__)
        return None

    def get_all_plans(self) -> List[Plan]:
        plan_models = self.session.query(PlanModel).all()
        return [Plan.from_dict(plan_model.__dict__) for plan_model in plan_models]

    def get_active_plans(self) -> List[Plan]:
        plan_models = self.session.query(PlanModel).filter(PlanModel.is_active == True).all()
        return [Plan.from_dict(plan_model.__dict__) for plan_model in plan_models]

    def update_plan(self, plan: Plan) -> Plan:
        plan_model = self.session.query(PlanModel).filter(PlanModel.id == plan.id).first()
        if plan_model:
            plan_model.name = plan.name
            plan_model.description = plan.description
            plan_model.price = plan.price
            plan_model.duration_days = plan.duration_days
            plan_model.max_projects = plan.max_projects
            plan_model.features = plan.features
            plan_model.is_active = plan.is_active
            plan_model.updated_at = plan.updated_at
            self.session.commit()
        return plan

    def delete_plan(self, plan_id: str) -> bool:
        plan_model = self.session.query(PlanModel).filter(PlanModel.id == plan_id).first()
        if plan_model:
            self.session.delete(plan_model)
            self.session.commit()
            return True
        return False

    def get_free_plan(self) -> Optional[Plan]:
        free_plan_model = self.session.query(PlanModel).filter(
            PlanModel.price == 0,
            PlanModel.is_active == True
        ).first()
        if free_plan_model:
            return Plan.from_dict(free_plan_model.__dict__)
        return None

    def get_subscription_plans(self) -> List[Plan]:
        subscription_plan_models = self.session.query(PlanModel).filter(
            PlanModel.price > 0,
            PlanModel.is_active == True
        ).all()
        return [Plan.from_dict(plan_model.__dict__) for plan_model in subscription_plan_models]