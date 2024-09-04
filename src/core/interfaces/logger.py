from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class ILogger(ABC):
    @abstractmethod
    def info(self, message: str) -> None:
        """
        Log an info message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        """
        Log a warning message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        """
        Log an error message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def debug(self, message: str, **kwargs: Any) -> None:
        """
        Log a debug message.

        Args:
            message (str): The message to log.
            **kwargs: Additional key-value pairs to include in the log entry.
        """
        pass

    @abstractmethod
    def critical(self, message: str, exc_info: Optional[Exception] = None, **kwargs: Any) -> None:
        """
        Log a critical message.

        Args:
            message (str): The message to log.
            exc_info (Optional[Exception]): Exception information to include in the log.
            **kwargs: Additional key-value pairs to include in the log entry.
        """
        pass

    @abstractmethod
    def set_level(self, level: str) -> None:
        """
        Set the logging level.

        Args:
            level (str): The logging level to set (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        """
        pass

    @abstractmethod
    def get_level(self) -> str:
        """
        Get the current logging level.

        Returns:
            str: The current logging level.
        """
        pass

    @abstractmethod
    def add_handler(self, handler: Any) -> None:
        """
        Add a logging handler.

        Args:
            handler (Any): The handler to add.
        """
        pass

    @abstractmethod
    def remove_handler(self, handler: Any) -> None:
        """
        Remove a logging handler.

        Args:
            handler (Any): The handler to remove.
        """
        pass
