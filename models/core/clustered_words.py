# -*- coding: utf-8 -*-

import io
import json
import os.path

import utils


class BagOfClustersFeature:

    PARAM_CLUSTERED_WORDS_FILEPATH = 'clustered_words_filepath'
    PARAM_ENABLED = "enabled"

    def __init__(self, unique_name, base_filepath, parameters):
        """
        Arguments
        ---------
            keyword_name -- feature unique name
            base_filepath -- filepath of feature config
            parameters -- lexicon parameters, presented by dictionary
        """
        self.unique_name = unique_name
        self.parameters = parameters

        filepath = os.path.join(
            base_filepath,
            parameters[BagOfClustersFeature.PARAM_CLUSTERED_WORDS_FILEPATH])

        print "Loading file with clusters of words: {}".format(filepath)
        with io.open(filepath, 'r', encoding='utf-8') as f:
            self.clustered_words = json.load(f, encoding='utf-8')

        print "Create dictionary with all clusters, accessed by cluster_id ..."
        self.clusters = {}
        for word in self.clustered_words.iterkeys():
            cluster_id = self.clustered_words[word]
            if cluster_id not in self.clusters:
                self.clusters[cluster_id] = []
            self.clusters[cluster_id].append(utils.to_unicode(word))

    def vectorize(self, terms):
        """
        Produce features vector, bag of clusters for 'terms'

        Returns
        -------
            features -- {feature: value, ...}
        """
        features = {}

        if self.parameters[BagOfClustersFeature.PARAM_ENABLED] == 'false':
            return features

        for term in terms:
            if term in self.clustered_words:
                feature_name = self.__get_feature_name(
                    int(self.clustered_words[term]))
                if feature_name in features:
                    features[feature_name] += 1
                else:
                    features[feature_name] = 1

        return features

    def get_name(self):
        return self.unique_name

    def contains_word(self, word):
        return word in self.clustered_words

    def get_cluster_id(self, word):
        """
        Returns
        -------
           Returns id of cluster, which is contain the 'word'
        """
        return self.clustered_words[utils.to_unicode(word)]

    def get_words(self, cluster_id):
        """
        Returns
        -------
            List of words, presented in cluster with 'cluster_id'
        """
        return self.clusters[cluster_id]

    def __get_feature_name(self, cluster_index):
        return '{name}_{cluster}'.format(name=self.unique_name,
                                         cluster=cluster_index)
