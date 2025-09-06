import json
from typing import Dict, Any
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}

    def load_config(self) -> None:
        """Load the configuration from the JSON file."""
        try:
            with self.config_path.open('r') as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file: {self.config_path}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.
        
        Args:
            key (str): The configuration key to retrieve.
            default (Any, optional): The default value to return if the key is not found.

        Returns:
            Any: The configuration value, or the default if not found.
        """
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value

    def validate_config(self) -> None:
        """Validate the loaded configuration."""
        required_keys = ['output_directory', 'backend', 'frontend', 'database', 'naming', 'templates', 'swagger']
        
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")

        backend_keys = ['output_dir', 'namespace', 'use_soft_deletes']
        for key in backend_keys:
            if key not in self.config['backend']:
                raise ValueError(f"Missing required backend configuration key: {key}")

        frontend_keys = ['output_dir', 'use_typescript']
        for key in frontend_keys:
            if key not in self.config['frontend']:
                raise ValueError(f"Missing required frontend configuration key: {key}")

    def get_config(self) -> Dict[str, Any]:
        """Return the loaded configuration."""
        return self.config

    def get_backend_config(self) -> Dict[str, Any]:
        """Return the backend-specific configuration."""
        return self.config['backend']

    def get_frontend_config(self) -> Dict[str, Any]:
        """Return the frontend-specific configuration."""
        return self.config['frontend']

    def get_database_config(self) -> Dict[str, Any]:
        """Return the database configuration."""
        return self.config['database']

    def get_naming_config(self) -> Dict[str, Any]:
        """Return the naming configuration."""
        return self.config['naming']

    def get_templates_config(self) -> Dict[str, Any]:
        """Return the templates configuration."""
        return self.config['templates']

    def get_swagger_config(self) -> Dict[str, Any]:
        """Return the Swagger configuration."""
        return self.config['swagger']

    def update_config(self, new_config: Dict[str, Any]) -> None:
        """Update the configuration with new values."""
        self.config.update(new_config)

    def save_config(self) -> None:
        """Save the current configuration back to the JSON file."""
        with self.config_path.open('w') as config_file:
            json.dump(self.config, config_file, indent=2)
