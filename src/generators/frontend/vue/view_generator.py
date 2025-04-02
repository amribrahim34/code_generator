from typing import Dict, Any, List
from src.core.interfaces.code_generator import ICodeGenerator
from src.core.entities.schema import Schema, Model , Attribute
from src.core.interfaces.template_renderer import ITemplateRenderer
from src.core.interfaces.config_loader import IConfigLoader
from src.utilities.string_utils import (
    to_pascal_case, 
    to_kebab_case, 
    to_camel_case, 
    pluralize
)
import os
import logging



class ViewGenerator(ICodeGenerator):
    def __init__(self, config_loader: IConfigLoader, template_renderer: ITemplateRenderer):
        self.config_loader = config_loader
        self.template_renderer = template_renderer
        self.config = config_loader.get_config()
        self.view_dir = os.path.join(
            self.config['frontend']['output_dir'],
            'src',
            self.config['frontend']['view_dir']
        )
        self.logger = logging.getLogger(__name__)

    def generate(self, schema: Schema) -> Dict[str, str]:
        generated_files = {}

        # Generate views for each model
        for model in schema.models:
            # List view
            list_view_content = self.prepare_context(model)
            list_view_path = self.get_output_path(model.name, 'list')
            generated_files[list_view_path] = list_view_content

            # Create view
            create_view_content = self.prepare_context(model)
            create_view_path = self.get_output_path(model.name, 'create')
            generated_files[create_view_path] = create_view_content

            # Update view
            update_view_content = self.prepare_context(model)
            update_view_path = self.get_output_path(model.name, 'update')
            generated_files[update_view_path] = update_view_content

        return generated_files

    def generate_list_view(self, model: Model) -> str:
        # Prepare context for list view template
        context = {
            'MODEL_NAME': to_pascal_case(model.name),
            'MODEL_NAME_PLURAL': to_pascal_case(pluralize(model.name)),
            'MODEL_NAME_LOWERCASE': model.name.lower(),
            'MODEL_NAME_PLURAL_LOWERCASE': pluralize(model.name).lower(),
            'MODEL_NAME_KEBAB': to_kebab_case(model.name),
            'MODEL_NAME_PLURAL_KEBAB': to_kebab_case(pluralize(model.name)),
            'COLUMNS': self._generate_table_columns(model.attributes),
            'FILTER_FIELDS': self._generate_filter_fields(model.attributes),
            'EXPORT_FIELDS': self._generate_export_fields(model.attributes)
        }

        # Render list view template
        template = 'frontend/vue/views/list.stub'
        return self.render_template(template, context)
    
    def get_output_path(self, model_name: str, view_type: str) -> str:
        """Generate output path for different view types"""
        model_name_kebab_plural = to_kebab_case(pluralize(model_name))
        
        if view_type == 'list':
            return os.path.join(
                self.view_dir, 
                model_name_kebab_plural, 
                f"{model_name_kebab_plural}-list.vue"
            )
        elif view_type == 'create':
            return os.path.join(
                self.view_dir, 
                model_name_kebab_plural, 
                f"{to_kebab_case(model_name)}-create.vue"
            )
        elif view_type == 'update':
            return os.path.join(
                self.view_dir, 
                model_name_kebab_plural, 
                f"{to_kebab_case(model_name)}-update.vue"
            )
        else:
            raise ValueError(f"Invalid view type: {view_type}")
        
    def prepare_context(self, model: Model) -> str:
        """Prepare context for view template rendering"""
        # Determine view type (list, create, update)
        view_type = 'list'  # Default to list view
        if 'create' in self.get_output_path(model.name, 'create'):
            view_type = 'create'
        elif 'update' in self.get_output_path(model.name, 'update'):
            view_type = 'update'

        context = {
            'MODEL_NAME': to_pascal_case(model.name),
            'MODEL_NAME_PLURAL': to_pascal_case(pluralize(model.name)),
            'MODEL_NAME_LOWERCASE': model.name.lower(),
            'MODEL_NAME_PLURAL_LOWERCASE': pluralize(model.name).lower(),
            'MODEL_NAME_KEBAB': to_kebab_case(model.name),
            'MODEL_NAME_PLURAL_KEBAB': to_kebab_case(pluralize(model.name)),
        }

        # Add specific context based on view type
        if view_type == 'list':
            context.update({
                'COLUMNS': self._generate_table_columns(model.attributes),
                'FILTER_FIELDS': self._generate_filter_fields(model.attributes),
                'EXPORT_FIELDS': self._generate_export_fields(model.attributes)
            })
        elif view_type in ['create', 'update']:
            context.update({
                'FORM_FIELDS': self._generate_form_fields(model.attributes)
            })

        # Get the appropriate template
        template = self.get_template(view_type)
        
        # Render and return the template
        return self.render_template(template, context)
    
    def get_template(self, template_name: str) -> str:
        template_path = "frontend/vue/type.stub"
        return self.template_renderer.load_template(template_path)

    def generate_create_view(self, model: Model) -> str:
        context = {
            'MODEL_NAME': to_pascal_case(model.name),
            'MODEL_NAME_LOWERCASE': model.name.lower(),
            'MODEL_NAME_KEBAB': to_kebab_case(model.name),
            'FORM_FIELDS': self._generate_form_fields(model.attributes)
        }

        template = 'frontend/vue/views/create.stub'
        return self.render_template(template, context)

    def generate_update_view(self, model: Model) -> str:
        context = {
            'MODEL_NAME': to_pascal_case(model.name),
            'MODEL_NAME_LOWERCASE': model.name.lower(),
            'MODEL_NAME_KEBAB': to_kebab_case(model.name),
            'FORM_FIELDS': self._generate_form_fields(model.attributes)
        }

        template = 'frontend/vue/views/update.stub'
        return self.render_template(template, context)

    def _generate_table_columns(self, fields: List[Attribute]) -> str:
        """Generate table columns for the list view"""
        columns = []
        for field in fields:
            # Skip 'id' field or add custom logic for primary key
            if field.name.lower() == 'id':
                columns.append(f"""{{
                    title: 'ID',
                    dataIndex: 'id',
                    key: 'id',
                    width: 80
                }}""")
            elif field.type in ['string', 'text']:
                columns.append(f"""{{
                    title: '{to_pascal_case(field.name)}',
                    dataIndex: '{field.name}',
                    key: '{field.name}',
                    ellipsis: true
                }}""")
            elif field.type in ['integer', 'float', 'decimal']:
                columns.append(f"""{{
                    title: '{to_pascal_case(field.name)}',
                    dataIndex: '{field.name}',
                    key: '{field.name}',
                    align: 'right'
                }}""")
            elif field.type == 'date' or field.type == 'datetime':
                columns.append(f"""{{
                    title: '{to_pascal_case(field.name)}',
                    dataIndex: '{field.name}',
                    key: '{field.name}',
                    render: (text) => formatDate(text)
                }}""")
            elif field.type == 'boolean':
                columns.append(f"""{{
                    title: '{to_pascal_case(field.name)}',
                    dataIndex: '{field.name}',
                    key: '{field.name}',
                    render: (text) => text ? 'Yes' : 'No'
                }}""")
        
        # Add action column
        columns.append("""
        {
            title: 'Actions',
            key: 'actions',
            width: 150,
            render: (text, record) => (
                <space>
                    <router-link to={`/update/${record.id}`}>
                        <a-button type="link">Edit</a-button>
                    </router-link>
                    <a-button type="link" danger onClick={() => handleDelete(record.id)}>
                        Delete
                    </a-button>
                </space>
            )
        }
        """)

        return ',\n'.join(columns)

    def _generate_filter_fields(self, fields: List[Attribute]) -> str:
        """Generate filter fields for the list view"""
        filters = []
        for field in fields:
            if field.name.lower() == 'id':
                continue  # Skip ID field for filters
            
            filter_type = 'input'
            if field.type in ['integer', 'float', 'decimal']:
                filter_type = 'number'
            elif field.type == 'boolean':
                filter_type = 'select'
            elif field.type == 'date' or field.type == 'datetime':
                filter_type = 'date-range'
            
            filters.append(f"""{{
                title: '{to_pascal_case(field.name)}',
                dataIndex: '{field.name}',
                key: '{field.name}Filter',
                type: '{filter_type}'
            }}""")
        
        return ',\n'.join(filters)

    def _generate_export_fields(self, fields: List[Attribute]) -> str:
        """Generate export fields for the list view"""
        export_fields = []
        for field in fields:
            export_fields.append(f"""{{
                title: '{to_pascal_case(field.name)}',
                dataIndex: '{field.name}',
                key: '{field.name}Export'
            }}""")
        
        return ',\n'.join(export_fields)

    def _generate_form_fields(self, fields: List[Attribute]) -> str:
        """Generate form fields for create and update views"""
        form_fields = []
        for field in fields:
            # Skip ID field
            if field.name.lower() == 'id':
                continue
            
            # Determine form input type based on field type
            input_type = 'input'
            input_props = ''
            validation_rules = []

            if field.type in ['integer', 'float', 'decimal']:
                input_type = 'number-input'
                input_props = 'min={0} precision={2}'
                validation_rules.append('{ type: "number", message: "Please input a valid number" }')
            elif field.type == 'boolean':
                input_type = 'switch'
            elif field.type == 'date' or field.type == 'datetime':
                input_type = 'date-picker'
                input_props = 'format="YYYY-MM-DD"'
            elif field.type == 'string':
                # Remove the constraints check
                pass

            # Required validation
            if not field.nullable:
                validation_rules.insert(0, '{ required: true, message: "This field is required" }')

            form_field = f"""{{
                name: '{field.name}',
                label: '{to_pascal_case(field.name)}',
                type: '{input_type}',
                props: {{ 
                    {input_props} 
                }},
                rules: [
                    {', '.join(validation_rules)}
                ]
            }}"""
            
            form_fields.append(form_field)
    
        return ',\n'.join(form_fields)

    def render_template(self, template: str, context: Dict) -> str:
        """Render the template with given context"""
        try:
            return self.template_renderer.render(template, context)
        except Exception as e:
            self.logger.error(f"Error rendering template: {str(e)}")
            raise

    def validate_model(self, model: Model) -> None:
        """Validate the model before generation"""
        if not model.name:
            raise ValueError("Model must have a name")