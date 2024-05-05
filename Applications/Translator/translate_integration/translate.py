from googletrans import Translator
from langdetect import detect


class Translator:
    translator = Translator() # translator

    @classmethod
    def translate_text(cls, text: str, source: str, dest: str) -> str:
        try:
            return cls.translator.translate(text, src=source, dest=dest).text
        except Exception as e:
            print(e)
            return ""
        
        # return translated text
    
    @classmethod
    def detect_language(cls, text: str) -> str:
        return detect(text) # return detected language