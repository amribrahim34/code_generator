from typing import Dict, Any, List ,Tuple
from src.core.entities.schema import Schema
from src.core.entities.model import Model
from src.core.entities.attribute import Attribute
from src.core.entities.relationship import Relationship
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger

class SchemaValidationService:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger):
        self.config_loader = config_loader
        self.logger = logger

    def validate_schema(self, schema: Schema) -> Tuple[List[str], List[str]]:
        """
        Validate the input schema against predefined rules and constraints.

        Args:
            schema (Schema): The parsed Schema object.

        Returns:
            Dict[str, Any]: A dictionary containing validation results and any errors or warnings.
        """
        self.logger.info("Starting schema validation")

        errors = []
        warnings = []
        self._validate_models(schema, errors, warnings)
        self._validate_relationships(schema, errors, warnings)
        self._validate_naming_conventions(schema, errors, warnings)
        self._validate_attribute_types(schema, errors, warnings)
        self._validate_unique_constraints(schema, errors, warnings)

        validation_result = {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }

        self.logger.info("Schema validation completed")
        return validation_result

    def _validate_models(self, schema: Schema, errors: List[str], warnings: List[str]):
        """Validate models in the schema."""
        if len(schema.models) == 0:
            errors.append("Schema must contain at least one model")

        for model in schema.models:
            if len(model.attributes) == 0:
                errors.append(f"Model '{model.name}' must have at least one attribute")

            if not any(attr.name == 'id' for attr in model.attributes):
                warnings.append(f"Model '{model.name}' does not have an 'id' attribute")

    def _validate_relationships(self, schema: Schema, errors: List[str], warnings: List[str]):
        """Validate relationships in the schema."""
        model_names = set(model.name for model in schema.models)
        for model in schema.models:
            for relationship in model.relationships:
                if relationship.related_model not in model_names:
                    errors.append(f"Relationship in model '{model.name}' references non-existent model: {relationship.related_model}")

                if relationship.type not in ['hasOne', 'hasMany', 'belongsTo', 'belongsToMany']:
                    errors.append(f"Invalid relationship type in model '{model.name}': {relationship.type}")

    def _validate_naming_conventions(self, schema: Schema, errors: List[str], warnings: List[str]):
        """Validate naming conventions for models and attributes."""
        for model in schema.models:
            if not model.name[0].isupper():
                warnings.append(f"Model name '{model.name}' should start with an uppercase letter")

            for attr in model.attributes:
                if not attr.name.islower():
                    warnings.append(f"Attribute '{attr.name}' in model '{model.name}' should be lowercase")

    def _validate_attribute_types(self, schema: Schema, errors: List[str], warnings: List[str]):
        """Validate attribute types."""
        valid_types = self.config_loader.get('valid_attribute_types', [
            'string', 'integer', 'boolean', 'float', 'date', 'datetime',
        'uuid', 'timestamp', 'decimal', 'enum', 'text', 'json'
        ])

        for model in schema.models:
            for attr in model.attributes:
                if attr.type not in valid_types:
                    errors.append(f"Invalid attribute type '{attr.type}' for '{attr.name}' in model '{model.name}'")
                
                if attr.type == 'enum' and not attr.enum_values:
                    errors.append(f"Enum attribute '{attr.name}' in model '{model.name}' must have enum_values defined")

    def _validate_unique_constraints(self, schema: Schema, errors: List[str], warnings: List[str]):
        """Validate unique constraints."""
        for model in schema.models:
            unique_attributes = [attr for attr in model.attributes if attr.unique]
            if len(unique_attributes) == 0:
                warnings.append(f"Model '{model.name}' does not have any unique attributes")

    def suggest_improvements(self, schema: Schema) -> List[str]:
        """
        Suggest improvements for the schema.

        Args:
            schema (Schema): The parsed schema object.

        Returns:
            List[str]: A list of improvement suggestions.
        """
        suggestions = []

        for model in schema.models:
            if any(attr.name in ['email', 'username', 'slug'] for attr in model.attributes):
                suggestions.append(f"Consider adding an index to frequently queried fields in '{model.name}'")

            if not any(attr.name == 'deleted_at' for attr in model.attributes):
                suggestions.append(f"Consider implementing soft deletes by adding a 'deleted_at' timestamp to '{model.name}'")

            if not any(attr.name in ['created_at', 'updated_at'] for attr in model.attributes):
                suggestions.append(f"Consider adding 'created_at' and 'updated_at' timestamps to '{model.name}'")

            status_attrs = [attr for attr in model.attributes if 'status' in attr.name.lower()]
            for attr in status_attrs:
                if attr.type == 'string':
                    suggestions.append(f"Consider using an enum for the '{attr.name}' field in '{model.name}'")

        return suggestions

    def validate_performance_implications(self, schema: Schema) -> List[str]:
        """
        Validate the schema for potential performance implications.

        Args:
            schema (Schema): The parsed schema object.

        Returns:
            List[str]: A list of performance-related warnings.
        """
        warnings = []

        for model in schema.models:
            if len(model.attributes) > 20:
                warnings.append(f"Model '{model.name}' has a high number of attributes. Consider splitting it into multiple tables.")

            text_fields = [attr for attr in model.attributes if attr.type == 'text']
            if len(text_fields) > 3:
                warnings.append(f"Model '{model.name}' has many text fields. Ensure they are necessary as they can impact performance.")

            foreign_keys = [attr for attr in model.attributes if attr.name.endswith('_id')]
            for fk in foreign_keys:
                warnings.append(f"Consider adding an index to the foreign key '{fk.name}' in model '{model.name}'")

        max_relationship_depth = self._calculate_max_relationship_depth(schema)
        if max_relationship_depth > 3:
            warnings.append(f"The schema has a maximum relationship depth of {max_relationship_depth}. Deep relationships can lead to performance issues.")

        return warnings

    def _calculate_max_relationship_depth(self, schema: Schema) -> int:
        """Calculate the maximum depth of relationships in the schema."""
        def dfs(model_name, visited):
            if model_name in visited:
                return 0
            visited.add(model_name)
            max_depth = 0
            for model in schema.models:
                if model.name == model_name:
                    for rel in model.relationships:
                        depth = dfs(rel.related_model, visited.copy()) + 1
                        max_depth = max(max_depth, depth)
            return max_depth

        max_depth = 0
        for model in schema.models:
            depth = dfs(model.name, set())
            max_depth = max(max_depth, depth)
        return max_depth

    def validate_security_implications(self, schema: Schema) -> List[str]:
        """
        Validate the schema for potential security implications.

        Args:
            schema (Schema): The parsed schema object.

        Returns:
            List[str]: A list of security-related warnings.
        """
        warnings = []

        for model in schema.models:
            sensitive_fields = ['password', 'credit_card', 'ssn', 'secret']
            for attr in model.attributes:
                if any(sensitive in attr.name.lower() for sensitive in sensitive_fields):
                    warnings.append(f"Model '{model.name}' contains potentially sensitive data in '{attr.name}'. Ensure proper encryption and access controls.")

            if not any(attr.name in ['created_by', 'updated_by'] for attr in model.attributes):
                warnings.append(f"Consider adding 'created_by' and 'updated_by' fields to '{model.name}' for auditing purposes.")

        if not any('role' in model.name.lower() for model in schema.models):
            warnings.append("Consider implementing role-based access control by adding a 'Role' model.")

        return warnings

    def generate_schema_documentation(self, schema: Schema) -> str:
        """
        Generate documentation for the schema.

        Args:
            schema (Schema): The parsed schema object.

        Returns:
            str: Markdown formatted documentation of the schema.
        """
        doc = "# Schema Documentation\n\n"

        for model in schema.models:
            doc += f"## {model.name}\n\n"
            doc += "| Attribute | Type | Description |\n"
            doc += "|-----------|------|-------------|\n"
            for attr in model.attributes:
                description = attr.config.get('description', '')
                doc += f"| {attr.name} | {attr.type} | {description} |\n"
            doc += "\n"

        doc += "## Relationships\n\n"
        for model in schema.models:
            for rel in model.relationships:
                doc += f"- {model.name} {rel.type} {rel.related_model}\n"

        return doc