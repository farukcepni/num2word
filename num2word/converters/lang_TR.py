# -*- coding: utf-8 -*-

from .base import BaseConverter


class Converter(BaseConverter):
    """convert number to word in Turkish"""
    LANG_CODE = 'tr'

    values = {
        0: 'sıfır',
        1: 'bir',
        2: 'iki',
        3: 'üç',
        4: 'dört',
        5: 'beş',
        6: 'altı',
        7: 'yedi',
        8: 'sekiz',
        9: 'dokuz',
        10: 'on',
        20: 'yirmi',
        30: 'otuz',
        40: 'kırk',
        50: 'elli',
        60: 'altmış',
        70: 'yetmiş',
        80: 'seksen',
        90: 'doksan',
        100: 'yüz',
        1000: 'bin'
    }

    period_values = [
        'on',
        'yüz',
        'bin',
        'milyon',
        'milyar',
        'trilyon',
        'katrilyon',
        'kentilyon',
        'sekstilyon',
        'septilyon',
        'oktilyon',
        'nonilyon',
        'desilyon',
        'andesilyon'  # 10^36
    ]
