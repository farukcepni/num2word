import unittest

from tests import TestBase


class Test(TestBase, unittest.TestCase):
    language_code = 'en'
    cases = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        15: 'fifteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one'
    }
