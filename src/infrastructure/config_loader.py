import json
import yaml
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        """Load the configuration file."""
        try:
            with open(self.config_path, 'r') as config_file:
                config = json.load(config_file)
            print(f"Successfully loaded config from {self.config_path}")
            return config
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON in config file: {self.config_path}")
            return {}

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.
        
        Args:
            key (str): The configuration key to retrieve.
            default (Any, optional): The default value to return if the key is not found.

        Returns:
            Any: The configuration value, or the default if not found.
        """
        return self.config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """
        Allow dictionary-style access to configuration values.
        
        Args:
            key (str): The configuration key to retrieve.

        Returns:
            Any: The configuration value.

        Raises:
            KeyError: If the key is not found in the configuration.
        """
        return self.config[key]

    def __contains__(self, key: str) -> bool:
        """
        Check if a key exists in the configuration.
        
        Args:
            key (str): The configuration key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in self.config

