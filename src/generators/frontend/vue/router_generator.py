from typing import Dict, Any, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Schema, Model
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case, pluralize ,to_camel_case
import os

class RouterGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.config = config_loader.get_config()
        self.routes_dir = os.path.join(
            self.config['frontend']['output_dir'],
            'src',
            self.config['frontend']['route_dir']
        )

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        # Generate individual route files for each model
        for model in schema.models:
            route_content = self.prepare_context(model)
            file_path = os.path.join(self.routes_dir, f"{to_kebab_case(model.name)}Routes.ts")
            generated_files[file_path] = route_content

        # Generate the index file that combines all routes
        index_content = self._generate_index_file(schema.models)
        index_path = os.path.join(self.routes_dir, "index.ts")
        generated_files[index_path] = index_content
        

        # Generate the base router configuration file
        router_config_content = self._generate_router_config()
        router_config_path = os.path.join(self.routes_dir, "router.ts")
        generated_files[router_config_path] = router_config_content

        return generated_files
    
    def prepare_context(self, model: Model) -> str:
        model_name = to_pascal_case(model.name)
        model_name_plural = pluralize(model_name)
        route_path = to_kebab_case(model_name_plural)
        model_name_camel = to_camel_case(model_name)

        template = 'frontend/vue/model_route.stub'
        context = {
            'MODEL_NAME_PASCAL': model_name,
            'MODEL_NAME_PLURAL_PASCAL': model_name_plural,
            'MODEL_NAME_PLURAL_KEBAB': route_path,
            'MODEL_NAME_CAMEL': model_name_camel
        }
        return self.template_renderer.render_with_custom_delimiter(template, context)

    def _generate_index_file(self, models: List[Model]) -> str:
        imports = []
        route_spreads = []

        for model in models:
            model_name = to_kebab_case(model.name)
            imports.append(f"import {model_name}Routes from './{model_name}Routes';")
            route_spreads.append(f"  ...{model_name}Routes,")

        template = 'frontend/vue/router_index.stub'
        context = {
            'imports': '\n'.join(imports),
            'route_spreads': '\n'.join(route_spreads)
        }
        return self.template_renderer.render_with_custom_delimiter(template, context)

    def _generate_router_config(self) -> str:
        template = 'frontend/vue/router_config.stub'
        return self.template_renderer.render_with_custom_delimiter(template, {})


    def get_template(self, template_name: str) -> str:
        template_paths = {
            'model_routes': 'frontend/vue/model_routes.stub',
            'index_routes': 'frontend/vue/index_routes.stub',
            'router_config': 'frontend/vue/router_config.stub'
        }
        template_path = self.config_loader.get(f'{template_name}_template_path', template_paths[template_name])
        return self.template_renderer.load_template(template_path)


    def validate_model(self, model: Model) -> None:
        if not model.name:
            raise ValueError("Model must have a name")


    def get_output_path(self, model_name: str) -> str:
        return ""
        
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise
