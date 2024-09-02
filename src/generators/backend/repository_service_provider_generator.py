from src.core.interfaces.generator import Generator
from src.infrastructure.template_reader import TemplateReader

class RepositoryServiceProviderGenerator(Generator):
    def __init__(self, config: dict):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, models: list) -> dict:
        provider_content = self._generate_provider(models)
        return {"app/Providers/RepositoryServiceProvider.php": provider_content}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('repository_service_provider_template_path', 
                                        'src/templates/backend/repository_service_provider_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: dict) -> str:
        return template.format(**context)

    def _generate_provider(self, models: list) -> str:
        template = self.get_template('repository_service_provider')
        
        context = {
            'bindings': self._generate_bindings(models),
            'namespace': self.config.get('provider_namespace', 'App\\Providers'),
            'repository_interface_namespace': self.config.get('repository_interface_namespace', 'App\\Repositories'),
            'repository_namespace': self.config.get('repository_namespace', 'App\\Repositories')
        }
        
        return self.render_template(template, context)

    def _generate_bindings(self, models: list) -> str:
        bindings = []
        for model in models:
            binding = self._generate_single_binding(model)
            bindings.append(binding)
        return "\n\n        ".join(bindings)

    def _generate_single_binding(self, model: dict) -> str:
        interface_namespace = self.config.get('repository_interface_namespace', 'App\\Repositories')
        repository_namespace = self.config.get('repository_namespace', 'App\\Repositories')
        
        return f"""$this->app->bind(
            {interface_namespace}\\{model['name']}RepositoryInterface::class,
            {repository_namespace}\\{model['name']}Repository::class
        );"""