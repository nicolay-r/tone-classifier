# -*- coding: utf-8 -*-

import io
import json
from nltk.tokenize import TweetTokenizer


class TwitterMessage:
    INCLUDE_URLS = 'urls_used'
    INCLUDE_HASHTAGS = 'ht_used'
    INCLUDE_USERS = 'users_used'
    INCLUDE_RETWEET_SYMBOL = 'retweet_used'
    REMOVE_STOP_WORDS = 'use_stop_words'
    APPLY_BIGRAM_PROCESSOR = 'use_bigram_processor'
    TONE_PREFIXES = 'tone_prefix'
    ABSOLUTE_STOP_WORDS = 'abs_stop_words'
    GARBAGE_CHARS = 'garbage_chars'

    def __init__(self, text, mystem, configpath, task_type='none'):
        """
        Arguments
        ---------
            text
            mystem
            configpath
            task_type
        """
        self.mystem = mystem

        # Read config file
        with io.open(configpath, "r") as f:
            self.settings = json.load(f, encoding='utf-8')

        if (task_type != 'none'):
            key = task_type + '_stop_words'
            self.task_specific_stop_words = self.settings[key]
        else:
            self.task_specific_stop_words = []

        # Tokenize message
        tokenizer = TweetTokenizer()
        self.words = tokenizer.tokenize(text)

        # Process
        self.__process()

    def get_terms(self, lemmatize=True):
        """
        Get terms of twitter message

        Returns
        -------
            terms -- list of twitter words of natural language (with or
                     without applying lemmatizer) and other metainformation
                     (such as URL, hashtags, etc.)
        """
        terms = [w.strip() for w in
                 self.mystem.lemmatize(' '.join(self.words)) if
                 not(w in ['\n', ' ', '\t', '\r'])]

        terms = self.__transform(terms)

        if (self.settings[TwitterMessage.INCLUDE_URLS]):
            terms += self.urls
        if (self.settings[TwitterMessage.INCLUDE_HASHTAGS]):
            terms += self.hash_tags
        if (self.settings[TwitterMessage.INCLUDE_USERS]):
            terms += self.users

        return terms

    def __transform(self, terms):
        self.__remove_prefix_symbols(terms, self.settings[self.GARBAGE_CHARS])

        if self.settings[self.APPLY_BIGRAM_PROCESSOR]:
            terms = self.__sentiment_bigram_filter(
                    terms, self.settings[self.TONE_PREFIXES])

        if (self.settings[self.REMOVE_STOP_WORDS]):
            terms = [term for term in terms if
                     not(term in self.settings[self.ABSOLUTE_STOP_WORDS]) and
                     not(term in self.task_specific_stop_words)]

        return terms

    # @staticmethod
    # def show_terms(terms):
    #     for t in terms:
    #         print "<%s>" % (t),
    #     print

    def __process(self):
        words = self.words

        retweet_term = 'RT'

        urls = []
        users = []
        hash_tags = []
        has_retweet = False
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
            elif(word == retweet_term):
                # retweet
                has_retweet = True

        for f in urls + users + hash_tags + [retweet_term]:
            if f in words:
                words.remove(f)

        self.words = words
        self.urls = urls
        self.users = users
        self.hash_tags = hash_tags
        self.has_retweet = has_retweet

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
            unicode_terms -- filtered list in which some of terms has been
                             replaced by '+'/'-' char, which becomes a prefix
                             of the following term.
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
