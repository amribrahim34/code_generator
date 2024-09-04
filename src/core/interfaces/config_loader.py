from abc import ABC, abstractmethod
from typing import Any, Dict

class IConfigLoader(ABC):
    @abstractmethod
    def load(self, config_path: str) -> Dict[str, Any]:
        """
        Load the configuration from a given file path.

        Args:
            config_path (str): The path to the configuration file.

        Returns:
            Dict[str, Any]: The loaded configuration as a dictionary.
        """
        pass

    @abstractmethod
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key.
        
        Args:
            key (str): The configuration key to retrieve.
            default (Any, optional): The default value to return if the key is not found.

        Returns:
            Any: The configuration value, or the default if not found.
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def __contains__(self, key: str) -> bool:
        """
        Check if a key exists in the configuration.
        
        Args:
            key (str): The configuration key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        pass

    @abstractmethod
    def get_all(self) -> Dict[str, Any]:
        """
        Get the entire configuration as a dictionary.

        Returns:
            Dict[str, Any]: The complete configuration dictionary.
        """
        pass

    @abstractmethod
    def reload(self) -> None:
        """
        Reload the configuration from the source.
        This method should be used when the configuration needs to be refreshed.
        """
        pass
