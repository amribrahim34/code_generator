from typing import Dict, Any
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.infrastructure.external_services.swagger_generator import SwaggerGenerator

class APIDocumentationService:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.swagger_generator = SwaggerGenerator()

    def generate_documentation(self, schema: Schema) -> Dict[str, Any]:
        """
        Generate API documentation based on the provided schema.

        Args:
            schema (Schema): The parsed schema object containing all models and relationships.

        Returns:
            Dict[str, Any]: A dictionary containing information about the generated documentation.

        Raises:
            Exception: If there's an error during the documentation generation process.
        """
        self.logger.info("Starting API documentation generation process")

        try:
            # Generate the API documentation
            swagger_spec = self.swagger_generator.generate_swagger_doc(schema)

            # Get output configuration
            output_config = self.config_loader.get('api_documentation', {})
            output_format = output_config.get('format', 'json')
            output_file = f"{output_config.get('output_file', 'api_documentation')}.{output_format}"

            # Serialize the documentation content
            content = self._serialize_content(swagger_spec, output_format)

            # Write the serialized content to the specified file
            self.output_writer.write_file(output_file, content)
            self.logger.info(f"API documentation generated successfully: {output_file}")

            return {
                "output_path": output_file,
                "format": output_format,
                "content_length": len(content)
            }
        except Exception as e:
            self.logger.error(f"Error generating API documentation: {str(e)}")
            raise

    def _serialize_content(self, content: Dict[str, Any], format: str) -> str:
        """
        Serialize content based on the given format.

        Args:
            content (Dict[str, Any]): The content to serialize.
            format (str): The format to serialize the content into (json, yaml).

        Returns:
            str: The serialized content as a string.

        Raises:
            ValueError: If an unsupported format is specified.
        """
        if format == 'json':
            import json
            return json.dumps(content, indent=2)
        elif format in ('yaml', 'yml'):
            import yaml
            return yaml.dump(content, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported format: {format}")

    # Additional methods like update_documentation, validate_documentation, etc. can be added here
    # following the same pattern of dependency injection and error handling