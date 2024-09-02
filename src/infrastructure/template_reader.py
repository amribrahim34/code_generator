import os
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape

class TemplateReader:
    def __init__(self, template_dir: str):
        self.template_dir = template_dir
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def read_template(self, template_name: str) -> str:
        """
        Read a template file and return its contents as a string.
        
        :param template_name: Name of the template file (with extension)
        :return: Contents of the template file as a string
        """
        full_path = os.path.join(self.template_dir, template_name)
        try:
            with open(full_path, 'r') as template_file:
                return template_file.read()
        except FileNotFoundError:
            raise ValueError(f"Template file not found: {full_path}")

    def render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Render a template file with the given context using Jinja2.
        
        :param template_name: Name of the template file (with extension)
        :param context: Dictionary containing variables to be rendered in the template
        :return: Rendered template as a string
        """
        template = self.env.get_template(template_name)
        return template.render(**context)

    def render_string_template(self, template_string: str, context: Dict[str, Any]) -> str:
        """
        Render a template string with the given context using Jinja2.
        
        :param template_string: The template as a string
        :param context: Dictionary containing variables to be rendered in the template
        :return: Rendered template as a string
        """
        template = self.env.from_string(template_string)
        return template.render(**context)

    def list_templates(self, extension: Optional[str] = None) -> list:
        """
        List all template files in the template directory.
        
        :param extension: Optional file extension to filter templates
        :return: List of template file names
        """
        templates = []
        for root, _, files in os.walk(self.template_dir):
            for file in files:
                if extension is None or file.endswith(extension):
                    templates.append(os.path.relpath(os.path.join(root, file), self.template_dir))
        return templates

    def add_filter(self, name: str, filter_func: callable):
        """
        Add a custom filter to the Jinja2 environment.
        
        :param name: Name of the filter
        :param filter_func: Function to be used as a filter
        """
        self.env.filters[name] = filter_func

    def add_global(self, name: str, value: Any):
        """
        Add a global variable to the Jinja2 environment.
        
        :param name: Name of the global variable
        :param value: Value of the global variable
        """
        self.env.globals[name] = value