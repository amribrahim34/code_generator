import os
from typing import Dict, List, Any
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case
from src.infrastructure.config_loader import ConfigLoader
from src.infrastructure.template_reader import TemplateReader
import logging
from src.core.models.schema import Model, Attribute
from jinja2 import Template, TemplateSyntaxError

class ModalComponentGenerator(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend/modal_component_stub.vue')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'], 'src', self.config['frontend']['component_dir'])
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Dict) -> Dict[str, str]:
        model_name_pascal = to_pascal_case(model['name'])
        model_name_camel = to_camel_case(model['name'])
        template = self.get_template('modal_component_stub.vue')
        
        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
            'FORM_FIELDS': self._generate_form_fields(model['attributes'])
        }
        
        content = self.render_template(template, context)
        output_path = f"{self.output_dir}/{model_name_pascal}Modal.vue"
        return {output_path: content}

    def _generate_form_fields(self, attributes: List[Attribute]) -> List[Dict[str, Any]]:
        form_fields = []
        for attr in attributes:
            field = {
                'name': attr.name,
                'type': self._map_type_to_field(attr.type),
                'required': not attr.nullable,
                'label': self._generate_label(attr.name)
            }
            
            if field['type'] == 'select':
                field['options'] = self._generate_options(attr)
            elif field['type'] == 'date':
                field['format'] = 'yyyy-MM-dd'
            
            form_fields.append(field)
        
        return form_fields

    def _map_type_to_field(self, attr_type: str) -> str:
        type_mapping = {
            'integer': 'number',
            'float': 'number',
            'decimal': 'number',
            'string': 'text',
            'text': 'textarea',
            'boolean': 'checkbox',
            'date': 'date',
            'datetime': 'datetime',
            'enum': 'select'
        }
        return type_mapping.get(attr_type.lower(), 'text')

    def _generate_label(self, name: str) -> str:
        return name.replace('_', ' ').title()

    def _generate_options(self, attr: Attribute) -> List[Dict[str, str]]:
        if hasattr(attr, 'enum_values'):
            return [{'label': value.title(), 'value': value} for value in attr.enum_values]
        return []

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get(template_name, 'frontend/' + template_name)
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict) -> str:
        try:
            jinja_template = Template(
                template,
                variable_start_string='[[',
                variable_end_string=']]',
                block_start_string='[%',
                block_end_string='%]',
                comment_start_string='[#',
                comment_end_string='#]'
            )
            return jinja_template.render(**context)
        except TemplateSyntaxError as e:
            logging.error(f"Template Syntax Error: {str(e)}")
            logging.error(f"Error on line {e.lineno}: {e.message}")
            logging.error(f"Problematic template section:\n{template.splitlines()[max(0, e.lineno-3):e.lineno+2]}")
            raise
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise