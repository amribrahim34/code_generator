import os
from typing import Dict, List

class ViewGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.config = config
        self.models = models
        self.template_dir = os.path.join(self.config['template_dir'], 'admin')
        self.frontend_dir = self.config['frontend']['output_dir']
        self.src_dir = os.path.join(self.frontend_dir, 'src')
        self.view_dir = os.path.join(self.src_dir, self.config['frontend']['view_dir'])

    def generate(self, model):
        generated_files = {}

        if not os.path.exists(self.src_dir):
            os.makedirs(self.src_dir)

        generated_files.update(self._generate_list_view(model))
        generated_files.update(self._generate_form_component(model))
        if len(model['attributes']) > 3:
            generated_files.update(self._generate_create_view(model))
        generated_files.update(self._generate_modal_component(model))

        generated_files.update(self._generate_main_ts())
        generated_files.update(self._generate_app_vue())
        generated_files.update(self._generate_vite_env_d_ts())
        generated_files.update(self._update_sidebar())
        generated_files.update(self._update_routes())

        return generated_files

    def _generate_main_ts(self):
        template_path = os.path.join(self.template_dir, 'main_stub.ts')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'main.ts')
        return {output_path: content}

    def _generate_app_vue(self):
        template_path = os.path.join(self.template_dir, 'app_stub.vue')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'App.vue')
        return {output_path: content}

    def _generate_vite_env_d_ts(self):
        template_path = os.path.join(self.template_dir, 'vite-env.d.ts')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'vite-env.d.ts')
        return {output_path: content}

    def _generate_list_view(self, model: Dict):
        model_name = model['name']
        model_name_plural = self._pluralize(model_name)
        model_name_lowercase = model_name.lower()
        model_name_plural_lowercase = model_name_plural.lower()
        self.template_path = os.path.join(self.template_dir, 'list_view_stub.vue')

        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"List view template not found at {self.template_path}")

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

    def _generate_form_component(self, model: Dict):
        # Implementation for generating form component
        return {}  # Return an empty dict for now

    def _generate_create_view(self, model: Dict):
        # Implementation for generating create view
        return {}  # Return an empty dict for now

    def _generate_modal_component(self, model: Dict):
        # Implementation for generating modal component
        return {}  # Return an empty dict for now

    def _update_sidebar(self):
        # Implementation for updating sidebar
        return {}  # Return an empty dict for now

    def _update_routes(self):
        # Implementation for updating routes
        return {}  # Return an empty dict for now

    def _generate_detail_view(self, model: Dict):
        model_name = model['name']
        model_name_lowercase = model_name.lower()

        self.template_path = os.path.join(self.template_dir, 'detail_view_stub.vue')
        
        with open(self.template_path, 'r') as template_file:
            template = template_file.read()
        
        # For now, return an empty dict
        return {}

    def _pluralize(self, singular: str) -> str:
        # This is a very simple pluralization method. For a real-world application,
        # you might want to use a more robust pluralization library.
        if singular.endswith('y'):
            return singular[:-1] + 'ies'
        elif singular.endswith('s'):
            return singular + 'es'
        else:
            return singular + 's'

def generate_views(config: Dict, models: List[Dict]):
    generator = ViewGenerator(config, models)
    return generator.generate(models)