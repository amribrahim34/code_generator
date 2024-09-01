import os
from abc import ABC, abstractmethod
from googletrans import Translator

class TranslationGenerator:
    def __init__(self):
        self.translator = Translator()

    def generate_translations(self, messages):
        translations = {}
        for key, value in messages.items():
            translations[key] = {
                'en': value,
                'ar': self.translator.translate(value, src='en', dest='ar').text
            }
        return translations

class TemplateReader:
    @staticmethod
    def read_template(template_path):
        with open(template_path, 'r') as file:
            return file.read()

class SwaggerDocGenerator:
    @staticmethod
    def generate_swagger_doc(model):
        return f"""/**
     * @OA\\Tag(
     *     name="{model['name']}s",
     *     description="{model['name']} resource"
     * )
     */"""

    @staticmethod
    def generate_index_doc(model):
        return f"""
    /**
     * @OA\\Get(
     *     path="/{model['name'].lower()}s",
     *     tags={{"{model['name']}s"}},
     *     summary="Get list of {model['name']}s",
     *     description="Returns list of {model['name']}s",
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_store_doc(model):
        return f"""
    /**
     * @OA\\Post(
     *     path="/{model['name'].lower()}s",
     *     tags={{"{model['name']}s"}},
     *     summary="Store a new {model['name']}",
     *     description="Returns {model['name']} data",
     *     @OA\\RequestBody(
     *         required=true,
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}StoreRequest")
     *     ),
     *     @OA\\Response(
     *         response=201,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_show_doc(model):
        return f"""
    /**
     * @OA\\Get(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Get {model['name']} information",
     *     description="Returns {model['name']} data",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_update_doc(model):
        return f"""
    /**
     * @OA\\Put(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Update existing {model['name']}",
     *     description="Returns updated {model['name']} data",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\RequestBody(
     *         required=true,
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}UpdateRequest")
     *     ),
     *     @OA\\Response(
     *         response=200,
     *         description="Successful operation",
     *         @OA\\JsonContent(ref="#/components/schemas/{model['name']}Resource")
     *     )
     * )
     */"""

    @staticmethod
    def generate_destroy_doc(model):
        return f"""
    /**
     * @OA\\Delete(
     *     path="/{model['name'].lower()}s/{{id}}",
     *     tags={{"{model['name']}s"}},
     *     summary="Delete existing {model['name']}",
     *     description="Deletes a record and returns no content",
     *     @OA\\Parameter(
     *         name="id",
     *         description="{model['name']} id",
     *         required=true,
     *         in="path",
     *         @OA\\Schema(
     *             type="integer"
     *         )
     *     ),
     *     @OA\\Response(
     *         response=204,
     *         description="Successful operation",
     *         @OA\\JsonContent()
     *     )
     * )
     */"""

class ControllerGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates', 'backend', 'controller_stub.php')
        self.translation_generator = TranslationGenerator()
        self.template_reader = TemplateReader()
        self.swagger_doc_generator = SwaggerDocGenerator()

    def generate(self, model):
        controller_content = self._generate_controller(model)
        translations = self._generate_translations(model)
        return {
            f"app/Http/Controllers/{model['name']}Controller.php": controller_content,
            f"resources/lang/en/{model['name'].lower()}.php": self._format_translations(translations, 'en'),
            f"resources/lang/ar/{model['name'].lower()}.php": self._format_translations(translations, 'ar')
        }

    def _generate_controller(self, model):
        template = self.template_reader.read_template(self.template_path)

        model_name = model['name']
        model_variable = model_name.lower()
        
        return template.format(
            namespace=self._generate_namespace(),
            use_statements=self._generate_use_statements(model),
            class_name=f"{model_name}Controller",
            model_name=model_name,
            model_variable=model_variable,
            repository_variable=f"{model_variable}Repository",
            constructor=self._generate_constructor(model),
            swagger_class_doc=self.swagger_doc_generator.generate_swagger_doc(model),
            index_method=self._generate_index_method(model),
            store_method=self._generate_store_method(model),
            show_method=self._generate_show_method(model),
            update_method=self._generate_update_method(model),
            destroy_method=self._generate_destroy_method(model)
        )

    def _generate_namespace(self):
        return "namespace App\\Http\\Controllers;"

    def _generate_use_statements(self, model):
        return f"""use App\\Models\\{model['name']};
