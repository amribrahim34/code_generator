import os
from typing import Dict, Any
from src.core.interfaces.output_writer import IOutputWriter
from src.core.interfaces.logger import ILogger

class OutputManager:
    def __init__(self, output_writer: IOutputWriter, logger: ILogger, base_path: str):
        self.output_writer = output_writer
        self.logger = logger
        self.base_path = base_path
        self.file_count = 0
        self.directory_count = 0

    def write_file(self, relative_path: str, content: str, overwrite: bool = False) -> bool:
        """Write content to a file at the specified relative path."""
        full_path = os.path.join(self.base_path, relative_path)
        directory = os.path.dirname(full_path)

        if not self.output_writer.directory_exists(directory):
            self.create_directory(directory)

        if self.output_writer.file_exists(full_path) and not overwrite:
            self.logger.warning(f"File already exists and overwrite is set to False: {full_path}")
            return False

        try:
            self.output_writer.write_file(full_path, content)
            self.file_count += 1
            self.logger.info(f"File written successfully: {full_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error writing file {full_path}: {str(e)}")
            return False

    def create_directory(self, relative_path: str) -> bool:
        """Create a directory at the specified relative path."""
        full_path = os.path.join(self.base_path, relative_path)
        
        if self.output_writer.directory_exists(full_path):
            self.logger.info(f"Directory already exists: {full_path}")
            return True

        try:
            self.output_writer.create_directory(full_path)
            self.directory_count += 1
            self.logger.info(f"Directory created successfully: {full_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error creating directory {full_path}: {str(e)}")
            return False

    def get_statistics(self) -> Dict[str, Any]:
        """Return statistics about the output operations."""
        return {
            "files_written": self.file_count,
            "directories_created": self.directory_count
        }

    def clear_output_directory(self) -> bool:
        """Clear the entire output directory. Use with caution!"""
        try:
            self.output_writer.remove_directory(self.base_path)
            self.output_writer.create_directory(self.base_path)
            self.logger.info(f"Output directory cleared and recreated: {self.base_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error clearing output directory {self.base_path}: {str(e)}")
            return False

    def list_generated_files(self) -> List[str]:
        """Return a list of all generated files."""
        generated_files = []
        for root, _, files in self.output_writer.walk(self.base_path):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, self.base_path)
                generated_files.append(relative_path)
        return generated_files

    def get_file_content(self, relative_path: str) -> str:
        """Return the content of a generated file."""
        full_path = os.path.join(self.base_path, relative_path)
        if not self.output_writer.file_exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")
        return self.output_writer.read_file(full_path)

    def copy_file(self, source_path: str, destination_path: str, overwrite: bool = False) -> bool:
        """Copy a file from source_path to destination_path."""
        full_source = os.path.join(self.base_path, source_path)
        full_destination = os.path.join(self.base_path, destination_path)

        if not self.output_writer.file_exists(full_source):
            self.logger.error(f"Source file does not exist: {full_source}")
            return False

        if self.output_writer.file_exists(full_destination) and not overwrite:
            self.logger.warning(f"Destination file already exists and overwrite is set to False: {full_destination}")
            return False

        try:
            self.output_writer.copy_file(full_source, full_destination)
            self.logger.info(f"File copied successfully from {full_source} to {full_destination}")
            return True
        except Exception as e:
            self.logger.error(f"Error copying file from {full_source} to {full_destination}: {str(e)}")
            return False

    def move_file(self, source_path: str, destination_path: str, overwrite: bool = False) -> bool:
        """Move a file from source_path to destination_path."""
        if self.copy_file(source_path, destination_path, overwrite):
            return self.delete_file(source_path)
        return False

    def delete_file(self, relative_path: str) -> bool:
        """Delete a file at the specified relative path."""
        full_path = os.path.join(self.base_path, relative_path)
        if not self.output_writer.file_exists(full_path):
            self.logger.warning(f"File does not exist: {full_path}")
            return False

        try:
            self.output_writer.delete_file(full_path)
            self.logger.info(f"File deleted successfully: {full_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error deleting file {full_path}: {str(e)}")
            return False