from abc import ABC, abstractmethod
from typing import Dict

class FileGenerator(ABC):
    @abstractmethod
    def generate(self, model: Dict) -> Dict[str, str]:
        pass