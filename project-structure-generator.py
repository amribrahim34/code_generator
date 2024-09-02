import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content='# Placeholder file'):
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure(base_path):
    structure = {
        'src': {
            'core': {
                'models': ['__init__.py', 'schema.py'],
                'interfaces': ['__init__.py', 'generator.py'],
                'utils': ['__init__.py', 'string_utils.py']
            },
            'infrastructure': ['__init__.py', 'config_loader.py', 'schema_parser.py'],
            'generators': {
                '__init__.py': '',
                'base_generator.py': '',
                'backend': {
                    '__init__.py': '',
                    'model_generator.py': '',
                    'migration_generator.py': '',
                    'controller_generator.py': ''
                },
                'frontend': {
                    '__init__.py': '',
                    'component_generator.py': '',
                    'view_generator.py': '',
                    'store_generator.py': ''
                }
            },
            'templates': {
                'backend': ['model_stub.php', 'migration_stub.php'],
                'frontend': ['component_stub.vue', 'view_stub.vue']
            },
            'main.py': '# Main entry point'
        },
        'tests': {
            'unit': [],
            'integration': []
        },
        'config': ['default_config.json'],
        'input_examples': ['ecommerce_schema.json'],
        'output': {
            'backend': [],
            'frontend': []
        },
        'requirements.txt': '# List your project dependencies here',
        'setup.py': '# Setup script for your project',
        'README.md': '# Laravel Code Generator\n\nAdd your project description here.'
    }

    def create_structure(current_path, structure):
        for key, value in structure.items():
            path = os.path.join(current_path, key)
            if isinstance(value, dict):
                create_directory(path)
                create_structure(path, value)
            elif isinstance(value, list):
                create_directory(path)
                for item in value:
                    create_file(os.path.join(path, item))
            else:
                create_file(path, value)

    create_structure(base_path, structure)

if __name__ == "__main__":
    base_path = input("Enter the base path for your project: ")
    create_project_structure(base_path)
    print(f"Project structure created at {base_path}")