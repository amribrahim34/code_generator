from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class RepositoryGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer


    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        repository_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for repo_type in repository_types:
            for model in schema.models:
                repository_content = self._generate_repository(model, repo_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Repositories/{repo_type}/{model_name}Repository.php"
                generated_files[file_path] = repository_content

        # Generate Repository Interface
        # interface_content = self._generate_repository_interface(model)
        # interface_path = f"backend/app/Repositories/Interfaces/{model_name}RepositoryInterface.php"
        # generated_files[interface_path] = interface_content          
        return generated_files

    def get_output_path(self, model_name: str ) -> str:
        return f"backend/app/Repositories/{model_name}Repository.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/repository.stub', context)



    def _generate_repository(self, model: Union[Dict[str, Any], Model], repo_type: str) -> str:
        context = self.prepare_context(model, repo_type)
        template = self.get_template('repository')
        return self.template_renderer.render('backend/laravel/repository.stub', context)

    def _generate_repository_interface(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self._prepare_interface_context(model)
        template = self.get_template('repository_interface')
        return self.template_renderer.render('backend/laravel/repository_interface.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], repo_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'repository_name': f"{model_name}Repository",
            'model_variable': to_snake_case(model_name),
            'namespace': f"App\\Repositories\\{repo_type}",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'interface_namespace': f"App\\Repositories\\{repo_type}\\Interfaces\\{model_name}RepositoryInterface",
            'repo_type': repo_type,
            'table_name': pluralize(to_snake_case(model_name)),
        }

    def _prepare_interface_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'interface_name': f"{model_name}RepositoryInterface",
            'model_variable': to_snake_case(model_name),
            'namespace': "App\\Repositories\\Interfaces",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
        }

    def get_template(self, template_name: str) -> str:
        if template_name == 'repository':
            template_path = self.config_loader.get('repository_template_path', 'backend/laravel/repository.stub')
        else:
            template_path = self.config_loader.get('repository_interface_template_path', 'backend/laravel/repository_interface.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")
