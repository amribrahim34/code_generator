from typing import List, Optional
from src.core.interfaces.project_manager import IProjectManager
from src.core.entities.project import Project
from src.core.entities.user import User
from src.infrastructure.persistence.repositories.project_repository import ProjectRepository
from src.infrastructure.persistence.repositories.user_repository import UserRepository
from src.application.services.plan_service import PlanService
from src.application.dtos.project_dtos import ProjectDTO, ProjectCreateDTO, ProjectUpdateDTO, ProjectListDTO, ModelDTO, ConfigDTO

class ProjectService(IProjectManager):
    def __init__(self, project_repository: ProjectRepository, user_repository: UserRepository, plan_service: PlanService):
        self.project_repository = project_repository
        self.user_repository = user_repository
        self.plan_service = plan_service

    async def create_project(self, user: User, name: str, description: str) -> Project:
        can_create = await self.plan_service.can_user_create_project(user)
        if not can_create:
            raise ValueError("User has reached their project limit.")
        
        project = Project(name=name, description=description, user_id=user.id)
        return await self.project_repository.create(project)

    async def get_project(self, project_id: int) -> Optional[Project]:
        return await self.project_repository.get_by_id(project_id)

    async def get_user_projects(self, user: User) -> List[Project]:
        return await self.project_repository.get_by_user_id(user.id)

    async def update_project(self, project: Project) -> Project:
        existing_project = await self.get_project(project.id)
        if not existing_project:
            raise ValueError(f"Project with id {project.id} does not exist.")
        return await self.project_repository.update(project)

    async def delete_project(self, project_id: int) -> bool:
        return await self.project_repository.delete(project_id)

    async def add_model_to_project(self, project: Project, model_data: dict) -> Project:
        project.add_model(model_data)
        return await self.update_project(project)

    async def update_project_config(self, project: Project, part: str, config: dict) -> Project:
        if part == 'backend':
            project.backend_config = config
        elif part == 'frontend':
            project.frontend_config = config
        elif part == 'mobile':
            project.mobile_config = config
        elif part == 'admin_panel':
            project.admin_panel_config = config
        else:
            raise ValueError(f"Invalid project part: {part}")
        
        return await self.update_project(project)

    async def generate_project(self, project: Project) -> bool:
        # This method would typically initiate the project generation process
        # For now, we'll just update the status
        project.status = 'generating'
        await self.update_project(project)
        return True

    async def get_project_status(self, project_id: int) -> str:
        project = await self.get_project(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} does not exist.")
        return project.status

    async def get_generated_files(self, project_id: int) -> List[str]:
        project = await self.get_project(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} does not exist.")
        # This method would typically return a list of generated file paths
        # For now, we'll return a placeholder
        return [f"{project.generation_path}/file1.py", f"{project.generation_path}/file2.py"]

    # Helper methods to convert between entities and DTOs
    def _project_to_dto(self, project: Project) -> ProjectDTO:
        return ProjectDTO(
            id=project.id,
            name=project.name,
            description=project.description,
            user_id=project.user_id,
            created_at=project.created_at,
            updated_at=project.updated_at,
            status=project.status,
            models=[ModelDTO(**model) for model in project.models],
            backend_config=ConfigDTO(**project.backend_config) if project.backend_config else None,
            frontend_config=ConfigDTO(**project.frontend_config) if project.frontend_config else None,
            mobile_config=ConfigDTO(**project.mobile_config) if project.mobile_config else None,
            admin_panel_config=ConfigDTO(**project.admin_panel_config) if project.admin_panel_config else None,
            generation_path=project.generation_path,
            is_free_plan=project.is_free_plan
        )

    def _dto_to_project(self, dto: ProjectCreateDTO, user_id: int) -> Project:
        return Project(
            name=dto.name,
            description=dto.description,
            user_id=user_id,
            models=[model.dict() for model in dto.models],
            backend_config=dto.backend_config.dict(),
            frontend_config=dto.frontend_config.dict() if dto.frontend_config else None,
            mobile_config=dto.mobile_config.dict() if dto.mobile_config else None,
            admin_panel_config=dto.admin_panel_config.dict() if dto.admin_panel_config else None
        )

    # Additional methods to handle DTOs
    async def create_project_from_dto(self, user: User, dto: ProjectCreateDTO) -> ProjectDTO:
        project = self._dto_to_project(dto, user.id)
        created_project = await self.create_project(user, project.name, project.description)
        created_project.models = project.models
        created_project.backend_config = project.backend_config
        created_project.frontend_config = project.frontend_config
        created_project.mobile_config = project.mobile_config
        created_project.admin_panel_config = project.admin_panel_config
        updated_project = await self.update_project(created_project)
        return self._project_to_dto(updated_project)

    async def update_project_from_dto(self, project_id: int, dto: ProjectUpdateDTO) -> ProjectDTO:
        project = await self.get_project(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} does not exist.")
        
        for field, value in dto.dict(exclude_unset=True).items():
            setattr(project, field, value)
        
        updated_project = await self.update_project(project)
        return self._project_to_dto(updated_project)

    async def get_user_projects_dto(self, user: User, page: int = 1, per_page: int = 10) -> ProjectListDTO:
        projects = await self.get_user_projects(user)
        total = len(projects)
        start = (page - 1) * per_page
        end = start + per_page
        paginated_projects = projects[start:end]
        
        return ProjectListDTO(
            projects=[self._project_to_dto(project) for project in paginated_projects],
            total=total,
            page=page,
            per_page=per_page
        )

    async def get_project_dto(self, project_id: int) -> ProjectDTO:
        project = await self.get_project(project_id)
        if not project:
            raise ValueError(f"Project with id {project_id} does not exist.")
        return self._project_to_dto(project)