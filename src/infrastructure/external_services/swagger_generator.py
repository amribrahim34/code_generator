from typing import Dict, Any
from src.core.entities.schema import Schema
from src.core.entities.model import Model

class SwaggerGenerator:
    def __init__(self):
        self.openapi_version = "3.0.0"
        self.info = {
            "title": "API Documentation",
            "version": "1.0.0"
        }
        self.paths = {}
        self.components = {"schemas": {}}
    
    def generate_swagger_doc(self, schema: Schema) -> Dict[str, Any]:
        self._generate_paths(schema)
        self._generate_components(schema)
        
        return {
            "openapi": self.openapi_version,
            "info": self.info,
            "paths": self.paths,
            "components": self.components
        }

    def _generate_paths(self, schema: Schema):
        for model in schema.models:
            self._generate_model_paths(model)

    def _generate_model_paths(self, model: Model):
        base_path = f"/{model.name.lower()}s"
        
        self.paths[base_path] = {
            "get": self._generate_index_operation(model),
            "post": self._generate_store_operation(model)
        }
        
        self.paths[f"{base_path}/{{id}}"] = {
            "get": self._generate_show_operation(model),
            "put": self._generate_update_operation(model),
            "delete": self._generate_destroy_operation(model)
        }

    def _generate_index_operation(self, model: Model) -> Dict[str, Any]:
        return {
            "tags": [f"{model.name}s"],
            "summary": f"Get list of {model.name}s",
            "description": f"Returns list of {model.name}s",
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{model.name}Resource"
                            }
                        }
                    }
                }
            }
        }

    def _generate_store_operation(self, model: Model) -> Dict[str, Any]:
        return {
            "tags": [f"{model.name}s"],
            "summary": f"Store a new {model.name}",
            "description": f"Returns {model.name} data",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": f"#/components/schemas/{model.name}StoreRequest"
                        }
                    }
                }
            },
            "responses": {
                "201": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{model.name}Resource"
                            }
                        }
                    }
                }
            }
        }

    def _generate_show_operation(self, model: Model) -> Dict[str, Any]:
        return {
            "tags": [f"{model.name}s"],
            "summary": f"Get {model.name} information",
            "description": f"Returns {model.name} data",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": f"{model.name} id",
                    "required": True,
                    "schema": {
                        "type": "integer"
                    }
                }
            ],
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{model.name}Resource"
                            }
                        }
                    }
                }
            }
        }

    def _generate_update_operation(self, model: Model) -> Dict[str, Any]:
        return {
            "tags": [f"{model.name}s"],
            "summary": f"Update existing {model.name}",
            "description": f"Returns updated {model.name} data",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": f"{model.name} id",
                    "required": True,
                    "schema": {
                        "type": "integer"
                    }
                }
            ],
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": f"#/components/schemas/{model.name}UpdateRequest"
                        }
                    }
                }
            },
            "responses": {
                "200": {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{model.name}Resource"
                            }
                        }
                    }
                }
            }
        }

    def _generate_destroy_operation(self, model: Model) -> Dict[str, Any]:
        return {
            "tags": [f"{model.name}s"],
            "summary": f"Delete existing {model.name}",
            "description": "Deletes a record and returns no content",
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "description": f"{model.name} id",
                    "required": True,
                    "schema": {
                        "type": "integer"
                    }
                }
            ],
            "responses": {
                "204": {
                    "description": "Successful operation"
                }
            }
        }

    def _generate_components(self, schema: Schema):
        for model in schema.models:
            self._generate_model_schemas(model)

    def _generate_model_schemas(self, model: Model):
        self.components["schemas"][f"{model.name}Resource"] = self._generate_resource_schema(model)
        self.components["schemas"][f"{model.name}StoreRequest"] = self._generate_request_schema(model)
        self.components["schemas"][f"{model.name}UpdateRequest"] = self._generate_request_schema(model)

    def _generate_resource_schema(self, model: Model) -> Dict[str, Any]:
        properties = {attr.name: {"type": self._map_type(attr.type)} for attr in model.attributes}
        return {
            "type": "object",
            "properties": properties
        }

    def _generate_request_schema(self, model: Model) -> Dict[str, Any]:
        properties = {attr.name: {"type": self._map_type(attr.type)} for attr in model.attributes if attr.name != "id"}
        return {
            "type": "object",
            "properties": properties
        }

    def _map_type(self, attr_type: str) -> str:
        type_mapping = {
            "string": "string",
            "integer": "integer",
            "float": "number",
            "boolean": "boolean",
            "date": "string",
            "datetime": "string",
            "text": "string"
        }
        return type_mapping.get(attr_type, "string")