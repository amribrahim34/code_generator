import argparse
import json
import os
from typing import Dict, Any

from src.configuration.config_manager import ConfigManager
from src.core.entities.schema import Schema, parse_schema
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from src.infrastructure.adapters.file_system_output_writer import FileSystemOutputWriter
from src.infrastructure.adapters.console_logger import ConsoleLogger
from src.application.services.backend_generation_service import BackendGenerationService
from src.application.services.frontend_generation_service import FrontendGenerationService
from src.application.services.react_native_generation_service import ReactNativeGenerationService
from src.application.services.schema_validation_service import SchemaValidationService

# Global variables for components and services
config_manager = None
logger = None
output_writer = None
template_renderer = None
schema_parser = None
backend_service = None
frontend_service = None
react_native_service = None
schema_validation_service = None

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

def initialize_components(config_path: str, log_level: str, output_dir: str):
    global config_manager, logger, output_writer, template_renderer, schema_parser, \
           backend_service, frontend_service, react_native_service, schema_validation_service

    config_manager = ConfigManager(config_path)
    config_manager.load_config()
    
    logger = ConsoleLogger(name="CodeGenerationSystem", level=log_level)
    output_writer = FileSystemOutputWriter(base_path=output_dir)
    template_renderer = JinjaTemplateRenderer(template_dir="src/templates")
    
    backend_service = BackendGenerationService(config_manager, logger, output_writer, template_renderer)
    frontend_service = FrontendGenerationService(config_manager, logger, output_writer, template_renderer)
    react_native_service = ReactNativeGenerationService(config_manager, logger, output_writer, template_renderer)
    schema_validation_service = SchemaValidationService(config_manager, logger)

def generate_code(schema_data: Dict[str, Any], output_dir: str, generate_backend: bool = True, 
                  generate_frontend: bool = True, generate_mobile: bool = True):
    try:
        schema = parse_schema(schema_data)

        # Validate schema
        validation_result = schema_validation_service.validate_schema(schema)

        if not validation_result["is_valid"]:
            return {"error": "Schema validation failed", "details": validation_result["errors"]}, 400

        results = {}

        if generate_backend:
            logger.info("Generating backend code...")
            backend_result = backend_service.generate(schema)
            results["backend"] = {
                "files_generated": len(backend_result.generated_files),
                "warnings": backend_result.warnings,
                "errors": backend_result.errors
            }

        if generate_frontend:
            logger.info("Generating frontend code...")
            frontend_result = frontend_service.generate(schema)
            results["frontend"] = {
                "files_generated": len(frontend_result.generated_files),
                "warnings": frontend_result.warnings,
                "errors": frontend_result.errors
            }

        if generate_mobile:
            logger.info("Generating React Native mobile code...")
            react_native_result = react_native_service.generate(schema)
            results["mobile"] = {
                "files_generated": len(react_native_result.generated_files),
                "warnings": react_native_result.warnings,
                "errors": react_native_result.errors
            }

        logger.info("Code generation completed successfully.")
        return results, 200

    except Exception as e:
        logger.error(f"An error occurred during code generation: {str(e)}")
        return {"error": str(e)}, 500

def main():
    parser = argparse.ArgumentParser(description="Code Generation System")
    parser.add_argument("--schema", help="Path to the input schema JSON file")
    parser.add_argument("--config", default="config/default_config.json", help="Path to the configuration JSON file")
    parser.add_argument("--output", default="output", help="Output directory for generated code")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level")
    parser.add_argument("--backend-only", action="store_true", help="Generate only backend code")
    parser.add_argument("--frontend-only", action="store_true", help="Generate only frontend code")
    parser.add_argument("--mobile-only", action="store_true", help="Generate only React Native mobile code")
    args = parser.parse_args()

    initialize_components(args.config, args.log_level, args.output)

    if args.schema:
        try:
            schema_data = load_schema(args.schema)
            results, status_code = generate_code(
                schema_data,
                args.output,
                generate_backend=not args.frontend_only and not args.mobile_only,
                generate_frontend=not args.backend_only and not args.mobile_only,
                generate_mobile=not args.backend_only and not args.frontend_only
            )

            if status_code == 200:
                print("Code generation completed successfully.")
                print(json.dumps(results, indent=2))
            else:
                print("Code generation failed.")
                print(json.dumps(results, indent=2))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("Please provide a schema file using the --schema argument.")

if __name__ == "__main__":
    main()