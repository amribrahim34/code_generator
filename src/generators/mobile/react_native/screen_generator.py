from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Schema, Attribute
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_camel_case, to_kebab_case
import logging

class ScreenGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        screen_types = ['List', 'Form', 'Details']
        
        for model in schema.models:
            for screen_type in screen_types:
                screen_content = self._generate_screen(model, screen_type)
                model_name = model.name if isinstance(model, Model) else model['name']
                file_name = f"{to_pascal_case(model_name)}{screen_type}Screen.js"
                file_path = f"mobile/screens/{model_name}/{file_name}"
                generated_files[file_path] = screen_content
        
        return generated_files

    def _generate_screen(self, model: Union[Dict[str, Any], Model], screen_type: str) -> str:
        context = self.prepare_context(model, screen_type)
        template_name = f'mobile/react_native/{screen_type.lower()}_screen.stub'
        self.logger.info(f"Generating React Native {screen_type} screen, template name: {template_name}")
        return self.template_renderer.render(template_name, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], screen_type: str) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        
        context = {
            'model_name': model_name,
            'pascal_name': to_pascal_case(model_name),
            'camel_name': to_camel_case(model_name),
            'kebab_name': to_kebab_case(model_name),
            'screen_name': f"{to_pascal_case(model_name)}{screen_type}Screen",
            'attributes': self._prepare_attributes(attributes),
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
            'use_hooks': self.config_loader.get('mobile.use_hooks', True),
        }
        return context

    def _prepare_attributes(self, attributes: List[Union[Dict[str, Any], Attribute]]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if isinstance(attr, dict):
                prepared_attributes.append({
                    'name': attr['name'],
                    'type': self._map_type(attr['type']),
                    'label': to_pascal_case(attr['name'].replace('_', ' ')),
                    'is_required': attr.get('required', False),
                })
            else:
                prepared_attributes.append({
                    'name': attr.name,
                    'type': self._map_type(attr.type),
                    'label': to_pascal_case(attr.name.replace('_', ' ')),
                    'is_required': getattr(attr, 'required', False),
                })
        return prepared_attributes

    def _map_type(self, db_type: str) -> str:
        type_mapping = {
            'bigIncrements': 'number',
            'bigInteger': 'number',
            'boolean': 'boolean',
            'date': 'string',
            'dateTime': 'string',
            'decimal': 'number',
            'double': 'number',
            'float': 'number',
            'integer': 'number',
            'json': 'object',
            'jsonb': 'object',
            'string': 'string',
            'text': 'string',
            'time': 'string',
            'timestamp': 'string',
            'unsignedBigInteger': 'number',
            'unsignedInteger': 'number',
        }
        return type_mapping.get(db_type, 'any')

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get(f'templates.mobile.react_native.{template_name}', f'mobile/react_native/{template_name}.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")


    def get_output_path(self, model_name: str) -> str:
        return f"src/screens/{model_name}/"
    
    
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise
        
    