import os
import shutil
from typing import List, Dict, Any
import json

def create_directory(path: str) -> None:
    """
    Create a directory if it doesn't exist.
    
    :param path: Path of the directory to create
    """
    os.makedirs(path, exist_ok=True)

def write_file(path: str, content: str) -> None:
    """
    Write content to a file, creating directories if they don't exist.
    
    :param path: Path of the file to write
    :param content: Content to write to the file
    """
    directory = os.path.dirname(path)
    create_directory(directory)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def read_file(path: str) -> str:
    """
    Read content from a file.
    
    :param path: Path of the file to read
    :return: Content of the file as a string
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def list_files(directory: str, extension: str = None) -> List[str]:
    """
    List all files in a directory, optionally filtering by extension.
    
    :param directory: Directory to list files from
    :param extension: Optional file extension to filter by
    :return: List of file paths
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if extension is None or filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

def copy_file(src: str, dst: str) -> None:
    """
    Copy a file from source to destination, creating directories if they don't exist.
    
    :param src: Source file path
    :param dst: Destination file path
    """
    directory = os.path.dirname(dst)
    create_directory(directory)
    shutil.copy2(src, dst)

def delete_file(path: str) -> None:
    """
    Delete a file if it exists.
    
    :param path: Path of the file to delete
    """
    if os.path.exists(path):
        os.remove(path)

def rename_file(old_path: str, new_path: str) -> None:
    """
    Rename a file, creating directories if they don't exist.
    
    :param old_path: Current path of the file
    :param new_path: New path for the file
    """
    directory = os.path.dirname(new_path)
    create_directory(directory)
    os.rename(old_path, new_path)

def get_file_size(path: str) -> int:
    """
    Get the size of a file in bytes.
    
    :param path: Path of the file
    :return: Size of the file in bytes
    """
    return os.path.getsize(path)

def is_file_empty(path: str) -> bool:
    """
    Check if a file is empty.
    
    :param path: Path of the file
    :return: True if the file is empty, False otherwise
    """
    return os.path.getsize(path) == 0

def read_json_file(path: str) -> Dict[str, Any]:
    """
    Read a JSON file and return its content as a dictionary.
    
    :param path: Path of the JSON file
    :return: Dictionary representation of the JSON content
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(path: str, data: Dict[str, Any], indent: int = 2) -> None:
    """
    Write a dictionary to a JSON file.
    
    :param path: Path of the JSON file to write
    :param data: Dictionary to write to the JSON file
    :param indent: Number of spaces for indentation (default is 2)
    """
    directory = os.path.dirname(path)
    create_directory(directory)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=indent)

def get_file_extension(path: str) -> str:
    """
    Get the extension of a file.
    
    :param path: Path of the file
    :return: Extension of the file (without the dot)
    """
    return os.path.splitext(path)[1][1:]

def change_file_extension(path: str, new_extension: str) -> str:
    """
    Change the extension of a file path.
    
    :param path: Current path of the file
    :param new_extension: New extension for the file (without the dot)
    :return: New file path with the changed extension
    """
    root, _ = os.path.splitext(path)
    return f"{root}.{new_extension}"

# Example usage
if __name__ == "__main__":
    # Create a test directory
    test_dir = "test_directory"
    create_directory(test_dir)

    # Write a test file
    test_file = os.path.join(test_dir, "test_file.txt")
    write_file(test_file, "Hello, World!")

    # Read the test file
    content = read_file(test_file)
    print(f"File content: {content}")

    # List files in the test directory
    files = list_files(test_dir)
    print(f"Files in directory: {files}")

    # Get file size
    size = get_file_size(test_file)
    print(f"File size: {size} bytes")

    # Clean up
    delete_file(test_file)
    os.rmdir(test_dir)