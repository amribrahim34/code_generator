from abc import ABC, abstractmethod
from typing import Dict, Any

class Generator(ABC):
    @abstractmethod
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the generator with configuration settings.

        Args:
            config (Dict[str, Any]): Configuration dictionary for the generator.
        """
        pass

    @abstractmethod
    def generate(self, model: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate code based on the provided model.

        Args:
            model (Dict[str, Any]): A dictionary representing the model structure.

        Returns:
            Dict[str, str]: A dictionary where keys are file paths and values are file contents.
        """
        pass

    @abstractmethod
    def get_template(self, template_name: str) -> str:
        """
        Retrieve the content of a template file.

        Args:
            template_name (str): The name of the template file.

        Returns:
            str: The content of the template file.
        """
        pass

    @abstractmethod
    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        """
        Render a template with the given context.

        Args:
            template (str): The template string to render.
            context (Dict[str, Any]): The context to use for rendering the template.

        Returns:
            str: The rendered template as a string.
        """
        pass