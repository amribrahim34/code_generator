import os
from typing import Dict, List
from jinja2 import Template
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case, pluralize
from src.infrastructure.config_loader import ConfigLoader
from src.infrastructure.template_reader import TemplateReader
import logging

class RouteGenerator(Generator):
    def __init__(self, config: ConfigLoader , models):
        self.config = config
        frontend_config = self.config.get('frontend', {})
        self.output_dir = os.path.join(
            frontend_config.get('output_dir', 'frontend'),
            'src',
            frontend_config.get('route_dir', 'routes')
        )
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend/route_stub.ts')
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Dict) -> Dict[str, str]:
        generated_files = {}
        generated_files.update(self._generate_model_route(model))
        return generated_files

    def _generate_model_route(self, model: Dict) -> Dict[str, str]:
        model_name_pascal = to_pascal_case(model['name'])
        model_name_camel = to_camel_case(model['name'])
        model_name_plural_pascal = to_pascal_case(pluralize(model['name']))
        model_name_plural_camel = to_camel_case(pluralize(model['name']))

        template = self.get_template('route_stub.ts')
        
        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
            'MODEL_NAME_PLURAL_PASCAL': model_name_plural_pascal,
            'MODEL_NAME_PLURAL_CAMEL': model_name_plural_camel
        }
        
        route_content = self.render_template(template, context)

        output_path = os.path.join(self.output_dir, f'{model_name_camel}Routes.ts')
        return {output_path: route_content}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get(template_name, 'frontend/' + template_name)
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