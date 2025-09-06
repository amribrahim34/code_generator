from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities .string_utils import to_pascal_case, to_snake_case, pluralize

class MailGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer


    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        mail_types = ['Created', 'Updated', 'Deleted']

        for mail_type in mail_types:
            for model in schema.models:
                mail_content = self._generate_mail(model, mail_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Mail/{model_name}{mail_type}Mail.php"
                generated_files[file_path] = mail_content
                
        return generated_files

    def get_output_path(self, model_name: str , mail_type) -> str:
        return f"backend/app/Mail/{model_name}{mail_type}Mail.php"

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/mail.stub', context)

    def _generate_mail(self, model: Union[Dict[str, Any], Model], mail_type: str) -> str:
        context = self.prepare_context(model, mail_type)
        template = self.get_template('mail')
        return self.template_renderer.render('backend/laravel/mail.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], mail_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'mail_name': f"{model_name}{mail_type}Mail",
            'namespace': self.config_loader.get('mail_namespace', 'App\\Mail'),
            'model_namespace': self.config_loader.get('model_namespace', 'App\\Models'),
            'attributes': attributes,
            'model_variable': to_snake_case(model_name),
            'mail_type': mail_type,
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('mail_template_path', 'backend/laravel/mail.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")
