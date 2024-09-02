import os
from typing import Dict
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case
from src.infrastructure.config_loader import ConfigLoader
import logging
from jinja2 import Template
from src.infrastructure.template_reader import TemplateReader


class SidebarUpdater(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend/sidebar_stub.vue')
        self.output_dir = os.path.join(self.config['frontend']['output_dir'], 'src', self.config['frontend']['component_dir'])
        self.output_path = os.path.join(self.output_dir, 'Sidebar.vue')
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Dict) -> Dict[str, str]:
        model_name_pascal = to_pascal_case(model['name'])
        model_name_camel = to_camel_case(model['name'])
        
        current_content = self._read_current_sidebar()
        updated_content = self._update_sidebar_content(current_content, model_name_pascal, model_name_camel)
        
        return {self.output_path: updated_content}

    def _read_current_sidebar(self) -> str:
        try:
            with open(self.output_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return self.get_template('sidebar_stub.vue')

    def _update_sidebar_content(self, current_content: str, model_name_pascal: str, model_name_camel: str) -> str:
        new_item = f"{{ name: '{model_name_pascal}', path: '/{model_name_camel}', icon: 'pi pi-list' }},"
        
        # Find the position to insert the new item (after the MENU_ITEMS placeholder)
        menu_items_position = current_content.find('[[ MENU_ITEMS ]]')
        if menu_items_position != -1:
            # Insert the new item after the MENU_ITEMS placeholder
            updated_content = current_content[:menu_items_position] + '[[ MENU_ITEMS ]]\n      ' + new_item + current_content[menu_items_position:]
            return updated_content
        else:
            # If we can't find the MENU_ITEMS placeholder, just append the new item to the menuItems array
            menu_items_end = current_content.find(']);')
            if menu_items_end != -1:
                return current_content[:menu_items_end] + '      ' + new_item + '\n' + current_content[menu_items_end:]
            else:
                # If we can't find the end of the menuItems array, return the content unchanged
                return current_content


    def get_template(self, template_name: str) -> str:
        template_path = self.config.get(template_name , 'frontend/'+template_name)
        return self.template_reader.read_template(template_path)


    def render_template(self, template: str, context: Dict) -> str:
        try:
            template = Template(template, variable_start_string='[[', variable_end_string=']]')
            return template.render(**context)
        except KeyError as e:
            missing_key = str(e).strip("'")
            available_keys = ", ".join(context.keys())
            error_message = f"Missing key '{missing_key}' in context. Available keys are: {available_keys}"
            logging.error(error_message)
            raise KeyError(error_message)