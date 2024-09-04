import json
import os
from typing import Any, Dict
from src.core.interfaces.config_loader import IConfigLoader

class JSONConfigLoader(IConfigLoader):
    def __init__(self, config_path: str):
        self._config_path = config_path
        self._config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self) -> None:
        try:
            with open(self._config_path, 'r', encoding='utf-8') as config_file:
                self._config = json.load(config_file)
            print(f"Successfully loaded config from {self._config_path}")
        except FileNotFoundError:
            raise ValueError(f"Config file not found: {self._config_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in config file {self._config_path}: {str(e)}")

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value

    def __getitem__(self, key: str) -> Any:
        value = self.get(key)
        if value is None:
            raise KeyError(f"Configuration key '{key}' not found")
        return value

    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None

    def get_all(self) -> Dict[str, Any]:
        return self._config.copy()

    def reload(self) -> None:
        self.load_config()

    def set(self, key: str, value: Any) -> None:
        keys = key.split('.')
        config = self._config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            elif not isinstance(config[k], dict):
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value

    def save(self) -> None:
        try:
            with open(self._config_path, 'w', encoding='utf-8') as config_file:
                json.dump(self._config, config_file, indent=2)
            print(f"Successfully saved config to {self._config_path}")
        except IOError as e:
            raise ValueError(f"Error saving config to {self._config_path}: {str(e)}")