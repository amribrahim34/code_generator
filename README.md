# Laravel Code Generator

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Configuration](#configuration)
8. [Customization](#customization)
9. [Backend Generation](#backend-generation)
10. [Frontend Generation](#frontend-generation)
11. [API Documentation](#api-documentation)
12. [Testing](#testing)
13. [Contributing](#contributing)
14. [Troubleshooting](#troubleshooting)
15. [Changelog](#changelog)
16. [License](#license)

## Introduction

The Laravel Code Generator is an advanced, Python-based tool designed to streamline the development process for Laravel and Vue.js applications. By automating the creation of both backend and frontend components, it significantly reduces development time and ensures consistency across your project.

This tool takes a JSON schema as input and generates a complete set of Laravel backend components and Vue.js frontend components for admin panels. It's particularly useful for rapid prototyping, creating MVPs, or kickstarting large-scale projects with a solid foundation.

## Features

### Backend Generation

- **Models**: Eloquent models with relationships, fillable attributes, and type-hinted properties
- **Migrations**: Database migrations with proper column types and foreign key constraints
- **Controllers**: RESTful API controllers with standard CRUD operations
- **Requests**: Form request classes for validation
- **Resources**: API resources for data transformation
- **Repositories**: Repository classes and interfaces for data access abstraction
- **Policies**: Authorization policies integrated with Laravel's policy system
- **Factories**: Model factories for database seeding and testing
- **Seeders**: Database seeders for initial data population

### Frontend Generation

- **Vue Components**:
  - List views with sorting, filtering, and pagination
  - Form components for creating and editing models
  - Modal components for quick edits and confirmations
- **Vuex Store**:
  - Store modules for each model with actions, mutations, and getters
  - TypeScript support for type-safe state management
- **Vue Router**: Automatic route generation for generated components
- **Admin Panel**: A complete admin panel layout with sidebar navigation
- **UI Components**: Integration with PrimeVue for a rich set of UI components

### Additional Features

- **Swagger Documentation**: Automatic generation of OpenAPI (Swagger) documentation for API endpoints
- **Relationship Handling**: Support for various types of Eloquent relationships
- **Customizable Templates**: Easily modifiable Jinja2 templates for all generated components
- **Configuration System**: Flexible JSON-based configuration for customizing the generation process
- **Type Safety**: TypeScript integration for frontend code to ensure type safety
- **Code Style**: Generated code adheres to Laravel and Vue.js best practices and coding standards

## System Requirements

- Python 3.7+
- Laravel 8.x+ (for the generated backend code)
- Vue.js 3.x+ (for the generated frontend code)
- Composer (for Laravel dependencies)
- Node.js 14+ and npm 6+ (for frontend dependencies)
- Git (for version control and installation)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/laravel-code-generator.git
   ```

2. Navigate to the project directory:

   ```
   cd laravel-code-generator
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Install frontend dependencies:

   ```
   cd frontend
   npm install
   ```

6. Copy the example configuration file:

   ```
   cp config/default_config.example.json config/default_config.json
   ```

7. Edit `config/default_config.json` to match your project requirements.

## Usage

1. Prepare your input schema JSON file. You can use the provided example in `input_examples/ecommerce_schema.json` as a starting point.

2. Run the code generator:

   ```
   python src/main.py --schema path/to/your/schema.json --config config/default_config.json
   ```

3. The generated code will be output to the directories specified in your configuration.

4. Review the generated code and make any necessary adjustments.

5. Integrate the generated code into your Laravel and Vue.js projects.

## Project Structure

```
laravel-code-generator/
├── src/
│   ├── core/
│   │   ├── models/
│   │   │   └── schema.py
│   │   ├── interfaces/
│   │   │   └── generator.py
│   │   └── utils/
│   │       └── string_utils.py
│   ├── infrastructure/
│   │   ├── config_loader.py
│   │   ├── schema_parser.py
│   │   └── template_reader.py
│   ├── generators/
│   │   ├── backend/
│   │   │   ├── model_generator.py
│   │   │   ├── migration_generator.py
│   │   │   ├── controller_generator.py
│   │   │   ├── request_generator.py
│   │   │   ├── resource_generator.py
│   │   │   ├── repository_generator.py
│   │   │   ├── policy_generator.py
│   │   │   ├── factory_generator.py
│   │   │   └── seeder_generator.py
│   │   └── frontend/
│   │       ├── component_generator.py
│   │       ├── store_generator.py
│   │       ├── router_generator.py
│   │       └── admin_panel_generator.py
│   ├── templates/
│   │   ├── backend/
│   │   └── frontend/
│   └── main.py
├── tests/
│   ├── unit/
│   └── integration/
├── config/
│   └── default_config.json
├── input_examples/
│   └── ecommerce_schema.json
├── output/
│   ├── backend/
│   └── frontend/
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── requirements.txt
├── setup.py
└── README.md
```

## Configuration

The `config/default_config.json` file allows you to customize various aspects of the code generation process. Key configuration options include:

- `output_directory`: Root directory for generated code
- `backend`: Configuration for backend generation
  - `output_dir`: Directory for Laravel backend code
  - `namespace`: Base namespace for Laravel classes
  - `use_soft_deletes`: Enable soft deletes in models
- `frontend`: Configuration for frontend generation
  - `output_dir`: Directory for Vue.js frontend code
  - `use_typescript`: Enable TypeScript for frontend code
- `database`: Database configuration (engine, charset, collation)
- `naming`: Naming conventions for files and classes
- `templates`: Custom paths for code templates
- `swagger`: Configuration for Swagger documentation generation

Refer to the comments in the configuration file for detailed explanations of each option.

## Customization

### Modifying Templates

You can customize the generated code by modifying the template files in the `src/templates/` directory. Templates use the Jinja2 templating engine.

1. Locate the template you want to modify (e.g., `src/templates/backend/model_stub.php`)
2. Make your desired changes, using Jinja2 syntax for dynamic content
3. The changes will be reflected in subsequent code generations

### Adding New Generators

To add a new generator:

1. Create a new Python file in `src/generators/backend/` or `src/generators/frontend/`
2. Implement the `Generator` interface defined in `src/core/interfaces/generator.py`
3. Add appropriate templates in `src/templates/`
4. Register the new generator in `src/main.py`

Example of a new generator class:

```python
from src.core.interfaces.generator import Generator

class NewGenerator(Generator):
    def __init__(self, config):
        self.config = config

    def generate(self, model):
        # Implementation here
        pass
```

## Backend Generation

The backend generation creates the following Laravel components:

### Models

- Located in `app/Models/`
- Includes fillable attributes, relationships, and type-hinted properties
- Supports soft deletes if enabled in config

### Migrations

- Located in `database/migrations/`
- Creates tables with appropriate column types
- Handles foreign key constraints for relationships

### Controllers

- Located in `app/Http/Controllers/`
- Implements RESTful API actions (index, store, show, update, destroy)
- Uses repository pattern for data access

### Requests

- Located in `app/Http/Requests/`
- Implements form validation rules based on model attributes

### Resources

- Located in `app/Http/Resources/`
- Transforms model data for API responses

### Repositories

- Located in `app/Repositories/`
- Implements data access logic
- Includes an interface and concrete implementation

### Policies

- Located in `app/Policies/`
- Defines authorization rules for model actions

### Factories

- Located in `database/factories/`
- Creates model factories for testing and seeding

### Seeders

- Located in `database/seeders/`
- Populates the database with initial data

## Frontend Generation

The frontend generation creates a Vue.js 3 admin panel with the following components:

### Vue Components

- List views (`src/views/`)
- Form components (`src/components/forms/`)
- Modal components (`src/components/modals/`)

### Vuex Store

- Store modules for each model (`src/store/modules/`)
- Actions for API calls
- Mutations for state updates
- Getters for derived state

### Vue Router

- Route configuration (`src/router/index.js`)
- Automatic route generation for list and form views

### Admin Panel

- Layout component with sidebar navigation
- Integration with PrimeVue UI components

### TypeScript Support

- Type definitions for models and store state
- Type-safe component props and emits

## API Documentation

The generator creates Swagger (OpenAPI) documentation for your API endpoints:

- Located in `public/api-docs/`
- Includes endpoint descriptions, request parameters, and response schemas
- Can be viewed using Swagger UI

## Testing

To run the test suite:

```
python -m pytest tests/
```

This will execute both unit and integration tests. Ensure you have a test database configured in your `.env.testing` file.

## Contributing

We welcome contributions to the Laravel Code Generator! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please ensure your code adheres to our coding standards and include tests for new features.

## Troubleshooting

If you encounter any issues:

1. Check the logs in `storage/logs/laravel.log`
2. Ensure all dependencies are installed and up to date
3. Verify your configuration in `config/default_config.json`
4. Check the [GitHub Issues](https://github.com/your-username/laravel-code-generator/issues) page for known problems or to report a new issue

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## License

The Laravel Code Generator is open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
