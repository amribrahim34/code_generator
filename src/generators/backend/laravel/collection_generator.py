from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case, pluralize

class CollectionGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def get_output_path(self, model_name: str) -> str:
        return f"app/Http/Resources/{model_name}Collection.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        generated_files = {}
        collection_types = ['Admin', 'CustomerWebsite', 'MobileApp']
        
        for collection_type in collection_types:
            collection_content = self._generate_collection(model, collection_type)
            model_name = model['name'] if isinstance(model, dict) else model.name
            file_path = f"app/Http/Resources/{collection_type}/{model_name}Collection.php"
            generated_files[file_path] = collection_content
        
        return generated_files

    def _generate_collection(self, model: Union[Dict[str, Any], Model], collection_type: str) -> str:
        context = self.prepare_context(model, collection_type)
        template = self.get_template('collection')
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], collection_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'collection_name': f"{model_name}Collection",
            'namespace': f"App\\Http\\Resources\\{collection_type}",
            'resource_class': f"{model_name}Resource",
            'collection_type': collection_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('collection_template_path', 'backend/collection_stub.php')
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