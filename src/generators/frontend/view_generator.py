import os
from typing import Dict
from src.core.interfaces.generator import Generator
from src.infrastructure.config_loader import ConfigLoader
from .list_view_generator import ListViewGenerator
from .form_component_generator import FormComponentGenerator
from .create_view_generator import CreateViewGenerator
from .modal_component_generator import ModalComponentGenerator
from .sidebar_updater import SidebarUpdater
from .routes_updater import RoutesUpdater
from src.infrastructure.template_reader import TemplateReader
import logging

class ViewGenerator(Generator):
    def __init__(self, config: ConfigLoader , models):
        self.config = config
        self.models = models
        frontend_config = self.config.get('frontend', {})
        self.template_dir = os.path.join(self.config.get('template_dir', 'src/templates'), 'frontend')
        self.frontend_dir = frontend_config.get('output_dir', 'frontend')
        self.src_dir = os.path.join(self.frontend_dir, 'src')
        self.view_dir = os.path.join(self.src_dir, 'views')

        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

        self.generators = [
            ListViewGenerator(config),
            FormComponentGenerator(config),
            CreateViewGenerator(config),
            ModalComponentGenerator(config),
            SidebarUpdater(config),
            RoutesUpdater(config)
        ]

    def generate(self, schema: Dict) -> Dict[str, str]:
        generated_files = {}

        if not os.path.exists(self.view_dir):
            os.makedirs(self.view_dir)

        models = schema.get('models', [])
        for model in self.models:
            # logging.info('this is the model', model)
            for generator in self.generators:
                generated_files.update(generator.generate(model))

        generated_files.update(self._generate_main_ts())
        generated_files.update(self._generate_app_vue())
        generated_files.update(self._generate_vite_env_d_ts())

        return generated_files

    def _generate_main_ts(self) -> Dict[str, str]:
        template = self.get_template('main_stub.ts')
        output_path = os.path.join(self.src_dir, 'main.ts')
        return {output_path: template}
    
    def _generate_list_view_ts(self) -> Dict[str, str]:
        template = self.get_template('list_view_stub.vue')
        output_path = os.path.join(self.src_dir, 'components','ListView.vue')
        return {output_path: template}

    def _generate_app_vue(self) -> Dict[str, str]:
        template = self.get_template('app_stub.vue')
        output_path = os.path.join(self.src_dir, 'App.vue')
        return {output_path: template}

    def _generate_vite_env_d_ts(self) -> Dict[str, str]:
        template = self.get_template('vite-env.d.ts')
        output_path = os.path.join(self.src_dir, 'vite-env.d.ts')
        return {output_path: template}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get(template_name , 'frontend/'+template_name)
        return self.template_reader.read_template(template_path)
        

    def render_template(self, template: str, context: Dict) -> str:
        return self.config.template_reader.render_template(template, context)