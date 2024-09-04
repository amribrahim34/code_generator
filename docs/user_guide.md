# User Guide for Code Generation System

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Input Schema](#input-schema)
5. [Configuration](#configuration)
6. [Generating Code](#generating-code)
7. [Output Structure](#output-structure)
8. [Customizing Templates](#customizing-templates)
9. [API Documentation](#api-documentation)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)
12. [FAQ](#faq)

## Introduction

Welcome to the Code Generation System user guide. This system automates the process of generating both backend (Laravel) and frontend (Vue.js) code based on a provided schema. It aims to accelerate development by creating a solid foundation for your web application.

## Installation

1. Ensure you have Python 3.8+ installed.
2. Install the Code Generation System using pip:
   ```
   pip install code-generation-system
   ```

## Quick Start

1. Create a JSON file `schema.json` with your data model:

   ```json
   {
     "models": {
       "User": {
         "attributes": {
           "id": "integer",
           "name": "string",
           "email": "string"
         }
       }
     }
   }
   ```

2. Run the code generator:

   ```
   code-gen --schema schema.json --output ./my-project
   ```

3. Your generated code will be in the `./my-project` directory.

## Input Schema

The input schema is a JSON file that describes your data models. Here's a more complex example:

```json
{
  "models": {
    "User": {
      "attributes": {
        "id": "integer",
        "name": "string",
        "email": { "type": "string", "unique": true },
        "password": "string"
      }
    },
    "Post": {
      "attributes": {
        "id": "integer",
        "title": "string",
        "content": "text",
        "published_at": "datetime"
      }
    }
  },
  "relationships": [
    {
      "type": "hasMany",
      "from": "User",
      "to": "Post"
    }
  ]
}
```

### Supported Attribute Types

- string
- integer
- float
- boolean
- date
- datetime
- text

### Relationship Types

- hasOne
- hasMany
- belongsTo
- belongsToMany

## Configuration

Create a `config.json` file to customize the code generation:

```json
{
  "app_name": "My Awesome App",
  "database": {
    "name": "my_app_db",
    "user": "root",
    "password": ""
  },
  "backend": {
    "framework": "laravel",
    "version": "8.x"
  },
  "frontend": {
    "framework": "vue",
    "version": "3.x"
  }
}
```

Use the config file with the generator:

```
code-gen --schema schema.json --config config.json --output ./my-project
```

## Generating Code

### Basic Usage

```
code-gen --schema <path-to-schema> --output <output-directory>
```

### Options

- `--schema`: Path to the input schema JSON file (required)
- `--output`: Directory where generated code will be placed (required)
- `--config`: Path to configuration JSON file (optional)
- `--backend-only`: Generate only backend code
- `--frontend-only`: Generate only frontend code
- `--force`: Overwrite existing files in the output directory

## Output Structure

The generated code will have the following structure:

```
my-project/
├── backend/
│   ├── app/
│   ├── database/
│   ├── routes/
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   └── store/
│   └── ...
└── api-docs/
    └── openapi.json
```

## Customizing Templates

You can customize the generated code by modifying the templates. Copy the default templates:

```
code-gen --export-templates ./my-templates
```

Modify the templates in `./my-templates`, then use them:

```
code-gen --schema schema.json --templates ./my-templates --output ./my-project
```

## API Documentation

The system generates OpenAPI (formerly Swagger) documentation for your API. Find it at `api-docs/openapi.json` in the output directory.

To view the documentation in a user-friendly format:

1. Install `swagger-ui`:
   ```
   npm install -g swagger-ui-cli
   ```
2. Serve the documentation:
   ```
   swagger-ui-cli serve ./my-project/api-docs/openapi.json
   ```

## Best Practices

1. **Start Small**: Begin with a simple schema and gradually add complexity.
2. **Version Control**: Keep your schema and configuration files in version control.
3. **Consistent Naming**: Use consistent naming conventions in your schema.
4. **Validate First**: Always validate your schema before generating code.
5. **Customize Thoughtfully**: When customizing templates, consider maintainability.

## Troubleshooting

### Common Issues

1. **Schema Validation Errors**:

   - Ensure all required fields are present in your schema.
   - Check that attribute types are valid.
   - Verify that relationship definitions are correct.

2. **Generation Failures**:

   - Check that the output directory is writable.
   - Ensure you have the latest version of the code generator.

3. **Customization Issues**:
   - When customizing templates, make sure all required placeholders are present.
   - Check for syntax errors in modified templates.

### Debugging

Use the `--verbose` flag for detailed output:

```
code-gen --schema schema.json --output ./my-project --verbose
```

## FAQ

**Q: Can I use this for existing projects?**
A: Yes, but be cautious. It's best to generate code into a new directory and then manually integrate it into your existing project.

**Q: How do I add custom logic to generated code?**
A: The generated code is meant to be a starting point. Add custom logic by editing the generated files or by extending the generated classes.

**Q: Is the generated code production-ready?**
A: The generated code provides a solid foundation, but you should review and test it thoroughly before using it in production.

**Q: How often should I regenerate code?**
A: Regenerate when your data model changes significantly. Be cautious when regenerating for existing projects to avoid overwriting custom changes.

---

For more information or if you encounter any issues not covered here, please visit our GitHub repository or contact our support team.
