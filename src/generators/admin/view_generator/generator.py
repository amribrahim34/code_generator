import os
from typing import Dict, List
from .view import (
    ListViewGenerator,
    FormComponentGenerator,
    CreateViewGenerator,
    ModalComponentGenerator,
    SidebarUpdater,
    RoutesUpdater
)

class ViewGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.config = config
        self.models = models
        self.template_dir = os.path.join(self.config['template_dir'], 'admin')
        self.frontend_dir = self.config['frontend']['output_dir']
        self.src_dir = os.path.join(self.frontend_dir, 'src')
        self.view_dir = os.path.join(self.src_dir, 'views')

        self.generators = [
            ListViewGenerator(self.template_dir, self.view_dir),
            FormComponentGenerator(self.template_dir, self.view_dir),
            CreateViewGenerator(self.template_dir, self.view_dir),
            ModalComponentGenerator(self.template_dir, self.view_dir),
            SidebarUpdater(self.src_dir , self.view_dir),
            RoutesUpdater(self.src_dir , self.view_dir)
        ]

    def generate(self , models) -> Dict[str, str]:
        generated_files = {}

        if not os.path.exists(self.view_dir):
            os.makedirs(self.view_dir)

        for model in self.models:
            for generator in self.generators:
                generated_files.update(generator.generate(model))

        generated_files.update(self._generate_main_ts())
        generated_files.update(self._generate_app_vue())
        generated_files.update(self._generate_vite_env_d_ts())

        return generated_files

    def _generate_main_ts(self) -> Dict[str, str]:
        template_path = os.path.join(self.template_dir, 'main_stub.ts')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'main.ts')
        return {output_path: content}

    def _generate_app_vue(self) -> Dict[str, str]:
        template_path = os.path.join(self.template_dir, 'app_stub.vue')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'App.vue')
        return {output_path: content}

    def _generate_vite_env_d_ts(self) -> Dict[str, str]:
        template_path = os.path.join(self.template_dir, 'vite-env.d.ts')
        with open(template_path, 'r') as template_file:
            content = template_file.read()

        output_path = os.path.join(self.src_dir, 'vite-env.d.ts')
        return {output_path: content}

def generate_views(config: Dict, models: List[Dict]) -> Dict[str, str]:
    generator = ViewGenerator(config, models)
    return generator.generate()