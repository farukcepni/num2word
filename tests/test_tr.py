# -*- coding: utf-8 -*-
import unittest

from tests import TestBase


class Test(TestBase, unittest.TestCase):
    language_code = 'tr'
    cases = {
        0: 'sıfır',
        1: 'bir',
        2: 'iki',
        3: 'üç',
        10: 'on',
        11: 'on bir',
        12: 'on iki',
        15: 'on beş',
        19: 'on dokuz',
        20: 'yirmi',
        21: 'yirmi bir',
        22: 'yirmi iki',
        30: 'otuz',
        50: 'elli',
        60: 'altmış',
        99: 'doksan dokuz',
        100: 'yüz',
        101: 'yüz bir',
        110: 'yüz on',
        150: 'yüz elli',
        199: 'yüz doksan dokuz',
        200: 'iki yüz',
        201: 'iki yüz bir',
        210: 'iki yüz on',
        225: 'iki yüz yirmi beş',
        290: 'iki yüz doksan',
        300: 'üç yüz',
        305: 'üç yüz beş',
        310: 'üç yüz on',
        1000: 'bin',
        2000: 'iki bin',
        2001: 'iki bin bir',
        2010: 'iki bin on',
        2100: 'iki bin yüz',
        2101: 'iki bin yüz bir',
        2500: 'iki bin beş yüz',
        3000: 'üç bin',
        10000: 'on bin',
        10001: 'on bin bir',
        10010: 'on bin on',
        10100: 'on bin yüz',
        10101: 'on bin yüz bir',
        10999: 'on bin dokuz yüz doksan dokuz',
        11000: 'on bir bin',
        19999: 'on dokuz bin dokuz yüz doksan dokuz',
        20000: 'yirmi bin',
        20001: 'yirmi bin bir',
        50000: 'elli bin',
        99999: 'doksan dokuz bin dokuz yüz doksan dokuz',
        100000: 'yüz bin',
        100001: 'yüz bin bir',
        999999: 'dokuz yüz doksan dokuz bin dokuz yüz doksan dokuz',
        1000000: 'bir milyon',
        1000001: 'bir milyon bir',
    }