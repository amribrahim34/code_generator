import os

class RepositoryInterfaceGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates', 'backend','repository_interface_stub.php')

    def generate(self, model):
        interface_content = self._generate_interface(model)
        return {f"app/Repositories/{model['name']}RepositoryInterface.php": interface_content}

    def _generate_interface(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        interface_name = f"{model['name']}RepositoryInterface"
        model_name = model['name']
        
        return template.format(
            interface_name=interface_name,
            model_name=model_name
        )