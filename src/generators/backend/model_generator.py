from src.core.interfaces.generator import Generator
from src.core.utils.string_utils import to_pascal_case, to_camel_case, pluralize
from src.infrastructure.template_reader import TemplateReader
from src.core.models.schema import Attribute, Relationship
import logging
import os

class ModelGenerator(Generator):
    def __init__(self, config: dict):
        self.config = config or {}  # Use an empty dict if config is None
        template_dir = self.config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)
        self.logger = logging.getLogger(__name__)

    def generate(self, model: dict) -> dict:
        self.logger.info(f"Generating model for: {model.get('name', 'UnknownModel')}")
        model_content = self._generate_model(model)
        model_name = model.get('name', 'UnknownModel')
        return {f"app/Models/{model_name}.php": model_content}

    def get_template(self, template_name: str) -> str:
        self.logger.info(f"Reading template: {template_name}")
        return self.template_reader.read_template(template_name)

    def render_template(self, template: str, context: dict) -> str:
        return template.format(**context)

    def _generate_model(self, model: dict) -> str:
        self.logger.info("Generating model content")
        template = self.get_template('backend/model_stub.php')
        
        context = {
            'class_name': model.get('name', 'UnknownModel'),
            'fillable': self._generate_fillable(model.get('attributes', [])),
            'relationships': self._generate_relationships(model.get('relationships', [])),
            'use_soft_deletes': self._use_soft_deletes(model),
            'table_name': self._generate_table_name(model),
            'casts': self._generate_casts(model.get('attributes', []))
        }
        
        return self.render_template(template, context)

    def _generate_fillable(self, attributes: list) -> str:
        return ", ".join(f"'{attr.name}'" for attr in attributes if isinstance(attr, Attribute) and attr.name not in ['id', 'created_at', 'updated_at', 'deleted_at'])

    def _generate_relationships(self, relationships: list) -> str:
        methods = []
        for relation in relationships:
            if isinstance(relation, Relationship):
                method = self._relationship_method(relation.type, relation.model)
                methods.append(method)
        return "\n\n".join(methods)

    def _relationship_method(self, relation_type: str, related_model: str) -> str:
        method_name = to_camel_case(related_model)
        if relation_type in ['hasMany', 'belongsToMany']:
            method_name = pluralize(method_name)
        
        return f"""
    public function {method_name}()
    {{
        return $this->{relation_type}({to_pascal_case(related_model)}::class);
    }}
"""

    def _use_soft_deletes(self, model: dict) -> str:
        return "use SoftDeletes;" if model.get('soft_deletes', False) else ""

    def _generate_table_name(self, model: dict) -> str:
        return f"protected $table = '{model['table_name']}';" if 'table_name' in model else ""

    def _generate_casts(self, attributes: list) -> str:
        casts = []
        for attr in attributes:
            if isinstance(attr, Attribute):
                if attr.type in ['date', 'datetime', 'timestamp']:
                    casts.append(f"'{attr.name}' => 'datetime'")
                elif attr.type == 'boolean':
                    casts.append(f"'{attr.name}' => 'boolean'")
                elif attr.type in ['decimal', 'float']:
                    casts.append(f"'{attr.name}' => 'float'")
        
        return "protected $casts = [" + ", ".join(casts) + "];" if casts else ""