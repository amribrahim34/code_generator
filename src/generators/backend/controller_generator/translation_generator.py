from ..services.translation_service import TranslationService

class TranslationGenerator:
    def __init__(self, translation_service: TranslationService):
        self.translation_service = translation_service

    def generate_translations(self, messages: dict) -> dict:
        return self.translation_service.generate_translations(messages)

    def format_translations(self, translations: dict, lang: str) -> str:
        formatted = [f"    '{key}' => '{value[lang]}'" for key, value in translations.items()]
        return "<?php\n\nreturn [\n" + ",\n".join(formatted) + "\n];\n"