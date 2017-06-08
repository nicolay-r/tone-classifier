# -*- coding: utf-8 -*-

"""
File contains necessary utils for module
"""

from math import exp


def normalize(value, k=6):
    if (value >= 0):
        return 1.0 - exp(-abs(value/k))
    else:
        return - (1.0 - exp(-abs(value/k)))


def to_unicode(s):
    if isinstance(s, str):
        return unicode(s, 'utf-8')
    elif isinstance(s, unicode):
        return s
