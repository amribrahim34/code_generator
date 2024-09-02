from datetime import datetime
from typing import Dict, Any, List, Union
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_snake_case, to_pascal_case
from src.infrastructure.template_reader import TemplateReader
from src.core.models.schema import Model, Attribute, Relationship

class MigrationGenerator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        migration_content = self._generate_migration(model)
        timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
        model_name = model.name if isinstance(model, Model) else model['name']
        filename = f"{timestamp}_create_{to_snake_case(model_name)}s_table.php"
        return {f"database/migrations/{filename}": migration_content}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('migration_template_path', 'backend/migration_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return template.format(**context)

    def _generate_migration(self, model: Union[Dict[str, Any], Model]) -> str:
        template = self.get_template('migration')
        model_name = model.name if isinstance(model, Model) else model['name']
        table_name = f"{to_snake_case(model_name)}s"
        class_name = f"Create{to_pascal_case(model_name)}sTable"
        
        context = {
            'class_name': class_name,
            'table_name': table_name,
            'schema_up': self._generate_schema_up(model),
            'schema_down': self._generate_schema_down(table_name)
        }
        
        return self.render_template(template, context)

    def _generate_schema_up(self, model: Union[Dict[str, Any], Model]) -> str:
        schema = [
            "$table->id();",
            *self._generate_columns(model.attributes if isinstance(model, Model) else model['attributes']),
            *self._generate_foreign_keys(model),
            "$table->timestamps();"
        ]
        return '\n            '.join(schema)

    def _generate_schema_down(self, table_name: str) -> str:
        return f"Schema::dropIfExists('{table_name}');"

    def _generate_columns(self, attributes: List[Union[Dict[str, Any], Attribute]]) -> List[str]:
        columns = []
        for attr in attributes:
            name = attr.name if isinstance(attr, Attribute) else attr['name']
            attr_type = attr.type if isinstance(attr, Attribute) else attr['type']
            if name.lower() == 'id':
                continue  # Skip 'id' as it's already added
            column = f"$table->{self._map_type(attr_type)}('{name}')"
            if isinstance(attr, Attribute):
                if attr.required is False:
                    column += "->nullable()"
            else:
                if attr.get('nullable', False):
                    column += "->nullable()"
            if isinstance(attr, Attribute):
                if hasattr(attr, 'default'):
                    column += f"->default({self._format_default(attr.default)})"
            else:
                if 'default' in attr:
                    column += f"->default({self._format_default(attr['default'])})"
            column += ";"
            columns.append(column)
        return columns

    def _generate_foreign_keys(self, model: Union[Dict[str, Any], Model]) -> List[str]:
        foreign_keys = []
        relationships = model.relationships if isinstance(model, Model) else model.get('relationships', [])
        for relation in relationships:
            if isinstance(relation, Relationship):
                if relation.type == 'belongsTo':
                    related_model = to_snake_case(relation.model)
                    foreign_keys.append(f"$table->foreignId('{related_model}_id')->constrained('{related_model}s')->onDelete('cascade');")
            else:
                if relation['type'] == 'belongsTo':
                    related_model = to_snake_case(relation['model'])
                    foreign_keys.append(f"$table->foreignId('{related_model}_id')->constrained('{related_model}s')->onDelete('cascade');")
        return foreign_keys

    def _map_type(self, type: str) -> str:
        type_mapping = {
            'string': 'string',
            'integer': 'integer',
            'boolean': 'boolean',
            'text': 'text',
            'date': 'date',
            'datetime': 'dateTime',
            'float': 'float',
            'decimal': 'decimal',
            'bigIncrements': 'bigIncrements',
            'unsignedBigInteger': 'unsignedBigInteger',
            'timestamp': 'timestamp',
        }
        return type_mapping.get(type.lower(), 'string')

    def _format_default(self, default_value: Any) -> str:
        if isinstance(default_value, str):
            return f"'{default_value}'"
        elif isinstance(default_value, bool):
            return 'true' if default_value else 'false'
        else:
            return str(default_value)