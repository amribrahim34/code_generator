
from typing import Dict, Any, List, Union
from src.core.interfaces.IContextPreparer import IContextPreparer
from src.core.entities.schema import Model, Attribute, Relationship ,Schema

class CollectionContextPreparer(IContextPreparer):
    def prepare_context(self, model: Union[Dict[str, Any], Model], collection_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        return {
            'model_name': model_name,
            'collection_name': f"{model_name}Collection",
            'namespace': f"App\\Http\\Resources\\{collection_type}",
            'resource_class': f"{model_name}Resource",
            'collection_type': collection_type,
        }