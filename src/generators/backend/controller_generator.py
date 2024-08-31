import os

class ControllerGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates' , 'backend','controller_stub.php')

    def generate(self, model):
        controller_content = self._generate_controller(model)
        return {f"app/Http/Controllers/{model['name']}Controller.php": controller_content}

    def _generate_controller(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        model_name = model['name']
        model_variable = model_name.lower()
        
        return template.format(
            class_name=f"{model_name}Controller",
            model_name=model_name,
            model_variable=model_variable,
            use_statements=self._generate_use_statements(model),
            repository_variable=f"{model_variable}Repository",
            constructor=self._generate_constructor(model),
            index_method=self._generate_index_method(model),
            store_method=self._generate_store_method(model),
            show_method=self._generate_show_method(model),
            update_method=self._generate_update_method(model),
            destroy_method=self._generate_destroy_method(model)
        )

    def _generate_use_statements(self, model):
        return f"""use App\\Http\\Requests\\{model['name']}StoreRequest;
use App\\Http\\Requests\\{model['name']}UpdateRequest;
use App\\Http\\Resources\\{model['name']}Resource;
use App\\Repositories\\{model['name']}RepositoryInterface;"""

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
        return f"""
    public function index()
    {{
        ${model_variable}s = $this->{model_variable}Repository->paginate(15);
        return {model['name']}Resource::collection(${model_variable}s);
    }}
"""

    def _generate_store_method(self, model):
        model_variable = model['name'].lower()
        return f"""
    public function store({model['name']}StoreRequest $request)
    {{
        ${model_variable} = $this->{model_variable}Repository->create($request->validated());
        return new {model['name']}Resource(${model_variable});
    }}
"""

    def _generate_show_method(self, model):
        model_variable = model['name'].lower()
        return f"""
    public function show($id)
    {{
        ${model_variable} = $this->{model_variable}Repository->find($id);
        return new {model['name']}Resource(${model_variable});
    }}
"""

    def _generate_update_method(self, model):
        model_variable = model['name'].lower()
        return f"""
    public function update({model['name']}UpdateRequest $request, $id)
    {{
        ${model_variable} = $this->{model_variable}Repository->update($id, $request->validated());
        return new {model['name']}Resource(${model_variable});
    }}
"""

    def _generate_destroy_method(self, model):
        model_variable = model['name'].lower()
        return f"""
    public function destroy($id)
    {{
        $this->{model_variable}Repository->delete($id);
        return response()->json(null, 204);
    }}
"""