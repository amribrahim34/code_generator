from abc import ABC, abstractmethod
from src.core.interfaces.code_generator import ICodeGenerator


from typing import Dict, Any, List, Union
from src.core.entities.schema import Model, Attribute, Relationship ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize
import logging

class AbstractCodeGenerator(ICodeGenerator, ABC ):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        logging.info("this is the AbstractCodeGenerator")
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    @abstractmethod
    def get_template_path(self) -> str:
        pass

    def get_template(self, template_name: str) -> str:
        template_path = self.get_template_path()
        # logging.info(f"this is the template path : ${template_path}")
        return self.template_renderer.load_template(template_path)


    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        # logging.info(f"this is the template path : {context}")
        return self.template_renderer.render(template, context)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        pass
    
    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        pass
    
    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        pass
    
    def get_output_path(self, model_name: str) -> str:
        pass
