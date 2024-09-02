from typing import List
from src.core.models.schema import Attribute

class TypeConverter:
    def db_to_primevue(self, db_type: str) -> str:
        mapping = {
            'string': 'InputText',
            'text': 'Textarea',
            'integer': 'InputNumber',
            'boolean': 'Checkbox',
            'date': 'Calendar',
            'datetime': 'Calendar',
            'decimal': 'InputNumber',
        }
        return mapping.get(db_type.lower(), 'InputText')

    def get_primevue_v_model_type(self, db_type: str) -> str:
        mapping = {
            'boolean': 'v-model:checked',
        }
        return mapping.get(db_type.lower(), 'v-model')

    def get_primevue_import_list(self, attributes: List[Attribute]) -> List[str]:
        components = set(self.db_to_primevue(attr.type) for attr in attributes)
        return list(components)

    def get_default_value(self, db_type: str) -> str:
        mapping = {
            'string': "''",
            'text': "''",
            'integer': '0',
            'boolean': 'false',
            'date': 'null',
            'datetime': 'null',
            'decimal': '0.0',
        }
        return mapping.get(db_type.lower(), 'null')