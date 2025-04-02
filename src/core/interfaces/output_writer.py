from abc import ABC, abstractmethod
from typing import Dict, IO

class IOutputWriter(ABC):
    @abstractmethod
    def write_file(self, path: str, content: str) -> None:
        """
        Write content to a file at the specified path.

        Args:
            path (str): The path where the file should be written.
            content (str): The content to write to the file.

        Raises:
            IOError: If there's an error writing to the file.
        """
        pass

    @abstractmethod
    def write_multiple_files(self, files: Dict[str, str]) -> None:
        """
        Write multiple files at once.

        Args:
            files (Dict[str, str]): A dictionary where keys are file paths and values are file contents.

        Raises:
            IOError: If there's an error writing any of the files.
        """
        pass

    @abstractmethod
    def create_directory(self, path: str) -> None:
        """
        Create a directory at the specified path.

        Args:
            path (str): The path where the directory should be created.

        Raises:
            OSError: If there's an error creating the directory.
        """
        pass

    @abstractmethod
    def file_exists(self, path: str) -> bool:
        """
        Check if a file exists at the specified path.

        Args:
            path (str): The path to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        pass

    @abstractmethod
    def get_file_content(self, path: str) -> str:
        """
        Read and return the content of a file.

        Args:
            path (str): The path of the file to read.

        Returns:
            str: The content of the file.

        Raises:
            IOError: If there's an error reading the file.
        """
        pass

    @abstractmethod
    def append_to_file(self, path: str, content: str) -> None:
        """
        Append content to an existing file.

        Args:
            path (str): The path of the file to append to.
            content (str): The content to append.

        Raises:
            IOError: If there's an error appending to the file.
        """
        pass

    @abstractmethod
    def delete_file(self, path: str) -> None:
        """
        Delete a file at the specified path.

        Args:
            path (str): The path of the file to delete.

        Raises:
            OSError: If there's an error deleting the file.
        """
        pass

