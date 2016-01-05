#!/usr/bin/python

import json
from lexicon import Lexicon
from math import exp

class Features:

    @staticmethod
    def normalize_tone_sum(tone, k):
        if (tone >= 0):
            return 1.0 - exp(-abs(tone/k))
        else:
            return - (1.0 - exp(-abs(tone/k)))

    @staticmethod
    def lexicon_feature(lex, terms):
        value = sum([lex.get_tone(term) for term in terms])
        return lex.get_name(), Features.normalize_tone_sum(value, 10)

    def create(self, terms):
        features = {}

        for lex in self.lexicons:
            name, value = Features.lexicon_feature(lex, terms)
            features[name] = value

        return features

    def __init__(self, configpath):

        # read config file
        with open(configpath, 'r') as f:
            self.settings = json.load(f, encoding='utf-8')

        self.lexicons = []
        for lexicon_settings in self.settings['lexicons']:
            self.lexicons.append(Lexicon(lexicon_settings['lexicon_configpath'],
                lexicon_settings['table'], lexicon_settings['name'],
                lexicon_settings['term_column_name'],
                lexicon_settings['value_column_name']));
