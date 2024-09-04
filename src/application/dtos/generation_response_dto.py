from dataclasses import dataclass, field
from typing import Dict, Any, List

@dataclass
class GenerationResponseDTO:
    """
    Data Transfer Object for code generation responses.
    """
    generated_files: List[Dict[str, Any]] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    statistics: Dict[str, Any] = field(default_factory=dict)

    def add_generated_file(self, file_path: str, content: str) -> None:
        """
        Add a generated file to the response.
        """
        self.generated_files.append({"path": file_path, "content": content})

    def add_warning(self, warning: str) -> None:
        """
        Add a warning message to the response.
        """
        self.warnings.append(warning)

    def add_error(self, error: str) -> None:
        """
        Add an error message to the response.
        """
        self.errors.append(error)

    def set_statistics(self, stats: Dict[str, Any]) -> None:
        """
        Set the generation statistics.
        """
        self.statistics = stats

    def is_success(self) -> bool:
        """
        Check if the generation was successful (no errors).
        """
        return len(self.errors) == 0

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the DTO to a dictionary.
        """
        return {
            "generated_files": self.generated_files,
            "warnings": self.warnings,
            "errors": self.errors,
            "statistics": self.statistics,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GenerationResponseDTO':
        """
        Create a GenerationResponseDTO instance from a dictionary.
        """
        return cls(**data)