import os
from typing import Dict, List

class RouteGenerator:
    def __init__(self, config: Dict, models: List[Dict]):
        self.config = config
        self.models = models
        frontend_config = self.config.get('frontend', {})
        self.output_dir = os.path.join(
            frontend_config.get('output_dir', 'frontend'),
            'src',
            frontend_config.get('route_dir', 'routes')
        )
        self.template_path = os.path.join(self.config.get('template_dir', 'templates'), 'admin/route_stub.ts')

    def generate(self, model: Dict):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        generated_files = {}
        generated_files.update(self._generate_model_route(model))
        generated_files.update(self._generate_index_file())
        return generated_files

    def _generate_model_route(self, model: Dict):
        model_name = model['name']
        model_name_plural = self._pluralize(model_name)
        model_name_lowercase = model_name.lower()
        model_name_plural_lowercase = model_name_plural.lower()

        with open(self.template_path, 'r') as template_file:
            template = template_file.read()

        route_content = template.replace('{{MODEL_NAME}}', model_name)
        route_content = route_content.replace('{{MODEL_NAME_PLURAL}}', model_name_plural)
        route_content = route_content.replace('{{MODEL_NAME_LOWERCASE}}', model_name_lowercase)
        route_content = route_content.replace('{{MODEL_NAME_PLURAL_LOWERCASE}}', model_name_plural_lowercase)

        output_path = f'{model_name_lowercase}Routes.ts'
        with open(os.path.join(self.output_dir, output_path), 'w') as output_file:
            output_file.write(route_content)
        return {output_path: route_content}

    def _generate_index_file(self):
        index_content = [
            "import { RouteRecordRaw } from 'vue-router'",
            ""
        ]

        for model in self.models:
            model_name = model['name']
            model_name_lowercase = model_name.lower()
            import_statement = f"import {model_name_lowercase}Routes from './{model_name_lowercase}Routes'"
            index_content.append(import_statement)

        index_content.extend([
            "",
            "const routes: RouteRecordRaw[] = [",
            "  {",
            "    path: '/',",
            "    name: 'Home',",
            "    component: () => import('@/views/Home.vue'),",
            "    meta: { requiresAuth: true }",
            "  }",
            "]",
            "",
            "// Combine all model routes",
            "const modelRoutes = ["
        ])

        for model in self.models:
            model_name_lowercase = model['name'].lower()
            index_content.append(f"  ...{model_name_lowercase}Routes,")

        index_content.extend([
            "]",
            "",
            "routes.push(...modelRoutes)",
            "",
            "export default routes"
        ])

        index_content = "\n".join(index_content)

        output_path = 'index.ts'
        with open(os.path.join(self.output_dir, output_path), 'w') as output_file:
            output_file.write(index_content)
        return {output_path: index_content}

    def _pluralize(self, singular: str) -> str:
        # This is a very simple pluralization method. For a real-world application,
        # you might want to use a more robust pluralization library.
        if singular.endswith('y'):
            return singular[:-1] + 'ies'
        elif singular.endswith('s'):
            return singular + 'es'
        else:
            return singular + 's'

def generate_routes(config: Dict, models: List[Dict]):
    generator = RouteGenerator(config, models)
    generator.generate()
