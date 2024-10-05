import argparse
import json
import os
from typing import Dict, Any
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import threading
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
from src.presentation.api.swagger_config import api_bp, swaggerui_blueprint, SWAGGER_URL, get_swagger_json

from src.configuration.config_manager import ConfigManager
from src.core.entities.schema import Schema, parse_schema
from src.infrastructure.adapters.json_schema_parser import JSONSchemaParser
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from src.infrastructure.adapters.file_system_output_writer import FileSystemOutputWriter
from src.infrastructure.adapters.console_logger import ConsoleLogger
from src.application.services.backend_generation_service import BackendGenerationService
from src.application.services.frontend_generation_service import FrontendGenerationService
from src.application.services.react_native_generation_service import ReactNativeGenerationService
from src.application.services.api_documentation_service import APIDocumentationService
from src.application.services.schema_validation_service import SchemaValidationService



app = Flask(__name__)

# Global variables for components and services
config_manager = None
logger = None
output_writer = None
template_renderer = None
schema_parser = None
backend_service = None
frontend_service = None
react_native_service = None
api_doc_service = None
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
           backend_service, frontend_service, react_native_service, api_doc_service, \
           schema_validation_service

    config_manager = ConfigManager(config_path)
    config_manager.load_config()
    
    logger = ConsoleLogger(name="CodeGenerationSystem", level=log_level)
    output_writer = FileSystemOutputWriter(base_path=output_dir)
    template_renderer = JinjaTemplateRenderer(template_dir="src/templates")
    
    backend_service = BackendGenerationService(config_manager, logger, output_writer, template_renderer)
    frontend_service = FrontendGenerationService(config_manager, logger, output_writer, template_renderer)
    react_native_service = ReactNativeGenerationService(config_manager, logger, output_writer, template_renderer)
    api_doc_service = APIDocumentationService(config_manager, logger, output_writer)
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

        # Generate API documentation
        logger.info("Generating API documentation...")
        api_doc_result = api_doc_service.generate_documentation(schema)
        results["api_documentation"] = {
            "output_path": api_doc_result['output_path']
        }

        return results, 200

    except Exception as e:
        logger.error(f"An error occurred during code generation: {str(e)}")
        return {"error": str(e)}, 500


@app.route('/swagger.json')
def swagger_json():
    return get_swagger_json()

@app.route('/generate', methods=['POST'])
def api_generate():
    if 'schema' not in request.files:
        return jsonify({"error": "No schema file provided"}), 400
    
    schema_file = request.files['schema']
    if schema_file.filename == '':
        return jsonify({"error": "No schema file selected"}), 400
    
    if schema_file:
        filename = secure_filename(schema_file.filename)
        schema_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        schema_file.save(schema_path)
        
        try:
            schema_data = load_schema(schema_path)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON in schema file"}), 400
        except Exception as e:
            return jsonify({"error": f"Error reading schema file: {str(e)}"}), 500
        
        generate_backend = request.form.get('generate_backend', 'true').lower() == 'true'
        generate_frontend = request.form.get('generate_frontend', 'true').lower() == 'true'
        generate_mobile = request.form.get('generate_mobile', 'true').lower() == 'true'
        
        results, status_code = generate_code(schema_data, app.config['OUTPUT_FOLDER'], 
                                             generate_backend, generate_frontend, generate_mobile)
        
        return jsonify(results), status_code

def run_api(host: str, port: int):
    # Generate OpenAPI specification
    # openapi_spec = generate_openapi_spec()
    # with open('openapi.yaml', 'w') as f:
    #     yaml.dump(openapi_spec, f)

    # Create Swagger UI blueprint
    SWAGGER_URL = '/swagger-ui'
    API_URL = '/api-docs'
    # swaggerui_blueprint = get_swaggerui_blueprint(
    #     SWAGGER_URL,
    #     API_URL,
    #     config={
    #         'app_name': "Code Generation API"
    #     }
    # )
    # app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    # app.register_blueprint(api_bp, url_prefix='/api')

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Create a simple HTML file to redirect to Swagger UI
    with open('swagger.html', 'w') as f:
        f.write(f'<meta http-equiv="refresh" content="0; url={SWAGGER_URL}" />')

    app.run(host=host, port=port)
    
@app.route('/api-docs')
def api_docs():
    return send_from_directory('.', 'openapi.yaml')

@app.route('/swagger')
def swagger_ui():
    return send_from_directory('.', 'swagger.html')

def run_api_server(args):
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['OUTPUT_FOLDER'] = args.output
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    print(f"Starting API server on {args.host}:{args.port}")
    run_api(args.host, args.port)


def run_cli_mode(args):
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

def main():
    parser = argparse.ArgumentParser(description="Code Generation System")
    parser.add_argument("--schema", help="Path to the input schema JSON file")
    parser.add_argument("--config", default="config/default_config.json", help="Path to the configuration JSON file")
    parser.add_argument("--output", default="output", help="Output directory for generated code")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level")
    parser.add_argument("--backend-only", action="store_true", help="Generate only backend code")
    parser.add_argument("--frontend-only", action="store_true", help="Generate only frontend code")
    parser.add_argument("--mobile-only", action="store_true", help="Generate only React Native mobile code")
    parser.add_argument("--api", action="store_true", help="Run as an API server")
    parser.add_argument("--host", default="localhost", help="Host for the API server")
    parser.add_argument("--port", type=int, default=5000, help="Port for the API server")
    args = parser.parse_args()

    initialize_components(args.config, args.log_level, args.output)

    if args.api:
        run_api_server(args)
    elif args.schema:
        run_cli_mode(args)
    else:
        print("Please provide a schema file or use the --api flag to run as an API server.")

if __name__ == "__main__":
    main()