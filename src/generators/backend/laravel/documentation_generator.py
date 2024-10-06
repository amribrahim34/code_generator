from typing import Dict, Any
from src.core.entities.schema import Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class ProjectDocumentationGenerator:
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.output_dir = self.config_loader.get('output_directory', 'output')
        self.template_dir = self.config_loader.get('template_directory', 'src/templates/backend/laravel')

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        generated_files.update(self._generate_readme(schema))
        generated_files.update(self._generate_backend_docs(schema))
        generated_files.update(self._generate_customer_app_docs(schema))
        generated_files.update(self._generate_customer_website_docs(schema))
        generated_files.update(self._generate_api_docs(schema))
        generated_files.update(self._generate_database_docs(schema))
        generated_files.update(self._generate_deployment_docs(schema))
        return generated_files

    def _generate_documentation(self, template_name: str, output_file: str, context: Dict[str, Any]) -> Dict[str, str]:
        template_path = f"{self.template_dir}/{template_name}.stub"
        print(f"Attempting to render template: {template_path}")
        print(f"Context: {context}")
        try:
            rendered_content = self.template_renderer.render(template_path, context)
            print("Template rendered successfully")
        except Exception as e:
            print(f"Error rendering template: {str(e)}")
            raise
        output_path = f"{self.output_dir}/{output_file}"
        return {output_path: rendered_content}

    def _generate_readme(self, schema: Schema) -> Dict[str, str]:
        context = {
            "project_name": self.config_loader.get('project_name', "Your Project Name"),
            "documentation_files": [
                "BACKEND.md",
                "CUSTOMER_APP.md",
                "CUSTOMER_WEBSITE.md",
                "API.md",
                "DATABASE.md",
                "DEPLOYMENT.md"
            ]
        }
        print(f"README Context: {context}")  # Debug print
        return self._generate_documentation('readme', 'README.md', context)

    def _generate_backend_docs(self, schema: Schema) -> Dict[str, str]:
        context = {
            "models": [model.name for model in schema.models],
            "namespaces": ['Admin', 'CustomerWebsite', 'CustomerApp']
        }
        return self._generate_documentation('backend', 'BACKEND.md', context)

    def _generate_customer_app_docs(self, schema: Schema) -> Dict[str, str]:
        context = {"models": [model.name for model in schema.models]}
        return self._generate_documentation('customer_app', 'CUSTOMER_APP.md', context)

    def _generate_customer_website_docs(self, schema: Schema) -> Dict[str, str]:
        context = {"models": [model.name for model in schema.models]}
        return self._generate_documentation('customer_website', 'CUSTOMER_WEBSITE.md', context)

    def _generate_api_docs(self, schema: Schema) -> Dict[str, str]:
        context = {
            "models": [model.name for model in schema.models],
            "namespaces": ['Admin', 'CustomerWebsite', 'CustomerApp']
        }
        return self._generate_documentation('api', 'API.md', context)

    def _generate_database_docs(self, schema: Schema) -> Dict[str, str]:
        context = {"schema": self._prepare_schema_for_template(schema)}
        return self._generate_documentation('database', 'DATABASE.md', context)

    def _generate_deployment_docs(self, schema: Schema) -> Dict[str, str]:
        return self._generate_documentation('deployment', 'DEPLOYMENT.md', {})

    def _prepare_schema_for_template(self, schema: Schema) -> Dict[str, Any]:
        prepared_schema = {}
        for model in schema.models:
            prepared_schema[model.name] = {
                "attributes": [attr.__dict__ for attr in model.attributes],
                "relationships": [rel.__dict__ for rel in model.relationships]
            }
        return prepared_schema