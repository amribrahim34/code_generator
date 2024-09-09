from typing import Dict, Any, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Schema, Model
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case
import logging

class NavigationGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        
        # Generate main navigation file
        main_nav_content = self._generate_main_navigation(schema.models)
        generated_files["mobile/components/navigation/MainNavigation.js"] = main_nav_content
        
        # Generate stack navigators for each model
        for model in schema.models:
            stack_nav_content = self._generate_stack_navigation(model)
            model_name = model.name if isinstance(model, Model) else model['name']
            file_name = f"{to_pascal_case(model_name)}StackNavigator.js"
            generated_files[f"mobile/components/navigation/{file_name}"] = stack_nav_content
        
        return generated_files

    def _generate_main_navigation(self, models: List[Model]) -> str:
        context = self.prepare_main_navigation_context(models)
        template_name = 'mobile/react_native/main_navigation.stub'
        self.logger.info(f"Generating React Native main navigation, template name: {template_name}")
        return self.template_renderer.render(template_name, context)

    def _generate_stack_navigation(self, model: Model) -> str:
        context = self.prepare_stack_navigation_context(model)
        template_name = 'mobile/react_native/stack_navigation.stub'
        self.logger.info(f"Generating React Native stack navigation for {model.name}, template name: {template_name}")
        return self.template_renderer.render(template_name, context)

    def prepare_main_navigation_context(self, models: List[Model]) -> Dict[str, Any]:
        return {
            'models': [
                {
                    'name': model.name if isinstance(model, Model) else model['name'],
                    'pascal_name': to_pascal_case(model.name if isinstance(model, Model) else model['name']),
                    'kebab_name': to_kebab_case(model.name if isinstance(model, Model) else model['name'])
                }
                for model in models
            ],
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
        }

    def prepare_stack_navigation_context(self, model: Model) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        return {
            'model_name': model_name,
            'pascal_name': to_pascal_case(model_name),
            'kebab_name': to_kebab_case(model_name),
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get(f'templates.mobile.react_native.{template_name}', f'mobile/react_native/{template_name}.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Model) -> None:
        if not model.name:
            raise ValueError("Model must have a name")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

    def get_output_path(self, file_name: str) -> str:
        return f"src/navigation/{file_name}"
    
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise
    
    def prepare_context(self, model: Union[Dict[str, Any], Model], component_type: str) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        
        context = {
            'model_name': model_name,
            'component_name': f"{model_name}{component_type}",
            'model_kebab': to_kebab_case(model_name),
            'attributes': attributes,
            'model_attributes': self._generate_model_attributes(attributes),
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
            'use_hooks': self.config_loader.get('mobile.use_hooks', True),
        }
        return context