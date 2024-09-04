# Unified Code Generator Structure and Flow

## 1. Core (Domain Layer)

### Entities

#### 1.1 schema.py

- **Purpose**: Represents the overall structure of the input schema.
- **Contents**:
  - `Schema` class:
    - Properties: `models` (List[Model]), `global_options` (Dict)
    - Methods:
      - `add_model(model: Model) -> None`
      - `get_model(name: str) -> Model`
      - `validate() -> List[str]`
      - `to_dict() -> Dict`
  - `SchemaValidator` class:
    - Methods:
      - `validate_relationships() -> List[str]`
      - `validate_unique_model_names() -> List[str]`
- **Usage**: Central to schema parsing and validation. The `ParseInputSchema` use case creates and populates a `Schema` instance.

#### 1.2 model.py

- **Purpose**: Represents a single model in the schema.
- **Contents**:
  - `Model` class:
    - Properties: `name` (str), `table_name` (str), `attributes` (List[Attribute]), `relationships` (List[Relationship]), `options` (Dict)
    - Methods:
      - `add_attribute(attribute: Attribute) -> None`
      - `add_relationship(relationship: Relationship) -> None`
      - `get_primary_key() -> Attribute`
      - `get_fillable_attributes() -> List[Attribute]`
      - `generate_laravel_model_code() -> str`
      - `generate_vue_interface_code() -> str`
- **Usage**: Used by various generators to create model-specific code for both backend and frontend.

#### 1.3 relationship.py

- **Purpose**: Represents relationships between models.
- **Contents**:
  - `Relationship` class:
    - Properties: `type` (str), `related_model` (str), `foreign_key` (str), `local_key` (str)
    - Methods:
      - `to_laravel_method() -> str`
      - `to_typescript_property() -> str`
- **Usage**: Used in model generation to create relationship methods and properties.

#### 1.4 attribute.py

- **Purpose**: Represents individual attributes of a model.
- **Contents**:
  - `Attribute` class:
    - Properties: `name` (str), `type` (str), `nullable` (bool), `default` (Any), `unique` (bool)
    - Methods:
      - `to_migration_column() -> str`
      - `to_typescript_property() -> str`
      - `to_form_input() -> str`
- **Usage**: Used by various generators to create attribute-specific code.

### Use Cases

#### 1.5 generate_backend_code.py

- **Purpose**: Orchestrates backend code generation.
- **Contents**:
  - `GenerateBackendCode` class:
    - Methods:
      - `execute(schema: Schema) -> Dict[str, str]`
      - `generate_models() -> Dict[str, str]`
      - `generate_migrations() -> Dict[str, str]`
      - `generate_controllers() -> Dict[str, str]`
- **Usage**: Called by the `BackendGenerationService` to generate all backend code.

#### 1.6 generate_frontend_code.py

- **Purpose**: Orchestrates frontend code generation.
- **Contents**:
  - `GenerateFrontendCode` class:
    - Methods:
      - `execute(schema: Schema) -> Dict[str, str]`
      - `generate_components() -> Dict[str, str]`
      - `generate_store_modules() -> Dict[str, str]`
      - `generate_routes() -> str`
- **Usage**: Called by the `FrontendGenerationService` to generate all frontend code.

#### 1.7 generate_api_documentation.py

- **Purpose**: Generates API documentation.
- **Contents**:
  - `GenerateAPIDocumentation` class:
    - Methods:
      - `execute(schema: Schema) -> str`
      - `generate_swagger_json() -> Dict`
- **Usage**: Called to create Swagger/OpenAPI documentation.

#### 1.8 parse_input_schema.py

- **Purpose**: Parses and validates the input schema.
- **Contents**:
  - `ParseInputSchema` class:
    - Methods:
      - `execute(schema_data: Dict) -> Schema`
      - `validate_schema_structure(schema_data: Dict) -> None`
- **Usage**: First step in the generation process, creating the `Schema` object.

### Interfaces (Ports)

#### 1.9 schema_parser.py

- **Purpose**: Defines schema parsing interface.
- **Contents**:
  - `ISchemaParser` interface:
    - Methods:
      - `parse(schema_data: Dict) -> Schema`
      - `validate(schema_data: Dict) -> None`
