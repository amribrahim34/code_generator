from typing import Dict, Any, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Schema, Model
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case, pluralize ,to_camel_case , to_snake_case
import os
import logging


class StoreGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.config = config_loader.get_config()
        self.store_dir = os.path.join(
            self.config['frontend']['output_dir'],
            'src',
            self.config['frontend']['store_dir']
        )
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        # Generate individual stores files for each model
        for model in schema.models:
            # self.logger.warning(f"Generating store for model: {model.name}")
            store_content = self.prepare_context(model)
            # self.logger.warning(f"Generating store for model , store content: {store_content}")
            file_path = os.path.join(self.store_dir, f"{to_camel_case(model.name)}Store.ts")
            generated_files[file_path] = store_content


        return generated_files
    
    def prepare_context(self, model: Dict) -> Dict[str, str]:     
        # Prepare model-specific variables
        model_name = model.name
        model_name_pascal = to_pascal_case(model.name)
        model_name_camel = to_camel_case(model.name)
        model_name_lowercase = model.name.lower()
        model_name_plural_lowercase = to_kebab_case(pluralize(model.name))
        model_name_plural_snake_case = to_snake_case(pluralize(model.name))
        model_name_plural_camel_case = to_camel_case(pluralize(model.name))
        
        
        
        template = 'frontend/vue/store.stub'
        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
            'MODEL_NAME': model_name,
            'MODEL_NAME_LOWERCASE': model_name_lowercase,
            'MODEL_NAME_PLURAL_LOWERCASE': model_name_plural_lowercase,
            'MODEL_NAME_PLURAL_SNAKE': model_name_plural_snake_case,
            'MODEL_NAME_PLURAL_CAMEL': model_name_plural_camel_case,
        }

        return self.render_template(template, context)
        

    def get_template(self, template_name: str) -> str:
        
        template_path = "frontend/vue/store.stub"
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
