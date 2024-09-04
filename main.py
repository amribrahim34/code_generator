import argparse
import json
import os
from typing import Dict, Any

from src.configuration.config_manager import ConfigManager
from src.core.entities.schema import Schema, parse_schema
from src.infrastructure.adapters.json_schema_parser import JSONSchemaParser
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from src.infrastructure.adapters.file_system_output_writer import FileSystemOutputWriter
from src.infrastructure.adapters.console_logger import ConsoleLogger
from src.application.services.backend_generation_service import BackendGenerationService
from src.application.services.frontend_generation_service import FrontendGenerationService
from src.application.services.api_documentation_service import APIDocumentationService
from src.application.services.schema_validation_service import SchemaValidationService

def load_schema(schema_path: str) -> Dict[str, Any]:
    possible_paths = [
        schema_path,
        os.path.join(os.getcwd(), schema_path),
        os.path.join(os.getcwd(), 'examples', schema_path)
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, 'r') as schema_file:
                return json.load(schema_file)
    
    raise FileNotFoundError(f"Schema file not found. Tried paths: {', '.join(possible_paths)}")

def main():
    parser = argparse.ArgumentParser(description="Code Generation System")
    parser.add_argument("--schema", required=True, help="Path to the input schema JSON file")
    parser.add_argument("--config", default="config/default_config.json", help="Path to the configuration JSON file")
    parser.add_argument("--output", default="output", help="Output directory for generated code")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level")
    parser.add_argument("--backend-only", action="store_true", help="Generate only backend code")
    parser.add_argument("--frontend-only", action="store_true", help="Generate only frontend code")
    parser.add_argument("--mobile-only", action="store_true", help="Generate only mobile code")
    args = parser.parse_args()

    # Initialize components
    config_manager = ConfigManager(args.config)
    config_manager.load_config()
    
    logger = ConsoleLogger(name="CodeGenerationSystem", level=args.log_level)
    output_writer = FileSystemOutputWriter(base_path=args.output)
    template_renderer = JinjaTemplateRenderer(template_dir="src/templates")
    
    # Initialize services
    schema_parser = JSONSchemaParser(args.schema)
    backend_service = BackendGenerationService(config_manager, logger, output_writer, template_renderer)
    frontend_service = FrontendGenerationService(config_manager, logger, output_writer, template_renderer)
    api_doc_service = APIDocumentationService(config_manager, logger, output_writer)
    schema_validation_service = SchemaValidationService(config_manager, logger)

    try:
        # Load and parse schema
        schema_data = load_schema(args.schema)
        schema = parse_schema(schema_data)

        # Validate schema
        validation_result = schema_validation_service.validate_schema(schema)

        if not validation_result["is_valid"]:
            logger.error("Schema validation failed:")
            for error in validation_result["errors"]:
                logger.error(f"- {error}")
            return

        backend_result = None
        frontend_result = None

        if args.backend_only:
            logger.info("Generating backend code...")
            backend_result = backend_service.generate(schema)
            if backend_result.generated_files:
                logger.warning("this is backend only ")
                logger.info(f"Backend generation completed. Files generated: {len(backend_result.generated_files)}")
                # logger.warning(f"Backend generation completed. Files generated: {backend_result.generated_files}")
                for file_path in backend_result.generated_files:
                    logger.info(f"Generated file: {file_path}")
            else:
                logger.warning("No backend files were generated. Check the backend generators.")
                
        elif args.frontend_only:
            # Only generate frontend code
            logger.info("Generating frontend code...")
            frontend_result = frontend_service.generate(schema)
            logger.info(f"Frontend generation completed. Files generated: {len(frontend_result.generated_files)}")
        else:
            # Generate both backend and frontend code
            logger.info("this is the else ")
            logger.info("Generating backend code...")
            backend_result = backend_service.generate(schema)
            logger.info(f"Backend generation completed. Files generated: {len(backend_result.generated_files)}")
            
            logger.info("Generating frontend code...")
            frontend_result = frontend_service.generate(schema)
            logger.info(f"Frontend generation completed. Files generated: {len(frontend_result.generated_files)}")

        # Generate API documentation
        logger.info("Generating API documentation...")
        api_doc_result = api_doc_service.generate_documentation(schema)
        logger.info(f"API documentation generated: {api_doc_result['output_path']}")

        # Output generation summary
        logger.info("Code generation completed successfully.")
        total_files = (len(backend_result.generated_files) if backend_result else 0) + \
                      (len(frontend_result.generated_files) if frontend_result else 0) + 1
        logger.info(f"Total files generated: {total_files}")
        logger.info(f"Output directory: {args.output}")

        # Log any warnings or errors
        if backend_result:
            for warning in backend_result.warnings:
                logger.warning(f"Backend warning: {warning}")
            for error in backend_result.errors:
                logger.error(f"Backend error: {error}")

        if frontend_result:
            for warning in frontend_result.warnings:
                logger.warning(f"Frontend warning: {warning}")
            for error in frontend_result.errors:
                logger.error(f"Frontend error: {error}")

    except Exception as e:
        logger.error(f"An error occurred during code generation: {str(e)}")
        raise

if __name__ == "__main__":
    main()