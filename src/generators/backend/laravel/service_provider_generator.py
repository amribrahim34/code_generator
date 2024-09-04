from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case

class ServiceProviderGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, models: List[Union[Dict[str, Any], Model]]) -> Dict[str, str]:
        generated_files = {}
        provider_types = ['Admin', 'CustomerWebsite', 'MobileApp']
        
        for provider_type in provider_types:
            provider_content = self._generate_service_provider(models, provider_type)
            file_path = f"app/Providers/{provider_type}RepositoryServiceProvider.php"
            generated_files[file_path] = provider_content
        
        return generated_files

    def _generate_service_provider(self, models: List[Union[Dict[str, Any], Model]], provider_type: str) -> str:
        context = self._prepare_service_provider_context(models, provider_type)
        template = self.get_template('service_provider')
        return self.template_renderer.render(template, context)

    def _prepare_service_provider_context(self, models: List[Union[Dict[str, Any], Model]], provider_type: str) -> Dict[str, Any]:
        bindings = []
        for model in models:
            model_name = model['name'] if isinstance(model, dict) else model.name
            bindings.append({
                'interface': f"{model_name}RepositoryInterface",
                'implementation': f"{model_name}Repository",
            })

        return {
            'provider_name': f"{provider_type}RepositoryServiceProvider",
            'namespace': f"App\\Providers",
            'provider_type': provider_type,
            'bindings': bindings,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('service_provider_template_path', 'backend/service_provider_stub.php')
         return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        # No specific validation needed for service providers
        pass

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# service_provider_generator = ServiceProviderGenerator(config_loader, template_renderer)
# generated_files = service_provider_generator.generate(models)