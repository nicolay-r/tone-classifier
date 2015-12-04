#!/usr/bin/python

from msg import Message
from vocs import TermVocabulary

urls_used = True
ht_used = True
users_used = True
retweet_used = True

print "urls:\t", urls_used
print "ht:\t", ht_used
print "users:\t", users_used
print "rt:\t", retweet_used

def process_text(mystem, text):
    message = Message(text, mystem)
    message.normalize()
    terms = message.getLemmas()

    features = {}
    if (urls_used):
        terms += message.urls
    if (ht_used):
        terms += message.hash_tags
    if (users_used):
        terms += message.users
    if (retweet_used):
        if (message.has_retweet):
            features['RT'] = 1

    return (terms, features)
