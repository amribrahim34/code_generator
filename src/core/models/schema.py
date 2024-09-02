from typing import List, Optional, Dict, Any

class Attribute:
    def __init__(self, name: str, type: str, required: bool = False, unique: bool = False , nullable: bool = True,):
        self.name = name
        self.type = type
        self.required = required
        self.nullable = nullable
        self.unique = unique

class Relationship:
    def __init__(self, name: str, type: str, model: str, foreign_key: Optional[str] = None):
        self.name = name
        self.type = type
        self.model = model
        self.foreign_key = foreign_key

class Model:
    def __init__(self, name: str, attributes: List[Attribute], relationships: List[Relationship]):
        self.name = name
        self.attributes = attributes
        self.relationships = relationships

class Schema:
    def __init__(self, models: List[Model]):
        self.models = models

def parse_schema(schema_data: Dict[str, Any]) -> Schema:
    # If schema_data is a dictionary, convert it to a list of models
    if isinstance(schema_data, dict):
        schema_data = [schema_data]

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
                unique=attr.get('unique', False)
            ) for attr in model_dict.get('attributes', [])
        ]
        relationships = [
            Relationship(
                name=rel.get('name', ''),
                type=rel.get('type', ''),
                model=rel.get('model', ''),
                foreign_key=rel.get('foreignKey')
            ) for rel in model_dict.get('relationships', [])
        ]
        models.append(Model(name=name, attributes=attributes, relationships=relationships))
    return Schema(models)
