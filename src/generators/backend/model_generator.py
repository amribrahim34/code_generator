import os

class ModelGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates', 'backend','model_stub.php')

    def generate(self, model):
        model_content = self._generate_model(model)
        return {f"app/Models/{model['name']}.php": model_content}

    def _generate_model(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        fillable = self._generate_fillable(model.get('attributes', []))
        relationship_methods = self._generate_relationships(model)

        return template.format(
            class_name=model['name'],
            fillable=fillable,
            relationships=relationship_methods
        )


    def _generate_fillable(self, attributes):
        return ", ".join(f"'{attr['name']}'" for attr in attributes if attr['name'] not in ['id', 'created_at', 'updated_at'])

    def _generate_relationships(self, model):
        methods = []
        for relation in model.get('relationships', []):
            method = self._relationship_method(relation['type'], relation['model'])
            methods.append(method)
        return "\n\n".join(methods)

    def _relationship_method(self, relation_type, related_model):
        method_name = related_model.lower()
        if relation_type in ['hasMany', 'belongsToMany']:
            method_name = f"{method_name}s"
        
        return f"""
    public function {method_name}()
    {{
        return $this->{relation_type}({related_model}::class);
    }}
"""