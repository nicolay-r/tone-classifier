#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
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

                urls = []
                users = []
                hash_tags = []
                retweet = []
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
                    elif(word == 'RT'):
                        # retweet
                        retweet.append(word)

                for f in urls + users + hash_tags + retweet:
                    if f in words:
                        words.remove(f)

                self.words = words
                self.urls = urls
                self.users = users
                self.hash_tags = hash_tags
                self.retweet = retweet

        def __init__(self, message, mystem):
                self.mystem = mystem
                self.words = filter(None, message.split(' '))
