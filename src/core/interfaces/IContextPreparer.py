from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union
from src.core.entities.schema import Model, Attribute, Relationship ,Schema

class IContextPreparer(ABC):
    @abstractmethod
    def prepare_context(self, model: Union[Dict[str, Any], Model], type: str) -> Dict[str, Any]:
        pass