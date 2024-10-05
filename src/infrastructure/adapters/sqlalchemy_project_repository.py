from typing import List, Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from src.core.interfaces.project_manager import IProjectManager
from src.core.entities.project import Project, ProjectStatus, ProjectPart
from src.core.entities.user import User

class SQLAlchemyProjectRepository(IProjectManager):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_project(self, user: User, name: str, description: str) -> Project:
        async with self.session.begin():
            project = Project(name=name, description=description, user_id=user.id, is_free_plan=user.is_free_plan)
            self.session.add(project)
            await self.session.flush()
            return project

    async def get_project(self, project_id: int) -> Optional[Project]:
        async with self.session.begin():
            result = await self.session.execute(select(Project).filter(Project.id == project_id))
            return result.scalar_one_or_none()

    async def get_user_projects(self, user: User) -> List[Project]:
        async with self.session.begin():
            result = await self.session.execute(select(Project).filter(Project.user_id == user.id))
            return result.scalars().all()

    async def update_project(self, project: Project) -> Project:
        async with self.session.begin():
            await self.session.merge(project)
            return project

    async def delete_project(self, project_id: int) -> bool:
        async with self.session.begin():
            result = await self.session.execute(delete(Project).where(Project.id == project_id))
            return result.rowcount > 0

    async def add_model_to_project(self, project: Project, model_data: dict) -> Project:
        async with self.session.begin():
            project.add_model(model_data)
            await self.session.merge(project)
            return project

    async def update_project_config(self, project: Project, part: str, config: dict) -> Project:
        async with self.session.begin():
            project.update_config(ProjectPart(part), config)
            await self.session.merge(project)
            return project

    async def generate_project(self, project: Project) -> bool:
        async with self.session.begin():
            project.set_status(ProjectStatus.QUEUED)
            await self.session.merge(project)
            # Here you would typically add the project to a generation queue
            # and return True if it was successfully queued
            return True

    async def get_project_status(self, project_id: int) -> str:
        async with self.session.begin():
            result = await self.session.execute(select(Project.status).filter(Project.id == project_id))
            status = result.scalar_one_or_none()
            return status.value if status else "unknown"

    async def get_generated_files(self, project_id: int) -> List[str]:
        async with self.session.begin():
            result = await self.session.execute(select(Project.generation_path).filter(Project.id == project_id))
            generation_path = result.scalar_one_or_none()
            if generation_path:
                # Here you would typically list files in the generation_path
                # For now, we'll just return the path as a placeholder
                return [generation_path]
            return []

    # Helper methods (not part of the interface)
    async def _get_project_by_id(self, project_id: int) -> Optional[Project]:
        result = await self.session.execute(select(Project).filter(Project.id == project_id))
        return result.scalar_one_or_none()