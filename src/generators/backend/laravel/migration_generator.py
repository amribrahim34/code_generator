from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Relationship , Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize
from datetime import datetime

class MigrationGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    # def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
    #     generated_files = {}
    #     migration_content = self._generate_migration(model)
    #     model_name = model['name'] if isinstance(model, dict) else model.name
    #     timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
    #     file_name = f"{timestamp}_create_{pluralize(to_snake_case(model_name))}_table.php"
    #     file_path = f"database/migrations/{file_name}"
    #     generated_files[file_path] = migration_content
    #     return generated_files
    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        for model in schema.models:
            content = self._generate_migration(model)
            model_name = model['name'] if isinstance(model, dict) else model.name
            timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
            file_name = f"{timestamp}_create_{pluralize(to_snake_case(model_name))}_table.php"
            file_path = "backend/database/migrations/{file_name}"
            generated_files[file_path] = content
        return generated_files

    def get_output_path(self, model_name: str) -> str:
        timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
        return f"backend/database/migrations/{timestamp}_create_{model_name.lower()}s_table.php"


    def _generate_migration(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self.prepare_context(model)
        template = self.get_template('migration')
        return self.template_renderer.render('backend/laravel/migration.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships

        return {
            'class_name': f"Create{pluralize(model_name)}Table",
            'table_name': pluralize(to_snake_case(model_name)),
            'attributes': self._prepare_attributes(attributes),
            'relationships': self._prepare_relationships(relationships),
            'use_soft_deletes': self.config_loader.get('database.use_soft_deletes', False),
            'use_timestamps': self.config_loader.get('database.use_timestamps', True),
        }
    
    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

    def _prepare_attributes(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if isinstance(attr, dict):
                prepared_attributes.append({
                    'name': attr['name'],
                    'type': attr['type'],
                    'nullable': attr.get('nullable', True),
                    'unique': attr.get('unique', False),
                    'default': attr.get('default'),
                })
            else:
                prepared_attributes.append({
                    'name': attr.name,
                    'type': attr.type,
                    'nullable': attr.nullable,
                    'unique': attr.unique,
                    'default': attr.default,
                })
        return prepared_attributes

    def _prepare_relationships(self, relationships: Union[List[Dict[str, Any]], List[Relationship]]) -> List[Dict[str, Any]]:
        prepared_relationships = []
        for rel in relationships:
            if isinstance(rel, dict):
                prepared_relationships.append({
                    'type': rel['type'],
                    'related_model': rel['related_model'],
                    'foreign_key': rel.get('foreign_key'),
                })
            else:
                prepared_relationships.append({
                    'type': rel.type,
                    'related_model': rel.related_model,
                    'foreign_key': rel.foreign_key,
                })
        return prepared_relationships

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('migration_template_path', 'backend/laravel/migration.stub')
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

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# migration_generator = MigrationGenerator(config_loader, template_renderer)
# generated_files = migration_generator.generate(model)