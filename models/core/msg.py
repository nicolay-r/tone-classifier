# -*- coding: utf-8 -*-

import io
import json
import pymystem3
from nltk.tokenize import TweetTokenizer


class TwitterMessageParser:
    INCLUDE_URLS = 'urls_used'
    INCLUDE_HTAGS = 'ht_used'
    INCLUDE_USERS = 'users_used'
    REMOVE_STOP_WORDS = 'use_stop_words'
    TONE_PREFIXES = 'tone_prefix'
    ABSOLUTE_STOP_WORDS = 'abs_stop_words'
    GARBAGE_CHARS = 'garbage_chars'

    def __init__(self, configpath, task_type='none'):
        """
        Arguments
        ---------
            mystem
            configpath
            task_type
        """
        self.mystem = pymystem3.Mystem(entire_input=False)

        # Read config file
        with io.open(configpath, "r") as f:
            self.settings = json.load(f, encoding='utf-8')

        if (task_type != 'none'):
            key = task_type + '_stop_words'
            self.task_specific_stop_words = self.settings[key]
        else:
            self.task_specific_stop_words = []

    def parse(self, text):

        # Tokenize message
        tokenizer = TweetTokenizer()
        words = tokenizer.tokenize(text)

        retweet_term = 'RT'

        urls = []
        users = []
        hash_tags = []
        for word in words:
            if (word[0] == '@'):
                # user in Twitter
                users.append(word)
            elif (word[0] == '#'):
                # hash tags
                hash_tags.append(word)
            elif (word.find('http:') == 0 or word.find('https:') == 0):
                # url
                urls.append(word)

        for f in urls + users + hash_tags + [retweet_term]:
            if f in words:
                words.remove(f)

        self.words = words
        self.urls = urls
        self.users = users
        self.hash_tags = hash_tags

    def get_terms(self, lemmatize=True, apply_bigram_processor=False):
        """
        Get terms of twitter message

        Returns
        -------
            terms     -- list of twitter words of natural language (with or
                         without applying lemmatizer) and other metainformation
                         (such as URL, hashtags, etc.)
            lemmatize -- apply Mystem lemmatizer or not
            apply_bigram_processor -- convert unigrams or bigrams with tone
                                      prefixes '+' or '-'
        """
        terms = [w.strip() for w in
                 self.mystem.lemmatize(' '.join(self.words)) if
                 not(w in ['\n', ' ', '\t', '\r'])]

        terms = self.__transform(terms, apply_bigram_processor)

        if self.__str2bool(self.settings[TwitterMessageParser.INCLUDE_URLS]):
            terms += self.urls
        if self.__str2bool(self.settings[TwitterMessageParser.INCLUDE_HTAGS]):
            terms += self.hash_tags
        if self.__str2bool(self.settings[TwitterMessageParser.INCLUDE_USERS]):
            terms += self.users

        return terms

    def __transform(self, terms, apply_bigram_processor):
        self.__remove_prefix_symbols(terms, self.settings[self.GARBAGE_CHARS])

        if apply_bigram_processor:
            terms = self.__sentiment_bigram_filter(
                    terms, self.settings[self.TONE_PREFIXES])

        if self.__str2bool(self.settings[self.REMOVE_STOP_WORDS]):
            terms = [term for term in terms if
                     not(term in self.settings[self.ABSOLUTE_STOP_WORDS]) and
                     not(term in self.task_specific_stop_words)]

        return terms

    @staticmethod
    def __remove_prefix_symbols(terms, chars_to_remove):
        """
        Remove terms prefixes (such as commas, dashes, etc) which is presented
        in chars_to_remove
        """
        for i in range(len(terms)):
            term = terms[i]
            while (len(term) > 0 and (term[0] in chars_to_remove)):
                term = term[1:]
            terms[i] = term

        return terms

    def __sentiment_bigram_filter(self, terms, tone_prefixes):
        """
        Transforms bigrams 'term1 term2' into '+term2' or '-term2' according
        to the 'tone_prefixes' argument.

        Returns
        -------
            terms -- filtered list in which some of terms has been replaced by
                     '+'/'-' char, which becomes a prefix of the following
                     term.
        """
        to_remove = []
        i = 0
        while i < len(terms) - 1:
            bigram = terms[i] + ' ' + terms[i + 1]
            if (bigram in tone_prefixes) and (i < len(terms)-2):
                terms[i + 2] = tone_prefixes[bigram] + terms[i + 2]
                to_remove.append(i)
                to_remove.append(i + 1)
                i += 3
            else:
                unigram = terms[i]
                if (unigram in tone_prefixes):
                    terms[i + 1] = tone_prefixes[unigram] + terms[i + 1]
                    to_remove.append(i)
                    i += 2
                else:
                    i += 1
        # Filter
        terms = [terms[term_index]
                 for term_index in range(len(terms))
                 if not(term_index in to_remove)]
        return terms

    @staticmethod
    def __str2bool(value):
        return value.lower() in ('true')
