import os

class ResourceGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates','backend', 'resource_stub.php')

    def generate(self, model):
        resource_content = self._generate_resource(model)
        return {f"app/Http/Resources/{model['name']}Resource.php": resource_content}

    def _generate_resource(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        class_name = f"{model['name']}Resource"
        
        return template.format(
            class_name=class_name,
            attributes=self._generate_attributes(model),
            relationships=self._generate_relationships(model)
        )

    def _generate_attributes(self, model):
        attributes = []
        for attr in model['attributes']:
            attributes.append(f"'{attr['name']}' => $this->{attr['name']},")
        return '\n            '.join(attributes)

    def _generate_relationships(self, model):
        relation_methods = []
        for relation in model.get('relationships', []):
            method_name = self._get_relation_method_name(relation)
            if relation['type'] in ['hasMany', 'belongsToMany']:
                relation_methods.append(f"'{method_name}' => {relation['model']}Resource::collection($this->{method_name}),")
            else:
                relation_methods.append(f"'{method_name}' => new {relation['model']}Resource($this->{method_name}),")
        return '\n            '.join(relation_methods)

    def _get_relation_method_name(self, relation):
        if relation['type'] in ['hasMany', 'belongsToMany']:
            return f"{relation['model'].lower()}s"
        else:
            return relation['model'].lower()