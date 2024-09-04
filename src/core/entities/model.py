# src/core/entities/model.py

from typing import List, Dict, Optional
from .attribute import Attribute
from .relationship import Relationship

class Model:
    def __init__(self, name: str, attributes: List[Attribute] = None, relationships: List[Relationship] = None):
        self.name = name
        self.table_name = name.lower() + 's'  # Default table name, can be overridden
        self.attributes = attributes or []
        self.relationships = relationships or []
        self.options: Dict = {}

    def add_attribute(self, attribute: Attribute) -> None:
        self.attributes.append(attribute)

    def add_relationship(self, relationship: Relationship) -> None:
        self.relationships.append(relationship)

    def get_primary_key(self) -> Optional[Attribute]:
        return next((attr for attr in self.attributes if attr.is_primary_key()), None)

    def get_fillable_attributes(self) -> List[Attribute]:
        return [attr for attr in self.attributes if attr.is_fillable()]

    def generate_laravel_model_code(self) -> str:
        # Implement Laravel model code generation logic here
        # This is a placeholder implementation
        return f"class {self.name} extends Model {{\n    // Laravel model code\n}}"

    def generate_vue_interface_code(self) -> str:
        # Implement Vue interface code generation logic here
        # This is a placeholder implementation
        return f"interface {self.name} {{\n    // Vue interface code\n}}"

    def __repr__(self):
        return f"Model(name='{self.name}', table_name='{self.table_name}', attributes={self.attributes}, relationships={self.relationships}, options={self.options})"