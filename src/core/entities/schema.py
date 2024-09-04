# src/core/entities/schema.py

from typing import List, Dict, Any, Optional
from .model import Model
from .attribute import Attribute
from .relationship import Relationship

class Schema:
    def __init__(self, models: List[Model] = None, global_options: Dict = None):
        self.models = models or []
        self.global_options = global_options or {}

    def add_model(self, model: Model) -> None:
        self.models.append(model)

    def get_model(self, name: str) -> Optional[Model]:
        return next((model for model in self.models if model.name == name), None)

    def validate(self) -> List[str]:
        validator = SchemaValidator(self)
        errors = []
        errors.extend(validator.validate_relationships())
        errors.extend(validator.validate_unique_model_names())
        return errors

    def to_dict(self) -> Dict:
        return {
            "models": [model.to_dict() for model in self.models],
            "global_options": self.global_options
        }

    def __repr__(self):
        return f"Schema(models={self.models}, global_options={self.global_options})"

class SchemaValidator:
    def __init__(self, schema: Schema):
        self.schema = schema

    def validate_relationships(self) -> List[str]:
        errors = []
        for model in self.schema.models:
            for relationship in model.relationships:
                if not self.schema.get_model(relationship.model):
                    errors.append(f"Invalid relationship in model '{model.name}': "
                                  f"Referenced model '{relationship.model}' does not exist.")
        return errors

    def validate_unique_model_names(self) -> List[str]:
        model_names = [model.name for model in self.schema.models]
        duplicates = set([name for name in model_names if model_names.count(name) > 1])
        return [f"Duplicate model name: '{name}'" for name in duplicates]

def parse_schema(schema_data: Dict[str, Any]) -> Schema:
    # If schema_data is a dictionary, convert it to a list of models
    if isinstance(schema_data, dict):
        schema_data = schema_data.get('models', [])

    models = []
    for i, model_dict in enumerate(schema_data):
        if not isinstance(model_dict, dict):
            raise TypeError(f"Expected each model to be a dictionary, but model at index {i} is {type(model_dict)}")

        name = model_dict.get('name')
        if not name:
            raise ValueError(f"Missing 'name' for model at index {i}")

        attributes = [
            Attribute(
                name=attr.get('name', ''),
                type=attr.get('type', ''),
                required=attr.get('required', False),
                nullable=attr.get('nullable', True),
                unique=attr.get('unique', False),
                enum_values=attr.get('options', [])  # Add this line
            ) for attr in model_dict.get('attributes', [])
        ]
        relationships = [
            Relationship(
                name=rel.get('name', ''),
                type=rel.get('type', ''),
                related_model=rel.get('model', ''),
                foreign_key=rel.get('foreignKey')
            ) for rel in model_dict.get('relationships', [])
        ]
        models.append(Model(name=name, attributes=attributes, relationships=relationships))
    return Schema(models)