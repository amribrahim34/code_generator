from typing import Dict, Any, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case

class ObserverGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        for model in schema.models:
            observer_content = self._generate_observer(model)
            model_name = model['name'] if isinstance(model, dict) else model.name
            file_path = f"backend/app/Observers/{model_name}Observer.php"
            generated_files[file_path] = observer_content
                    
        return generated_files

    def _generate_observer(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        template = self.get_template('observer')
        return self.template_renderer.render('backend/laravel/observer.stub', context)

    def get_output_path(self, model_name: str) -> str:
        return f"app/Observers/{model_name}Observer.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/observer.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'observer_name': f"{model_name}Observer",
            'namespace': self.config_loader.get('observer_namespace', 'App\\Observers'),
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'model_variable': to_snake_case(model_name),
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('observer_template_path', 'backend/laravel/observer.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass