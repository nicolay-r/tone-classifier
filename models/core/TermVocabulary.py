# -*- coding: utf-8 -*-

import operator
import json
import io

from utils import to_unicode


class TermVocabulary:
    ALL = 'all'

    def __init__(self):
        self.term_index = {}
        self.term_in_voc_count = {}
        self.current_index = 0

    def contains(self, term):
        return to_unicode(term) in self.term_index

    def get_terms(self):
        return self.term_index.keys()

    def get_term_index(self, term):
        uterm = to_unicode(term)
        return self.term_index[uterm]

    def get_term_in_voc_count(self, term, sentiment=None):
        """
        term : string
        sentiment: '-1', '0', '1'
            Describes the sentiment class
        """
        uterm = to_unicode(term)
        term_counters = self.term_in_voc_count[self.get_term_index(uterm)]
        return term_counters[sentiment] if sentiment is not None \
            else term_counters[self.ALL]

    def top(self, n):
        r = sorted(self.term_in_voc_count.items(),
                   key=operator.itemgetter(1))[::-1]
        print "top %d:" % (n)
        for i in range(min(len(self.term_in_voc_count), n)):
            for w, index in self.term_index.iteritems():
                if (index == r[i][0]):
                    print w, ', ',

    def get_indexes(self, terms):
        """
        returns : int[]
            list of indexes for terms
        """
        return [self.get_term_index(term) for term in terms]

    def insert_term(self, term, sentiment=None):
        """
        term : string
        sentiment : '-1', '0', '1'
            describes the term sentiment class
        returns : int
            index of inserted or existed term
        """
        uterm = to_unicode(term)

        if uterm not in self.term_index:
            self.__insert_new_term(uterm, sentiment)
        else:
            self.__insert_existed_term(self.get_term_index(uterm), sentiment)

        return self.get_term_index(uterm)

    def __insert_new_term(self, uterm, sentiment=None):
        term_index = self.__get_new_index()
        self.term_index[uterm] = term_index
        self.term_in_voc_count[term_index] = {self.ALL: 0}
        self.__insert_existed_term(term_index, sentiment)

    def __insert_existed_term(self, term_index, sentiment=None):
        terms_count = self.term_in_voc_count
        terms_count[term_index][self.ALL] += 1
        if sentiment is not None:
            if sentiment in terms_count[term_index]:
                terms_count[term_index][sentiment] += 1
            else:
                terms_count[term_index][sentiment] = 1

    def __get_new_index(self):
        self.current_index += 1
        return self.current_index

    def insert_terms(self, terms, sentiment=None):
        for term in terms:
            self.insert_term(term, sentiment)

    def save(self, filepath):
        with io.open(filepath, 'w', encoding='utf-8') as out:
            data = json.dumps({
                              'term_index': self.term_index,
                              'current_index': self.current_index,
                              'term_in_voc_count': self.term_in_voc_count
                              }, ensure_ascii=False, encoding='utf8')
            out.write(unicode(data))

    @staticmethod
    def load(filepath):
        v = TermVocabulary()
        with io.open(filepath, 'r', encoding='utf-8') as f:
            voc = json.load(f, encoding='utf8')
        v.term_index = voc['term_index']
        v.current_index = voc['current_index']
        v.term_in_voc_count = voc['term_in_voc_count']
        return v
