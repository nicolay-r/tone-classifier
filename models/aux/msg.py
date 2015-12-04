#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymystem3 import Mystem

min_word_len = 4
print "Use filter len(w) > %s"%(min_word_len)

class Message:
    def getLemmas(self):
        lemmas = filter(lambda l: len(l.decode('utf-8')) > min_word_len,
            self.mystem.lemmatize(' '.join(self.words)))
        return lemmas

    def normalize(self):
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

    def __init__(self, message, mystem):
        self.mystem = mystem
        self.words = filter(None, message.split(' '))
