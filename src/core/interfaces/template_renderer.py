from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

class ITemplateRenderer(ABC):
    @abstractmethod
    def load_template(self, template_name: str) -> str:
        """
        Load a template file and return its contents as a string.
        
        Args:
            template_name (str): Name of the template file (with extension)
        
        Returns:
            str: Contents of the template file as a string
        
        Raises:
            ValueError: If the template file is not found
        """
        pass

    @abstractmethod
    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Render a template file with the given context.
        
        Args:
            template_name (str): Name of the template file (with extension)
            context (Dict[str, Any]): Dictionary containing variables to be rendered in the template
        
        Returns:
            str: Rendered template as a string
        """
        pass

    @abstractmethod
    def render_string_template(self, template_string: str, context: Dict[str, Any]) -> str:
        """
        Render a template string with the given context.
        
        Args:
            template_string (str): The template as a string
            context (Dict[str, Any]): Dictionary containing variables to be rendered in the template
        
        Returns:
            str: Rendered template as a string
        """
        pass

    @abstractmethod
    def list_templates(self, extension: Optional[str] = None) -> List[str]:
        """
        List all template files in the template directory.
        
        Args:
            extension (Optional[str]): Optional file extension to filter templates
        
        Returns:
            List[str]: List of template file names
        """
        pass

    @abstractmethod
    def add_filter(self, name: str, filter_func: callable) -> None:
        """
        Add a custom filter to the template environment.
        
        Args:
            name (str): Name of the filter
            filter_func (callable): Function to be used as a filter
        """
        pass

    @abstractmethod
    def add_global(self, name: str, value: Any) -> None:
        """
        Add a global variable to the template environment.
        
        Args:
            name (str): Name of the global variable
            value (Any): Value of the global variable
        """
        pass

    @abstractmethod
    def get_template_dir(self) -> str:
        """
        Get the current template directory.

        Returns:
            str: The path to the current template directory
        """
        pass

    @abstractmethod
    def set_template_dir(self, template_dir: str) -> None:
        """
        Set a new template directory.

        Args:
            template_dir (str): The path to the new template directory
        """
        pass
