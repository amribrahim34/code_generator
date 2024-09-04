import os
from typing import Dict, Union, List, IO
from src.core.interfaces.output_writer import IOutputWriter

class FileSystemOutputWriter(IOutputWriter):
    def __init__(self, base_path: str = ""):
        self.base_path = base_path

    def write_file(self, path: str, content: str) -> None:
        full_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        try:
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error writing to file {full_path}: {str(e)}")

    def write_multiple_files(self, files: Dict[str, str]) -> None:
        for path, content in files.items():
            self.write_file(path, content)
            
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def create_directory(self, path: str) -> None:
        full_path = os.path.join(self.base_path, path)
        try:
            os.makedirs(full_path, exist_ok=True)
        except OSError as e:
            raise OSError(f"Error creating directory {full_path}: {str(e)}")

    def file_exists(self, path: str) -> bool:
        full_path = os.path.join(self.base_path, path)
        return os.path.exists(full_path)

    def get_file_content(self, path: str) -> str:
        full_path = os.path.join(self.base_path, path)
        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            raise IOError(f"Error reading file {full_path}: {str(e)}")

    def append_to_file(self, path: str, content: str) -> None:
        full_path = os.path.join(self.base_path, path)
        try:
            with open(full_path, 'a', encoding='utf-8') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Error appending to file {full_path}: {str(e)}")

    def delete_file(self, path: str) -> None:
        full_path = os.path.join(self.base_path, path)
        try:
            os.remove(full_path)
        except OSError as e:
            raise OSError(f"Error deleting file {full_path}: {str(e)}")

    def get_file_handler(self, path: str, mode: str) -> IO:
        full_path = os.path.join(self.base_path, path)
        try:
            return open(full_path, mode, encoding='utf-8')
        except IOError as e:
            raise IOError(f"Error opening file {full_path} in mode {mode}: {str(e)}")