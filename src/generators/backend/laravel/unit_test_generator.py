from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class TestGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        test_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for test_type in test_types:
            for model in schema.models:
                test_content = self._generate_test(model, test_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/tests/{test_type}/{model_name}Test.php"
                generated_files[file_path] = test_content
        
        for test_type in test_types:
            test_case_content = self._generate_test_case(test_type)
            file_path = f"backend/tests/{test_type}/TestCase.php"
            generated_files[file_path] = test_case_content

        return generated_files

    def get_output_path(self, model_name: str , test_type) -> str:
        return f"tests/{test_type}{model_name}TestCase.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/unit_test.stub', context)


    def _generate_test(self, model: Union[Dict[str, Any], Model], test_type: str) -> str:
        context = self.prepare_context(model, test_type)
        template ='backend/laravel/unit_test.stub'
        return self.template_renderer.render(template, context)

    def _generate_test_case(self, test_type: str) -> str:
        context = self._prepare_test_case_context(test_type)
        template = 'backend/laravel/unit_test.stub'
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], test_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'test_name': f"{model_name}Test",
            'namespace': f"Tests\\{test_type}",
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'test_type': test_type,
            'table_name': pluralize(to_snake_case(model_name)),
            'attributes': attributes,
        }

    def _prepare_test_case_context(self, test_type: str) -> Dict[str, Any]:
        return {
            'namespace': f"Tests\\{test_type}",
            'test_type': test_type,
        }

    def get_template(self, template_name: str) -> str:
        if template_name == 'test':
            template_path = self.config_loader.get('test_template_path', 'backend/test.stub')
        else:
            template_path = self.config_loader.get('test_case_template_path', 'backend/test_case.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")
