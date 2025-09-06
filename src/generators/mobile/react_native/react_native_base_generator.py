from src.generators.base_generator import BaseGenerator
from src.core.entities.project import Project
from src.core.entities.model import Model
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from typing import Dict, Any, List
import os

class ReactNativeBaseGenerator(BaseGenerator):
    def __init__(self, project: Project, template_renderer: JinjaTemplateRenderer):
        super().__init__(project, template_renderer)
        self.api_base_url = 'https://api.example.com'  # This should be configurable

    def generate(self) -> Dict[str, str]:
        self.generate_app_entry()
        self.generate_components()
        self.generate_screens()
        self.generate_navigation()
        self.generate_redux_store()
        self.generate_api()
        self.generate_config_files()
        self.generate_styles()
        self.generate_utils()
        self.add_file('README.md', self.generate_readme())
        self.add_file('.gitignore', self.generate_gitignore())
        self.add_file('LICENSE', self.generate_license())
        return self.get_output()

    def generate_app_entry(self):
        context = {
            'project_name': self.project.name
        }
        content = self.render_template('react_native/App.js.j2', context)
        self.add_file('App.js', content)

    def generate_components(self):
        for model in self.project.models:
            self.generate_list_component(model)
            self.generate_form_component(model)
            self.generate_detail_component(model)

    def generate_screens(self):
        for model in self.project.models:
            self.generate_list_screen(model)
            self.generate_create_screen(model)
            self.generate_edit_screen(model)
            self.generate_detail_screen(model)

    def generate_navigation(self):
        content = self.generate_navigation_file()
        self.add_file('src/navigation/AppNavigator.js', content)

    def generate_redux_store(self):
        content = self.generate_store_index()
        self.add_file('src/store/index.js', content)
        for model in self.project.models:
            content = self.generate_store_slice(model)
            self.add_file(f'src/store/slices/{self.snake_case(model.name)}Slice.js', content)

    def generate_api(self):
        content = self.generate_api_index()
        self.add_file('src/api/index.js', content)
        for model in self.project.models:
            content = self.generate_api_module(model)
            self.add_file(f'src/api/{self.snake_case(model.name)}Api.js', content)

    def generate_list_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('react_native/components/List.js.j2', context)
        self.add_file(f'src/components/{model.name}List.js', content)

    def generate_form_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('react_native/components/Form.js.j2', context)
        self.add_file(f'src/components/{model.name}Form.js', content)

    def generate_detail_component(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('react_native/components/Detail.js.j2', context)
        self.add_file(f'src/components/{model.name}Detail.js', content)

    def generate_list_screen(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('react_native/screens/ListScreen.js.j2', context)
        self.add_file(f'src/screens/{model.name}ListScreen.js', content)

    def generate_create_screen(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('react_native/screens/CreateScreen.js.j2', context)
        self.add_file(f'src/screens/{model.name}CreateScreen.js', content)

    def generate_edit_screen(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('react_native/screens/EditScreen.js.j2', context)
        self.add_file(f'src/screens/{model.name}EditScreen.js', content)

    def generate_detail_screen(self, model: Model):
        context = {
            'model_name': model.name,
        }
        content = self.render_template('react_native/screens/DetailScreen.js.j2', context)
        self.add_file(f'src/screens/{model.name}DetailScreen.js', content)

    def generate_navigation_file(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('react_native/navigation/AppNavigator.js.j2', context)

    def generate_store_index(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('react_native/store/index.js.j2', context)

    def generate_store_slice(self, model: Model):
        context = {
            'model_name': model.name,
            'api_base_url': self.api_base_url
        }
        return self.render_template('react_native/store/slice.js.j2', context)

    def generate_api_index(self):
        context = {
            'models': self.project.models
        }
        return self.render_template('react_native/api/index.js.j2', context)

    def generate_api_module(self, model: Model):
        context = {
            'model_name': model.name,
            'api_base_url': self.api_base_url
        }
        return self.render_template('react_native/api/module.js.j2', context)

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
        
        package_json_content = self.render_template('react_native/package.json.j2', {'project_name': self.project.name})
        config_files['package.json'] = package_json_content
        
        app_json_content = self.render_template('react_native/app.json.j2', {'project_name': self.project.name})
        config_files['app.json'] = app_json_content
        
        babel_config_content = self.render_template('react_native/babel.config.js.j2', {})
        config_files['babel.config.js'] = babel_config_content
        
        metro_config_content = self.render_template('react_native/metro.config.js.j2', {})
        config_files['metro.config.js'] = metro_config_content
        
        return config_files

    def generate_readme(self) -> str:
        context = {
            'project_name': self.project.name,
            'models': self.project.models
        }
        return self.render_template('react_native/readme.md.j2', context)

    def generate_styles(self):
        content = self.render_template('react_native/styles/global.js.j2', {})
        self.add_file('src/styles/global.js', content)

    def generate_utils(self):
        content = self.render_template('react_native/utils/api.js.j2', {'api_base_url': self.api_base_url})
        self.add_file('src/utils/api.js', content)

        content = self.render_template('react_native/utils/validation.js.j2', {})
        self.add_file('src/utils/validation.js', content)

    def generate_tests(self):
        for model in self.project.models:
            self.generate_component_test(model)
            self.generate_screen_test(model)
            self.generate_redux_test(model)

    def generate_component_test(self, model: Model):
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model)
        }
        content = self.render_template('react_native/tests/component.test.js.j2', context)
        self.add_file(f'__tests__/components/{model.name}List.test.js', content)

    def generate_screen_test(self, model: Model):
        context = {
            'model_name': model.name
        }
        content = self.render_template('react_native/tests/screen.test.js.j2', context)
        self.add_file(f'__tests__/screens/{model.name}ListScreen.test.js', content)

    def generate_redux_test(self, model: Model):
        context = {
            'model_name': model.name
        }
        content = self.render_template('react_native/tests/redux.test.js.j2', context)
        self.add_file(f'__tests__/store/{self.snake_case(model.name)}Slice.test.js', content)