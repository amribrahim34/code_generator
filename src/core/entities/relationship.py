# src/core/entities/relationship.py

from typing import Optional

class Relationship:
    def __init__(self, name: str, type: str, related_model: str, foreign_key: Optional[str] = None, local_key: Optional[str] = None):
        self.name = name
        self.type = type
        self.related_model = related_model
        self.foreign_key = foreign_key
        self.local_key = local_key

    def to_laravel_method(self) -> str:
        method = f"public function {self.name}()\n{{\n    return $this->{self.type}({self.related_model}::class"
        if self.foreign_key:
            method += f", '{self.foreign_key}'"
        if self.local_key:
            method += f", '{self.local_key}'"
        method += ");\n}"
        return method

    def to_typescript_property(self) -> str:
        if self.type in ['hasMany', 'belongsToMany']:
            return f"{self.name}: {self.related_model}[];"
        else:
            return f"{self.name}: {self.related_model};"

    def __repr__(self):
        return f"Relationship(type='{self.type}', related_model='{self.related_model}', foreign_key='{self.foreign_key}', local_key='{self.local_key}', name='{self.name}')"