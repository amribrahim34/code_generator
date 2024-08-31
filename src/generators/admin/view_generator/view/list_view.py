import os
from typing import Dict, List
from .base import FileGenerator

class ListViewGenerator(FileGenerator):
    def __init__(self, template_dir: str, frontend_dir: str):
        self.template_path = os.path.join(template_dir, 'list_view_stub.vue')
        self.frontend_dir = frontend_dir

    def generate(self, model: Dict) -> Dict[str, str]:
        model_name = model['name']
        model_name_plural = self._pluralize(model_name)
        model_name_lowercase = model_name.lower()
        model_name_plural_lowercase = model_name_plural.lower()

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        view_content = template.replace('{{MODEL_NAME}}', model_name)
        view_content = view_content.replace('{{MODEL_NAME_PLURAL}}', model_name_plural)
        view_content = view_content.replace('{{MODEL_NAME_LOWERCASE}}', model_name_lowercase)
        view_content = view_content.replace('{{MODEL_NAME_PLURAL_LOWERCASE}}', model_name_plural_lowercase)
        view_content = view_content.replace('{{TABLE_COLUMNS}}', self._generate_table_columns(model['attributes']))
        view_content = view_content.replace('{{GLOBAL_FILTER_FIELDS}}', ', '.join([f"'{attr['name']}'" for attr in model['attributes']]))
        
        if len(model['attributes']) <= 3:
            view_content = view_content.replace('{{DIALOG_COMPONENT}}', f'<{model_name}Dialog v-model:visible="{{MODEL_NAME_LOWERCASE}}Dialog" :item="item" @save="saveItem" />')
            view_content = view_content.replace('{{DIALOG_IMPORT}}', f"import {model_name}Dialog from './{model_name}Dialog.vue'")
            view_content = view_content.replace('{{DIALOG_COMPONENT_IMPORT}}', f"{model_name}Dialog")
        else:
            view_content = view_content.replace('{{DIALOG_COMPONENT}}', '')
            view_content = view_content.replace('{{DIALOG_IMPORT}}', '')
            view_content = view_content.replace('{{DIALOG_COMPONENT_IMPORT}}', '')

        output_path = os.path.join(self.frontend_dir, f'{model_name}List.vue')
        return {output_path: view_content}

        

    def _generate_table_columns(self, attributes: List[Dict]) -> str:
        columns = []
        for attr in attributes:
            columns.append(f"""
        <Column field="{attr['name']}" header="{attr['name'].capitalize()}">
          <template #body="{{{{ data }}}}">
            {{{{ data.{attr['name']} }}}}
          </template>
        </Column>
            """)
        return '\n'.join(columns)

    def _pluralize(self, singular: str) -> str:
        if singular.endswith('y'):
            return singular[:-1] + 'ies'
        elif singular.endswith('s'):
            return singular + 'es'
        else:
            return singular + 's'
