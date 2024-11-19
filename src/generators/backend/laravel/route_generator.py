from typing import Dict, Any, List, Union
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Model, Attribute, Relationship, Schema
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import to_snake_case, pluralize, to_kebab_case, to_pascal_case
import os

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

        self._modify_route_service_provider(route_types)
        return generated_files
    
    def _modify_route_service_provider(self, route_types) -> Dict[str, str]:
        # Prepare the route file registration lines
        route_registration_lines = []
        for route_type in route_types:
            route_group_middleware = self._get_route_group_middleware(route_type)
            route_file_path = f"routes/{to_snake_case(route_type)}.php"
            
            # Filter out empty middlewares and join
            valid_middlewares = [mw for mw in route_group_middleware if mw and mw.strip()]
            
            # If no valid middlewares, use web as default
            if not valid_middlewares:
                valid_middlewares = ['web']
            
            # Join multiple middlewares if necessary
            middleware_string = "'" + "', '".join(route_group_middleware) + "'"
            
            route_registration_lines.append(
                f"            Route::middleware([{middleware_string}])\n"
                f"                ->group(base_path('{route_file_path}'));"
            )
        
        # Path to the PHP file
        php_file_path = "output/backend/app/Providers/RouteServiceProvider.php"

        # Modify the PHP file
        self._modify_php_file(php_file_path, '\n'.join(route_registration_lines))
        
        return {}  # Return an empty dict as per the type hint

        
    def _modify_php_file(self ,file_path, text_to_add):
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return
        
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()
            content = file.read()
            
        import re
        
        # Pattern to find the routes block within the boot method
        pattern = r'(\$this->routes\(function \(\) \{).*?(\};)'

        # Replace the routes block, preserving the standard routes
        updated_content = re.sub(
            pattern, 
            r'\1\n' + text_to_add + r'\n\n            Route::middleware(\'api\')\n'
                r'                ->prefix(\'api\')\n'
                r'                ->group(base_path(\'routes/api.php\'));\n\n'
                r'            Route::middleware(\'web\')\n'
                r'                ->group(base_path(\'routes/web.php\'));\n\2', 
            content, 
            flags=re.DOTALL
        )
    
        # Locate the specific function and block to modify
        inside_boot_function = False
        inside_routes_block = False
        updated_lines = []
        
        for line in lines:
            stripped_line = line.strip()
            
            # Check for the start of the boot function
            if stripped_line == 'public function boot(): void':
                inside_boot_function = True
            
            # Check for the routes block
            if inside_boot_function and stripped_line.startswith('$this->routes(function () {'):
                inside_routes_block = True
                updated_lines.append(line)
            
                # Split the text_to_add into lines and add each with proper indentation
                for add_line in text_to_add.split('\n'):
                    if add_line.strip():  # Only add non-empty lines
                        updated_lines.append(f"            {add_line}\n")
                
                continue
            
            # Check for the end of the routes block
            if inside_routes_block and stripped_line == '});':
                inside_routes_block = False
            
            # Check for the end of the boot function
            if inside_boot_function and stripped_line == '}':
                inside_boot_function = False
            
            updated_lines.append(line)
        
        # Write back the updated content to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print(f"Successfully updated the file: {file_path}")
    
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
        if isinstance(model, dict):
            if not model.get('name'):
                raise ValueError("Model must have a name")
        else:
            if not model.name:
                raise ValueError("Model must have a name")

    def get_output_path(self, route_type: str) -> str:
        return f"routes/{to_snake_case(route_type)}.php"

    def post_generation_tasks(self, generated_files: Dict[str, str]) -> None:
        # Optional post-generation tasks like formatting or validation
        pass
    
    
    def get_template(self, template_name: str) -> str:
        template_path = self.config_loader.get('route_template_path', 'backend/laravel/route.stub')
        return self.template_renderer.load_template(template_path)

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        return self.template_renderer.render(template, context)
