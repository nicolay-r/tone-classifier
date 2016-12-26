#!/usr/bin/python

import io
import json
import utils
from lexicon import LexiconFeature


class Features:
    FEATURE_SMILES = '$smiles'
    FEATURE_SIGNS = '$signs'
    FEATURE_PREFIX_SUM = '$prefix_sum'
    FEATURE_UPPERCASE_WORDS = '$uppercase_words'

    def __init__(self, connection, configpath):
        """
        Arguments
        ---------
            connection -- PostgreSLQ connection for database which contains
                          lexicon table
            configpath -- configuration file for features
        """

        with io.open(configpath, 'r') as f:
            self.settings = json.load(f, encoding='utf-8')

        self.lexicons = []
        lexicons = self.settings['lexicons']
        for lexicon_name in lexicons.iterkeys():
            self.lexicons.append(
                LexiconFeature(connection,
                               lexicon_name,
                               lexicons[lexicon_name]))

    def vectorize(self, terms, text=None):
        """
        Produce vector of features

        Returns
        -------
            features -- dictionary {feature_name: value, ...}
        """
        features = {}

        for lexicon in self.lexicons:
            features.update(lexicon.vectorize(terms))

        if self.FEATURE_PREFIX_SUM in self.settings:
            features[self.FEATURE_PREFIX_SUM] = Features.__prefix_sum(terms)

        if (text is not None):
            text = utils.to_unicode(text)
        else:
            return features

        if self.FEATURE_SIGNS in self.settings:
            features[self.FEATURE_SIGNS] = Features.__signs(
                text, self.settings[self.FEATURE_SIGNS]['chars'])

        if self.FEATURE_UPPERCASE_WORDS is True:
            features[self.FEATURE_UPPERCASE_WORDS] = \
                Features.__uppercase_words(text)

        return features

    @staticmethod
    def __prefix_sum(terms):
        """
        Prefix fum
        """
        tone = 0
        for term in terms:
            if len(term) > 0:
                if term[0] == '+':
                    tone += 1
                elif term[0] == '-':
                    tone -= 1
        return tone

    @staticmethod
    def __signs(text, chars):
        """
        Signs feature
        """
        total = 0

        for char in chars:
            total += text.count(char)

        return utils.normalize(total)

    @staticmethod
    def __uppercase_words(text):
        """
        Uppercase words feature
        """
        total = 0
        for word in text.split(' '):
            if len(word) > 0 and word.upper() == word:
                total += 1

        return utils.normalize(total)
