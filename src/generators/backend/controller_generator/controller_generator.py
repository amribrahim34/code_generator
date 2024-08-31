import os
from .translation_generator import TranslationGenerator
from .swagger_doc_generator import SwaggerDocGenerator
from ..common.template_reader import TemplateReader
from ..services.translation_service import TranslationService
from ..services.google_translator import GoogleTranslator

class ControllerGenerator:
    def __init__(self, config):
        self.config = config
        self.template_reader = TemplateReader()
        self.swagger_doc_generator = SwaggerDocGenerator()
        google_translator = GoogleTranslator()
        translation_service = TranslationService(google_translator)
        self.translation_generator = TranslationGenerator(translation_service)

    def generate(self, model: dict) -> dict:
        controller_content = self._generate_controller(model)
        translations = self._generate_translations(model)
        return {
            f"app/Http/Controllers/{model['name']}Controller.php": controller_content,
            f"resources/lang/en/{model['name'].lower()}.php": self.translation_generator.format_translations(translations, 'en'),
            f"resources/lang/ar/{model['name'].lower()}.php": self.translation_generator.format_translations(translations, 'ar')
        }

    def _generate_controller(self, model: dict) -> str:
        template_path = self.config.get('controller_template_path', '')
        if not template_path or not os.path.exists(template_path):
            return self._generate_default_controller(model)
        
        template = self.template_reader.read_template(template_path)
        # Fill in the template with generated content
        return template.format(model_name=model['name'])

    def _generate_default_controller(self, model: dict) -> str:
        model_name = model['name']
        model_variable = model_name.lower()
        
        swagger_class_doc = self.swagger_doc_generator.generate_swagger_doc(model)
        index_doc = self.swagger_doc_generator.generate_index_doc(model)
        store_doc = self.swagger_doc_generator.generate_store_doc(model)
        show_doc = self.swagger_doc_generator.generate_show_doc(model)
        update_doc = self.swagger_doc_generator.generate_update_doc(model)
        destroy_doc = self.swagger_doc_generator.generate_destroy_doc(model)

        return f"""<?php

namespace App\\Http\\Controllers;

use App\\Models\\{model_name};
use App\\Http\\Requests\\{model_name}StoreRequest;
use App\\Http\\Requests\\{model_name}UpdateRequest;
use App\\Http\\Resources\\{model_name}Resource;
use App\\Repositories\\{model_name}RepositoryInterface;
use Illuminate\\Support\\Facades\\Lang;

{swagger_class_doc}
class {model_name}Controller extends Controller
{{
    protected ${model_variable}Repository;

    public function __construct({model_name}RepositoryInterface ${model_variable}Repository)
    {{
        $this->{model_variable}Repository = ${model_variable}Repository;
    }}

    {index_doc}
    public function index()
    {{
        ${model_variable}s = $this->{model_variable}Repository->paginate(15);
        return {model_name}Resource::collection(${model_variable}s)
            ->additional(['message' => Lang::get('{model_variable}.index_success')]);
    }}

    {store_doc}
    public function store({model_name}StoreRequest $request)
    {{
        ${model_variable} = $this->{model_variable}Repository->create($request->validated());
        return new {model_name}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.store_success')]);
    }}

    {show_doc}
    public function show($id)
    {{
        ${model_variable} = $this->{model_variable}Repository->find($id);
        if (!${model_variable}) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return new {model_name}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.show_success')]);
    }}

    {update_doc}
    public function update({model_name}UpdateRequest $request, $id)
    {{
        ${model_variable} = $this->{model_variable}Repository->update($id, $request->validated());
        if (!${model_variable}) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return new {model_name}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.update_success')]);
    }}

    {destroy_doc}
    public function destroy($id)
    {{
        $result = $this->{model_variable}Repository->delete($id);
        if (!$result) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return response()->json(['message' => Lang::get('{model_variable}.destroy_success')], 200);
    }}
}}
"""

    def _generate_translations(self, model: dict) -> dict:
        messages = {
            'index_success': f"{model['name']} list retrieved successfully.",
            'store_success': f"{model['name']} created successfully.",
            'show_success': f"{model['name']} retrieved successfully.",
            'update_success': f"{model['name']} updated successfully.",
            'destroy_success': f"{model['name']} deleted successfully.",
            'not_found': f"{model['name']} not found."
        }
        return self.translation_generator.generate_translations(messages)