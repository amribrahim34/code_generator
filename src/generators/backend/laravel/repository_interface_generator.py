from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case

class RepositoryInterfaceGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        repository_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for repo_type in repository_types:
            for model in schema.models:
                interface_content = self._generate_interface(model, repo_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Repositories/{repo_type}/Interfaces/{model_name}RepositoryInterface.php"
                generated_files[file_path] = interface_content

        return generated_files

    def get_output_path(self, model_name: str ) -> str:
        return f"backend/app/Repositories/{repo_type}/Interfaces/{model_name}RepositoryInterface.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/repository_interface.stub', context)


    def _generate_interface(self, model: Union[Dict[str, Any], Model], repo_type: str) -> str:
        context = self.prepare_context(model, repo_type)
        template = self.get_template('repository_interface')
        return self.template_renderer.render('backend/laravel/repository_interface.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], repo_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'interface_name': f"{model_name}RepositoryInterface",
            'model_variable': to_snake_case(model_name),
            'namespace': f"App\\Repositories\\{repo_type}\\Interfaces",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'repo_type': repo_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = 'backend/laravel/repository_interface.stub'
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