- **Usage**: Implemented by concrete schema parsers.

#### 1.10 template_renderer.py

- **Purpose**: Defines template rendering interface.
- **Contents**:
  - `ITemplateRenderer` interface:
    - Methods:
      - `render(template_name: str, context: Dict) -> str`
      - `load_template(template_name: str) -> str`
- **Usage**: Implemented by concrete template renderers.

#### 1.11 code_generator.py

- **Purpose**: Defines code generator interface.
- **Contents**:
  - `ICodeGenerator` interface:
    - Methods:
      - `generate(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Implemented by all code generators.

#### 1.12 config_loader.py

- **Purpose**: Defines configuration loading interface.
- **Contents**:
  - `IConfigLoader` interface:
    - Methods:
      - `load(config_path: str) -> Dict`
      - `get(key: str, default: Any = None) -> Any`
- **Usage**: Implemented by configuration loaders.

#### 1.13 output_writer.py

- **Purpose**: Defines interface for writing output files.
- **Contents**:
  - `IOutputWriter` interface:
    - Methods:
      - `write_file(file_path: str, content: str) -> None`
      - `create_directory(directory_path: str) -> None`
- **Usage**: Implemented by concrete output writers.

#### 1.14 logger.py

- **Purpose**: Defines logging interface.
- **Contents**:
  - `ILogger` interface:
    - Methods:
      - `info(message: str) -> None`
      - `warning(message: str) -> None`
      - `error(message: str) -> None`
- **Usage**: Implemented by concrete loggers.

## 2. Application Layer

### Services

#### 2.1 backend_generation_service.py

- **Purpose**: Coordinates backend code generation.
- **Contents**:
  - `BackendGenerationService` class:
    - Methods:
      - `generate(schema: Schema) -> GenerationResponseDTO`
- **Usage**: Called by the main application to generate backend code.

#### 2.2 frontend_generation_service.py

- **Purpose**: Coordinates frontend code generation.
- **Contents**:
  - `FrontendGenerationService` class:
    - Methods:
      - `generate(schema: Schema) -> GenerationResponseDTO`
- **Usage**: Called by the main application to generate frontend code.

#### 2.3 api_documentation_service.py

- **Purpose**: Manages API documentation generation.
- **Contents**:
  - `APIDocumentationService` class:
    - Methods:
      - `generate(schema: Schema) -> str`
- **Usage**: Called to generate API documentation.

#### 2.4 schema_validation_service.py

- **Purpose**: Validates input schemas.
- **Contents**:
  - `SchemaValidationService` class:
    - Methods:
      - `validate(schema_data: Dict) -> List[str]`
- **Usage**: Called before schema parsing to ensure valid input.

### DTOs

#### 2.5 generation_request_dto.py

- **Purpose**: Represents generation request data.
- **Contents**:
  - `GenerationRequestDTO` class:
    - Properties: `schema_data` (Dict), `config` (Dict)
- **Usage**: Used to pass generation request data between layers.

#### 2.6 generation_response_dto.py

- **Purpose**: Represents generation response data.
- **Contents**:
  - `GenerationResponseDTO` class:
    - Properties: `generated_files` (Dict[str, str]), `warnings` (List[str]), `errors` (List[str])
- **Usage**: Used to return generation results.

## 3. Infrastructure Layer

### Adapters

#### 3.1 json_schema_parser.py

- **Purpose**: Implements JSON schema parsing.
- **Contents**:
  - `JSONSchemaParser` class (implements `ISchemaParser`):
    - Methods:
      - `parse(schema_data: Dict) -> Schema`
      - `validate(schema_data: Dict) -> None`
- **Usage**: Used to parse JSON input schemas.

#### 3.2 jinja_template_renderer.py

- **Purpose**: Implements Jinja2 template rendering.
- **Contents**:
  - `JinjaTemplateRenderer` class (implements `ITemplateRenderer`):
    - Methods:
      - `render(template_name: str, context: Dict) -> str`
      - `load_template(template_name: str) -> str`
- **Usage**: Used by generators to render templates.

#### 3.3 file_system_output_writer.py

- **Purpose**: Implements file system writing.
- **Contents**:
  - `FileSystemOutputWriter` class (implements `IOutputWriter`):
    - Methods:
      - `write_file(file_path: str, content: str) -> None`
      - `create_directory(directory_path: str) -> None`
- **Usage**: Used to write generated code to files.

#### 3.4 json_config_loader.py

- **Purpose**: Implements JSON configuration loading.
- **Contents**:
  - `JSONConfigLoader` class (implements `IConfigLoader`):
    - Methods:
      - `load(config_path: str) -> Dict`
      - `get(key: str, default: Any = None) -> Any`
- **Usage**: Used to load and access configuration.

#### 3.5 console_logger.py

- **Purpose**: Implements console logging.
- **Contents**:
  - `ConsoleLogger` class (implements `ILogger`):
    - Methods:
      - `info(message: str) -> None`
      - `warning(message: str) -> None`
      - `error(message: str) -> None`
- **Usage**: Used for logging throughout the application.

### External Services

#### 3.6 swagger_generator.py

- **Purpose**: Generates Swagger/OpenAPI documentation.
- **Contents**:
  - `SwaggerGenerator` class:
    - Methods:
      - `generate(schema: Schema) -> Dict`
- **Usage**: Used by API documentation service.

## 4. Presentation Layer

### CLI

#### 4.1 command_line_interface.py

- **Purpose**: Provides CLI for the generator.
- **Contents**:
  - `CommandLineInterface` class:
    - Methods:
      - `run() -> None`
      - `parse_arguments() -> argparse.Namespace`
- **Usage**: Entry point for CLI usage of the generator.

### API

#### 4.2 restful_api.py

- **Purpose**: Provides RESTful API for the generator.
- **Contents**:
  - `RESTfulAPI` class:
    - Methods:
      - `generate_code() -> Response`
      - `get_schema() -> Response`
- **Usage**: Entry point for API usage of the generator (for future expansion).

## 5. Generators

### Backend (Laravel)

#### 5.1 model_generator.py

- **Purpose**: Generates Laravel Eloquent models.
- **Contents**:
  - `LaravelModelGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_relationship_method(relationship: Relationship) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel model classes.

