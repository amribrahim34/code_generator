import importlib
import shutil
import os
from typing import Dict, Any, List
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.use_cases.generate_frontend_code import GenerateFrontendCode
from src.application.dtos.generation_response_dto import GenerationResponseDTO

class FrontendGenerationService:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.template_renderer = template_renderer
        self.logger.info("this is the backend generation service")
        self.generators = self._initialize_generators()
        self.generate_frontend_code = GenerateFrontendCode(
            config_loader,
            logger,
            output_writer,
            template_renderer
        )

        
    def _initialize_generators(self):
        generators = []
        generator_configs = self.config_loader.get('generators.frontend', [])
        self.logger.info(f"these are the config generators {generator_configs}")
        for gen_config in generator_configs:
            try:
                module = importlib.import_module(gen_config['module'])
                generator_class = getattr(module, gen_config['class'])
                generators.append(generator_class(self.config_loader, self.template_renderer))
                self.logger.info(f"this is a loaded generator name {gen_config['name']}")
                self.logger.info(f"this is a loaded generator module {gen_config['module']}")
            except Exception as e:
                self.logger.error(f"Failed to initialize generator {gen_config['name']}: {str(e)}")
        return generators


    def generate(self, schema: Schema) -> GenerationResponseDTO:
        """
        Coordinate the frontend code generation process.

        Args:
            schema (Schema): The parsed schema object containing all models and relationships.

        Returns:
            GenerationResponseDTO: An object containing information about the generated frontend code.
        """
        self.logger.info("Starting frontend code generation process")

        response = GenerationResponseDTO()

        try:
            # Copy the frontend template
            self.copy_template()
            
            generated_files = {}
            for generator in self.generators:
                generated_files.update(generator.generate(schema))
            
            self.output_writer.write_multiple_files(generated_files)

            # Compile statistics
            statistics = self._compile_statistics(generated_files)
            response.set_statistics(statistics)

            for file_path, content in generated_files.items():
                response.add_generated_file(file_path, content)

            self.logger.info("Frontend code generation completed successfully")

            return response

        except Exception as e:
            error_message = f"Error during frontend code generation: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)
            return response

    def _update_package_json(self):
        """Update the package.json file with necessary dependencies and scripts."""
        try:
            package_path = "package.json"
            package_content = self.output_writer.read_file(package_path)
            
            import json
            package_data = json.loads(package_content)

            # Add or update dependencies
            package_data['dependencies'].update({
                "axios": "^0.21.1",
                "vuex": "^4.0.0",
                "vue-router": "^4.0.0",
                "@vue/composition-api": "^1.0.0-rc.1",
                "tailwindcss": "^2.0.4"
            })

            # Add or update dev dependencies
            package_data['devDependencies'].update({
                "@vue/cli-plugin-babel": "~4.5.0",
                "@vue/cli-plugin-eslint": "~4.5.0",
                "@vue/cli-plugin-router": "~4.5.0",
                "@vue/cli-plugin-vuex": "~4.5.0",
                "@vue/cli-service": "~4.5.0"
            })

            # Add or update scripts
            package_data['scripts'].update({
                "serve": "vue-cli-service serve",
                "build": "vue-cli-service build",
                "lint": "vue-cli-service lint"
            })

            # Write updated package.json
            updated_content = json.dumps(package_data, indent=2)
            self.output_writer.write_file(package_path, updated_content)

            self.logger.info("package.json updated successfully")
        except Exception as e:
            self.logger.error(f"Error updating package.json: {str(e)}")

    def _update_vue_config(self):
        """Create or update vue.config.js file."""
        try:
            vue_config_content = self.template_renderer.render('vue.config.js', {
                'app_name': self.config_loader.get('app_name', 'Vue App')
            })
            self.output_writer.write_file('vue.config.js', vue_config_content)

            self.logger.info("vue.config.js updated successfully")
        except Exception as e:
            self.logger.error(f"Error updating vue.config.js: {str(e)}")

    def _generate_dockerfiles(self):
        """Generate Docker-related files for the frontend."""
        try:
            # Generate Dockerfile
            dockerfile_content = self.template_renderer.render('Dockerfile.frontend', {
                'node_version': self.config_loader.get('node_version', '14')
            })
            self.output_writer.write_file('Dockerfile', dockerfile_content)

            # Generate docker-compose.yml
            docker_compose_content = self.template_renderer.render('docker-compose.frontend.yml', {
                'app_name': self.config_loader.get('app_name', 'vue-app')
            })
            self.output_writer.write_file('docker-compose.yml', docker_compose_content)

            self.logger.info("Docker files generated successfully")
        except Exception as e:
            self.logger.error(f"Error generating Docker files: {str(e)}")

    def _compile_statistics(self, generated_files: Dict[str, str]) -> Dict[str, Any]:
        """
        Compile statistics about the generated frontend code.

        Args:
            generated_files (Dict[str, str]): Dictionary where keys are file paths and values are file contents.

        Returns:
            Dict[str, Any]: Statistics about the generated frontend code.
        """
        stats = {
            "total_files": 0,
            "total_lines": 0,
            "files_per_type": {}
        }

        for file_path, content in generated_files.items():
            stats["total_files"] += 1
            stats["total_lines"] += content.count('\n') + 1
            
            # Extract file type from the path
            file_type = file_path.split('/')[-2] if '/' in file_path else 'unknown'
            stats["files_per_type"][file_type] = stats["files_per_type"].get(file_type, 0) + 1

        return stats
    
    def copy_template(self) -> str:
        self.logger.info("Copying empty frontend template")
        
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Navigate to the project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
        
        # Construct the path to the frontend template
        source = os.path.join(project_root, "src", "templates", "frontend", "vue", "template")
        
        self.output_dir = os.path.join(project_root, "output", "admin")
        
        self.logger.info(f"Attempting to copy from: {source}")
        self.logger.info(f"Copying to: {self.output_dir}")
        
        if not os.path.exists(source):
            self.logger.error(f"Source directory does not exist: {source}")
            return ""

        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        
        shutil.copytree(source, self.output_dir)
        return self.output_dir
