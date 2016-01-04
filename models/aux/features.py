#!/usr/bin/python

import json
from lexicon import Lexicon

class Features:

    @staticmethod
    def lexicon_feature(lex, terms):
        value = sum([lex.get_tone(term) for term in terms])
        return lex.get_name(), value

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
