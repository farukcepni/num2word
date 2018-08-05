class BaseConverter(object):
    values = {}
    period_values = []

    def __init__(self, number):
        self.number = int(number)
        self.words = []

    def get_number_periods(self, number):
        return '{0:,}'.format(number).split(',')

    def convert(self, delimiter=' '):
        words = self.words or self._convert(self.number)
        return delimiter.join(words)

    def _convert(self, number):
        words = []
        number_str = str(number)

        while (number_str):
            number_int = int(number_str)
            place_value = int(number_str[0]) * 10 ** (len(number_str) - 1)
            periods = self.get_number_periods(number_int)

            if place_value == 0 and number != 0:
                number_str = number_str[1:]
            elif number_int in self.values:
                words.append(self.values[number_int])
                number_str = ''
            elif place_value in self.values:
                words.append(self.values[place_value])
                number_str = number_str[1:]
            else:
                val = len(number_str) <= 3 and number_str[0] or periods[0]

                words += self._convert(val)
                words += [self.period_values[len(periods)]]
                number_str = number_str[len(val):]

        return words
