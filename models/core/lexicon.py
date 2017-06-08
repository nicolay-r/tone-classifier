#!/usr/bin/python

import utils
import logging
import pandas as pd
import os.path


class LexiconFeature:
    PARAM_TABLE_FILEPATH = 'table'
    PARAM_TERM_COLUMN_NAME = 'term_column_name'
    PARAM_VAL_COLUMN_NAME = 'value_column_name'
    PARAM_MULTIPLIER = 'multiplier'
    PARAM_APPLY_FOR_TERMS = 'terms_used'
    PARAM_FUNCTIONS = 'functions'
    PARAM_ENABLED = "enabled"

    def __init__(self, data_folder, unique_name, parameters,
                 bag_of_clusters_features):
        """
        Arguments
        ---------
            data_folder: str
                Root data folder path
            keyword_name : str
                Unique lexicon name
            parameters : dict
                Lexicon parameters, presented by dictionary with PARAM_* keys
            bag_of_clusters_features : list
                List of features (for sum calculation)
        """

        self.cache = {}

        self.parameters = parameters
        self.unique_name = unique_name
        self.table_filepath = os.path.join(
            data_folder,
            parameters[LexiconFeature.PARAM_TABLE_FILEPATH])

        self.term_column_name = parameters[
                LexiconFeature.PARAM_TERM_COLUMN_NAME]
        self.value_column_name = parameters[
                LexiconFeature.PARAM_VAL_COLUMN_NAME]
        self.multiplier = parameters[LexiconFeature.PARAM_MULTIPLIER]
        self.terms_used = parameters[LexiconFeature.PARAM_APPLY_FOR_TERMS]
        self.functions = parameters[LexiconFeature.PARAM_FUNCTIONS]
        self.bag_of_clusters_features = bag_of_clusters_features

        if parameters[LexiconFeature.PARAM_ENABLED] != 'false':
            self.get_all_tones_from_table()

    def vectorize(self, terms):
        """
        Produce features vector, based on lexicon functions for 'terms'

        Returns
        -------
            features -- {feature: value, ...}
        """
        features = {}

        if self.parameters[LexiconFeature.PARAM_ENABLED] == 'false':
            return features

        tones = []
        if (self.terms_used == 'all'):
            tones = [self.get_tone(term) for term in terms]
        elif (self.used_terms == 'hashtags_only'):
            tones = [self.get_tone(term) for term in terms
                     if len(term) > 0 and term[0] == '#']

        if (len(tones) == 0):
            tones.append(0)

        for function_name in self.functions:
            if (function_name == 'sum'):
                value = (sum(tones))
            elif (function_name == 'max'):
                value = max(tones)
            elif (function_name == 'min'):
                value = min(tones)
            else:
                raise ValueError(
                        "unexpected function: '{}'".format(function_name))

            feature_name = "{}_{}".format(self.get_name(), function_name)
            features[feature_name] = utils.normalize(value)

        #
        # Calculate sum of cluster scores
        #
        # for cluster in self.bag_of_clusters_features:
        #     cluster_tones = [self.get_cluster_tone(
        #                      cluster, cluster.get_cluster_id(word))
        #                      for word in terms if cluster.contains_word(word)]
        #     if len(cluster_tones) == 0:
        #         cluster_tones.append(0)

        #     feature_name = "{}_score_sum".format(cluster.get_name())
        #     value = sum(cluster_tones)
        #     features[feature_name] = utils.normalize(value)

        return features

    def get_name(self):
        return self.unique_name

    def get_all_tones_from_table(self):
        logging.info("Loading lexicon '%s': %s ..." % (self.unique_name,
                                                       self.table_filepath))

        df = pd.read_csv(self.table_filepath, sep=',')

        for row in df.index:
            name = df[self.term_column_name][row]
            value = df[self.value_column_name][row]
            self.cache[utils.to_unicode(name)] = float(value)

    def get_cluster_tone(self, cluster, cluster_id):
        tone = 0
        for term in cluster.get_words(cluster_id):
            tone += self.get_tone(term)

        return tone

    def get_tone(self, term):
        tone = 0

        invert_tone = False
        positive_tone = False

        if (term[0] == '-'):
            term = term[1:]
            invert_tone = True
        elif (term[0] == '+'):
            term = term[1:]
            positive_tone = True

        if (term in self.cache):
            tone = self.cache[term]

        # Invert term tonality in case of negative mark '-' and '+'
        if (invert_tone):
            tone *= -self.multiplier
        if (positive_tone):
            tone *= self.multiplier

        return tone
