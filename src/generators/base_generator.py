from abc import ABC, abstractmethod
from src.core.interfaces.generator import Generator
from src.infrastructure.template_reader import TemplateReader
from src.infrastructure.config_loader import ConfigLoader
from typing import Dict, Any

class BaseGenerator(Generator, ABC):
    def __init__(self, config_loader: ConfigLoader):
        self.config_loader = config_loader
        self.template_reader = TemplateReader()

    @abstractmethod
    def generate(self, model: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate the output for a given model.
        
        Args:
            model (Dict[str, Any]): The model data.
        
        Returns:
            Dict[str, str]: A dictionary where keys are file paths and values are file contents.
        """
        pass

    def get_template(self, template_name: str) -> str:
        """
        Get the content of a template file.
        
        Args:
            template_name (str): The name of the template file.
        
        Returns:
            str: The content of the template file.
        """
        template_path = self.config_loader.get(f'{template_name}_template_path', f'src/templates/backend/{template_name}_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        """
        Render a template with the given context.
        
        Args:
            template (str): The template string.
            context (Dict[str, Any]): The context to render the template with.
        
        Returns:
            str: The rendered template.
        """
        return template.format(**context)

    def get_config(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key (str): The configuration key.
            default (Any, optional): The default value if the key is not found.
        
        Returns:
            Any: The configuration value.
        """
        return self.config_loader.get(key, default)

    def generate_file_path(self, model: Dict[str, Any], file_type: str) -> str:
        """
        Generate a file path for the given model and file type.
        
        Args:
            model (Dict[str, Any]): The model data.
            file_type (str): The type of file (e.g., 'controller', 'model').
        
        Returns:
            str: The generated file path.
        """
        base_path = self.get_config(f'{file_type}_path', f"app/{file_type.capitalize()}s")
        return f"{base_path}/{model['name']}{file_type.capitalize()}.php"