use App\\Http\\Requests\\{model['name']}\\StoreRequest;
use App\\Http\\Requests\\{model['name']}\\UpdateRequest;
use App\\Http\\Resources\\{model['name']}Resource;
use App\\Repositories\\{model['name']}\\{model['name']}RepositoryInterface;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Lang;"""

    def _generate_constructor(self, model):
        model_variable = model['name'].lower()
        return f"""
    protected ${model_variable}Repository;

    public function __construct({model['name']}RepositoryInterface ${model_variable}Repository)
    {{
        $this->{model_variable}Repository = ${model_variable}Repository;
    }}
"""
    def _generate_translations(self, model):
        messages = {
            'index_success': f'{model["name"]} list retrieved successfully.',
            'store_success': f'{model["name"]} created successfully.',
            'show_success': f'{model["name"]} retrieved successfully.',
            'update_success': f'{model["name"]} updated successfully.',
            'destroy_success': f'{model["name"]} deleted successfully.',
            'not_found': f'{model["name"]} not found.'
        }
        return self.translation_generator.generate_translations(messages)

    def _format_translations(self, translations, lang):
        return "<?php\n\nreturn " + str({key: value[lang] for key, value in translations.items()}) + ";\n"

    def _generate_use_statements(self, model):
        return f"""use App\\Http\\Requests\\{model['name']}StoreRequest;
use App\\Http\\Requests\\{model['name']}UpdateRequest;
use App\\Http\\Resources\\{model['name']}Resource;
use App\\Repositories\\{model['name']}RepositoryInterface;
use Illuminate\\Support\\Facades\\Lang;"""

    def _generate_constructor(self, model):
        model_variable = model['name'].lower()
        return f"""
    protected ${model_variable}Repository;

    public function __construct({model['name']}RepositoryInterface ${model_variable}Repository)
    {{
        $this->{model_variable}Repository = ${model_variable}Repository;
    }}
"""

    def _generate_index_method(self, model):
        model_variable = model['name'].lower()
        return f"""{self.swagger_doc_generator.generate_index_doc(model)}
    public function index()
    {{
        ${model_variable}s = $this->{model_variable}Repository->paginate(15);
        return {model['name']}Resource::collection(${model_variable}s)
            ->additional(['message' => Lang::get('{model_variable}.index_success')]);
    }}
"""

    def _generate_store_method(self, model):
        model_variable = model['name'].lower()
        return f"""{self.swagger_doc_generator.generate_store_doc(model)}
    public function store({model['name']}StoreRequest $request)
    {{
        ${model_variable} = $this->{model_variable}Repository->create($request->validated());
        return new {model['name']}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.store_success')]);
    }}
"""

    def _generate_show_method(self, model):
        model_variable = model['name'].lower()
        return f"""{self.swagger_doc_generator.generate_show_doc(model)}
    public function show($id)
    {{
        ${model_variable} = $this->{model_variable}Repository->find($id);
        if (!${model_variable}) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return new {model['name']}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.show_success')]);
    }}
"""

    def _generate_update_method(self, model):
        model_variable = model['name'].lower()
        return f"""{self.swagger_doc_generator.generate_update_doc(model)}
    public function update({model['name']}UpdateRequest $request, $id)
    {{
        ${model_variable} = $this->{model_variable}Repository->update($id, $request->validated());
        if (!${model_variable}) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return new {model['name']}Resource(${model_variable})
            ->additional(['message' => Lang::get('{model_variable}.update_success')]);
    }}
"""

    def _generate_destroy_method(self, model):
        model_variable = model['name'].lower()
        return f"""{self.swagger_doc_generator.generate_destroy_doc(model)}
    public function destroy($id)
    {{
        $result = $this->{model_variable}Repository->delete($id);
        if (!$result) {{
            return response()->json(['message' => Lang::get('{model_variable}.not_found')], 404);
        }}
        return response()->json(['message' => Lang::get('{model_variable}.destroy_success')], 200);
    }}
"""