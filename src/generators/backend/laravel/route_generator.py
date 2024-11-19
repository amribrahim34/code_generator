from typing import Dict, Any, List, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Relationship, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_snake_case, pluralize, to_kebab_case, to_pascal_case

class RouteGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}
        route_types = ['CustomerWebsite', 'Admin', 'MobileApp']

        for route_type in route_types:
            content = self._generate_routes(schema, route_type)
            file_path = f"backend/routes/{to_snake_case(route_type)}.php"
            generated_files[file_path] = content

        return generated_files
    
    def _generate_routes(self, schema: Schema, route_type: str) -> str:  
        # Collect routes for all models
        all_routes = []
        for model in schema.models:
            context = self.prepare_context(model, route_type)
            all_routes.extend(context['routes'])
            
        # Create final context for rendering
        final_context = {
            'routes': all_routes,
            'route_type': route_type,
            'route_middleware': self._get_route_group_middleware(route_type),
            'route_prefix': route_type.lower(),
            'api_version': self.config_loader.get('api_versions', {}).get(route_type.lower(), 'v1')
        }

        return self.template_renderer.render('backend/laravel/route.stub', final_context)

    

    def prepare_context(self, model: Union[Dict[str, Any], Model], route_type: str) -> Dict[str, Any]:
        # Extract model name
        model_name = model['name'] if isinstance(model, dict) else model.name
        
        # Determine route prefix and controller namespace
        route_prefix = to_kebab_case(model_name)
        controller_namespace = f"{route_type}\\{model_name}Controller"
        
        # Define standard CRUD routes with access control
        routes = [
            {
                'model': model_name,
                'methods' : [
                    {
                        'action': f'{controller_namespace}@index',
                        'method': 'GET',
                        'uri': f'/{route_prefix}'
                    },
                    {
                        'method': 'POST',
                        'uri': f'/{route_prefix}',
                        'action': f'{controller_namespace}@store'
                    },
                    {
                        'method': 'GET',
                        'uri': f'/{route_prefix}/{{id}}',
                        'action': f'{controller_namespace}@show'
                    },
                    {
                        'method': 'PUT',
                        'uri': f'/{route_prefix}/{{id}}',
                        'action': f'{controller_namespace}@update'
                    },
                    {
                        'method': 'DELETE',
                        'uri': f'/{route_prefix}/{{id}}',
                        'action': f'{controller_namespace}@destroy'
                    }
                ]
            },
        ]
        # Additional context
        context = {
            'routes': routes,
            'route_type': route_type,
            'route_prefix': to_snake_case(route_type),
            'route_middleware': self._get_route_group_middleware(route_type),
            'api_version': self.config_loader.get('api_versions', {}).get(route_type.lower(), 'v1')
        }

        return context
        

    def _get_route_group_middleware(self, route_type: str) -> List[str]:
        """
        Get middleware for the entire route group
        
        :param route_type: Type of routes
        :return: List of middleware
        """
        # Default middleware based on route type
        default_middleware = {
            'CustomerWebsite': ['web'],
            'Admin': ['web', 'auth:admin'],
            'MobileApp': ['api', 'auth:sanctum']
        }

        # Allow override from config
        route_group_middleware = self.config_loader.get('route_group_middleware', {})
        return route_group_middleware.get(route_type.lower(), default_middleware.get(route_type, []))

    def _get_route_middleware(self, route_type: str, action: str) -> List[str]:
        """
        Get middleware for specific route based on route type and action
        
        :param route_type: Type of routes (CustomerWebsite, Admin, MobileApp)
        :param action: CRUD action (index, store, show, update, destroy)
        :return: List of middleware
        """
        middleware_config = self.config_loader.get('route_middleware', {})
        
        # Default middleware based on route type and action
        default_middleware = {
            'CustomerWebsite': {
                'index': ['can:view'],
                'store': ['can:create'],
                'show': ['can:view'],
                'update': ['can:update'],
                'destroy': ['can:delete']
            },
            'Admin': {
                'index': ['can:view-admin'],
                'store': ['can:create-admin'],
                'show': ['can:view-admin'],
                'update': ['can:update-admin'],
                'destroy': ['can:delete-admin']
            },
            'MobileApp': {
                'index': [],
                'store': ['verified'],
                'show': [],
                'update': ['verified'],
                'destroy': ['verified']
            }
        }

        # Specific middleware key
        route_specific_key = f"{route_type.lower()}_{action}_middleware"
        
        # Prioritize config, then default
        return (
            middleware_config.get(route_specific_key, 
            default_middleware.get(route_type, {}).get(action, []))
        )

    def validate_model(self, model: Union[Dict[str, Any], Model]) -> None:
        """
        Validate the model before route generation
        
        :param model: Model to validate
        :raises ValueError: If model is invalid
        """
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")

    def get_output_path(self, route_type: str) -> str:
        """
        Get the output path for route files
        
        :param route_type: Type of routes
        :return: File path for routes
        """
        return f"routes/{to_snake_case(route_type)}.php"

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        """
        Perform any post-generation tasks
        
        :param generated_files: Generated route files
        """
        # Optional post-generation tasks like formatting or validation
        pass
    
    
    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('route_template_path', 'backend/laravel/route.stub')
        return self.template_renderer.load_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)

