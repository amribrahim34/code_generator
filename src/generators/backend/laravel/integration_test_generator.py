from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class IntegrationTestsGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        test_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for test_type in test_types:
            for model in schema.models:
                test_content = self._generate_integration_test(model, test_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/tests/Integration/{test_type}/{model_name}IntegrationTest.php"
                generated_files[file_path] = test_content
                
        return generated_files


    def _generate_integration_test(self, model: Union[Dict[str, Any], Model], test_type: str) -> str:
        context = self._prepare_integration_test_context(model, test_type)
        template = self.get_template('integration_test')
        return self.template_renderer.render('backend/laravel/unit_test.stub', context)

    def _prepare_integration_test_context(self, model: Union[Dict[str, Any], Model], test_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships

        return {
            'model_name': model_name,
            'test_name': f"{model_name}IntegrationTest",
            'namespace': f"Tests\\Integration\\{test_type}",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'test_type': test_type,
            'table_name': pluralize(to_snake_case(model_name)),
            'attributes': attributes,
            'relationships': relationships,
            'model_variable': to_snake_case(model_name),
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('integration_test_template_path', 'backend/unit_test.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass