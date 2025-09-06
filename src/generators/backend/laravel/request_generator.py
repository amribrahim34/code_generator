from typing import Dict, Any, Union, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_pascal_case, to_snake_case, pluralize

class RequestGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        request_types = ['Admin', 'CustomerWebsite', 'MobileApp']
        operations = ['Store', 'Update']

        for request_type in request_types:
            for model in schema.models:
                for operation in operations:
                    request_content = self._generate_request(model, request_type, operation)
                    model_name = model.name if isinstance(model, Model) else model['name']
                    file_path = f"backend/app/Http/Requests/{request_type}/{model_name}/{operation}{model_name}Request.php"
                    generated_files[file_path] = request_content

        return generated_files

    def _generate_request(self, model: Union[Dict[str, Any], Model], request_type: str, operation: str) -> str:
        context = self.prepare_context(model, request_type, operation)
        
        openapi_schema = self._generate_openapi_schema(model , request_type , operation)
        context['openapi_schema'] = openapi_schema
        
        return self.template_renderer.render('backend/laravel/request.stub', context)

    def prepare_context(self, model: Union[Dict[str, Any], Model], request_type: str, operation: str) -> Dict[str, Any]:
        model_name = model.name if isinstance(model, Model) else model['name']
        
        context = {
            'model_name': model_name,
            'request_name': f"{operation}{model_name}Request",
            'namespace': f"App\\Http\\Requests\\{request_type}\\{model_name}",
            'request_type': request_type,
            'operation': operation,
            'rules': self._generate_rules(model, operation),
        }
        return context

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

    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('request_template_path', 'backend/laravel/request.stub')
        return self.template_renderer.load_template(template_path)

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        if isinstance(model, dict):
            if not model.get('name') or not model.get('attributes'):
                raise ValueError("Model must have a name and attributes")
        else:
            if not model.name or not model.attributes:
                raise ValueError("Model must have a name and attributes")


    def get_output_path(self, model_name: str ) -> str:
        return f"backend/app/Http/Requests/{model_name}.php"
    
    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)
    
    
    def _generate_openapi_schema(self, model: Union[Dict[str, Any], Model], request_type: str , operation :str) -> str:
        """
        Generates OpenAPI schema annotations for request validation.
        
        Args:
            model: The model to generate schema for
            request_type: Type of request (Admin, CustomerWebsite, MobileApp)
        """
        model_name = model['name'] if isinstance(model, dict) else model.name
        attributes = model['attributes'] if isinstance(model, dict) else model.attributes

        schema_properties = []
        for attr in attributes:
            attr_name = attr['name'] if isinstance(attr, dict) else attr.name
            attr_type = attr['type'] if isinstance(attr, dict) else attr.type
            
            if attr_name.lower() == 'id':
                continue
                
            schema_properties.append(
                f'    *     @OA\Property(property="{attr_name}", type="{self._map_type_to_openapi(attr_type)}")'
            )

        schema_properties_str = ',\n'.join(schema_properties)

        return f'''
        /**
        * @OA\Schema(
        *     schema="{operation}{request_type}{model_name}Request",
        *     title="{operation} {request_type} {model_name} Request",
        *     description="Request schema for {model_name} operations",
        {schema_properties_str}
        * )
        */'''

    def _map_type_to_openapi(self, attr_type: str) -> str:
        """
        Maps model attribute types to OpenAPI types.
        """
        type_mapping = {
            'string': 'string',
            'integer': 'integer',
            'float': 'number',
            'boolean': 'boolean',
            'date': 'string',
            'datetime': 'string',
            'text': 'string',
            'decimal': 'number',
            'bigIncrements': 'integer',
            'unsignedBigInteger': 'integer',
            'timestamp': 'string'
        }
        return type_mapping.get(attr_type.lower(), 'string')