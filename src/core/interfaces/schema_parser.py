from abc import ABC, abstractmethod
from typing import Dict, List
from src.core.entities.schema import Schema, Model, parse_schema
from src.core.entities.attribute import Attribute
from src.core.entities.relationship import Relationship

class ISchemaParser(ABC):
    @abstractmethod
    def parse(self, schema_data: Dict) -> Schema:
        """
        Parse the schema data and return a Schema object.

        Args:
            schema_data (Dict): The schema data to be parsed.

        Returns:
            Schema: The parsed schema.

        Raises:
            ValueError: If there's an error parsing the schema data.
        """
        pass

    @abstractmethod
    def validate(self, schema_data: Dict) -> None:
        """
        Validate the schema data.

        Args:
            schema_data (Dict): The schema data to be validated.

        Raises:
            ValueError: If the schema data is invalid.
        """
        pass

    @abstractmethod
    def get_models(self) -> List[Model]:
        """
        Get all models from the parsed schema.

        Returns:
            List[Model]: A list of all models in the schema.

        Raises:
            ValueError: If the schema hasn't been parsed yet.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def validate_schema(self) -> bool:
        """
        Validate the schema structure.

        Returns:
            bool: True if the schema is valid, False otherwise.

        Raises:
            ValueError: If the schema hasn't been parsed yet.
        """
        pass

    @abstractmethod
    def get_schema_path(self) -> str:
        """
        Get the path of the schema file.

        Returns:
            str: The path of the schema file.
        """
        pass

    @abstractmethod
    def set_schema_path(self, path: str) -> None:
        """
        Set the path of the schema file.

        Args:
            path (str): The new path of the schema file.
        """
        pass
