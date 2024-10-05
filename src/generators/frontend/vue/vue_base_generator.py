from src.generators.base_generator import BaseGenerator
from src.core.entities.project import Project
from src.core.entities.model import Model
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from typing import Dict, Any, List
import os

class VueBaseGenerator(BaseGenerator):
    def __init__(self, project: Project, template_renderer: JinjaTemplateRenderer):
        super().__init__(project, template_renderer)
        self.api_base_url = '/api'  # This should be configurable

    def generate(self) -> Dict[str, str]:
        self.generate_components()
        self.generate_views()
        self.generate_store()
        self.generate_router()
        self.generate_api()
        self.generate_config_files()
        self.add_file('README.md', self.generate_readme())
        self.add_file('.gitignore', self.generate_gitignore())
        self.add_file('LICENSE', self.generate_license())
        return self.get_output()

    def generate_components(self):
        for model in self.project.models:
            self.generate_list_component(model)
            self.generate_form_component(model)
            self.generate_detail_component(model)

    def generate_views(self):
        for model in self.project.models:
            self.generate_list_view(model)
            self.generate_create_view(model)
            self.generate_edit_view(model)
            self.generate_detail_view(model)

    def generate_store(self):
        content = self.generate_store_index()
        self.add_file('src/store/index.js', content)
        for model in self.project.models:
            content = self.generate_store_module(model)
            self.add_file(f'src/store/modules/{self.snake_case(model.name)}.js', content)

    def generate_router(self):
        content = self.generate_router_index()
        self.add_file('src/router/index.js', content)

    def generate_api(self):
        content = self.generate_api_index()
        self.add_file('src/api/index.js', content)
        for model in self.project.models:
            content = self.generate_api_module(model)
            self.add_file(f'src/api/{self.snake_case(model.name)}.js', content)

    def generate_list_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('vue/components/list.vue.j2', context)
        self.add_file(f'src/components/{model.name}List.vue', content)

    def generate_form_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('vue/components/form.vue.j2', context)
        self.add_file(f'src/components/{model.name}Form.vue', content)

    def generate_detail_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('vue/components/detail.vue.j2', context)
        self.add_file(f'src/components/{model.name}Detail.vue', content)

    def generate_list_view(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('vue/views/list.vue.j2', context)
        self.add_file(f'src/views/{model.name}ListView.vue', content)

    def generate_create_view(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('vue/views/create.vue.j2', context)
        self.add_file(f'src/views/{model.name}CreateView.vue', content)

    def generate_edit_view(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('vue/views/edit.vue.j2', context)
        self.add_file(f'src/views/{model.name}EditView.vue', content)

    def generate_detail_view(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('vue/views/detail.vue.j2', context)
        self.add_file(f'src/views/{model.name}DetailView.vue', content)

    def generate_store_index(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('vue/store/index.js.j2', context)

    def generate_store_module(self, model: Model):
        context = {
            'model_name': model.name,
            'api_base_url': self.api_base_url
        }
        return self.render_template('vue/store/module.js.j2', context)

    def generate_router_index(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('vue/router/index.js.j2', context)

    def generate_api_index(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('vue/api/index.js.j2', context)

    def generate_api_module(self, model: Model):
        context = {
            'model_name': model.name,
            'api_base_url': self.api_base_url
        }
        return self.render_template('vue/api/module.js.j2', context)

    def map_attribute_type(self, attr_type: str) -> str:
        type_mapping = {
            'string': 'String',
            'integer': 'Number',
            'float': 'Number',
            'boolean': 'Boolean',
            'date': 'Date',
            'datetime': 'Date',
            'text': 'String',
            'json': 'Object',
        }
        return type_mapping.get(attr_type.lower(), 'String')

    def generate_config_files(self) -> Dict[str, str]:
        config_files = {}
        
        # Generate package.json
        package_json_content = self.render_template('vue/package.json.j2', {'project_name': self.project.name})
        config_files['package.json'] = package_json_content
        
        # Generate vue.config.js
        vue_config_content = self.render_template('vue/vue.config.js.j2', {})
        config_files['vue.config.js'] = vue_config_content
        
        # Generate .env files
        env_content = self.render_template('vue/env.j2', {'api_base_url': self.api_base_url})
        config_files['.env'] = env_content
        config_files['.env.production'] = env_content
        
        return config_files

    def generate_readme(self) -> str:
        context = {
            'project_name': self.project.name,
            'models': self.project.models
        }
        return self.render_template('vue/readme.md.j2', context)

    def generate_main_app(self):
        context = {
            'project_name': self.project.name
        }
        content = self.render_template('vue/App.vue.j2', context)
        self.add_file('src/App.vue', content)

        main_js_content = self.render_template('vue/main.js.j2', context)
        self.add_file('src/main.js', main_js_content)

    def generate_layouts(self):
        content = self.render_template('vue/layouts/default.vue.j2', {})
        self.add_file('src/layouts/Default.vue', content)

    def generate_mixins(self):
        content = self.render_template('vue/mixins/form.js.j2', {})
        self.add_file('src/mixins/form.js', content)

    def generate_utils(self):
        content = self.render_template('vue/utils/api.js.j2', {'api_base_url': self.api_base_url})
        self.add_file('src/utils/api.js', content)

    def generate_tests(self):
        for model in self.project.models:
            self.generate_component_test(model)
            self.generate_view_test(model)
            self.generate_store_test(model)

    def generate_component_test(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('vue/tests/component.spec.js.j2', context)
        self.add_file(f'tests/unit/components/{model.name}List.spec.js', content)

    def generate_view_test(self, model: Model):
        context = {
            'model_name': model.name
        }
        content = self.render_template('vue/tests/view.spec.js.j2', context)
        self.add_file(f'tests/unit/views/{model.name}ListView.spec.js', content)

    def generate_store_test(self, model: Model):
        context = {
            'model_name': model.name
        }
        content = self.render_template('vue/tests/store.spec.js.j2', context)
        self.add_file(f'tests/unit/store/{self.snake_case(model.name)}.spec.js', content)