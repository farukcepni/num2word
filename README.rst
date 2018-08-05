Num2Word
====
convert numbers to word representation (eg: 109 -> one hundred nine)


Usage
----
>>> from num2word import Num2Word
>>> Num2Word(23).convert('en')
'twenty three'


>>> Num2Word(12).convert('tr')
'on iki'

>>> Num2Word(1000000).convert('en')
'one million'

>>> # convert to multiple languages 
>>> Num2Word(12).convert_multi('tr', 'en')
{'en': 'twelve', 'tr': 'on iki'}

>>> # use converter directly.
>>> from num2word.converters.lang_EN import Converter
>>> Converter(123).convert()
'one hundred twenty three'


To run tests
-----
**To run all tests**

>>> python -m unittest discover -v tests

**To run test for only one language**

>>> python -m unittest -v tests.test_en

**Check Coverage**

>>> coverage run -m unittest discover -v tests
>>> coverage report -m

**Check pep8 validation**

>>> pycodestyle .

