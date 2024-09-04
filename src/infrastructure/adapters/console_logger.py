import logging
import colorlog
from typing import Any, Optional
from src.core.interfaces.logger import ILogger

class ConsoleLogger(ILogger):
    def __init__(self, name: str = "ConsoleLogger", level: str = "INFO"):
        self.logger = colorlog.getLogger(name)
        self.set_level(level)
        
        # Create console handler and set level
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        # Create color formatter
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            secondary_log_colors={},
            style='%'
        )
        
        # Add formatter to ch
        ch.setFormatter(formatter)
        
        # Add ch to logger
        self.logger.addHandler(ch)

    def debug(self, message: str, **kwargs: Any) -> None:
        self.logger.debug(message, extra=kwargs)

    def info(self, message: str, **kwargs: Any) -> None:
        self.logger.info(message, extra=kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        self.logger.warning(message, extra=kwargs)

    def error(self, message: str, exc_info: Optional[Exception] = None, **kwargs: Any) -> None:
        self.logger.error(message, exc_info=exc_info, extra=kwargs)

    def critical(self, message: str, exc_info: Optional[Exception] = None, **kwargs: Any) -> None:
        self.logger.critical(message, exc_info=exc_info, extra=kwargs)

    def set_level(self, level: str) -> None:
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        self.logger.setLevel(level_map.get(level.upper(), logging.INFO))

    def get_level(self) -> str:
        return logging.getLevelName(self.logger.level)

    def add_handler(self, handler: logging.Handler) -> None:
        self.logger.addHandler(handler)

    def remove_handler(self, handler: logging.Handler) -> None:
        self.logger.removeHandler(handler)