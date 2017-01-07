#!/usr/bin/python

import io
import json
import utils
import configs
from lexicon import LexiconFeature
from clustered_words import BagOfClustersFeature


class Features:
    FEATURE_SMILES = '$smiles'
    FEATURE_SIGNS = '$signs'
    FEATURE_PREFIX_SUM = '$prefix_sum'
    FEATURE_UPPERCASE_WORDS = '$uppercase_words'

    SETTINGS_LEXICONS = 'lexicons'
    SETTINGS_CLUSTERED_WORDS = 'clustered_words'

    def __init__(self, connection, message_parser, configpath):
        """
        Arguments
        ---------
            connection     -- PostgreSLQ connection for database which contains
                              lexicon table
            message_parser -- parser from msg.py
            configpath     -- configuration file for features
        """

        with io.open(configpath, 'r') as f:
            self.settings = json.load(f, encoding='utf-8')

        self.message_parser = message_parser

        self.cluster_groups = []
        cluster_groups = self.settings[Features.SETTINGS_CLUSTERED_WORDS]
        for cluster_group_name in cluster_groups.iterkeys():
            self.cluster_groups.append(
                BagOfClustersFeature(cluster_group_name,
                                     configs.DATA_ROOT,
                                     cluster_groups[cluster_group_name]))

        self.lexicons = []
        lexicons = self.settings[Features.SETTINGS_LEXICONS]
        for lexicon_name in lexicons.iterkeys():
            self.lexicons.append(
                LexiconFeature(connection,
                               lexicon_name,
                               lexicons[lexicon_name],
                               self.cluster_groups))

    def vectorize(self, text):
        """
        Produce vector of features

        Returns
        -------
            features -- dictionary {feature_name: value, ...}
        """
        features = {}

        self.message_parser.parse(text)
        clean_terms = self.message_parser.get_terms()
        prefixed_terms = self.message_parser.get_terms(
                            apply_bigram_processor=True)

        for lexicon in self.lexicons:
            features.update(lexicon.vectorize(prefixed_terms))

        for cluster_group in self.cluster_groups:
            features.update(cluster_group.vectorize(clean_terms))

        if self.FEATURE_PREFIX_SUM in self.settings:
            features[self.FEATURE_PREFIX_SUM] = \
                Features.__prefix_sum(prefixed_terms)

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
