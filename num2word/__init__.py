from .converters import ConverterFactory


class Num2Word(object):
    def __init__(self, number):
        self.number = number

    def convert(self, language_code):
        converter = ConverterFactory.get(language_code)
        return converter(self.number).convert()

    def convert_multi(self, *language_codes):
        return dict(
            (language_code, self.convert(language_code)) for language_code in language_codes
        )
