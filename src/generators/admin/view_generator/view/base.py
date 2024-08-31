from abc import ABC, abstractmethod
from typing import Dict

class FileGenerator(ABC):
    def __init__(self, template_dir: str, output_dir: str):
        self.template_dir = template_dir
        self.output_dir = output_dir

    @abstractmethod
    def generate(self, model: Dict) -> Dict[str, str]:
        pass