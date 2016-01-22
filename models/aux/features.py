#!/usr/bin/python

import io
import json
from lexicon import Lexicon
from math import exp

class Features:

    @staticmethod
    def to_unicode(s):
        if isinstance(s, str):
            return unicode(s, 'utf-8')
        elif isinstance(s, unicode):
            return s

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

    @staticmethod
    def smiles_feature(unicode_message, unicode_smiles):
        total = 0
        for smile in unicode_smiles:
            total += unicode_message.count(smile)
            unicode_message.replace(smile, '')

        if total > 0:
            total = 1
        return total

    @staticmethod
    def signs_feature(unicode_message, chars):
        total = 0
        max_sequence = 0
        for char in unicode_message:
            if char in chars:
                total += 1
            else:
                max_sequence = max(max_sequence, total)
                total = 0

        return max_sequence

    @staticmethod
    def uppercase_words(unicode_message):
        total = 0
        for word in unicode_message.split(' '):
            if len(word) > 0 and word.upper() == word:
                total += 1

        return total

    def create(self, terms, message = None):
        features = {}

        # lexicon
        for lex in self.lexicons:
            name, value = Features.lexicon_feature(lex, terms)
            features[name] = value

        if (message is not None):
            unicode_message = Features.to_unicode(message)

            # smiles
            if Features.str2bool(self.smiles_settings['enabled']):
                positive = Features.smiles_feature(unicode_message,
                    self.smiles_settings['positive_values'])
                negative = -Features.smiles_feature(unicode_message,
                    self.smiles_settings['negative_values'])

                score = 0
                if (positive != 0 and negative != 0):
                    score = 0
                elif positive != 0:
                    score = positive
                elif negative != 0:
                    score = negative

                features[self.smiles_settings['name']] = score

            # signs
            if self.use_signs is True:
                features[self.signs_settings['name']] = Features.signs_feature(
                unicode_message, self.signs_settings['chars'])

            # uppercase words
            if self.use_uppercase_words is True:
                features[self.signs_settings['name']] = Features.uppercase_words(
                    unicode_message)

        return features

    @staticmethod
    def str2bool(value):
        return value.lower() in ('true')

    def __init__(self, configpath):

        # read config file
        with io.open(configpath, 'r') as f:
            settings = json.load(f, encoding='utf-8')

        self.lexicons = []
        for lexicon_settings in settings['lexicons']:
            if (Features.str2bool(lexicon_settings['enabled']) == True):
                self.lexicons.append(Lexicon(
                    lexicon_settings['lexicon_configpath'],
                    lexicon_settings['table'], lexicon_settings['name'],
                    lexicon_settings['term_column_name'],
                    lexicon_settings['value_column_name']));
                print "use lexicon: ", lexicon_settings['name']

        self.smiles_settings = settings['smiles']

        self.signs_settings = settings['signs']
        self.use_signs = Features.str2bool(self.signs_settings['enabled'])

        self.uppercase_words_settings = settings['uppercase_words']
        self.use_uppercase_words = Features.str2bool(
            self.uppercase_words_settings['enabled'])