#### 5.2 migration_generator.py

- **Purpose**: Generates Laravel migrations.
- **Contents**:
  - `LaravelMigrationGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_column_definition(attribute: Attribute) -> str`
      - `generate_foreign_key_constraints(model: Model) -> List[str]`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel migration files.

#### 5.3 controller_generator.py

- **Purpose**: Generates Laravel controllers.
- **Contents**:
  - `LaravelControllerGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_index_method(model: Model) -> str`
      - `generate_store_method(model: Model) -> str`
      - `generate_update_method(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel controller classes.

#### 5.4 request_generator.py

- **Purpose**: Generates Laravel form requests.
- **Contents**:
  - `LaravelRequestGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model, operation: str) -> str`
      - `generate_validation_rules(model: Model, operation: str) -> Dict[str, str]`
      - `get_file_path(model: Model, operation: str) -> str`
- **Usage**: Used to generate Laravel form request classes.

#### 5.5 resource_generator.py

- **Purpose**: Generates Laravel API resources.
- **Contents**:
  - `LaravelResourceGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_to_array_method(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel API resource classes.

#### 5.6 repository_generator.py

- **Purpose**: Generates Laravel repositories.
- **Contents**:
  - `LaravelRepositoryGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_crud_methods(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel repository classes.

#### 5.7 repository_interface_generator.py

- **Purpose**: Generates Laravel repository interfaces.
- **Contents**:
  - `LaravelRepositoryInterfaceGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_method_signatures(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**: Used to generate Laravel repository interface files.

#### 5.8 policy_generator.py

- **Purpose**: Generates Laravel policies.
- **Contents**:
  - `LaravelPolicyGenerator` class (implements `ICodeGenerator`):
    - Methods:
      - `generate(model: Model) -> str`
      - `generate_policy_methods(model: Model) -> str`
      - `get_file_path(model: Model) -> str`
- **Usage**:
