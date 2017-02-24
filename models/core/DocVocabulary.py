# -*- coding: utf-8 -*-

from utils import to_unicode


class DocVocabulary:

    ALL = 'all'

    def __init__(self):
        self.terms_info = {}
        self.docs_count = {self.ALL: 0}

    def get_docs_count(self, sentiment=None):
        """
        returns : int
            amount of documents at all or in the certain 'sentiment' class
        """
        return self.docs_count[self.ALL] if sentiment is None \
            else self.docs_count[sentiment]

    def get_term_in_docs_count(self, term, sentiment=None):
        """
        term : str
        sentiment : None or '-1', '0', '1'
            sentiment class name
        returns : int
            amount of 'term' appeared in all documents or in a documents of
            the certain 'sentiment' class
        """
        uterm = to_unicode(term)
        term_info = self.terms_info[uterm]
        return term_info[self.ALL] if sentiment is None \
            else self.__get_term_info(sentiment)

    def __get_term_info(self, sentiment):
        return self.terms_info[sentiment] if sentiment in self.terms_info \
            else 0

    def add_doc(self, terms, sentiment=None):
        """
        terms : str[]
            List of terms which represents the document
        sentiment : '-1', '0', '1'
            Sentiment class of the document
        """
        used = []

        self.docs_count[self.ALL] += 1
        if sentiment not in self.docs_count:
            self.docs_count[sentiment] = 0
        self.docs_count[sentiment] += 1

        for term in terms:
            uterm = to_unicode(term)
            if not(uterm in used):
                self.__add_term(uterm, sentiment)
                used.append(uterm)

    def __add_term(self, uterm, sentiment):
        if uterm not in self.terms_info:
            self.terms_info[uterm] = {self.ALL: 0}
        term_info = self.terms_info[uterm]
        term_info[self.ALL] += 1
        if sentiment not in term_info:
            term_info[sentiment] = 0
        term_info[sentiment] + 1

    def get_terms_info(self, term):
        """
        returns: dict
            amount of documents which includes 'term' for different sentiment
            classes and at all (DocVocabulary.ALL)
        """
        uterm = to_unicode(term)
        return self.terms_info[uterm]

    def get_terms_info_safe(self, term):
        """
        returns : dict or 0
            amount of documents which includes 'term' for different sentiment
            classes and at all (DocVocabulary.ALL)
        """
        uterm = to_unicode(term)
        if (uterm in self.terms_info):
            return self.get_terms_info(uterm)
        else:
            return None
