from abc import ABC, abstractmethod
from typing import Dict, List, Any
from src.core.entities.project import Project
from src.core.entities.model import Model
from src.core.entities.attribute import Attribute
from src.core.entities.relationship import Relationship
from src.infrastructure.adapters.jinja_template_renderer import JinjaTemplateRenderer
from src.utilities.string_utils import camel_case, snake_case, plural
from datetime import datetime

class BaseGenerator(ABC):
    def __init__(self, project: Project, template_renderer: JinjaTemplateRenderer):
        self.project = project
        self.template_renderer = template_renderer
        self.output = {}

    @abstractmethod
    def generate(self) -> Dict[str, str]:
        """
        Main method to generate all necessary code files.
        Should be implemented by subclasses.
        Returns a dictionary where keys are file paths and values are file contents.
        """
        pass

    def render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Renders a template with the given context.
        """
        return self.template_renderer.render(template_name, context)


    def get_model_attributes(self, model: Model) -> List[Dict[str, Any]]:
        """
        Returns a list of attribute dictionaries for a given model.
        """
        return [
            {
                'name': attr.name,
                'type': self.map_attribute_type(attr.type),
                'nullable': attr.nullable,
                'unique': attr.unique,
                'default': attr.default
            }
            for attr in model.attributes
        ]

    def get_model_relationships(self, model: Model) -> List[Dict[str, Any]]:
        """
        Returns a list of relationship dictionaries for a given model.
        """
        return [
            {
                'name': rel.name,
                'type': rel.type,
                'related_model': rel.related_model,
                'foreign_key': rel.foreign_key,
                'back_populates': rel.back_populates
            }
            for rel in model.relationships
        ]

    @abstractmethod
    def map_attribute_type(self, attr_type: str) -> str:
        """
        Maps the generic attribute type to the specific language/framework type.
        Should be implemented by subclasses.
        """
        pass

    def camel_case(self, s: str) -> str:
        """
        Converts a string to camelCase.
        """
        return camel_case(s)

    def snake_case(self, s: str) -> str:
        """
        Converts a string to snake_case.
        """
        return snake_case(s)

    def plural(self, s: str) -> str:
        """
        Returns the plural form of a word.
        """
        return plural(s)

    def add_file(self, path: str, content: str):
        """
        Adds a generated file to the output dictionary.
        """
        self.output[path] = content

    def get_output(self) -> Dict[str, str]:
        """
        Returns the generated output.
        """
        return self.output

    @abstractmethod
    def generate_config_files(self) -> Dict[str, str]:
        """
        Generates configuration files for the project.
        Should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def generate_readme(self) -> str:
        """
        Generates a README file for the project.
        Should be implemented by subclasses.
        """
        pass

    def generate_gitignore(self) -> str:
        """
        Generates a .gitignore file for the project.
        """
        gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# IDE settings
.vscode/
.idea/
"""
        return gitignore_content.strip()

    def generate_license(self, license_type: str = "MIT") -> str:
        """
        Generates a license file for the project.
        """
        if license_type.upper() == "MIT":
            current_year = datetime.now().year
            license_content = f"""
MIT License

Copyright (c) {current_year} {self.project.name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
            return license_content.strip()
        else:
            raise ValueError(f"Unsupported license type: {license_type}")