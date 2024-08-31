# Laravel Code Generator

## Project Description

The Laravel Code Generator is a powerful tool designed to automate the creation of various Laravel components, including models, migrations, controllers, repositories, and more. This tool aims to streamline the development process by generating boilerplate code based on a JSON input file, allowing developers to focus on implementing business logic rather than writing repetitive code structures.

## Project Structure

```
.
├── input.json
├── main.py
├── requirements.txt
└── src
    ├── config
    │   ├── config.json
    │   └── config.yaml
    ├── generator.py
    ├── generators
    │   ├── controller_generator.py
    │   ├── migration_generator.py
    │   ├── model_generator.py
    │   ├── repository_generator.py
    │   ├── repository_interface_generator.py
    │   ├── repository_service_provider_generator.py
    │   ├── request_generator.py
    │   └── resource_generator.py
    ├── helpers
    │   └── relationship_helper.py
    ├── parsers
    │   ├── json_parser.py
    └── templates
        ├── controller_stub.php
        ├── migration_stub.php
        ├── model_stub.php
        ├── repository_interface_stub.php
        ├── repository_stub.php
        ├── request_stub.php
        └── resource_stub.php
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/laravel-code-generator.git
   ```

2. Navigate to the project directory:
   ```
   cd laravel-code-generator
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your `input.json` file with the desired structure for your Laravel components.

2. Run the main script:
   ```
   python main.py
   ```

3. The generated code will be output to a directory specified in your configuration.

## Configuration

The project uses configuration files located in the `src/config` directory:

- `config.json`: JSON-based configuration
- `config.yaml`: YAML-based configuration

You can modify these files to customize the output paths, naming conventions, and other generator settings.

## Components

### Generators

The `src/generators` directory contains various generator classes:

- `controller_generator.py`: Generates controller classes
- `migration_generator.py`: Generates database migration files
- `model_generator.py`: Generates Eloquent model classes
- `repository_generator.py`: Generates repository classes
- `repository_interface_generator.py`: Generates repository interface classes
- `repository_service_provider_generator.py`: Generates a service provider for binding repositories
- `request_generator.py`: Generates form request classes
- `resource_generator.py`: Generates API resource classes

### Parsers

The `src/parsers` directory contains:

- `json_parser.py`: Parses the input JSON file

### Helpers

The `src/helpers` directory contains:

- `relationship_helper.py`: Assists in generating code for model relationships

### Templates

The `src/templates` directory contains PHP stub files used as templates for generating the Laravel components.

## Input File Format

The `input.json` file should contain an array of objects, each representing a model with its attributes and relationships. For example:

```json
[
  {
    "name": "User",
    "attributes": [
      {"name": "id", "type": "bigIncrements"},
      {"name": "name", "type": "string"},
      {"name": "email", "type": "string"}
    ],
    "relationships": [
      {"type": "hasMany", "model": "Post"}
    ]
  },
  {
    "name": "Post",
    "attributes": [
      {"name": "id", "type": "bigIncrements"},
      {"name": "title", "type": "string"},
      {"name": "content", "type": "text"},
      {"name": "user_id", "type": "unsignedBigInteger"}
    ],
    "relationships": [
      {"type": "belongsTo", "model": "User"}
    ]
  }
]
```

## Expected Output

After running the generator, you can expect the following files to be created (paths may vary based on your configuration):

- Models: `app/Models/User.php`, `app/Models/Post.php`
- Migrations: `database/migrations/YYYY_MM_DD_HHMMSS_create_users_table.php`, `database/migrations/YYYY_MM_DD_HHMMSS_create_posts_table.php`
- Controllers: `app/Http/Controllers/UserController.php`, `app/Http/Controllers/PostController.php`
- Repositories: `app/Repositories/UserRepository.php`, `app/Repositories/PostRepository.php`
- Repository Interfaces: `app/Repositories/UserRepositoryInterface.php`, `app/Repositories/PostRepositoryInterface.php`
- Requests: `app/Http/Requests/UserStoreRequest.php`, `app/Http/Requests/UserUpdateRequest.php`, `app/Http/Requests/PostStoreRequest.php`, `app/Http/Requests/PostUpdateRequest.php`
- Resources: `app/Http/Resources/UserResource.php`, `app/Http/Resources/PostResource.php`
- Service Provider: `app/Providers/RepositoryServiceProvider.php`

## Customization

You can customize the generated code by modifying the stub files in the `src/templates` directory. These files contain placeholders that are replaced with actual values during the generation process.

## Contributing

Contributions to the Laravel Code Generator are welcome! Please feel free to submit pull requests, create issues, or suggest improvements.

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
