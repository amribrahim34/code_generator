from typing import Dict, List
from src.core.interfaces.generator import Generator
from src.services.translation_service import TranslationService
from src.services.google_translator import GoogleTranslator


class TranslationGenerator(Generator):
    def __init__(self, translation_service: TranslationService, google_translator: GoogleTranslator):
        # self.config = config
        self.translation_service = translation_service
        self.google_translator = google_translator

    def generate(self, model: dict) -> dict:
        messages = self._generate_messages(model)
        translations = self.translation_service.generate_translations(messages)
        return {
            f"resources/lang/en/{model['name'].lower()}.php": self.format_translations(translations, 'en'),
            f"resources/lang/ar/{model['name'].lower()}.php": self.format_translations(translations, 'ar')
        }

    def get_template(self, template_name: str) -> str:
        # Translations don't use templates, so this method can be a pass
        pass

    def generate_translations(self, model_name: str, fields: List[str]) -> Dict[str, Dict[str, str]]:
        translations = {}
        source_lang = self.google_translator.config.get('source_language', 'en')
        target_langs = self.google_translator.config.get('target_languages', ['ar', 'fr'])

        for lang in target_langs:
            translations[lang] = {}
            for field in fields:
                original_text = f"{model_name}.{field}"
                translated_text = self.google_translator.translate(original_text, source_lang, lang)
                translations[lang][field] = translated_text
                self.translation_service.add_translation(lang, f"{model_name}.{field}", translated_text)

        return translations

    def render_template(self, template: str, context: dict) -> str:
        # Translations don't use templates, so this method can be a pass
        pass

    def _generate_messages(self, model: dict) -> dict:
        return {
            'index_success': f"{model['name']} list retrieved successfully.",
            'store_success': f"{model['name']} created successfully.",
            'show_success': f"{model['name']} retrieved successfully.",
            'update_success': f"{model['name']} updated successfully.",
            'destroy_success': f"{model['name']} deleted successfully.",
            'not_found': f"{model['name']} not found."
        }

    def format_translations(self, translations: Dict[str, Dict[str, str]], language: str) -> str:
        formatted = "<?php\n\nreturn [\n"
        for key, value in translations.get(language, {}).items():
            formatted += f"    '{key}' => '{value}',\n"
        formatted += "];\n"
        return formatted

