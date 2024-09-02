# Placeholder fileimport json
import json
import os
from typing import Dict, Any, List
from src.core.models.schema import Schema, Model, Attribute, Relationship, parse_schema

class SchemaParser:
    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self.schema: Schema = None

    def parse(self) -> Schema:
        try:
            # Get the absolute path of the current working directory
            cwd = os.getcwd()

            # Try different possible paths
            possible_paths = [
                self.schema_path,
                os.path.join(cwd, self.schema_path),
                os.path.join(cwd, 'input_examples', os.path.basename(self.schema_path))
            ]

            for path in possible_paths:
                if os.path.exists(path):
                    with open(path, 'r') as schema_file:
                        schema_data = json.load(schema_file)
                        
                        # Check if schema_data is a dictionary, if so, wrap it in a list
                        if isinstance(schema_data, dict):
                            schema_data = schema_data.get('models', [])
                        
                        if not isinstance(schema_data, list):
                            raise ValueError(f"Schema data should be a list of models, but got {type(schema_data)}")

                        self.schema = parse_schema(schema_data)
                        print(f"Successfully loaded schema from: {path}")
                        return self.schema

            # If we've reached here, the file wasn't found
            raise FileNotFoundError(f"Tried paths: {', '.join(possible_paths)}")

        except FileNotFoundError as e:
            raise ValueError(f"Schema file not found. {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in schema file: {e}")
        except KeyError as e:
            raise ValueError(f"Missing required key in schema: {e}")
        except TypeError as e:
            raise ValueError(f"Type error in schema: {e}. Make sure the schema is a list of dictionaries.")
        except Exception as e:
            raise ValueError(f"Error parsing schema: {e}")


    def get_models(self) -> List[Model]:
        """
        Get all models from the parsed schema.

        Returns:
            List[Model]: A list of all models in the schema.

        Raises:
            ValueError: If the schema hasn't been parsed yet.
        """
        if not self.schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        return self.schema.models

    def get_model(self, model_name: str) -> Model:
        """
        Get a specific model from the parsed schema by name.

        Args:
            model_name (str): The name of the model to retrieve.

        Returns:
            Model: The requested model.

        Raises:
            ValueError: If the schema hasn't been parsed yet or the model is not found.
        """
        if not self.schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        
        for model in self.schema.models:
            if model.name.lower() == model_name.lower():
                return model
        
        raise ValueError(f"Model '{model_name}' not found in schema.")

    def validate_schema(self) -> bool:
        """
        Validate the schema structure.

        Returns:
            bool: True if the schema is valid, False otherwise.

        Raises:
            ValueError: If the schema hasn't been parsed yet.
        """
        if not self.schema:
            raise ValueError("Schema has not been parsed. Call parse() first.")
        
        # Add your validation logic here
        # For example, check if all required fields are present in each model
        for model in self.schema.models:
            if not model.name:
                return False
            if not model.attributes:
                return False
        
        return True

# Usage example:
if __name__ == "__main__":
    parser = SchemaParser("path/to/your/schema.json")
    schema = parser.parse()
    
    if parser.validate_schema():
        print("Schema is valid.")
        for model in parser.get_models():
            print(f"Model: {model.name}")
            print("Attributes:")
            for attr in model.attributes:
                print(f"  - {attr.name}: {attr.type}")
            print("Relationships:")
            for rel in model.relationships:
                print(f"  - {rel.type} {rel.model}")
    else:
        print("Schema is invalid.")