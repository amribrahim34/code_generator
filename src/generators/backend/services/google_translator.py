from googletrans import Translator

class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        return self.translator.translate(text, src=source_lang, dest=target_lang).text