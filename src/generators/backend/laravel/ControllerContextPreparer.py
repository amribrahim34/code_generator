from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize
from typing import Dict, Any, List, Union
from src.core.interfaces.config_loader import IConfigLoader
from src.core.entities.schema import Model, Attribute, Relationship ,Schema
from src.core.interfaces.IContextPreparer import IContextPreparer

class ControllerContextPreparer(IContextPreparer):
    def __init__(self, config_loader: IConfigLoader):
        self.config_loader = config_loader

    def prepare_context(self, model: Union[Dict[str, Any], Model], controller_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships

        return {
            'class_name': f"{model_name}Controller",
            'model_name': model_name,
            'model_variable': to_snake_case(model_name),
            'model_plural': pluralize(to_snake_case(model_name)),
            'namespace': f"App\\Http\\Controllers\\{controller_type}",
            'repository_namespace': f"App\\Repositories\\Interfaces\\{controller_type}",
            'request_namespace': f"App\\Http\\Requests\\{controller_type}",
            'resource_namespace': f"App\\Http\\Resources\\{controller_type}",
            'use_repository': True,
            'use_form_requests': True,
            'model_attributes': attributes,
            'relationships': relationships,
            'api_version': self.config_loader.get('api_versions', {}).get(controller_type.lower(), 'v1'),
            'request_class': f"{model_name}Request",
            'resource_class': f"{model_name}Resource",
            'repository_interface': f"I{model_name}Repository",
            'controller_type': controller_type,
            'translation_key': to_snake_case(model_name),
        }