from typing import Dict, Any, List
from src.core.entities.schema import Model, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize, to_camel_case
from datetime import datetime, timedelta

class MigrationGenerator:
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        
        # Arrange models before generation
        arranged_models = self._arrange_models(schema.models)
        
        for index, model in enumerate(arranged_models):
            try:
                print(f"Generating migration for model {model.name}")
                content = self._generate_migration(model)
                timestamp = (datetime.now() + timedelta(seconds=index)).strftime('%Y_%m_%d_%H%M%S')
                file_name = f"{timestamp}_create_{pluralize(to_snake_case(model.name))}_table.php"
                file_path = f"backend/database/migrations/{file_name}"
                generated_files[file_path] = content
                print(f"Successfully generated migration for {model.name}")
            except Exception as e:
                print(f"Error generating migration for model {model.name}: {str(e)}")
        
        return generated_files

    def _arrange_models(self, models: List[Model]) -> List[Model]:
        # Create a dictionary to store models and their dependencies
        model_deps = {model.name: set() for model in models}
        
        # Populate dependencies
        for model in models:
            for relationship in model.relationships:
                if relationship.type == 'belongsTo':
                    model_deps[model.name].add(relationship.related_model)
        
        # Topological sort
        arranged = []
        visited = set()
        
        def dfs(model_name):
            if model_name in visited:
                return
            visited.add(model_name)
            for dep in model_deps[model_name]:
                if dep not in visited:
                    dfs(dep)
            arranged.append(next(model for model in models if model.name == model_name))
        
        for model in models:
            if model.name not in visited:
                dfs(model.name)
        
        return arranged

    def _generate_migration(self, model: Model) -> str:
        context = self._prepare_context(model)
        template = 'backend/laravel/migration.stub'
        return self.template_renderer.render(template, context)

    def _prepare_context(self, model: Model) -> Dict[str, Any]:
        use_timestamps = self.config_loader.get('database.use_timestamps', True)
        use_soft_deletes = self.config_loader.get('database.use_soft_deletes', False)

        prepared_attributes = self._prepare_attributes(model.attributes)
        prepared_relationships = self._prepare_relationships(model.relationships)
        
        # Remove foreign key fields from attributes as they'll be handled in relationships
        foreign_keys = [rel['foreign_key'] for rel in prepared_relationships if 'foreign_key' in rel]
        
        # Remove timestamp and softDelete attributes if they're going to be added by the migration
        timestamp_fields = ['created_at', 'updated_at']
        if use_soft_deletes:
            timestamp_fields.append('deleted_at')
        
        prepared_attributes = [
            attr for attr in prepared_attributes 
            if attr['name'] not in foreign_keys and attr['name'] not in timestamp_fields
        ]

        return {
            'class_name': f"Create{pluralize(model.name)}Table",
            'table_name': pluralize(to_snake_case(model.name)),
            'attributes': prepared_attributes,
            'relationships': prepared_relationships,
            'use_soft_deletes': use_soft_deletes,
            'use_timestamps': use_timestamps,
        }

    def _prepare_attributes(self, attributes: List[Any]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if attr.name.lower() != 'id':  # Ignore the 'id' field
                attribute_dict = {
                    'name': attr.name,
                    'type': to_camel_case(attr.type),  # Convert type to camel case
                    'nullable': attr.nullable,
                    'unique': attr.unique,
                }
                
                # Only include 'default' if it's not a special field like 'created_at'
                if attr.name.lower() not in ['created_at', 'updated_at']:
                    attribute_dict['default'] = attr.default
                
                prepared_attributes.append(attribute_dict)
        
        return prepared_attributes

    def _prepare_relationships(self, relationships: List[Any]) -> List[Dict[str, Any]]:
        prepared_relationships = []
        for rel in relationships:
            if rel.type == 'belongsTo':
                prepared_relationships.append({
                    'type': rel.type,
                    'related_model': rel.related_model,
                    'foreign_key': rel.foreign_key or f"{to_snake_case(rel.related_model)}_id",
                    'foreign_key_type': 'unsignedBigInteger',  # Match the type used for 'id' in the stub
                })
        return prepared_relationships