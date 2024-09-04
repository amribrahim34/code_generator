import importlib
from typing import Dict, Any, List
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.application.dtos.generation_response_dto import GenerationResponseDTO
from src.core.interfaces.code_generator import ICodeGenerator

class GenerateBackendCode:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.template_renderer = template_renderer
        self.generators: Dict[str, ICodeGenerator] = self._initialize_generators()

    def execute(self, schema: Schema) -> GenerationResponseDTO:
        """
        Orchestrates the backend code generation process.

        Args:
            schema (Schema): The parsed schema object containing all models and relationships.

        Returns:
            GenerationResponseDTO: An object containing information about the generated backend code.
        """
        self.logger.info("Starting backend code generation process")
        response = GenerationResponseDTO()

        if not self.generators:
            warning_message = "No backend code generators were initialized. No code will be generated."
            self.logger.warning(warning_message)
            response.add_warning(warning_message)
            return response

        try:
            enabled_generators = self.config_loader.get('generators', [])
            for generator_name in enabled_generators:
                if generator_name in self.generators:
                    generated_files = self._generate_files(generator_name, schema)
                    for file_path, content in generated_files.items():
                        response.add_generated_file(file_path, content)
                else:
                    warning_message = f"Generator '{generator_name}' not found. Skipping."
                    self.logger.warning(warning_message)
                    response.add_warning(warning_message)

            statistics = self._compile_statistics(response.generated_files)
            response.set_statistics(statistics)

            self.logger.info("Backend code generation completed successfully")

        except Exception as e:
            error_message = f"Error during backend code generation: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)

        return response

    def _initialize_generators(self) -> Dict[str, ICodeGenerator]:
        """Initialize and return a dictionary of all available generators."""
        generators = {}
        generator_configs = self.config_loader.get('generators', [])

        for generator_name in generator_configs:
            try:
                # Convert generator name to PascalCase and append 'Generator'
                class_name = ''.join(word.capitalize() for word in generator_name.split('_')) + 'Generator'
                module_name = f"src.core.generators.{generator_name}_generator"

                # Dynamically import the module and class
                module = importlib.import_module(module_name)
                generator_class = getattr(module, class_name)

                # Initialize the generator
                generator = generator_class(self.config_loader, self.template_renderer)
                generators[generator_name] = generator

                self.logger.info(f"Successfully initialized {class_name}")

            except ImportError:
                self.logger.warning(f"Generator module for '{generator_name}' not found. Skipping.")
            except AttributeError:
                self.logger.warning(f"Generator class '{class_name}' not found in module. Skipping.")
            except Exception as e:
                self.logger.error(f"Error initializing generator for '{generator_name}': {str(e)}")

        return generators

    def _generate_files(self, generator_name: str, schema: Schema) -> Dict[str, str]:
        """Generate files using the specified generator."""
        generator = self.generators[generator_name]
        files = generator.generate(schema)
        for file_path, content in files.items():
            self.output_writer.write_file(file_path, content)
        return files

    def _compile_statistics(self, generated_files: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compile statistics about the generated backend code."""
        total_files = len(generated_files)
        total_lines = sum(len(file_info['content'].splitlines()) for file_info in generated_files)
        
        files_per_type = {}
        for file_info in generated_files:
            file_type = file_info.get('type', 'unknown')
            files_per_type[file_type] = files_per_type.get(file_type, 0) + 1

        return {
            "total_files": total_files,
            "total_lines": total_lines,
            "files_per_type": files_per_type
        }