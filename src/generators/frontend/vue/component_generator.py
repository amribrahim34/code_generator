from typing import Dict, Any, Union ,List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case
import logging

class ComponentGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.logger = logging.getLogger(__name__)


    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        component_types = ['List', 'Form', 'Details']
        
        for component_type in component_types:
            for model in schema.models:
                component_content = self._generate_component(model, component_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_name = f"{to_kebab_case(model_name)}-{to_kebab_case(component_type)}.vue"
                file_path = f"admin/src/components/{model_name}/{file_name}"
                generated_files[file_path] = component_content
        
        return generated_files
    

    def _generate_component(self, model: Union[Dict[str, Any], Model], component_type: str) -> str:
        context = self.prepare_context(model, component_type)
        # self.logger.warning("Generating component aaaaaa")
        template_name = f'frontend/vue/{component_type.lower()}_component.stub'
        self.logger.warning(f"Generating component , this is the template name : {template_name}")
        # return self.render_template(template, context)
        return self.template_renderer.render(template_name, context)
        

    def prepare_context(self, model: Union[Dict[str, Any], Model], component_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        
        context = {
            'model_name': model_name,
            'component_name': f"{model_name}{component_type}",
            'model_kebab': to_kebab_case(model_name),
            'attributes': attributes,
            'model_attributes': self._generate_model_attributes(attributes),
            'use_typescript': self.config_loader.get('frontend.use_typescript', True),
            'use_composition_api': self.config_loader.get('frontend.use_composition_api', True),
        }
        # self.logger.warning(f"this is the context of the component , this is the prepare_context method :{context}")
        return context

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get(f'templates.frontend.{template_name}', f'frontend/vue/{template_name}.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

    def get_output_path(self, model_name: str) -> str:
        return ""
    
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise
        
        
    def _generate_model_attributes(self, attributes: List) -> str:
        return '\n'.join([
            f'<div class="detail-item">'
            f'  <strong>{{ attribute.name }}:</strong> {{ item.{attr.name} }}'
            f'</div>'
            for attr in attributes
        ])
    
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
            'json': 'any',
            'jsonb': 'any',
            'string': 'string',
            'text': 'string',
            'time': 'string',
            'timestamp': 'string',
            'unsignedBigInteger': 'number',
            'unsignedInteger': 'number',
        }
        return type_mapping.get(db_type, 'any')