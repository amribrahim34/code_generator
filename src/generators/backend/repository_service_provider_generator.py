import os

class RepositoryServiceProviderGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates', 'backend','repository_service_provider_stub.php')

    def generate(self, models):
        provider_content = self._generate_provider(models)
        return {"app/Providers/RepositoryServiceProvider.php": provider_content}

    def _generate_provider(self, models):
        with open(self.template_path, 'r') as file:
            template = file.read()

        bindings = self._generate_bindings(models)
        
        return template.format(bindings=bindings)

    def _generate_bindings(self, models):
        bindings = []
        for model in models:
            binding = f"$this->app->bind(\n"
            binding += f"            \\App\\Repositories\\{model['name']}RepositoryInterface::class,\n"
            binding += f"            \\App\\Repositories\\{model['name']}Repository::class\n"
            binding += f"        );"
            bindings.append(binding)
        return "\n\n        ".join(bindings)