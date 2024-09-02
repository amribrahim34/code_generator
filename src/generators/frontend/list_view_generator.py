# src/generators/frontend/list_view_generator.py

import os
from typing import Dict, List
from src.core.interfaces.generator import Generator
from src.core.models.schema import Model, Attribute
from src.core.utils.string_utils import pluralize, to_pascal_case, to_camel_case
from src.infrastructure.config_loader import ConfigLoader
from src.infrastructure.template_reader import TemplateReader
import logging
from jinja2 import Template


class ListViewGenerator(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_path = os.path.join(config.get('template_dir', 'src/templates'), 'frontend/list_view_stub.vue')
        self.output_dir = os.path.join(config.get('frontend', {}).get('output_dir', 'frontend'), 'src', 'views')
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)
        
    def generate(self, model: Model) -> Dict[str, str]:
        model_name = model['name']
        model_name_pascal = to_pascal_case(model_name)
        model_name_camel = to_camel_case(model_name)
        model_name_plural = pluralize(model_name)
        model_name_plural_camel = to_camel_case(model_name_plural)

        template = self.get_template('list_view_stub.vue')
        # logging.debug('this is the template path for the list view' , template)

        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
            'MODEL_NAME_PLURAL_CAMEL': model_name_plural_camel,
            'TABLE_COLUMNS': self._generate_table_columns(model['attributes']),
            'GLOBAL_FILTER_FIELDS': ', '.join([f"'{attr.name}'" for attr in model['attributes']]),
            'DIALOG_COMPONENT': self._generate_dialog_component(model_name_pascal, model_name_camel, len(model['attributes'])),
            'DIALOG_IMPORT': self._generate_dialog_import(model_name_pascal, len(model['attributes'])),
            'DIALOG_COMPONENT_IMPORT': self._generate_dialog_component_import(model_name_pascal, len(model['attributes']))
        }

        view_content = self.render_template(template, context)
        output_path = os.path.join(self.output_dir, f'{model_name_pascal}List.vue')
        return {output_path: view_content}

    def _generate_table_columns(self, attributes: List[Attribute]) -> str:
        columns = []
        for attr in attributes:
            columns.append(f"""
        <Column field="{attr.name}" header="{attr.name.capitalize()}">
          <template #body="{{{{ data }}}}">
            {{{{ data.{attr.name} }}}}
          </template>
        </Column>
            """)
        return '\n'.join(columns)

    def _generate_dialog_component(self, model_name_pascal: str, model_name_camel: str, attr_count: int) -> str:
        if attr_count <= 3:
            return f'<{model_name_pascal}Dialog v-model:visible="{model_name_camel}Dialog" :item="item" @save="saveItem" />'
        return ''

    def _generate_dialog_import(self, model_name_pascal: str, attr_count: int) -> str:
        if attr_count <= 3:
            return f"import {model_name_pascal}Dialog from './{model_name_pascal}Dialog.vue'"
        return ''

    def _generate_dialog_component_import(self, model_name_pascal: str, attr_count: int) -> str:
        if attr_count <= 3:
            return model_name_pascal + 'Dialog'
        return ''

    def get_template(self, template_name: str) -> str:
        # return self.config.template_reader.read_template(self.template_path)
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