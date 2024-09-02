import os
from typing import Dict, Any, Union
from src.core.models.schema import Model, Attribute, Relationship

class ResourceGenerator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        template_dir = config.get('template_dir', 'src/templates')
        self.template_path = os.path.join(template_dir, 'backend', 'resource_stub.php')

    def generate(self, model: Union[Dict[str, Any], Model]) -> Dict[str, str]:
        resource_content = self._generate_resource(model)
        model_name = model.name if isinstance(model, Model) else model['name']
        return {f"app/Http/Resources/{model_name}Resource.php": resource_content}

    def _generate_resource(self, model: Union[Dict[str, Any], Model]) -> str:
        with open(self.template_path, 'r') as file:
            template = file.read()

        model_name = model.name if isinstance(model, Model) else model['name']
        class_name = f"{model_name}Resource"
        
        return template.format(
            namespace=self.config.get('resource_namespace', 'App\\Http\\Resources'),
            class_name=class_name,
            attributes=self._generate_attributes(model),
            relationships=self._generate_relationships(model)
        )

    def _generate_attributes(self, model: Union[Dict[str, Any], Model]) -> str:
        attributes = []
        model_attributes = model.attributes if isinstance(model, Model) else model['attributes']
        for attr in model_attributes:
            attr_name = attr.name if isinstance(attr, Attribute) else attr['name']
            attributes.append(f"'{attr_name}' => $this->{attr_name},")
        return '\n            '.join(attributes)

    def _generate_relationships(self, model: Union[Dict[str, Any], Model]) -> str:
        relation_methods = []
        relationships = model.relationships if isinstance(model, Model) else model.get('relationships', [])
        for relation in relationships:
            if isinstance(relation, Relationship):
                method_name = self._get_relation_method_name(relation)
                if relation.type in ['hasMany', 'belongsToMany']:
                    relation_methods.append(f"'{method_name}' => {relation.model}Resource::collection($this->{method_name}),")
                else:
                    relation_methods.append(f"'{method_name}' => new {relation.model}Resource($this->{method_name}),")
            else:
                method_name = self._get_relation_method_name(relation)
                if relation['type'] in ['hasMany', 'belongsToMany']:
                    relation_methods.append(f"'{method_name}' => {relation['model']}Resource::collection($this->{method_name}),")
                else:
                    relation_methods.append(f"'{method_name}' => new {relation['model']}Resource($this->{method_name}),")
        return '\n            '.join(relation_methods)

    def _get_relation_method_name(self, relation: Union[Dict[str, Any], Relationship]) -> str:
        if isinstance(relation, Relationship):
            if relation.type in ['hasMany', 'belongsToMany']:
                return f"{relation.model.lower()}s"
            else:
                return relation.model.lower()
        else:
            if relation['type'] in ['hasMany', 'belongsToMany']:
                return f"{relation['model'].lower()}s"
            else:
                return relation['model'].lower()