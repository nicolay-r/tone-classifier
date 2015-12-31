#/usr/bin/python
# -*- coding: utf-8 -*-

from pymystem3 import Mystem
import json
import io

class Message:

    @staticmethod
    def show_terms(terms):
        for t in terms:
            print "<%s>"%(t),
        print

    def transform(self, unicode_terms):

        # process as bigrams
        if (self.use_bigram_processor):
            to_remove = []
            i = 0
            while i < len(unicode_terms)-1:
                bigram = unicode_terms[i] + ' ' + unicode_terms[i+1]
                if (bigram in self.tone_prefix) and (i < len(unicode_terms)-2):
                    unicode_terms[i+2] = self.tone_prefix[bigram] + unicode_terms[i+2]
                    to_remove.append(i)
                    to_remove.append(i+1)
                    i += 3
                else:
                    unigram = unicode_terms[i]
                    if (unigram in self.tone_prefix):
                        unicode_terms[i+1] = self.tone_prefix[unigram] + unicode_terms[i+1]
                        to_remove.append(i)
                        i += 2
                    else:
                        i += 1

            unicode_terms = [unicode_terms[i]
                for i in range(len(unicode_terms)) if not(i in to_remove)]

        # filter stop words
        if (self.use_stop_words):
            unicode_terms = [t for t in unicode_terms if
                not(t in self.abs_stop_words)]

        return unicode_terms

    def get_terms_and_features(self):
        unicode_terms = [unicode(w.strip(), 'utf-8') for w in
            self.mystem.lemmatize(' '.join(self.words)) if
            not(w in ['\n', ' ', '\t', '\r'])]

        unicode_terms = self.transform(unicode_terms)

        features = {}

        if (self.urls_used):
            unicode_terms += self.urls
        if (self.ht_used):
            unicode_terms += self.hash_tags
        if (self.users_used):
            unicode_terms += self.users
        if (self.retweet_used):
            if (self.has_retweet):
                features['RT'] = 1

        return (unicode_terms, features)

    def process(self):
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
            elif (word.find('http:') == 0):
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

    def show(self):
        print "use urls:\t", self.urls_used
        print "use hashtags:\t", self.ht_used
        print "use @users:\t", self.users_used
        print "use 'rt':\t", self.retweet_used
        print "use absolute stop words:\t", self.use_stop_words
        print "use bigram tone processor: \t", self.use_bigram_processor

    def __init__(self, text, mystem, configpath):
        self.mystem = mystem
        self.words = [w.strip() for w in filter(None, text.split(' '))]

        # read config file
        with io.open(configpath, "r") as f:
            settings = json.load(f, encoding='utf8')

        # init settings variables
        self.urls_used = settings['urls_used']
        self.ht_used = settings['ht_used']
        self.users_used = settings['users_used']
        self.retweet_used = settings['retweet_used']
        self.use_stop_words = settings['use_stop_words']
        self.use_bigram_processor = settings['use_bigram_processor']
        self.tone_prefix = settings['tone_prefix']
        self.abs_stop_words = settings['abs_stop_words']
