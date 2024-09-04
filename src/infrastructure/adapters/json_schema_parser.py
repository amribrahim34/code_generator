import json
import os
from typing import List
from src.core.interfaces.schema_parser import ISchemaParser
from src.core.entities.schema import Schema, Model, Attribute, Relationship, parse_schema

class JSONSchemaParser(ISchemaParser):
    def __init__(self, schema_path: str):
        self._schema_path = schema_path
        self._schema: Schema = None

    def parse(self) -> Schema:
        try:
            schema_data = self._load_schema_file()
            self._schema = parse_schema(schema_data)
            print(f"Successfully loaded schema from: {self._schema_path}")
            return self._schema
        except Exception as e:
            raise ValueError(f"Error parsing schema: {str(e)}")

    def validate(self, schema_data: dict) -> None:
        # Implement basic validation logic here
        if not isinstance(schema_data, dict):
            raise ValueError("Schema must be a dictionary")
        
        if 'models' not in schema_data:
            raise ValueError("Schema must contain a 'models' key")
        
        for model_name, model_data in schema_data['models'].items():
            if 'attributes' not in model_data:
                raise ValueError(f"Model '{model_name}' must have 'attributes'")
            
            if not isinstance(model_data['attributes'], dict):
                raise ValueError(f"Attributes for model '{model_name}' must be a dictionary")

    def get_models(self) -> List[Model]:
        if not self._schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        return self._schema.models

    def get_model(self, model_name: str) -> Model:
        if not self._schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        
        for model in self._schema.models:
            if model.name.lower() == model_name.lower():
                return model
        
        raise ValueError(f"Model '{model_name}' not found in schema.")

    def validate_schema(self) -> bool:
        if not self._schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        
        for model in self._schema.models:
            if not model.name:
                return False
            if not model.attributes:
                return False
            for attr in model.attributes:
                if not attr.name or not attr.type:
                    return False
            for rel in model.relationships:
                if not rel.type or not rel.model:
                    return False
        
        return True

    def get_schema_path(self) -> str:
        return self._schema_path

    def set_schema_path(self, path: str) -> None:
        self._schema_path = path
        self._schema = None  # Reset the parsed schema when the path changes

    def _load_schema_file(self) -> List[dict]:
        cwd = os.getcwd()
        possible_paths = [
            self._schema_path,
            os.path.join(cwd, self._schema_path),
            os.path.join(cwd, 'input_examples', os.path.basename(self._schema_path))
        ]

        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r') as schema_file:
                    schema_data = json.load(schema_file)
                    
                    if isinstance(schema_data, dict):
                        schema_data = schema_data.get('models', [])
                    
                    if not isinstance(schema_data, list):
                        raise ValueError(f"Schema data should be a list of models, but got {type(schema_data)}")

                    return schema_data

        raise FileNotFoundError(f"Schema file not found. Tried paths: {', '.join(possible_paths)}")