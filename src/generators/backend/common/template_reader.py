class TemplateReader:
    @staticmethod
    def read_template(template_path: str) -> str:
        with open(template_path, 'r') as file:
            return file.read()