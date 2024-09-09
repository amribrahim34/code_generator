from typing import Dict, Any
from src.core.entities.schema import Schema
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.logger import ILogger
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.application.dtos.generation_response_dto import GenerationResponseDTO

class GenerateReactNativeCode:
    def __init__(self, config_loader: IConfigLoader, logger: ILogger, output_writer: IOutputWriter, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.logger = logger
        self.output_writer = output_writer
        self.template_renderer = template_renderer

    def execute(self, schema: Schema) -> GenerationResponseDTO:
        """
        Orchestrates the React Native code generation process.
        
        Args:
            schema (Schema): The parsed schema object containing all models and relationships.
        
        Returns:
            GenerationResponseDTO: An object containing information about the generated React Native code.
        """
        self.logger.info("Starting React Native code generation")
        response = GenerationResponseDTO()

        try:
            generated_files = {}
            generated_files.update(self.generate_components(schema))
            generated_files.update(self.generate_screens(schema))
            generated_files.update(self.generate_navigation(schema))
            generated_files.update(self.generate_store(schema))

            for file_path, content in generated_files.items():
                response.add_generated_file(file_path, content)

            statistics = self._compile_statistics(generated_files)
            response.set_statistics(statistics)

            self.logger.info("React Native code generation completed successfully")
            return response

        except Exception as e:
            error_message = f"Error during React Native code generation: {str(e)}"
            self.logger.error(error_message)
            response.add_error(error_message)
            return response

    def generate_components(self, schema: Schema) -> Dict[str, str]:
        """
        Generate React Native component files for each model in the schema.
        
        Args:
            schema (Schema): The parsed schema object.
        
        Returns:
            Dict[str, str]: A dictionary containing the generated component file paths and content.
        """
        components = {}
        for model in schema.models:
            component_name = f"{model.name}Component"
            component_content = self.template_renderer.render(
                'mobile/react_native/component.stub',
                {'model': model}
            )
            file_path = f"src/components/{component_name}.js"
            components[file_path] = component_content
        return components

    def generate_screens(self, schema: Schema) -> Dict[str, str]:
        """
        Generate React Native screen files for each model in the schema.
        
        Args:
            schema (Schema): The parsed schema object.
        
        Returns:
            Dict[str, str]: A dictionary containing the generated screen file paths and content.
        """
        screens = {}
        for model in schema.models:
            screen_types = ['List', 'Detail', 'Form']
            for screen_type in screen_types:
                screen_name = f"{model.name}{screen_type}Screen"
                screen_content = self.template_renderer.render(
                    f'mobile/react_native/{screen_type.lower()}_screen.stub',
                    {'model': model}
                )
                file_path = f"src/screens/{screen_name}.js"
                screens[file_path] = screen_content
        return screens

    def generate_navigation(self, schema: Schema) -> Dict[str, str]:
        """
        Generate React Navigation configuration for all models in the schema.
        
        Args:
            schema (Schema): The parsed schema object.
        
        Returns:
            Dict[str, str]: A dictionary containing the generated navigation file paths and content.
        """
        navigation = {}
        navigation_content = self.template_renderer.render(
            'mobile/react_native/navigation.stub',
            {'models': schema.models}
        )
        file_path = "src/navigation/AppNavigator.js"
        navigation[file_path] = navigation_content
        return navigation

    def generate_store(self, schema: Schema) -> Dict[str, str]:
        """
        Generate Redux store configuration, actions, and reducers for each model in the schema.
        
        Args:
            schema (Schema): The parsed schema object.
        
        Returns:
            Dict[str, str]: A dictionary containing the generated store file paths and content.
        """
        store_files = {}
        
        # Generate root reducer
        root_reducer_content = self.template_renderer.render(
            'mobile/react_native/root_reducer.stub',
            {'models': schema.models}
        )
        store_files["src/store/rootReducer.js"] = root_reducer_content

        # Generate actions and reducers for each model
        for model in schema.models:
            actions_content = self.template_renderer.render(
                'mobile/react_native/actions.stub',
                {'model': model}
            )
            reducer_content = self.template_renderer.render(
                'mobile/react_native/reducer.stub',
                {'model': model}
            )
            store_files[f"src/store/actions/{model.name}Actions.js"] = actions_content
            store_files[f"src/store/reducers/{model.name}Reducer.js"] = reducer_content

        # Generate store configuration
        store_config_content = self.template_renderer.render(
            'mobile/react_native/store_config.stub',
            {}
        )
        store_files["src/store/configureStore.js"] = store_config_content

        return store_files

    def _compile_statistics(self, generated_files: Dict[str, str]) -> Dict[str, Any]:
        """
        Compile statistics about the generated React Native code.

        Args:
            generated_files (Dict[str, str]): Dictionary where keys are file paths and values are file contents.

        Returns:
            Dict[str, Any]: Statistics about the generated React Native code.
        """
        stats = {
            "total_files": len(generated_files),
            "total_lines": sum(content.count('\n') + 1 for content in generated_files.values()),
            "files_per_type": {}
        }

        for file_path in generated_files.keys():
            file_type = file_path.split('/')[-2] if '/' in file_path else 'unknown'
            stats["files_per_type"][file_type] = stats["files_per_type"].get(file_type, 0) + 1

        return stats