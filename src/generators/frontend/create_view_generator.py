# src/generators/frontend/create_view_generator.py
import os
from typing import Dict
from src.core.interfaces.generator import Generator
from src.core.models.schema import Model
from src.core.utils.string_utils import to_pascal_case
from src.infrastructure.config_loader import ConfigLoader
from src.infrastructure.template_reader import TemplateReader
import logging
from jinja2 import Template


class CreateViewGenerator(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend/create_view_stub.vue')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'] ,'src', self.config['frontend']['view_dir'])
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Model) -> Dict[str, str]:
        model_name_pascal = to_pascal_case(model['name'])
        template = self.get_template('view_stub.vue')
        
        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
        }
        
        content = self.render_template(template, context)
        output_path = f"{self.output_dir}/{model_name_pascal}Create.vue"
        return {output_path: content}


    def get_template(self, template_name: str) -> str:
        template_path = self.config.get(template_name , 'frontend/'+template_name)
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except KeyError as e:
            missing_key = str(e).strip("'")
            available_keys = ", ".join(context.keys())
            error_message = f"Missing key '{missing_key}' in context. Available keys are: {available_keys}"
            logging.error(error_message)
            raise KeyError(error_message)