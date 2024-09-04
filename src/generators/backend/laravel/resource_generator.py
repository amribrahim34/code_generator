from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute ,Schema ,Relationship
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class ResourceGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
    
    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        resource_types = ['Admin', 'CustomerWebsite', 'MobileApp']

        for resource_type in resource_types:
            for model in schema.models:
                resource_content = self._generate_resource(model, resource_type)
                model_name = model['name'] if isinstance(model, dict) else model.name
                file_path = f"backend/app/Http/Resources/{resource_type}/{model_name}Resource.php"
                generated_files[file_path] = resource_content
        return generated_files

   
    def get_output_path(self, model_name: str , resource_type) -> str:
        return f"backend/app/Http/Resources/{resource_type}/{model_name}Resource.php"

    def render_template(self, context: Dict[str, Any]) -> str:
        return self.template_renderer.render('backend/laravel/resource.stub', context)
        
    def _generate_resource(self, model: Union[Dict[str, Any], Model], resource_type: str) -> str:
        context = self.prepare_context(model, resource_type)
        template = self.get_template('resource')
        return self.template_renderer.render('backend/laravel/resource.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], resource_type: str) -> Dict[str, Any]:
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes
        relationships = model['relationships'] if isinstance(model, dict) else model.relationships

        context =  {
            'model_name': model_name,
            'resource_name': f"{model_name}Resource",
            'namespace': f"App\\Http\\Resources\\{resource_type}",
            'resource_type': resource_type,
            'attributes': self._prepare_attributes(model),
            'relationships': self._prepare_relationships(model),
        }
        return context
    
    def _prepare_attributes(self, model: Union[Dict[str, Any], Model]) -> str:
        attributes = []
        model_attributes = model.attributes if isinstance(model, Model) else model['attributes']
        for attr in model_attributes:
            attr_name = attr.name if isinstance(attr, Attribute) else attr['name']
            attributes.append(f"'{attr_name}' => $this->{attr_name},")
        return '\n            '.join(attributes)

    
    def _prepare_relationships(self, model: Union[Dict[str, Any], Model]) -> str:
        relation_methods = []
        relationships = model.relationships if isinstance(model, Model) else model.get('relationships', [])
        for relation in relationships:
            if isinstance(relation, Relationship):
                method_name = self._get_relation_method_name(relation)
                if relation.type in ['hasMany', 'belongsToMany']:
                    relation_methods.append(f"'{method_name}' => {relation.related_model}Resource::collection($this->{method_name}),")
                else:
                    relation_methods.append(f"'{method_name}' => new {relation.related_model}Resource($this->{method_name}),")
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
                return f"{relation.related_model.lower()}s"
            else:
                return relation.related_model.lower()
        else:
            if relation['type'] in ['hasMany', 'belongsToMany']:
                return f"{relation['related_model'].lower()}s"
            else:
                return relation['related_model'].lower()

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('resource_template_path', 'backend/laravel/resource.stub')
        return self.template_renderer.load_template( 'backend/laravel/resource.stub')

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Perform any post-generation tasks here, such as formatting or linting
        pass

# Example usage (this would be part of the BackendGenerationService)
# config_loader = ConfigLoader()
# template_renderer = TemplateRenderer()
# resource_generator = ResourceGenerator(config_loader, template_renderer)
# generated_files = resource_generator.generate(model)