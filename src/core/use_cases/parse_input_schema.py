import json
from typing import Dict, Any, List
from src.core.entities.schema import Schema
from src.core.entities.model import Model
from src.core.entities.attribute import Attribute
from src.core.entities.relationship import Relationship
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger

class ParseInputSchema:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger):
        self.config_loader = config_loader
        self.logger = logger

    def execute(self, input_schema: str) -> Schema:
        """
        Parse and validate the input JSON schema, converting it to a Schema entity.
        
        Args:
            input_schema (str): The input JSON schema as a string.
        
        Returns:
            Schema: The parsed and validated Schema entity.
        """
        self.logger.info("Starting input schema parsing")
        
        try:
            # Parse JSON
            schema_data = json.loads(input_schema)
            
            # Validate overall structure
            self.validate_schema_structure(schema_data)
            
            # Parse models
            models = self._parse_models(schema_data['models'])
            
            # Parse relationships
            relationships = self._parse_relationships(schema_data.get('relationships', []))
            
            # Create Schema entity
            schema = Schema(
                models=models,
                relationships=relationships,
                config=schema_data.get('config', {})
            )
            
            # Validate that all models in relationships exist
            self._validate_relationship_models(schema)
            
            # Apply default configuration values
            self._apply_config_defaults(schema)
            
            self.logger.info("Input schema parsing completed successfully")
            return schema
        
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON: {str(e)}")
            raise ValueError("The input schema is not valid JSON")
        except Exception as e:
            self.logger.error(f"Error parsing input schema: {str(e)}")
            raise

    def validate_schema_structure(self, schema_data: Dict[str, Any]):
        """
        Validate the overall structure of the input schema.
        
        Args:
            schema_data (Dict[str, Any]): The parsed JSON schema data.
        
        Raises:
            ValueError: If the schema structure is invalid.
        """
        if not isinstance(schema_data, dict):
            raise ValueError("Schema must be a JSON object")
        
        if 'models' not in schema_data:
            raise ValueError("Schema must contain a 'models' key")
        
        if not isinstance(schema_data['models'], dict):
            raise ValueError("'models' must be an object")
        
        if 'relationships' in schema_data and not isinstance(schema_data['relationships'], list):
            raise ValueError("'relationships' must be an array")

    def _parse_models(self, models_data: Dict[str, Any]) -> Dict[str, Model]:
        """
        Parse the models section of the input schema.
        
        Args:
            models_data (Dict[str, Any]): The models data from the input schema.
        
        Returns:
            Dict[str, Model]: A dictionary of parsed Model entities.
        """
        models = {}
        for model_name, model_info in models_data.items():
            attributes = self._parse_attributes(model_info.get('attributes', {}))
            models[model_name] = Model(
                name=model_name,
                attributes=attributes,
                config=model_info.get('config', {})
            )
        return models

    def _parse_attributes(self, attributes_data: Dict[str, Any]) -> Dict[str, Attribute]:
        """
        Parse the attributes of a model.
        
        Args:
            attributes_data (Dict[str, Any]): The attributes data for a model.
        
        Returns:
            Dict[str, Attribute]: A dictionary of parsed Attribute entities.
        """
        attributes = {}
        for attr_name, attr_info in attributes_data.items():
            if isinstance(attr_info, str):
                attr_type = attr_info
                attr_config = {}
            elif isinstance(attr_info, dict):
                attr_type = attr_info.get('type', 'string')
                attr_config = {k: v for k, v in attr_info.items() if k != 'type'}
            else:
                raise ValueError(f"Invalid attribute definition for {attr_name}")
            
            attributes[attr_name] = Attribute(
                name=attr_name,
                type=attr_type,
                config=attr_config
            )
        return attributes

    def _parse_relationships(self, relationships_data: List[Dict[str, Any]]) -> List[Relationship]:
        """
        Parse the relationships section of the input schema.
        
        Args:
            relationships_data (List[Dict[str, Any]]): The relationships data from the input schema.
        
        Returns:
            List[Relationship]: A list of parsed Relationship entities.
        """
        relationships = []
        for rel_info in relationships_data:
            relationships.append(Relationship(
                type=rel_info['type'],
                from_model=rel_info['from'],
                to_model=rel_info['to'],
                config=rel_info.get('config', {})
            ))
        return relationships

    def _validate_relationship_models(self, schema: Schema):
        """
        Validate that all models referenced in relationships exist.
        
        Args:
            schema (Schema): The parsed Schema entity.
        
        Raises:
            ValueError: If a relationship references a non-existent model.
        """
        for relationship in schema.relationships:
            if relationship.from_model not in schema.models:
                raise ValueError(f"Relationship references non-existent model: {relationship.from_model}")
            if relationship.to_model not in schema.models:
                raise ValueError(f"Relationship references non-existent model: {relationship.to_model}")

    def _apply_config_defaults(self, schema: Schema):
        """
        Apply default configuration values from the global config.
        
        Args:
            schema (Schema): The parsed Schema entity.
        """
        global_defaults = self.config_loader.get('schema_defaults', {})
        
        for model in schema.models.values():
            model_defaults = global_defaults.get('models', {})
            for key, value in model_defaults.items():
                if key not in model.config:
                    model.config[key] = value
            
            for attribute in model.attributes.values():
                attr_defaults = global_defaults.get('attributes', {})
                for key, value in attr_defaults.items():
                    if key not in attribute.config:
                        attribute.config[key] = value
        
        for relationship in schema.relationships:
            rel_defaults = global_defaults.get('relationships', {})
            for key, value in rel_defaults.items():
                if key not in relationship.config:
                    relationship.config[key] = value
