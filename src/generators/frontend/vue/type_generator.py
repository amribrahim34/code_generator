from typing import Dict, Any, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Schema, Model
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case, pluralize ,to_camel_case
import os
import logging


class TypeGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.config = config_loader.get_config()
        self.type_dir = os.path.join(
            self.config['frontend']['output_dir'],
            'src',
            self.config['frontend']['type_dir']
        )
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        # Generate individual types files for each model
        for model in schema.models:
            # self.logger.warning(f"Generating type for model: {model.name}")
            type_content = self.prepare_context(model)
            # self.logger.warning(f"Generating type for model , type content: {type_content}")
            file_path = os.path.join(self.type_dir, f"{to_kebab_case(model.name)}Type.ts")
            generated_files[file_path] = type_content

        index_file = self._generate_index_file(schema.models)
        index_file_path = os.path.join(self.type_dir, 'index.ts')
        generated_files[index_file_path] = index_file

        return generated_files
    
    
    def prepare_context(self, model: Dict) -> Dict[str, str]:
        model_name = model.name
        model_attributes = self._generate_model_attributes(model.attributes)

        # self.logger.warning(f"prepare context Generating type for model: {model_name}")
        # self.logger.warning(f"these are the attr: {model_attributes}")
        model_name_pascal = to_pascal_case(model.name)
        model_name_camel = to_camel_case(model.name)
        template = 'frontend/vue/type.stub'
        context = {
            'MODEL_NAME': model_name_pascal,
            'MODEL_ATTRIBUTES': model_attributes,
        }

        return self.render_template(template, context)

    
    def _generate_model_attributes(self, attributes: List) -> str:
        return '\n'.join([f"  {attr.name}: {self._map_type(attr.type)}" for attr in attributes])

    def _generate_index_file(self, models: List[Dict]) -> str:
        index_content = []

        for model in models:
            model_name = model.name
            export_statement = f"export type {{ {model_name}, Create{model_name}DTO, Update{model_name}DTO }} from './{model_name.lower()}Types'"
            index_content.append(export_statement)

        return "\n".join(index_content)

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
    


    def get_template(self, template_name: str) -> str:
        
        template_path = "frontend/vue/type.stub"
        return self.template_renderer.load_template(template_path)
    

    def validate_model(self, model: Model) -> None:
        if not model.name:
            raise ValueError("Model must have a name")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

    def get_output_path(self, model_name: str) -> str:
        return ""
        
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = self.template_renderer.render(template, context)
            return template
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise


    


    

    


