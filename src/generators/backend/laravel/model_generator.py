from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Relationship, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class ModelGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        for model in schema.models:
            model_content = self._generate_model(model)
            file_path = f"backend/app/Models/{model.name}.php"
            generated_files[file_path] = model_content
        return generated_files

    def _generate_model(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        return self.template_renderer.render('backend/laravel/model.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        relationships = model.relationships if isinstance(model, Model) else model['relationships']

        return {
            'model_name': model_name,
            'table_name': pluralize(to_snake_case(model_name)),
            'fillable': self._get_fillable_attributes(attributes),
            'casts': self._get_casts(attributes),
            'relationships': self._prepare_relationships(relationships, model_name),
            'use_soft_deletes': self.config_loader.get('database.use_soft_deletes', False),
            'use_timestamps': self.config_loader.get('database.use_timestamps', True),
        }

    def _get_fillable_attributes(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> List[str]:
        return [
            attr.name if isinstance(attr, Attribute) else attr['name']
            for attr in attributes
            if not (isinstance(attr, Attribute) and getattr(attr, 'primary_key', False))
            and not (isinstance(attr, dict) and attr.get('primary_key', False))
        ]

    def _get_casts(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> Dict[str, str]:
        casts = {}
        for attr in attributes:
            attr_type = attr.type if isinstance(attr, Attribute) else attr['type']
            attr_name = attr.name if isinstance(attr, Attribute) else attr['name']
            
            if attr_type in ['date', 'datetime', 'boolean', 'array', 'json']:
                casts[attr_name] = attr_type
            elif attr_type == 'decimal':
                casts[attr_name] = 'decimal:2'  # You might want to make the precision configurable
        return casts

    def _prepare_relationships(self, relationships: Union[List[Dict[str, Any]], List[Relationship]], model_name: str) -> List[Dict[str, Any]]:
        prepared_relationships = []
        used_method_names = set()
        for rel in relationships:
            rel_type = rel.type if isinstance(rel, Relationship) else rel['type']
            related_model = rel.related_model if isinstance(rel, Relationship) else rel['related_model']
            
            # Handle self-referencing relationships
            if related_model == model_name:
                method_name = f"{to_snake_case(rel_type)}_{to_snake_case(related_model)}"
            else:
                method_name = to_snake_case(related_model)
            
            # Ensure unique method names
            base_method_name = method_name
            counter = 1
            while method_name in used_method_names:
                method_name = f"{base_method_name}_{counter}"
                counter += 1
            used_method_names.add(method_name)
            
            prepared_relationships.append({
                'type': rel_type,
                'related_model': related_model,
                'method_name': method_name,
                'foreign_key': getattr(rel, 'foreign_key', None) if isinstance(rel, Relationship) else rel.get('foreign_key'),
                'local_key': getattr(rel, 'local_key', None) if isinstance(rel, Relationship) else rel.get('local_key'),
            })
        return prepared_relationships

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('model_template_path', 'backend/laravel/model.stub')
        return self.template_renderer.load_template(template_path)
    
    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

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

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# model_generator = ModelGenerator(config_loader, template_renderer)
# generated_files = model_generator.generate(model)