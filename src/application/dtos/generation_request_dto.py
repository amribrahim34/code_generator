from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class GenerationRequestDTO:
    """
    Data Transfer Object for code generation requests.
    """
    schema_data: Dict[str, Any]
    config: Dict[str, Any]
    output_directory: str
    backend_only: bool = False
    frontend_only: bool = False
    force_overwrite: bool = False
    template_directory: Optional[str] = None

    def __post_init__(self):
        """
        Validate the DTO after initialization.
        """
        if self.backend_only and self.frontend_only:
            raise ValueError("Cannot specify both backend_only and frontend_only")

        if not self.schema_data:
            raise ValueError("schema_data must not be empty")

        if not self.config:
            raise ValueError("config must not be empty")

        if not self.output_directory:
            raise ValueError("output_directory must be specified")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the DTO to a dictionary.
        """
        return {
            "schema_data": self.schema_data,
            "config": self.config,
            "output_directory": self.output_directory,
            "backend_only": self.backend_only,
            "frontend_only": self.frontend_only,
            "force_overwrite": self.force_overwrite,
            "template_directory": self.template_directory,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GenerationRequestDTO':
        """
        Create a GenerationRequestDTO instance from a dictionary.
        """
        return cls(**data)