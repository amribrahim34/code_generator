from typing import Dict, Any, List
import json
import os
import importlib
import shutil
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.use_cases.generate_backend_code import GenerateBackendCode
from src.application.dtos.generation_response_dto import GenerationResponseDTO

class BackendGenerationService:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.template_renderer = template_renderer
        self.logger.info("this is the backend generation service")
        self.generators = self._initialize_generators()
        self.generate_backend_code = GenerateBackendCode(
            config_loader,
            logger,
            output_writer,
            template_renderer
        )
        self.output_dir = None

    def _initialize_generators(self):
        generators = []
        generator_configs = self.config_loader.get('generators.backend', [])
        # self.logger.info(f"these are the config generators {generator_configs}")
        for gen_config in generator_configs:
            try:
                module = importlib.import_module(gen_config['module'])
                generator_class = getattr(module, gen_config['class'])
                generators.append(generator_class(self.config_loader, self.template_renderer))
                # self.logger.info(f"this is a loaded generator name {gen_config['name']}")
                # self.logger.info(f"this is a loaded generator module {gen_config['module']}")
            except Exception as e:
                self.logger.error(f"Failed to initialize generator {gen_config['name']}: {str(e)}")
        return generators

    def generate(self, schema: Schema) -> GenerationResponseDTO:
        """
        Coordinates the backend code generation process.

        Args:
            schema (Schema): The parsed schema object containing all models and relationships.

        Returns:
            GenerationResponseDTO: An object containing information about the generated backend code.
        """
        self.logger.info("Starting backend code generation process")

        # response = self.generate_backend_code.execute(schema)
        response = GenerationResponseDTO()
        self.copy_template()
        generated_files = {}
        for generator in self.generators:
            generated_files.update(generator.generate(schema))
            self.output_writer.write_multiple_files(generated_files)
            
        # Post-processing and additional tasks
        self._update_composer_json(response)
        self._update_env_file(response)
        self._generate_docker_files(response)

        # self.logger.info("Backend code generation completed successfully")
        
        return GenerationResponseDTO(generated_files=generated_files)

        # return response

    def _update_composer_json(self, response: GenerationResponseDTO):
        """Update the composer.json file with any necessary dependencies."""
        try:
            composer_path = os.path.join(self.output_writer.base_path ,"backend", "composer.json")
            if not os.path.exists(composer_path):
                # Create a default composer.json if it doesn't exist
                composer_data = {
                    "require": {
                        "php": "^8.1",
                        "laravel/framework": "^10.10",
                    }
                }
            else:
                with open(composer_path, 'r') as file:
                    composer_data = json.load(file)

            # Add or update dependencies
            composer_data['require'].update({
                "laravel/sanctum": "^3.3",
                "spatie/laravel-permission": "^5.5"
            })

            # Write updated composer.json
            updated_content = json.dumps(composer_data, indent=4)
            self.output_writer.write_file("backend/composer.json", updated_content)
            response.add_generated_file("composer.json", updated_content)

            self.logger.info("composer.json updated successfully")
        except Exception as e:
            error_message = f"Error updating composer.json: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)

    def _update_env_file(self, response: GenerationResponseDTO):
        """Update the .env file with necessary configuration."""
        try:
            env_path = os.path.join(self.output_writer.base_path,"backend" ,".env")
            if not os.path.exists(env_path):
                # Create a default .env if it doesn't exist
                env_content = "APP_NAME=Laravel\nDB_CONNECTION=mysql\nDB_HOST=127.0.0.1\nDB_PORT=3306\n"
            else:
                with open(env_path, 'r') as file:
                    env_content = file.read()

            # Add or update environment variables
            env_lines = env_content.splitlines()
            env_dict = dict(line.split('=', 1) for line in env_lines if '=' in line)

            env_dict['APP_NAME'] = f'"{self.config_loader.get("app_name", "Laravel")}"'
            env_dict['DB_DATABASE'] = self.config_loader.get("database_name", "laravel")

            # Write updated .env file
            updated_content = '\n'.join(f"{k}={v}" for k, v in env_dict.items())
            self.output_writer.write_file("backend/.env", updated_content)
            response.add_generated_file(".env", updated_content)

            self.logger.info(".env file updated successfully")
        except Exception as e:
            error_message = f"Error updating .env file: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)

    def _generate_docker_files(self, response: GenerationResponseDTO):
        """Generate Docker-related files for the backend."""
        try:
            # Generate Dockerfile
            dockerfile_path = 'backend/Dockerfile'
            dockerfile_content = self._render_template_safe('backend/laravel/dockerFile.stub', {
                'php_version': self.config_loader.get('php_version', '8.1')
            })
            if dockerfile_content:
                self.output_writer.write_file(dockerfile_path, dockerfile_content)
                response.add_generated_file(dockerfile_path, dockerfile_content)

            # Generate docker-compose.yml
            docker_compose_path = 'backend/docker-compose.yml'
            docker_compose_content = self._render_template_safe('backend/laravel/docker-compose.stub', {
                'app_name': self.config_loader.get('app_name', 'laravel'),
                'database_name': self.config_loader.get('database_name', 'laravel')
            })
            if docker_compose_content:
                self.output_writer.write_file(docker_compose_path, docker_compose_content)
                response.add_generated_file(docker_compose_path, docker_compose_content)

            self.logger.info("Docker files generated successfully")
        except Exception as e:
            error_message = f"Error generating Docker files: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)

    def _render_template_safe(self, template_name: str, context: Dict[str, Any]) -> str:
        """Safely render a template, returning an empty string if the template is not found."""
        try:
            return self.template_renderer.render(template_name, context)
        except Exception as e:
            self.logger.warning(f"Error rendering template {template_name}: {str(e)}")
            return ""
        
    
    def copy_template(self) -> str:
        self.logger.info("copying empty backend template")
        
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Navigate to the project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
        
        # Construct the path to the template
        source = os.path.join(project_root, "src", "templates", "backend", "laravel", "template")
        
        self.output_dir = os.path.join(project_root, "output", "backend")
        
        self.logger.info(f"Attempting to copy from: {source}")
        self.logger.info(f"Copying to: {self.output_dir}")
        
        if not os.path.exists(source):
            self.logger.error(f"Source directory does not exist: {source}")
            return ""

        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        
        shutil.copytree(source, self.output_dir)
        return self.output_dir