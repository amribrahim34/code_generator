from abc import ABC, abstractmethod
from typing import Dict, Any, Union
from src.core.entities.schema import Model

class ICodeGenerator(ABC):
    @abstractmethod
    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        """
        Generate code based on the provided model.

        Args:
            model (Union[Dict[str, Any], Model]): The model containing the necessary information for code generation.

        Returns:
            Dict[str, str]: A dictionary where keys are file paths and values are the generated code content.
        """
        pass

    @abstractmethod
    def get_template(self, template_name: str) -> str:
        """
        Get the content of a template file.

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
            template (str): The template string to be rendered.
            context (Dict[str, Any]): The context data to be used in rendering.

        Returns:
            str: The rendered template as a string.
        """
        pass

    @abstractmethod
    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        """
        Validate the provided model to ensure it contains all necessary information for this generator.

        Args:
            model (Union[Dict[str, Any], Model]): The model to validate.

        Raises:
            ValueError: If the model is invalid or missing required information.
        """
        pass

    @abstractmethod
    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        """
        Perform any necessary tasks after code generation, such as formatting or linting.

        Args:
            generated_files (Dict[str, str]): A dictionary of generated files, where keys are file paths
                                              and values are file contents.
        """
        pass

    @abstractmethod
    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        """
        Prepare the context dictionary for template rendering.

        Args:
            model (Union[Dict[str, Any], Model]): The model to prepare the context for.

        Returns:
            Dict[str, Any]: The prepared context dictionary.
        """
        pass

    @abstractmethod
    def get_output_path(self, model_name: str) -> str:
        """
        Get the output path for the generated file.

        Args:
            model_name (str): The name of the model for which the code is being generated.

        Returns:
            str: The path where the generated file should be saved.
        """
        pass
