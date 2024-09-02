from typing import Dict, Any, Union
from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case
from src.infrastructure.template_reader import TemplateReader
from src.core.models.schema import Model, Attribute, Relationship

class RepositoryGenerator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        repository_content = self._generate_repository(model)
        model_name = model.name if isinstance(model, Model) else model['name']
        return {f"app/Repositories/{model_name}Repository.php": repository_content}

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('repository_template_path', 'backend/repository_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return template.format(**context)

    def _generate_repository(self, model: Union[Dict[str, Any], Model]) -> str:
        template = self.get_template('repository')
        model_name = model.name if isinstance(model, Model) else model['name']
        
        context = {
            'class_name': f"{model_name}Repository",
            'interface_name': f"{model_name}RepositoryInterface",
            'model_name': model_name,
            'namespace': self.config.get('repository_namespace', 'App\\Repositories'),
            'model_namespace': self.config.get('model_namespace', 'App\\Models'),
            'interface_namespace': self.config.get('repository_interface_namespace', 'App\\Repositories\\Interfaces'),
            'custom_methods': self._generate_custom_methods(model)
        }
        
        return self.render_template(template, context)

    def _generate_custom_methods(self, model: Union[Dict[str, Any], Model]) -> str:
        custom_methods = []
        
        if self.config.get('include_search_method', False):
            custom_methods.append(self._generate_search_method(model))
        
        if self.config.get('include_relation_methods', False):
            custom_methods.extend(self._generate_relation_methods(model))
        
        return "\n\n".join(custom_methods)

    def _generate_search_method(self, model: Union[Dict[str, Any], Model]) -> str:
        if isinstance(model, Model):
            searchable_fields = ", ".join([f"'{attr.name}'" for attr in model.attributes if getattr(attr, 'searchable', False)])
        else:
            searchable_fields = ", ".join([f"'{attr['name']}'" for attr in model.get('attributes', []) if attr.get('searchable', False)])
        
        return f"""
    public function search($search)
    {{
        return $this->model
            ->where(function ($query) use ($search) {{
                $query->where({searchable_fields}, 'like', "%{{$search}}%");
            }})
            ->paginate();
    }}
"""

    def _generate_relation_methods(self, model: Union[Dict[str, Any], Model]) -> list:
        methods = []
        relationships = model.relationships if isinstance(model, Model) else model.get('relationships', [])
        for relation in relationships:
            if isinstance(relation, Relationship):
                method_name = f"getWith{to_pascal_case(relation.model)}"
                methods.append(f"""
    public function {method_name}($id)
    {{
        return $this->model->with('{relation.model.lower()}')->findOrFail($id);
    }}
""")
            else:
                method_name = f"getWith{to_pascal_case(relation['model'])}"
                methods.append(f"""
    public function {method_name}($id)
    {{
        return $this->model->with('{relation['model'].lower()}')->findOrFail($id);
    }}
""")
        return methods