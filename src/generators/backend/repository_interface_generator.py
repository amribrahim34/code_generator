from typing import Dict, Any, Union
from src.core.interfaces.generator import Generator
from src.infrastructure.template_reader import TemplateReader
from src.core.models.schema import Model

class RepositoryInterfaceGenerator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        interface_content = self._generate_interface(model)
        model_name = model.name if isinstance(model, Model) else model['name']
        return {f"app/Repositories/Interfaces/{model_name}RepositoryInterface.php": interface_content}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('repository_interface_template_path', 'backend/repository_interface_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return template.format(**context)

    def _generate_interface(self, model: Union[Dict[str, Any], Model]) -> str:
        template = self.get_template('repository_interface')
        
        model_name = model.name if isinstance(model, Model) else model['name']
        context = {
            'interface_name': f"{model_name}RepositoryInterface",
            'model_name': model_name,
            'namespace': self.config.get('repository_interface_namespace', 'App\\Repositories\\Interfaces')
        }
        
        return self.render_template(template, context)