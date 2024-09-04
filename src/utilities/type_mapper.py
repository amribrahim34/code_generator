from typing import List, Dict, Any

class TypeMapper:
    def __init__(self):
        self.db_to_php = {
            'integer': 'int',
            'bigint': 'int',
            'smallint': 'int',
            'string': 'string',
            'text': 'string',
            'char': 'string',
            'varchar': 'string',
            'boolean': 'bool',
            'date': '\\DateTime',
            'datetime': '\\DateTime',
            'timestamp': '\\DateTime',
            'decimal': 'float',
            'float': 'float',
            'double': 'float',
            'json': 'array',
            'array': 'array',
        }

        self.db_to_typescript = {
            'integer': 'number',
            'bigint': 'number',
            'smallint': 'number',
            'string': 'string',
            'text': 'string',
            'char': 'string',
            'varchar': 'string',
            'boolean': 'boolean',
            'date': 'Date',
            'datetime': 'Date',
            'timestamp': 'Date',
            'decimal': 'number',
            'float': 'number',
            'double': 'number',
            'json': 'any',
            'array': 'any[]',
        }

        self.db_to_laravel_migration = {
            'integer': 'integer',
            'bigint': 'bigInteger',
            'smallint': 'smallInteger',
            'string': 'string',
            'text': 'text',
            'char': 'char',
            'varchar': 'string',
            'boolean': 'boolean',
            'date': 'date',
            'datetime': 'dateTime',
            'timestamp': 'timestamp',
            'decimal': 'decimal',
            'float': 'float',
            'double': 'double',
            'json': 'json',
            'array': 'json',
        }

        self.db_to_primevue = {
            'string': 'InputText',
            'text': 'Textarea',
            'integer': 'InputNumber',
            'bigint': 'InputNumber',
            'smallint': 'InputNumber',
            'boolean': 'Checkbox',
            'date': 'Calendar',
            'datetime': 'Calendar',
            'timestamp': 'Calendar',
            'decimal': 'InputNumber',
            'float': 'InputNumber',
            'double': 'InputNumber',
            'json': 'Editor',
            'array': 'Chips',
        }

        self.db_to_react_native = {
            'string': 'TextInput',
            'text': 'TextInput',
            'integer': 'TextInput',
            'bigint': 'TextInput',
            'smallint': 'TextInput',
            'boolean': 'Switch',
            'date': 'DatePicker',
            'datetime': 'DateTimePicker',
            'timestamp': 'DateTimePicker',
            'decimal': 'TextInput',
            'float': 'TextInput',
            'double': 'TextInput',
            'json': 'TextInput',
            'array': 'TextInput',
        }

    def to_php_type(self, db_type: str) -> str:
        return self.db_to_php.get(db_type.lower(), 'mixed')

    def to_typescript_type(self, db_type: str) -> str:
        return self.db_to_typescript.get(db_type.lower(), 'any')

    def to_laravel_migration_type(self, db_type: str) -> str:
        return self.db_to_laravel_migration.get(db_type.lower(), 'string')

    def to_primevue_component(self, db_type: str) -> str:
        return self.db_to_primevue.get(db_type.lower(), 'InputText')

    def to_react_native_component(self, db_type: str) -> str:
        return self.db_to_react_native.get(db_type.lower(), 'TextInput')

    def get_primevue_v_model_type(self, db_type: str) -> str:
        return 'v-model:checked' if db_type.lower() == 'boolean' else 'v-model'

    def get_default_value(self, db_type: str) -> str:
        mapping = {
            'string': "''",
            'text': "''",
            'integer': '0',
            'bigint': '0',
            'smallint': '0',
            'boolean': 'false',
            'date': 'null',
            'datetime': 'null',
            'timestamp': 'null',
            'decimal': '0.0',
            'float': '0.0',
            'double': '0.0',
            'json': '{}',
            'array': '[]',
        }
        return mapping.get(db_type.lower(), 'null')

    def get_primevue_import_list(self, attributes: List[Dict[str, Any]]) -> List[str]:
        components = set(self.to_primevue_component(attr['type']) for attr in attributes)
        return list(components)

    def get_react_native_import_list(self, attributes: List[Dict[str, Any]]) -> List[str]:
        components = set(self.to_react_native_component(attr['type']) for attr in attributes)
        return list(components)
