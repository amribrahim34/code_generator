from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class ProjectStatus(enum.Enum):
    NEW = "new"
    QUEUED = "queued"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"

class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    models = Column(JSON)
    backend_config = Column(JSON)
    admin_panel_config = Column(JSON)
    frontend_config = Column(JSON)
    mobile_app_config = Column(JSON)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.NEW)
    is_free_plan = Column(Boolean, default=True)
    generation_path = Column(String(255))

    # Relationship
    user = relationship("UserModel", back_populates="projects")

    def __init__(self, name: str, description: str, user_id: int, is_free_plan: bool = True):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.is_free_plan = is_free_plan
        self.models = []
        self.backend_config = {}
        self.admin_panel_config = {}
        self.frontend_config = {}
        self.mobile_app_config = {}

    def update_config(self, part: str, config: dict):
        """Update configuration for a specific part of the project."""
        config_attr = f"{part}_config"
        if hasattr(self, config_attr):
            getattr(self, config_attr).update(config)

    def add_model(self, model: dict):
        """Add a new model to the project configuration."""
        self.models.append(model)

    def update_model(self, model_id: str, updated_model: dict):
        """Update an existing model in the project configuration."""
        for i, model in enumerate(self.models):
            if model.get('id') == model_id:
                self.models[i] = updated_model
                break

    def remove_model(self, model_id: str):
        """Remove a model from the project configuration."""
        self.models = [model for model in self.models if model.get('id') != model_id]

    def set_status(self, new_status: ProjectStatus):
        """Set the project status."""
        self.status = new_status

    def is_completed(self) -> bool:
        """Check if the project generation is completed."""
        return self.status == ProjectStatus.COMPLETED

    def can_generate_part(self, part: str) -> bool:
        """Check if a specific part can be generated based on the plan."""
        if not self.is_free_plan:
            return True
        return part in ['backend', 'admin_panel']

    def set_generation_path(self, path: str):
        """Set the path where the generated project files are stored."""
        self.generation_path = path

    def to_dict(self) -> dict:
        """Convert the project to a dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "models": self.models,
            "backend_config": self.backend_config,
            "admin_panel_config": self.admin_panel_config,
            "frontend_config": self.frontend_config,
            "mobile_app_config": self.mobile_app_config,
            "status": self.status.value,
            "is_free_plan": self.is_free_plan,
            "generation_path": self.generation_path
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'ProjectModel':
        """Create a ProjectModel instance from a dictionary."""
        project = cls(
            name=data['name'],
            description=data['description'],
            user_id=data['user_id'],
            is_free_plan=data.get('is_free_plan', True)
        )
        project.id = data.get('id')
        project.created_at = datetime.fromisoformat(data['created_at'])
        project.updated_at = datetime.fromisoformat(data['updated_at'])
        project.models = data.get('models', [])
        project.backend_config = data.get('backend_config', {})
        project.admin_panel_config = data.get('admin_panel_config', {})
        project.frontend_config = data.get('frontend_config', {})
        project.mobile_app_config = data.get('mobile_app_config', {})
        project.status = ProjectStatus(data.get('status', 'new'))
        project.generation_path = data.get('generation_path')
        return project