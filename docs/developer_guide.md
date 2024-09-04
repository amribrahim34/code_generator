# Developer Guide for Code Generation System

## Table of Contents

1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Project Structure](#project-structure)
5. [Core Components](#core-components)
6. [Extending the System](#extending-the-system)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing Guidelines](#contributing-guidelines)
10. [Troubleshooting](#troubleshooting)

## Introduction

Welcome to the Code Generation System developer guide. This system is designed to automate the process of generating both backend (Laravel) and frontend (Vue.js) code based on a provided schema. This guide will help you understand the system's architecture, set up your development environment, and contribute to the project effectively.

## System Architecture

The Code Generation System follows a clean architecture pattern, divided into several layers:

1. **Core Layer**: Contains entities, use cases, and interfaces.
2. **Application Layer**: Contains services that coordinate use cases.
3. **Infrastructure Layer**: Contains implementations of interfaces defined in the core layer.
4. **Presentation Layer**: Contains the CLI and potential API for interacting with the system.

The system uses dependency injection to maintain loose coupling between components.

## Setting Up the Development Environment

1. Clone the repository:

   ```
   git clone https://github.com/your-repo/code-generation-system.git
   cd code-generation-system
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up pre-commit hooks:

   ```
   pre-commit install
   ```

5. Copy the example configuration file:
   ```
   cp config.example.json config.json
   ```
   Edit `config.json` to match your local setup.

## Project Structure

```
code-generation-system/
├── core/
│   ├── entities/
│   ├── use_cases/
│   └── interfaces/
├── application/
│   └── services/
├── infrastructure/
│   ├── adapters/
│   └── external_services/
├── presentation/
│   ├── cli/
│   └── api/
├── generators/
│   ├── backend/
│   └── frontend/
├── templates/
├── tests/
├── config.json
├── main.py
└── requirements.txt
```

## Core Components

### Schema Parser (core/use_cases/parse_input_schema.py)

Responsible for parsing and validating the input JSON schema.

### Backend Code Generator (core/use_cases/generate_backend_code.py)

Orchestrates the generation of Laravel backend code.

### Frontend Code Generator (core/use_cases/generate_frontend_code.py)

Orchestrates the generation of Vue.js frontend code.

### API Documentation Generator (core/use_cases/generate_api_documentation.py)

Generates OpenAPI/Swagger documentation for the API.

## Extending the System

### Adding a New Generator

1. Create a new file in `generators/backend/` or `generators/frontend/`.
2. Implement the `ICodeGenerator` interface.
3. Add the new generator to the configuration in `config.json`.

### Modifying Templates

Templates are located in the `templates/` directory. Modify these to change the generated code structure.

### Adding a New Service

1. Create a new file in `application/services/`.
2. Implement the service using existing use cases and interfaces.
3. Inject the new service where needed.

## Testing

We use pytest for testing. Run the tests with:

```
pytest
```

When adding new features, please add corresponding tests in the `tests/` directory.

## Deployment

1. Ensure all tests pass: `pytest`
2. Update the version number in `setup.py`
3. Build the distribution: `python setup.py sdist bdist_wheel`
4. Upload to PyPI: `twine upload dist/*`

## Contributing Guidelines

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Troubleshooting

### Common Issues

1. **Schema parsing errors**: Ensure your input schema follows the correct format. Refer to the schema documentation.

2. **Template rendering errors**: Check that all required variables are provided in the context when rendering templates.

3. **Dependency conflicts**: Make sure your virtual environment is using the correct versions of dependencies as specified in `requirements.txt`.

### Debugging

1. Set the log level to DEBUG in `config.json` for more detailed logging:

   ```json
   {
     "logging": {
       "level": "DEBUG"
     }
   }
   ```

2. Use the Python debugger (pdb) to step through code:

   ```python
   import pdb; pdb.set_trace()
   ```

3. Check the generated files in the output directory for any inconsistencies.

If you encounter any issues not covered here, please open an issue on the GitHub repository with a detailed description and steps to reproduce the problem.

---

Thank you for contributing to the Code Generation System! If you have any questions or need further clarification, please don't hesitate to reach out to the core development team.
