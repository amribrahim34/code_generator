import os
import logging
from typing import Dict, List
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case, to_kebab_case
from src.infrastructure.template_reader import TemplateReader
from src.infrastructure.config_loader import ConfigLoader
from src.core.converters.type_converter import TypeConverter

class ComponentGenerator(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.template_reader = TemplateReader(config.get('template_dir', 'src/templates'))
        self.type_converter = TypeConverter()
        frontend_config = self.config.get('frontend', {})
        self.template_path = 'frontend/component_stub.vue'
        self.output_dir = os.path.join(
            frontend_config.get('output_dir', 'frontend'),
            frontend_config.get('component_dir', 'components')
        )
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Dict) -> Dict[str, str]:
        self.logger.debug(f"Generate method called with schema type: {type(schema)}")
        generated_files = {}

        for model in schema.get('models', []):
            self.logger.debug(f"Processing model: {model['name']}")
            form_component = self._generate_form_component(model)
            if form_component:
                generated_files.update(form_component)

        return generated_files

    def _generate_form_component(self, model: Dict) -> Dict[str, str]:
        model_name = model['name']
        self.logger.debug(f"Generating form component for model: {model_name}")

        model_name_pascal = to_pascal_case(model_name)
        model_name_camel = to_camel_case(model_name)
        model_name_kebab = to_kebab_case(model_name)

        template = self.get_template(self.template_path)

        attributes = model.get('attributes', [])
        self.logger.debug(f"Model attributes: {attributes}")

        context = {
            'MODEL_NAME_PASCAL': model_name_pascal,
            'MODEL_NAME_CAMEL': model_name_camel,
            'MODEL_NAME_KEBAB': model_name_kebab,
            'FORM_FIELDS': self._generate_form_fields(attributes),
            'PRIME_VUE_IMPORTS': self._generate_prime_vue_imports(attributes),
            'PRIME_VUE_COMPONENTS': self._generate_prime_vue_components(attributes),
            'MODEL_STATE': self._generate_model_state(attributes)
        }

        component_content = self.render_template(template, context)

        output_path = os.path.join(self.output_dir, f'{model_name_pascal}Form.vue')
        return {output_path: component_content}

    def _generate_form_fields(self, attributes: List[Dict]) -> str:
        self.logger.debug(f"Generating form fields for attributes: {attributes}")
        fields = []
        for attr in attributes:
            if attr['name'] == 'id':
                continue
            component = self.type_converter.db_to_primevue(attr['type'])
            v_model = self.type_converter.get_primevue_v_model_type(attr['type'])
            fields.append(f"""
      <div class="field">
        <label for="{attr['name']}">{attr['name'].capitalize()}</label>
        <{component} id="{attr['name']}" {v_model}="form.{attr['name']}" />
      </div>""")
        return '\n'.join(fields)

    def _generate_prime_vue_imports(self, attributes: List[Dict]) -> str:
        components = self.type_converter.get_primevue_import_list(attributes)
        return '\n'.join([f"import {{ {component} }} from 'primevue/{component.toLowerCase()}'" for component in components])

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

    def get_template(self, template_name: str) -> str:
        return self.template_reader.read_template(template_name)

    def render_template(self, template: str, context: Dict) -> str:
        for key, value in context.items():
            template = template.replace(f'{{{{${key}}}}}', str(value))
        return template