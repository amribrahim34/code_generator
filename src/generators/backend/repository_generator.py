import os

class RepositoryGenerator:
    def __init__(self):
        self.template_path = os.path.join('src', 'templates','backend', 'repository_stub.php')

    def generate(self, model):
        repository_content = self._generate_repository(model)
        return {f"app/Repositories/{model['name']}Repository.php": repository_content}

    def _generate_repository(self, model):
        with open(self.template_path, 'r') as file:
            template = file.read()

        class_name = f"{model['name']}Repository"
        interface_name = f"{model['name']}RepositoryInterface"
        model_name = model['name']
        
        return template.format(
            class_name=class_name,
            interface_name=interface_name,
            model_name=model_name
        )