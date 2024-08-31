from typing import Dict, List, Union

class TypeConverter:
    def __init__(self):
        self.db_to_ts_map = {
            'bigIncrements': 'number',
            'bigInteger': 'number',
            'binary': 'string',
            'boolean': 'boolean',
            'char': 'string',
            'date': 'string',
            'dateTime': 'string',
            'dateTimeTz': 'string',
            'decimal': 'number',
            'double': 'number',
            'enum': 'string',
            'float': 'number',
            'integer': 'number',
            'ipAddress': 'string',
            'json': 'any',
            'jsonb': 'any',
            'longText': 'string',
            'macAddress': 'string',
            'mediumInteger': 'number',
            'mediumText': 'string',
            'morphs': 'number',
            'nullableMorphs': 'number | null',
            'nullableTimestamps': 'string | null',
            'rememberToken': 'string',
            'smallInteger': 'number',
            'string': 'string',
            'text': 'string',
            'time': 'string',
            'timeTz': 'string',
            'timestamp': 'string',
            'timestampTz': 'string',
            'tinyInteger': 'number',
            'unsignedBigInteger': 'number',
            'unsignedDecimal': 'number',
            'unsignedInteger': 'number',
            'unsignedMediumInteger': 'number',
            'unsignedSmallInteger': 'number',
            'unsignedTinyInteger': 'number',
            'uuid': 'string',
            'year': 'number',
        }

        self.db_to_primevue_map = {
            'bigIncrements': 'InputNumber',
            'bigInteger': 'InputNumber',
            'binary': 'InputText',
            'boolean': 'Checkbox',
            'char': 'InputText',
            'date': 'Calendar',
            'dateTime': 'Calendar',
            'dateTimeTz': 'Calendar',
            'decimal': 'InputNumber',
            'double': 'InputNumber',
            'enum': 'Dropdown',
            'float': 'InputNumber',
            'integer': 'InputNumber',
            'ipAddress': 'InputMask',
            'json': 'Textarea',
            'jsonb': 'Textarea',
            'longText': 'Textarea',
            'macAddress': 'InputMask',
            'mediumInteger': 'InputNumber',
            'mediumText': 'Textarea',
            'morphs': 'InputNumber',
            'nullableMorphs': 'InputNumber',
            'nullableTimestamps': 'Calendar',
            'rememberToken': 'InputText',
            'smallInteger': 'InputNumber',
            'string': 'InputText',
            'text': 'Textarea',
            'time': 'Calendar',
            'timeTz': 'Calendar',
            'timestamp': 'Calendar',
            'timestampTz': 'Calendar',
            'tinyInteger': 'InputNumber',
            'unsignedBigInteger': 'InputNumber',
            'unsignedDecimal': 'InputNumber',
            'unsignedInteger': 'InputNumber',
            'unsignedMediumInteger': 'InputNumber',
            'unsignedSmallInteger': 'InputNumber',
            'unsignedTinyInteger': 'InputNumber',
            'uuid': 'InputText',
            'year': 'InputNumber',
        }

    def db_to_ts(self, db_type: str) -> str:
        """Convert database type to TypeScript type"""
        return self.db_to_ts_map.get(db_type, 'any')

    def db_to_primevue(self, db_type: str) -> str:
        """Convert database type to PrimeVue component"""
        return self.db_to_primevue_map.get(db_type, 'InputText')

    def get_primevue_import_list(self, attributes: List[Dict[str, str]]) -> List[str]:
        """Get list of unique PrimeVue components to import based on attributes"""
        components = set(self.db_to_primevue(attr['type']) for attr in attributes)
        return sorted(list(components))

    def get_primevue_v_model_type(self, db_type: str) -> str:
        """Get the appropriate v-model type for PrimeVue components"""
        ts_type = self.db_to_ts(db_type)
        if ts_type == 'number':
            return 'v-model.number'
        return 'v-model'

    def get_default_value(self, db_type: str) -> Union[str, int, bool, None]:
        """Get default value for a given database type"""
        ts_type = self.db_to_ts(db_type)
        if ts_type == 'string':
            return "''"
        elif ts_type == 'number':
            return 0
        elif ts_type == 'boolean':
            return False
        elif ts_type == 'any':
            return None
        else:
            return None

def get_type_converter():
    return TypeConverter()

# Usage example
if __name__ == "__main__":
    converter = get_type_converter()
    print(converter.db_to_ts('integer'))  # Output: number
    print(converter.db_to_primevue('date'))  # Output: Calendar
    print(converter.get_primevue_import_list([
        {'name': 'id', 'type': 'bigIncrements'},
        {'name': 'name', 'type': 'string'},
        {'name': 'birth_date', 'type': 'date'},
        {'name': 'is_active', 'type': 'boolean'}
    ]))  # Output: ['Calendar', 'Checkbox', 'InputNumber', 'InputText']
    print(converter.get_primevue_v_model_type('integer'))  # Output: v-model.number
    print(converter.get_default_value('string'))  # Output: ''