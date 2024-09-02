import os
import logging
from typing import Dict
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case
from src.infrastructure.template_reader import TemplateReader
from src.infrastructure.config_loader import ConfigLoader

class StoreGenerator(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_reader = TemplateReader(config.get('template_dir', 'src/templates'))
        frontend_config = self.config.get('frontend', {})
        self.template_path = 'frontend/store_stub.ts'
        self.output_dir = os.path.join(
            frontend_config.get('output_dir', 'frontend'),
            frontend_config.get('store_dir', 'stores')
        )
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Dict) -> Dict[str, str]:
        self.logger.debug(f"Generate method called with schema type: {type(schema)}")
        generated_files = {}

        for model in schema.get('models', []):
            self.logger.debug(f"Generating store for model: {model['name']}")
            store = self._generate_store(model)
            if store:
                generated_files.update(store)

        return generated_files

    def _generate_store(self, model: Dict) -> Dict[str, str]:
        model_name = model['name']
        self.logger.debug(f"Generating store for model: {model_name}")
        
        model_name_pascal = to_pascal_case(model_name)
        model_name_camel = to_camel_case(model_name)

        template = self.get_template(self.template_path)

        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
        }

        store_content = self.render_template(template, context)

        output_path = os.path.join(self.output_dir, f'use{model_name_pascal}Store.ts')
        return {output_path: store_content}

    def get_template(self, template_name: str) -> str:
        return self.template_reader.read_template(template_name)

    def render_template(self, template: str, context: Dict) -> str:
        for key, value in context.items():
            template = template.replace(f'{{{{${key}}}}}', str(value))
        return template