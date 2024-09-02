from typing import Dict, Any, Union
from src.core.interfaces.generator import Generator
from src.infrastructure.template_reader import TemplateReader
from src.core.utils.string_utils import to_pascal_case
from src.core.models.schema import Model, Attribute

class RequestGenerator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_reader = TemplateReader(template_dir)

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        store_request = self._generate_request(model, 'Store')
        update_request = self._generate_request(model, 'Update')
        model_name = model.name if isinstance(model, Model) else model['name']
        return {
            f"app/Http/Requests/{model_name}StoreRequest.php": store_request,
            f"app/Http/Requests/{model_name}UpdateRequest.php": update_request
        }

    def get_template(self, template_name: str) -> str:
        template_path = self.config.get('request_template_path', 'backend/request_stub.php')
        return self.template_reader.read_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return template.format(**context)

    def _generate_request(self, model: Union[Dict[str, Any], Model], action: str) -> str:
        template = self.get_template('request')
        model_name = model.name if isinstance(model, Model) else model['name']
        
        context = {
            'class_name': f"{model_name}{action}Request",
            'namespace': self.config.get('request_namespace', 'App\\Http\\Requests'),
            'rules': self._generate_rules(model, action),
            'messages': self._generate_messages(model)
        }
        
        return self.render_template(template, context)

    def _generate_rules(self, model: Union[Dict[str, Any], Model], action: str) -> str:
        rules = []
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        for attr in attributes:
            name = attr.name if isinstance(attr, Attribute) else attr['name']
            attr_type = attr.type if isinstance(attr, Attribute) else attr['type']
            if name.lower() == 'id':
                continue  # Skip 'id' as it's typically not part of the request
            rule = f"'{name}' => '"
            rule += 'required|' if action == 'Store' else 'sometimes|'
            rule += self._get_validation_rule(attr_type)
            rule += "'"
            rules.append(rule)
        return ',\n            '.join(rules)

    def _get_validation_rule(self, type: str) -> str:
        type_rules = {
            'string': 'string|max:255',
            'integer': 'integer',
            'boolean': 'boolean',
            'text': 'string',
            'date': 'date',
            'datetime': 'date',
            'float': 'numeric',
            'decimal': 'numeric',
            'bigIncrements': 'integer',
            'unsignedBigInteger': 'integer',
            'timestamp': 'date',
        }
        return type_rules.get(type.lower(), 'string')

    def _generate_messages(self, model: Union[Dict[str, Any], Model]) -> str:
        messages = []
        attributes = model.attributes if isinstance(model, Model) else model['attributes']
        for attr in attributes:
            name = attr.name if isinstance(attr, Attribute) else attr['name']
            attr_type = attr.type if isinstance(attr, Attribute) else attr['type']
            if name.lower() == 'id':
                continue
            messages.append(f"'{name}.required' => 'The {name} field is required.'")
            messages.append(f"'{name}.{self._get_validation_rule(attr_type).split('|')[0]}' => 'The {name} must be a valid {attr_type}.'")
        return ',\n            '.join(messages)