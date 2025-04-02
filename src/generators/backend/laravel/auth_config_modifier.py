import os
import re
from typing import Dict, Any, List
from src.core.interfaces.config_loader import IConfigLoader
from src.core.interfaces.template_renderer import ITemplateRenderer

class AuthConfigModifier:
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer

    def generate_auth_config(self, auth_types: List[str]) -> Dict[str, Any]:
        """
        Generate authentication configuration for specified auth types.
        
        Args:
            auth_types (List[str]): List of authentication types to generate (e.g., ['admin', 'customer'])
        
        Returns:
            Dict[str, Any]: Dictionary containing guards and providers configurations
        """
        guards = self._generate_guards(auth_types)
        providers = self._generate_providers(auth_types)
        
        return {
            'guards': guards,
            'providers': providers
        }

    def _generate_guards(self, auth_types: List[str]) -> Dict[str, Dict[str, str]]:
        """
        Generate guards configuration for authentication types.
        
        Args:
            auth_types (List[str]): List of authentication types
        
        Returns:
            Dict[str, Dict[str, str]]: Guards configuration dictionary
        """
        # Base web guard
        guards = {
            'web': {
                'driver': 'session',
                'provider': 'users'
            }
        }
        
        # Add additional guards
        for auth_type in auth_types:
            if auth_type.lower() != 'web':
                guards[auth_type.lower()] = {
                    'driver': 'sanctum',
                    'provider': f'{auth_type.lower()}s'
                }
        
        return guards

    def _generate_providers(self, auth_types: List[str]) -> Dict[str, Dict[str, str]]:
        """
        Generate providers configuration for authentication types.
        
        Args:
            auth_types (List[str]): List of authentication types
        
        Returns:
            Dict[str, Dict[str, str]]: Providers configuration dictionary
        """
        # Base users provider
        providers = {
            'users': {
                'driver': 'eloquent',
                'model': 'App\\Models\\User'
            }
        }
        
        # Add additional providers
        for auth_type in auth_types:
            if auth_type.lower() != 'users':
                providers[f'{auth_type.lower()}s'] = {
                    'driver': 'eloquent',
                    'model': f'App\\Models\\{auth_type}'
                }
        
        return providers

    def update_auth_config(self, auth_types: List[str]) -> None:
        """
        Update the Laravel auth.php configuration file.
        
        Args:
            auth_types (List[str]): List of authentication types to add
        """
        # Path to the Laravel auth configuration file
        config_path = 'output/backend/config/auth.php'
        
        # Generate new configuration
        new_config = self.generate_auth_config(auth_types)
        
        # Read existing config file
        with open(config_path, 'r') as file:
            config_content = file.read()
        
        # Update guards section
        config_content = self._update_config_section(
            config_content, 
            'guards', 
            self._format_config_section(new_config['guards'])
        )
        
        # Update providers section
        config_content = self._update_config_section(
            config_content, 
            'providers', 
            self._format_config_section(new_config['providers'])
        )
        
        # Write updated configuration
        with open(config_path, 'w') as file:
            file.write(config_content)

    def _update_config_section(self, config_content: str, section: str, new_section_content: str) -> str:
        """
        Update a specific section in the config file.
        
        Args:
            config_content (str): Full config file content
            section (str): Section to update (e.g., 'guards', 'providers')
            new_section_content (str): New content for the section
        
        Returns:
            str: Updated config file content
        """
        # Improved regex pattern to match the entire section
        section_pattern = rf"'{section}'\s*=>\s*\[(.*?)\],"


        # Replace the section content
        updated_content = re.sub(
            section_pattern, 
            f"'{section}' => [\n{new_section_content}\n    ],", 
            config_content, 
            flags=re.DOTALL
        )
        
        return updated_content

    def _format_config_section(self, config_dict: Dict[str, Any]) -> str:
        """
        Format configuration dictionary as a PHP array string.
        
        Args:
            config_dict (Dict[str, Any]): Configuration dictionary
        
        Returns:
            str: Formatted PHP array string
        """
        formatted_lines = []
        for key, value in config_dict.items():
            line = f"        '{key}' => [\n"
            for k, v in value.items():
                line += f"            '{k}' => '{v}',\n"
            line += "        ],"
            formatted_lines.append(line)
        
        return "\n".join(formatted_lines)