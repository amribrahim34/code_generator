from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional
from src.core.entities.project import Project, ProjectStatus
from src.infrastructure.database.models.project_model import ProjectModel
from src.core.interfaces.project_manager import IProjectManager

class ProjectRepository(IProjectManager):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_project(self, user_id: int, name: str, description: str) -> Project:
        new_project = ProjectModel(name=name, description=description, user_id=user_id)
        self.session.add(new_project)
        await self.session.commit()
        await self.session.refresh(new_project)
        return self._model_to_entity(new_project)

    async def get_project(self, project_id: int) -> Optional[Project]:
        result = await self.session.execute(select(ProjectModel).filter_by(id=project_id))
        project_model = result.scalars().first()
        return self._model_to_entity(project_model) if project_model else None

    async def get_user_projects(self, user_id: int) -> List[Project]:
        result = await self.session.execute(select(ProjectModel).filter_by(user_id=user_id))
        project_models = result.scalars().all()
        return [self._model_to_entity(pm) for pm in project_models]

    async def update_project(self, project: Project) -> Project:
        stmt = update(ProjectModel).where(ProjectModel.id == project.id).values(
            name=project.name,
            description=project.description,
            models=project.models,
            backend_config=project.backend_config,
            admin_panel_config=project.admin_panel_config,
            frontend_config=project.frontend_config,
            mobile_app_config=project.mobile_app_config,
            status=project.status.value,
            generation_path=project.generation_path
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return project

    async def delete_project(self, project_id: int) -> bool:
        stmt = delete(ProjectModel).where(ProjectModel.id == project_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0

    async def add_model_to_project(self, project_id: int, model_data: dict) -> Project:
        project = await self.get_project(project_id)
        if project:
            project.add_model(model_data)
            return await self.update_project(project)
        return None

    async def update_project_config(self, project_id: int, part: str, config: dict) -> Project:
        project = await self.get_project(project_id)
        if project:
            project.update_config(part, config)
            return await self.update_project(project)
        return None

    async def generate_project(self, project_id: int) -> bool:
        project = await self.get_project(project_id)
        if project:
            project.set_status(ProjectStatus.QUEUED)
            await self.update_project(project)
            return True
        return False

    async def get_project_status(self, project_id: int) -> str:
        project = await self.get_project(project_id)
        return project.status.value if project else "unknown"

    async def get_generated_files(self, project_id: int) -> List[str]:
        project = await self.get_project(project_id)
        if project and project.generation_path:
            # Here you would typically list files in the generation_path
            # For now, we'll just return the path as a placeholder
            return [project.generation_path]
        return []

    def _model_to_entity(self, model: ProjectModel) -> Project:
        return Project(
            id=model.id,
            name=model.name,
            description=model.description,
            user_id=model.user_id,
            created_at=model.created_at,
            updated_at=model.updated_at,
            models=model.models,
            backend_config=model.backend_config,
            admin_panel_config=model.admin_panel_config,
            frontend_config=model.frontend_config,
            mobile_app_config=model.mobile_app_config,
            status=ProjectStatus(model.status),
            is_free_plan=model.is_free_plan,
            generation_path=model.generation_path
        )

    def _entity_to_model(self, entity: Project) -> ProjectModel:
        return ProjectModel(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            user_id=entity.user_id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            models=entity.models,
            backend_config=entity.backend_config,
            admin_panel_config=entity.admin_panel_config,
            frontend_config=entity.frontend_config,
            mobile_app_config=entity.mobile_app_config,
            status=entity.status.value,
            is_free_plan=entity.is_free_plan,
            generation_path=entity.generation_path
        )