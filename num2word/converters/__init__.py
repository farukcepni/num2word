import importlib
import os


def import_by_string(path):
    """return class or function using string path."""
    module_name, callback = path.rsplit('.', 1)
    _module = importlib.import_module(module_name)
    return getattr(_module, callback)


class ConverterFactory(object):
    @classmethod
    def get(cls, language_code):
        class_path = 'num2word.converters.lang_%s.Converter' % language_code.upper()
        return import_by_string(class_path)
