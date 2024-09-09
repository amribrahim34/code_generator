import importlib
import shutil
import os
from typing import Dict, Any, List
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.use_cases.generate_react_native_code import GenerateReactNativeCode
from src.application.dtos.generation_response_dto import GenerationResponseDTO

class ReactNativeGenerationService:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.template_renderer = template_renderer
        self.logger.info("This is the React Native generation service")
        self.generators = self._initialize_generators()
        self.generate_react_native_code = GenerateReactNativeCode(
            config_loader,
            logger,
            output_writer,
            template_renderer
        )
        self.output_dir = None

    def _initialize_generators(self):
        generators = []
        generator_configs = self.config_loader.get('generators.react_native', [])
        self.logger.info(f"These are the config generators: {generator_configs}")
        for gen_config in generator_configs:
            try:
                module = importlib.import_module(gen_config['module'])
                generator_class = getattr(module, gen_config['class'])
                generators.append(generator_class(self.config_loader, self.template_renderer))
                self.logger.info(f"Loaded generator name: {gen_config['name']}")
                self.logger.info(f"Loaded generator module: {gen_config['module']}")
            except Exception as e:
                self.logger.error(f"Failed to initialize generator {gen_config['name']}: {str(e)}")
        return generators

    def generate(self, schema: Schema) -> GenerationResponseDTO:
        """
        Coordinate the React Native code generation process.

        Args:
            schema (Schema): The parsed schema object containing all models and relationships.

        Returns:
            GenerationResponseDTO: An object containing information about the generated React Native code.
        """
        self.logger.info("Starting React Native code generation process")

        response = GenerationResponseDTO()

        try:
            # Copy the React Native template
            self.copy_template()
            
            generated_files = {}
            for generator in self.generators:
                generated_files.update(generator.generate(schema))
            
            self.output_writer.write_multiple_files(generated_files)

            # Update package.json
            self._update_package_json()

            # Generate app.json
            self._generate_app_json()

            # Generate index.js
            self._generate_index_js()

            # Generate babel.config.js
            self._generate_babel_config()

            # Generate metro.config.js
            self._generate_metro_config()

            # Compile statistics
            statistics = self._compile_statistics(generated_files)
            response.set_statistics(statistics)

            for file_path, content in generated_files.items():
                response.add_generated_file(file_path, content)

            self.logger.info("React Native code generation completed successfully")

            return response

        except Exception as e:
            error_message = f"Error during React Native code generation: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)
            return response

    def _update_package_json(self):
        """Update the package.json file with necessary dependencies and scripts."""
        try:
            package_path = os.path.join(self.output_dir, "package.json")
            with open(package_path, 'r') as file:
                package_content = file.read()
            
            import json
            package_data = json.loads(package_content)

            # Add or update dependencies
            package_data['dependencies'].update({
                "react": "18.2.0",
                "react-native": "0.72.3",
                "@react-navigation/native": "^6.1.7",
                "@react-navigation/stack": "^6.3.17",
                "axios": "^1.4.0",
                "react-redux": "^8.1.1",
                "redux": "^4.2.1",
                "redux-thunk": "^2.4.2"
            })

            # Add or update dev dependencies
            package_data['devDependencies'].update({
                "@babel/core": "^7.20.0",
                "@babel/preset-env": "^7.20.0",
                "@babel/runtime": "^7.20.0",
                "@react-native/eslint-config": "^0.72.2",
                "@react-native/metro-config": "^0.72.9",
                "@tsconfig/react-native": "^3.0.0",
                "@types/react": "^18.0.24",
                "@types/react-test-renderer": "^18.0.0",
                "babel-jest": "^29.2.1",
                "eslint": "^8.19.0",
                "jest": "^29.2.1",
                "metro-react-native-babel-preset": "0.76.7",
                "prettier": "^2.4.1",
                "react-test-renderer": "18.2.0",
                "typescript": "4.8.4"
            })

            # Add or update scripts
            package_data['scripts'].update({
                "android": "react-native run-android",
                "ios": "react-native run-ios",
                "lint": "eslint .",
                "start": "react-native start",
                "test": "jest"
            })

            # Write updated package.json
            updated_content = json.dumps(package_data, indent=2)
            with open(package_path, 'w') as file:
                file.write(updated_content)

            self.logger.info("package.json updated successfully")
        except Exception as e:
            self.logger.error(f"Error updating package.json: {str(e)}")

    def _generate_app_json(self):
        """Generate app.json file."""
        try:
            app_name = self.config_loader.get('app_name', 'MyReactNativeApp')
            app_json_content = self.template_renderer.render('mobile/react_native/app.json.stub', {
                'app_name': app_name
            })
            self.output_writer.write_file('app.json', app_json_content)

            self.logger.info("app.json generated successfully")
        except Exception as e:
            self.logger.error(f"Error generating app.json: {str(e)}")

    def _generate_index_js(self):
        """Generate index.js file."""
        try:
            index_js_content = self.template_renderer.render('mobile/react_native/index.stub', {})
            self.output_writer.write_file('index.js', index_js_content)

            self.logger.info("index.js generated successfully")
        except Exception as e:
            self.logger.error(f"Error generating index.js: {str(e)}")

    def _generate_babel_config(self):
        """Generate babel.config.js file."""
        try:
            babel_config_content = self.template_renderer.render('mobile/react_native/babel.config.stub', {})
            self.output_writer.write_file('babel.config.js', babel_config_content)

            self.logger.info("babel.config.js generated successfully")
        except Exception as e:
            self.logger.error(f"Error generating babel.config.js: {str(e)}")

    def _generate_metro_config(self):
        """Generate metro.config.js file."""
        try:
            metro_config_content = self.template_renderer.render('mobile/react_native/metro.config.stub', {})
            self.output_writer.write_file('metro.config.js', metro_config_content)

            self.logger.info("metro.config.js generated successfully")
        except Exception as e:
            self.logger.error(f"Error generating metro.config.js: {str(e)}")

    def _compile_statistics(self, generated_files: Dict[str, str]) -> Dict[str, Any]:
        """
        Compile statistics about the generated React Native code.

        Args:
            generated_files (Dict[str, str]): Dictionary where keys are file paths and values are file contents.

        Returns:
            Dict[str, Any]: Statistics about the generated React Native code.
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
            file_type = file_path.split('.')[-1] if '.' in file_path else 'unknown'
            stats["files_per_type"][file_type] = stats["files_per_type"].get(file_type, 0) + 1

        return stats
    
    def copy_template(self) -> str:
        self.logger.info("Copying empty React Native template")
        
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Navigate to the project root
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
        
        # Construct the path to the React Native template
        source = os.path.join(project_root, "src", "templates", "mobile", "react_native", "template")
        
        self.output_dir = os.path.join(project_root, "output", "mobile")
        
        self.logger.info(f"Attempting to copy from: {source}")
        self.logger.info(f"Copying to: {self.output_dir}")
        
        if not os.path.exists(source):
            self.logger.error(f"Source directory does not exist: {source}")
            return ""

        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        
        shutil.copytree(source, self.output_dir)
        return self.output_dir