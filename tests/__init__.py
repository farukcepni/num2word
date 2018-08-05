from num2word import Num2Word
from num2word.converters import ConverterFactory


class TestBase(object):
    language_code = None
    cases = None

    def setUp(self):
        self.assertIsNotNone(self.language_code, "'language_code' attribute must be set in test classes.")
        self.assertTrue(self.cases, "'cases' attribute must include test cases.")

    def test_to_word(self):
        converter = ConverterFactory.get(self.language_code)

        for number, word in self.cases.iteritems():
            converted = converter(number).convert()
            self.assertEqual(converted, word,
                             "%i must be converted as '%s' but it is '%s'." % (number, word, converted))

    def test_multi(self):
        for number, word in self.cases.iteritems():
            words = Num2Word(number).convert_multi(self.language_code)
            converted = words[self.language_code]
            self.assertEqual(
                word, converted, "%i must be converted as '%s' but it is '%s'." % (number, word, converted))
