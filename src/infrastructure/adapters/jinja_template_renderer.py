import os
from typing import Dict, Any, Optional, List
from jinja2 import Environment, FileSystemLoader, select_autoescape ,Template
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class JinjaTemplateRenderer(ITemplateRenderer):
    def __init__(self, template_dir: str):
        self._template_dir = template_dir
        self._env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
         # Add custom filters
        self._env.filters['to_snake_case'] = to_snake_case
        self._env.filters['pluralize'] = pluralize

    def load_template(self, template_name: str) -> str:
        try:
            return self._env.get_template(template_name).render()
        except Exception as e:
            raise ValueError(f"Error loading template {template_name}: {str(e)}")

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        try:
            template = self._env.get_template(template_name)
            return template.render(**context)
        except Exception as e:
            raise ValueError(f"Error rendering template {template_name}: {str(e)}")

    def render_string_template(self, template_string: str, context: Dict[str, Any]) -> str:
        try:
            template = self._env.from_string(template_string)
            return template.render(**context)
        except Exception as e:
            raise ValueError(f"Error rendering string template: {str(e)}")

    def list_templates(self, extension: Optional[str] = None) -> List[str]:
        templates = []
        for root, _, files in os.walk(self._template_dir):
            for file in files:
                if extension is None or file.endswith(extension):
                    templates.append(os.path.relpath(os.path.join(root, file), self._template_dir))
        return templates

    def add_filter(self, name: str, filter_func: callable) -> None:
        self._env.filters[name] = filter_func

    def add_global(self, name: str, value: Any) -> None:
        self._env.globals[name] = value

    def get_template_dir(self) -> str:
        return self._template_dir

    def set_template_dir(self, template_dir: str) -> None:
        self._template_dir = template_dir
        self._env.loader = FileSystemLoader(template_dir)
    
    def render_with_custom_delimiter(self, template_name: str, context: Dict[str, Any]):
        try:
            # Get the template
            jinja_template = self._env.get_template(template_name)
            
            # Render the template with the original environment
            # This gives us the template content as a string
            template_content = jinja_template.render()
            
            # Create a new Template with custom delimiters
            custom_template = Template(template_content, variable_start_string='[[', variable_end_string=']]')
            
            # Render the template with the provided context
            return custom_template.render(**context)
        except Exception as e:
            raise ValueError(f"Error rendering template {template_name}: {str(e)}")