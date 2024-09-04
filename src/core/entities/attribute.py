from typing import Dict, Any, List, Tuple, Optional

class Attribute:
    def __init__(self, name: str, type: str, required: bool = False, unique: bool = False, nullable: bool = True, enum_values: List[str] = None, default: Any = None):
        self.name = name
        self.type = type
        self.required = required
        self.nullable = nullable
        self.unique = unique
        self.default = default
        self.enum_values = enum_values or []

    def __repr__(self):
        return f"Attribute(name='{self.name}', type='{self.type}', required={self.required}, nullable={self.nullable}, unique={self.unique}, default={self.default})"