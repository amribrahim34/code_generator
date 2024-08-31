from .google_translator import GoogleTranslator

class TranslationService:
    def __init__(self, translator: GoogleTranslator):
        self.translator = translator

    def generate_translations(self, messages: dict) -> dict:
        translations = {}
        for key, value in messages.items():
            translations[key] = {
                'en': value,
                'ar': self.translator.translate(value, 'en', 'ar')
            }
        return translations