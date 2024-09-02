import os
import logging
from typing import Dict, List, Any
from src.core.interfaces.generator import Generator
from src.infrastructure.schema_parser import SchemaParser
from src.infrastructure.config_loader import ConfigLoader
from src.generators.backend.model_generator import ModelGenerator
from src.generators.backend.controller_generator import ControllerGenerator
from src.generators.backend.migration_generator import MigrationGenerator
from src.generators.backend.request_generator import RequestGenerator
from src.generators.backend.resource_generator import ResourceGenerator
from src.generators.backend.repository_generator import RepositoryGenerator
from src.generators.backend.repository_interface_generator import RepositoryInterfaceGenerator
from src.generators.frontend.component_generator import ComponentGenerator
from src.generators.frontend.package_json_generator import PackageJsonGenerator
from src.generators.frontend.route_generator import RouteGenerator
from src.generators.frontend.store_generator import StoreGenerator
from src.generators.frontend.type_generator import TypeGenerator
from src.generators.frontend.view_generator import ViewGenerator


class GenerationError(Exception):
    pass

class CodeGenerator:
    def __init__(self, config_path: str):
        logging.info(f"Initializing CodeGenerator with config path: {config_path}")
        self.config_loader = ConfigLoader(config_path)
        self.config = self.config_loader.load_config()
        self.models = []
        # logging.info(f"Loaded configuration: {self.config}")
        
    def _initialize_generators(self) -> Dict[str, Generator]:
        logging.info("Initializing generators...")
        generators = {
            "backend": {
                "model": ModelGenerator(self.config),
                "controller": ControllerGenerator(self.config),
                "migration": MigrationGenerator(self.config),
                "request": RequestGenerator(self.config),
                "resource": ResourceGenerator(self.config),
                "repository": RepositoryGenerator(self.config),
                "repository_interface": RepositoryInterfaceGenerator(self.config),
            },
            "frontend": {
                "component": ComponentGenerator(self.config),
                "package_json": PackageJsonGenerator(self.config),
                "route": RouteGenerator(self.config, self.models),
                "store": StoreGenerator(self.config),
                "type": TypeGenerator(self.config, self.models),
                "view": ViewGenerator(self.config , self.models),
            }
        }
        logging.info(f"Initialized generators: {generators.keys()}")
        return generators

    def generate(self, schema_path: str) -> Dict[str, str]:
        # logging.info(f"Generating code from schema: {schema_path}")
        self.schema_parser = SchemaParser(schema_path)
        schema = self.schema_parser.parse()
        
        if not schema.models:
            raise ValueError("The schema does not contain any models.")
        
        self.models = [model.__dict__ for model in schema.models]  
        # logging.info(f"Parsed models: {self.models}")
        
        generators = self._initialize_generators()
        output = {}

        for model in self.models:
            for category, category_generators in generators.items():
                for generator_name, generator in category_generators.items():
                    if generator_name in self.config.get('generators', []):
                        try:
                            logging.info(f"Generating {generator_name} for model {model['name']}...")
                            result = generator.generate(model)
                            if isinstance(result, dict):
                                output.update(result)
                                logging.info(f"Generated {len(result)} files for {generator_name}")
                            else:
                                raise GenerationError(f"Generator {generator_name} did not return a dictionary.")
                        except GenerationError as ge:
                            logging.error(f"Generation error for {generator_name}: {str(ge)}")
                        except Exception as e:
                            logging.error(f"Unexpected error in {generator_name} for model {model['name']}: {str(e)}")
                            raise GenerationError(f"Failed to generate {generator_name} for model {model['name']}") from e

        logging.info(f"Total generated files: {len(output)}")
        return output

    def save_to_files(self, generated_code: Dict[str, str]) -> None:
        logging.info("Saving generated files...")
        for filename, content in generated_code.items():
            category = 'backend' if filename.startswith('app/') else 'frontend'
            file_path = os.path.join(self.config.get(f'{category}_output_dir', ''), filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(content)
            logging.info(f"Saved: {file_path}")

        logging.info(f"Total files saved: {len(generated_code)}")