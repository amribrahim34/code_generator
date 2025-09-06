from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case, pluralize

class TraitGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        trait_types = ['Filterable', 'Searchable', 'Sortable']

        for trait_type in trait_types:
            for model in schema.models:
                trait_content = self._generate_trait(model, trait_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Traits/{model_name}/{trait_type}Trait.php"
                generated_files[file_path] = trait_content

        return generated_files

    def get_output_path(self, model_name: str , trait_type ) -> str:
        return f"backend/app/Traits/{model_name}/{trait_type}Trait.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/trait.stub', context)


    def _generate_trait(self, model: Union[Dict[str, Any], Model], trait_type: str) -> str:
        context = self.prepare_context(model, trait_type)
        template = 'backend/laravel/trait.stub'
        return self.template_renderer.render(template, context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], trait_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'trait_name': f"{trait_type}Trait",
            'namespace': f"App\\Traits\\{model_name}",
            'attributes': attributes,
            'model_variable': to_snake_case(model_name),
            'trait_type': trait_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('trait_template_path', 'backend/laravel/trait.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")
