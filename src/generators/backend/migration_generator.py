import os
from datetime import datetime

class MigrationGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates','backend', 'migration_stub.php')

    def generate(self, model):
        migration_content = self._generate_migration(model)
        timestamp = datetime.now().strftime('%Y_%m_%d_%H%M%S')
        filename = f"{timestamp}_create_{model['name'].lower()}s_table.php"
        return {f"database/migrations/{filename}": migration_content}

    def _generate_migration(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        table_name = f"{model['name'].lower()}s"
        class_name = f"Create{model['name']}sTable"
        
        return template.format(
            class_name=class_name,
            table_name=table_name,
            schema_up=self._generate_schema_up(model),
            schema_down=self._generate_schema_down(table_name)
        )

    def _generate_schema_up(self, model):
        schema = [
            "$table->id();",
            *self._generate_columns(model['attributes']),
            *self._generate_foreign_keys(model),
            "$table->timestamps();"
        ]
        return '\n            '.join(schema)

    def _generate_schema_down(self, table_name):
        return f"Schema::dropIfExists('{table_name}');"

    def _generate_columns(self, attributes):
        columns = []
        for attr in attributes:
            if attr['name'].lower() == 'id':
                continue  # Skip 'id' as it's already added
            column = f"$table->{self._map_type(attr['type'])}('{attr['name']}')"
            if attr['type'] != 'boolean':
                column += "->nullable()"
            column += ";"
            columns.append(column)
        return columns

    def _generate_foreign_keys(self, model):
        foreign_keys = []
        for relation in model.get('relationships', []):
            if relation['type'] == 'belongsTo':
                related_model = relation['model'].lower()
                foreign_keys.append(f"$table->foreignId('{related_model}_id')->constrained('{related_model}s')->onDelete('cascade');")
        return foreign_keys

    def _map_type(self, type):
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