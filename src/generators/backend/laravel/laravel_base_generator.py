from src.generators.base_generator import BaseGenerator
from src.core.entities.project import Project
from src.core.entities.model import Model
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from typing import Dict, Any, List
import os

class LaravelBaseGenerator(BaseGenerator):
    def __init__(self, project: Project, template_renderer: JinjaTemplateRenderer):
        super().__init__(project, template_renderer)
        self.namespace = f"App\\{self.project.name}"

    def generate(self) -> Dict[str, str]:
        self.generate_models()
        self.generate_migrations()
        self.generate_controllers()
        self.generate_routes()
        self.generate_views()
        self.generate_config_files()
        self.add_file('README.md', self.generate_readme())
        self.add_file('.gitignore', self.generate_gitignore())
        self.add_file('LICENSE', self.generate_license())
        return self.get_output()

    def generate_models(self):
        for model in self.project.models:
            content = self.generate_model(model)
            self.add_file(f"app/Models/{model.name}.php", content)

    def generate_migrations(self):
        for model in self.project.models:
            content = self.generate_migration(model)
            timestamp = self.get_timestamp()
            self.add_file(f"database/migrations/{timestamp}_create_{self.snake_case(self.plural(model.name))}_table.php", content)

    def generate_controllers(self):
        for model in self.project.models:
            content = self.generate_controller(model)
            self.add_file(f"app/Http/Controllers/{model.name}Controller.php", content)

    def generate_routes(self):
        content = self.generate_route_file()
        self.add_file("routes/web.php", content)

    def generate_views(self):
        for model in self.project.models:
            view_contents = self.generate_views_for_model(model)
            for view_name, content in view_contents.items():
                self.add_file(f"resources/views/{self.snake_case(self.plural(model.name))}/{view_name}.blade.php", content)

    def generate_model(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'table_name': self.snake_case(self.plural(model.name)),
            'fillable': [attr.name for attr in model.attributes if not attr.is_primary_key],
            'relationships': self.get_model_relationships(model),
            'namespace': self.namespace
        }
        return self.render_template('laravel/model.php.j2', context)

    def generate_migration(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'table_name': self.snake_case(self.plural(model.name)),
            'attributes': self.get_model_attributes(model),
            'relationships': self.get_model_relationships(model)
        }
        return self.render_template('laravel/migration.php.j2', context)

    def generate_controller(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'variable_name': self.camel_case(model.name),
            'namespace': self.namespace
        }
        return self.render_template('laravel/controller.php.j2', context)

    def generate_route_file(self) -> str:
        context = {
            'models': self.project.models,
            'namespace': self.namespace
        }
        return self.render_template('laravel/routes.php.j2', context)

    def generate_views_for_model(self, model: Model) -> Dict[str, str]:
        views = {}
        view_types = ['index', 'show', 'create', 'edit']
        
        for view_type in view_types:
            context = {
                'model_name': model.name,
                'attributes': self.get_model_attributes(model)
            }
            content = self.render_template(f'laravel/views/{view_type}.blade.php.j2', context)
            views[view_type] = content
        
        return views

    def map_attribute_type(self, attr_type: str) -> str:
        type_mapping = {
            'string': 'string',
            'integer': 'integer',
            'float': 'float',
            'boolean': 'boolean',
            'date': 'date',
            'datetime': 'dateTime',
            'text': 'text',
            'json': 'json',
        }
        return type_mapping.get(attr_type.lower(), 'string')

    def generate_config_files(self) -> Dict[str, str]:
        config_files = {}
        
        # Generate .env file
        env_content = self.render_template('laravel/env.j2', {'project_name': self.project.name})
        config_files['.env'] = env_content
        
        # Generate config/database.php
        db_config_content = self.render_template('laravel/database_config.php.j2', {})
        config_files['config/database.php'] = db_config_content
        
        # Generate config/app.php
        app_config_content = self.render_template('laravel/app_config.php.j2', {'project_name': self.project.name})
        config_files['config/app.php'] = app_config_content
        
        return config_files

    def generate_readme(self) -> str:
        context = {
            'project_name': self.project.name,
            'models': self.project.models
        }
        return self.render_template('laravel/readme.md.j2', context)

    def get_timestamp(self) -> str:
        # Generate a timestamp for migration files
        # In a real implementation, you might want to use the actual current timestamp
        return "2023_01_01_000000"

    def generate_factory(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'attributes': self.get_model_attributes(model),
            'namespace': self.namespace
        }
        return self.render_template('laravel/factory.php.j2', context)

    def generate_seeder(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'namespace': self.namespace
        }
        return self.render_template('laravel/seeder.php.j2', context)

    def generate_test(self, model: Model) -> str:
        context = {
            'model_name': model.name,
            'namespace': self.namespace
        }
        return self.render_template('laravel/test.php.j2', context)