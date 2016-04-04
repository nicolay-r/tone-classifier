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
    def normalize_tone(tone, k):
        if (tone >= 0):
            return 1.0 - exp(-abs(tone/k))
        else:
            return - (1.0 - exp(-abs(tone/k)))

    @staticmethod
    def lexicon_feature(lex, terms, lexicon_settings):
        terms_used = lexicon_settings['terms_used']

        tones = []
        if (terms_used == 'all'):
            tones = [lex.get_tone(term) for term in terms]
        elif (terms_used == 'hashtags_only'):
            tones = [lex.get_tone(term) for term in terms if len(term) > 0
                and term[0] == '#']

        if (len(tones) == 0):
            tones.append(0)

        if ('function' in lexicon_settings):
            func = lexicon_settings['function']
        else:
            func = 'sum'
        if (func == 'sum'):
            value = sum(tones)
        elif (func == 'max'):
            value = max(tones)
        elif (func == 'min'):
            value = min(tones)

        return lex.get_name(), Features.normalize_tone(value, 10)

    @staticmethod
    def pm_prefix_sum(terms):
        tone = 0
        for term in terms:
            if len(term) > 0:
                if term[0] == '+':
                    tone += 1
                elif term[0] == '-':
                    tone -= 1
        return tone

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

        for char in chars:
            total += unicode_message.count(char)

        return total

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
            name, value = Features.lexicon_feature(lex['lexicon'], terms,
                lex['settings'])
            features[name] = value

        # plus_minus prefix sum
        if self.pm_prefix_used is True:
            features[self.pm_prefix_sum_settings['name']] = Features.pm_prefix_sum(terms)

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
                self.lexicons.append( {
                        'lexicon' : Lexicon(
                            lexicon_settings['lexicon_configpath'],
                            lexicon_settings['table'], lexicon_settings['name'],
                            lexicon_settings['term_column_name'],
                            lexicon_settings['value_column_name']),
                        'settings' : lexicon_settings
                    }
                );
                print "use lexicon: ", lexicon_settings['name']

        self.pm_prefix_sum_settings = settings['pm_prefix_sum']
        self.pm_prefix_used = Features.str2bool(
            self.pm_prefix_sum_settings['enabled'])

        self.smiles_settings = settings['smiles']

        self.signs_settings = settings['signs']
        self.use_signs = Features.str2bool(self.signs_settings['enabled'])

        self.uppercase_words_settings = settings['uppercase_words']
        self.use_uppercase_words = Features.str2bool(
            self.uppercase_words_settings['enabled'])
