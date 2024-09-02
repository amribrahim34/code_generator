from typing import Dict, Any, Optional

class TranslationService:
    def __init__(self):
        self.translations: Dict[str, Dict[str, str]] = {}
        self.default_language = 'en'

    def add_translation(self, language: str, key: str, value: str):
        """Add a translation for a specific language and key."""
        if language not in self.translations:
            self.translations[language] = {}
        self.translations[language][key] = value

    def get_translation(self, key: str, language: str, params: Optional[Dict[str, Any]] = None) -> str:
        """
        Get a translation for a specific key and language.
        If the translation is not found, it falls back to the default language.
        If still not found, it returns the key itself.
        """
        if language in self.translations and key in self.translations[language]:
            translation = self.translations[language][key]
        elif self.default_language in self.translations and key in self.translations[self.default_language]:
            translation = self.translations[self.default_language][key]
        else:
            return key

        if params:
            return translation.format(**params)
        return translation

    def set_default_language(self, language: str):
        """Set the default language for fallback translations."""
        self.default_language = language

    def load_translations(self, translations: Dict[str, Dict[str, str]]):
        """Load multiple translations at once."""
        for language, trans in translations.items():
            for key, value in trans.items():
                self.add_translation(language, key, value)

    def get_all_translations(self, language: str) -> Dict[str, str]:
        """Get all translations for a specific language."""
        return self.translations.get(language, {})

    def remove_translation(self, language: str, key: str):
        """Remove a specific translation."""
        if language in self.translations and key in self.translations[language]:
            del self.translations[language][key]

    def clear_translations(self):
        """Clear all translations."""
        self.translations.clear()