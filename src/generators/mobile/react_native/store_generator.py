from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_camel_case, to_snake_case
import logging

class StoreGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        root_reducer_content = self._generate_root_reducer(schema.models)
        generated_files["mobile/store/rootReducer.js"] = root_reducer_content

        store_config_content = self._generate_store_config()
        generated_files["mobile/store/configureStore.js"] = store_config_content

        for model in schema.models:
            actions_content = self._generate_actions(model)
            reducer_content = self._generate_reducer(model)
            model_name = model.name if isinstance(model, Model) else model['name']
            snake_name = to_snake_case(model_name)
            generated_files[f"mobile/store/actions/{snake_name}Actions.js"] = actions_content
            generated_files[f"mobile/store/reducers/{snake_name}Reducer.js"] = reducer_content

        return generated_files

    def _generate_root_reducer(self, models: List[Model]) -> str:
        context = {
            'models': [
                {
                    'name': model.name if isinstance(model, Model) else model['name'],
                    'snake_name': to_snake_case(model.name if isinstance(model, Model) else model['name'])
                }
                for model in models
            ],
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
        }
        template_name = 'mobile/react_native/root_reducer.stub'
        return self.template_renderer.render(template_name, context)

    def _generate_store_config(self) -> str:
        context = {
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
        }
        template_name = 'mobile/react_native/store_config.stub'
        return self.template_renderer.render(template_name, context)

    def _generate_actions(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self._prepare_model_context(model)
        template_name = 'mobile/react_native/action.stub'
        return self.template_renderer.render(template_name, context)

    def _generate_reducer(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self._prepare_model_context(model)
        template_name = 'mobile/react_native/reducer.stub'
        return self.template_renderer.render(template_name, context)

    def _prepare_model_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        return {
            'model_name': model_name,
            'pascal_name': to_pascal_case(model_name),
            'camel_name': to_camel_case(model_name),
            'snake_name': to_snake_case(model_name),
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get(f'templates.mobile.react_native.{template_name}', f'mobile/react_native/{template_name}.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")


    def get_output_path(self, file_name: str) -> str:
        return f"src/store/{file_name}"
    
    
    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except Exception as e:
            logging.error(f"Error rendering template: {str(e)}")
            raise
        
    def prepare_context(self, model: Union[Dict[str, Any], Model], component_type: str) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        
        context = {
            'model_name': model_name,
            'component_name': f"{model_name}{component_type}",
            'model_kebab': to_kebab_case(model_name),
            'attributes': attributes,
            'model_attributes': self._generate_model_attributes(attributes),
            'use_typescript': self.config_loader.get('mobile.use_typescript', True),
            'use_hooks': self.config_loader.get('mobile.use_hooks', True),
        }
        return context