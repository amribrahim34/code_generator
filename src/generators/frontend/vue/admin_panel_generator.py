from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_kebab_case, pluralize

class AdminPanelGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, models: List[Union[Dict[str, Any], Model]]) -> Dict[str, str]:
        generated_files = {}
        
        # Generate main admin panel component
        admin_panel_content = self._generate_admin_panel(models)
        generated_files['src/views/AdminPanel.vue'] = admin_panel_content

        # Generate individual model management components
        for model in models:
            model_name = model['name'] if isinstance(model, dict) else model.name
            model_component_content = self._generate_model_component(model)
            file_path = f"src/components/admin/{model_name}Management.vue"
            generated_files[file_path] = model_component_content

        return generated_files

    def _generate_admin_panel(self, models: List[Union[Dict[str, Any], Model]]) -> str:
        context = self._prepare_admin_panel_context(models)
        template = self.get_template('admin_panel')
        return self.template_renderer.render(template, context)

    def _generate_model_component(self, model: Union[Dict[str, Any], Model]) -> str:
        context = self._prepare_model_component_context(model)
        template = self.get_template('model_management')
        return self.template_renderer.render(template, context)

    def _prepare_admin_panel_context(self, models: List[Union[Dict[str, Any], Model]]) -> Dict[str, Any]:
        model_list = []
        for model in models:
            model_name = model['name'] if isinstance(model, dict) else model.name
            model_list.append({
                'name': model_name,
                'route': to_kebab_case(pluralize(model_name)),
                'component': f"{model_name}Management",
            })

        return {
            'models': model_list,
            'app_name': self.config_loader.get('project.name', 'Admin Panel'),
        }

    def _prepare_model_component_context(self, model: Union[Dict[str, Any], Model]) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        return {
            'model_name': model_name,
            'model_name_plural': pluralize(model_name),
            'model_name_kebab': to_kebab_case(model_name),
            'attributes': self._prepare_attributes(attributes),
            'use_typescript': self.config_loader.get('frontend.use_typescript', False),
        }

    def _prepare_attributes(self, attributes: Union[List[Dict[str, Any]], List[Attribute]]) -> List[Dict[str, Any]]:
        prepared_attributes = []
        for attr in attributes:
            if isinstance(attr, dict):
                prepared_attributes.append({
                    'name': attr['name'],
                    'type': attr['type'],
                    'required': attr.get('required', False),
                    'editable': not attr.get('primary_key', False),
                })
            else:
                prepared_attributes.append({
                    'name': attr.name,
                    'type': attr.type,
                    'required': attr.required,
                    'editable': not attr.primary_key,
                })
        return prepared_attributes

    def get_template(self, template_name: str) -> str:
        if template_name == 'admin_panel':
            template_path = self.config_loader.get('admin_panel_template_path', 'frontend/vue/admin_panel.vue')
        else:
            template_path = self.config_loader.get('model_management_template_path', 'frontend/vue/model_management.vue')
        return self.template_renderer.read_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass