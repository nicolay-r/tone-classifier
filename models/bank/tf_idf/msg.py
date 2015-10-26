#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from pymystem3 import Mystem

class Message:
        # Returns list of lemmas
        def getIgnored(self):
                return self.ignored

        def getLemmas(self):
                lemmas = self.mystem.lemmatize(' '.join(self.words))
                return lemmas

        def normalize(self):
                words = self.words

                url_pattern = re.compile(
                    r'^(?:http|ftp)s?://' # http:// or https://
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                    r'localhost|' #localhost...
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                    r'(?::\d+)?' # optional port
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

                ignored = []
                for word in words:
                    if (word[0] == '@'):
                        # user in Twitter
                        ignored.append(word)
                    elif (word[0] == '#'):
                        # hash tags
                        ignored.append(word)
                    elif (re.search(url_pattern, word)):
                        # url
                        ignored.append(word)

                for f in ignored:
                    if f in words:
                        words.remove(f)

                self.words = words
                self.ignored = ignored

        def __init__(self, message, mystem):
                self.mystem = mystem
                self.words = filter(None, message.split(' '))
