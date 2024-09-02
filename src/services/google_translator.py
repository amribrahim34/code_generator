# File: src/generators/backend/google_translator.py

from googletrans import Translator
from src.core.interfaces.generator import Generator
from typing import Dict, Any

class GoogleTranslator(Generator):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.translator = Translator()

    def generate(self, model: Dict[str, Any]) -> Dict[str, str]:
        """
        Generates translations for the given model using Google Translate.

        Args:
            model (Dict[str, Any]): The model containing fields to be translated.

        Returns:
            Dict[str, str]: A dictionary of translated texts.
        """
        translations = {}
        source_lang = self.config.get('source_language', 'en')
        target_lang = self.config.get('target_language', 'es')

        for field_name, field_value in model.items():
            if isinstance(field_value, str):
                translations[field_name] = self.translate(field_value, source_lang, target_lang)

        return translations

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Translates the given text from source language to target language.

        Args:
            text (str): The text to be translated.
            source_lang (str): The source language code.
            target_lang (str): The target language code.

        Returns:
            str: The translated text.
        """
        return self.translator.translate(text, src=source_lang, dest=target_lang).text

    def get_template(self, template_name: str) -> str:
        # This method is not applicable for GoogleTranslator
        raise NotImplementedError("get_template is not implemented for GoogleTranslator")

    def render_template(self, template: str, context: Dict[str, Any]) -> str:
        # This method is not applicable for GoogleTranslator
        raise NotImplementedError("render_template is not implemented for GoogleTranslator")