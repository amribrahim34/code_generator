import os
from src.parsers.json_parser import JsonParser
from src.generators.backend.model_generator import ModelGenerator
from src.generators.backend.controller_generator import ControllerGenerator
from src.generators.backend.migration_generator import MigrationGenerator
from src.generators.backend.request_generator import RequestGenerator
from src.generators.backend.resource_generator import ResourceGenerator
from src.generators.backend.repository_generator import RepositoryGenerator
from src.generators.backend.repository_interface_generator import RepositoryInterfaceGenerator
from src.generators.admin.component_generator import ComponentGenerator
from src.generators.admin.package_json_generator import PackageJsonGenerator
from src.generators.admin.route_generator import RouteGenerator
from src.generators.admin.store_generator import StoreGenerator
from src.generators.admin.type_generator import TypeGenerator
from src.generators.admin.view_generator import ViewGenerator

class CodeGenerator:
    def __init__(self, config):
        self.config = config
        self.parser = JsonParser()
        self.models = []  # This will be populated in the generate method

    def _initialize_backend_generators(self):
        return [
            ModelGenerator(),
            ControllerGenerator(),
            MigrationGenerator(),
            RequestGenerator(),
            ResourceGenerator(),
            RepositoryGenerator(),
            RepositoryInterfaceGenerator(),
        ]

    def _initialize_admin_generators(self):
        return [
            ComponentGenerator(self.config, self.models),
             PackageJsonGenerator(self.config.get('project_name', 'default-project'), 
                             self.config.get('project_description', 'Auto-generated admin panel')),
            RouteGenerator(self.config, self.models),
            StoreGenerator(self.config, self.models),
            TypeGenerator(self.config, self.models),
            ViewGenerator(self.config, self.models),
        ]

    def generate(self, schema):
        output = {}
        if 'models' in schema:
            self.models = schema['models']
            backend_generators = self._initialize_backend_generators()
            admin_generators = self._initialize_admin_generators()
            
            for model in self.models:
                for generator in backend_generators:
                    output.update(generator.generate(model))
                for generator in admin_generators:
                    result = generator.generate(model)
                    if isinstance(result, dict):
                        output.update(result)
                    else:
                        print(f"Warning: Generator {type(generator).__name__} did not return a dictionary. Skipping.")
        else:
            raise ValueError("The schema does not contain a 'models' key.")
        return output

    def save_to_files(self, generated_code, output_path):
        for filename, content in generated_code.items():
            file_path = os.path.join(output_path, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(content)