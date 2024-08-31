import os
from typing import Dict, List
from ...helpers.type_converter import get_type_converter


class ComponentGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.type_converter = get_type_converter()
        self.config = config
        self.models = models
        frontend_config = self.config.get('frontend', {})
        self.template_path = os.path.join(self.config.get('template_dir', 'src/templates/admin'), 'admin/component_stub.vue')
        self.output_dir = os.path.join(
            frontend_config.get('output_dir', 'frontend'),
            frontend_config.get('component_dir', 'components')
        )

    def generate(self, model: Dict):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        generated_files = {}
        form_component = self._generate_form_component(model)
        if form_component is not None:
            generated_files.update(form_component)
        return generated_files

    def _generate_form_component(self, model: Dict):
        model_name = model['name']
        model_name_lowercase = model_name.lower()

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        form_fields = self._generate_form_fields(model['attributes'])
        prime_vue_imports = self._generate_prime_vue_imports(model['attributes'])
        prime_vue_components = self._generate_prime_vue_components(model['attributes'])
        model_state = self._generate_model_state(model['attributes'])

        component_content = template.replace('{{MODEL_NAME}}', model_name)
        component_content = component_content.replace('{{MODEL_NAME_LOWERCASE}}', model_name_lowercase)
        component_content = component_content.replace('{{FORM_FIELDS}}', form_fields)
        component_content = component_content.replace('{{PRIME_VUE_IMPORTS}}', prime_vue_imports)
        component_content = component_content.replace('{{PRIME_VUE_COMPONENTS}}', prime_vue_components)
        component_content = component_content.replace('{{MODEL_STATE}}', model_state)

        output_path = os.path.join(self.output_dir, f'{model_name}Form.vue')
        with open(output_path, 'w') as output_file:
            output_file.write(component_content)

    def _generate_form_fields(self, attributes: List[Dict]) -> str:
        fields = []
        for attr in attributes:
            if attr['name'] == 'id':
                continue
            component = self.type_converter.db_to_primevue(attr['type'])
            v_model = self.type_converter.get_primevue_v_model_type(attr['type'])
            fields.append(f"""
      <div class="field">
        <label for="{attr['name']}">{attr['name'].capitalize()}</label>
        <{component} id="{attr['name']}" {v_model}="{attr['name']}" />
      </div>""")
        return '\n'.join(fields)

    def _generate_prime_vue_imports(self, attributes: List[Dict]) -> str:
        components = self.type_converter.get_primevue_import_list(attributes)
        return '\n'.join([f"import {component} from 'primevue/{component.lower()}'" for component in components])

    def _generate_prime_vue_components(self, attributes: List[Dict]) -> str:
        components = self.type_converter.get_primevue_import_list(attributes)
        return ', '.join(components)

    def _generate_model_state(self, attributes: List[Dict]) -> str:
        state = []
        for attr in attributes:
            if attr['name'] == 'id':
                continue
            default_value = self.type_converter.get_default_value(attr['type'])
            state.append(f"{attr['name']}: props.modelValue?.{attr['name']} ?? {default_value}")
        return ',\n      '.join(state)

def generate_components(config: Dict, models: List[Dict]):
    generator = ComponentGenerator(config, models)
    generator.generate()

if __name__ == "__main__":
    # This is just for testing purposes
    test_config = {
        'template_dir': './templates',
        'frontend': {
            'output_dir': './output',
            'component_dir': 'components'
        }
    }
    test_models = [
        {
            'name': 'User',
            'attributes': [
                {'name': 'id', 'type': 'bigIncrements'},
                {'name': 'name', 'type': 'string'},
                {'name': 'email', 'type': 'string'},
                {'name': 'is_active', 'type': 'boolean'},
                {'name': 'birth_date', 'type': 'date'},
            ]
        }
    ]
    generate_components(test_config, test_models)