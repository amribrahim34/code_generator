import os
from typing import Dict
from src.core.interfaces.generator import Generator
from src.infrastructure.config_loader import ConfigLoader
from src.core.utils.string_utils import to_pascal_case, pluralize

class RoutesUpdater(Generator):
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.routes_dir = os.path.join(self.config['frontend']['output_dir'], 'src', self.config['frontend']['route_dir'])
        self.routes_path = os.path.join(self.routes_dir, 'index.ts')

    def generate(self, model: Dict) -> Dict[str, str]:
        model_name = to_pascal_case(model['name'])
        model_name_plural = pluralize(model_name)
        
        if not os.path.exists(self.routes_dir):
            os.makedirs(self.routes_dir)

        if not os.path.exists(self.routes_path):
            initial_content = self._create_initial_routes_content()
        else:
            with open(self.routes_path, 'r') as routes_file:
                initial_content = routes_file.read()

        new_route = f"""
  {{
    path: '/{model_name_plural.lower()}',
    name: '{model_name_plural}',
    component: () => import('@/views/{model_name}List.vue')
  }},
  {{
    path: '/{model_name_plural.lower()}/create',
    name: 'Create{model_name}',
    component: () => import('@/views/{model_name}Create.vue')
  }},"""

        updated_routes = initial_content.replace(']', f'{new_route}\n]')

        return {self.routes_path: updated_routes}

    def _create_initial_routes_content(self) -> str:
        return """import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
  },
];

export default routes;
"""

    def get_template(self, template_name: str) -> str:
        # Not used for this generator
        pass

    def render_template(self, template: str, context: Dict) -> str:
        # Not used for this generator
        pass