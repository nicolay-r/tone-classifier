#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymystem3 import Mystem
urls_used = False
ht_used = True
users_used = False
retweet_used = False

use_stop_words = True
use_bigram_processor = True

print "use urls:\t", urls_used
print "use hashtags:\t", ht_used
print "use @users:\t", users_used
print "use 'rt':\t", retweet_used
print "use absolute stop words:\t", use_stop_words
print "use bigram tone processor: \t", use_bigram_processor

class Message:

    @staticmethod
    def show_terms(terms):
        for t in terms:
            print "<%s>"%(t),
        print
    @staticmethod
    def transform(terms):
        # process as bigrams
        if (use_bigram_processor):
            to_remove = []
            i = 0
            while i < len(terms)-1:
                bigram = terms[i] + ' ' + terms[i+1]
                if (bigram in tone_prefix) and (i < len(terms)-2):
                    terms[i+2] = tone_prefix[bigram] + terms[i+2]
                    to_remove.append(i)
                    to_remove.append(i+1)
                    i += 3
                else:
                    unigram = terms[i]
                    if (unigram in tone_prefix):
                        terms[i+1] = tone_prefix[unigram] + terms[i+1]
                        to_remove.append(i)
                        i += 2
                    else:
                        i += 1
            terms = [terms[i] for i in range(len(terms)) if not(i in to_remove)]
        # filter stop words
        if (use_stop_words):
            terms = [t for t in terms if not(t in abs_stop_words)]
        return terms

    def get_terms_and_features(self):
        terms = [w.strip() for w in self.mystem.lemmatize(' '.join(self.words))
            if not(w in ['\n', ' ', '\t', '\r'])]
        #Message.show_terms(terms)
        terms = Message.transform(terms)
        #Message.show_terms(terms)
        features = {}

        if (urls_used):
            terms += self.urls
        if (ht_used):
            terms += self.hash_tags
        if (users_used):
            terms += self.users
        if (retweet_used):
            if (self.has_retweet):
                features['RT'] = 1

        return (terms, features)

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

    def __init__(self, text, mystem):
        self.mystem = mystem
        self.words = [w.strip() for w in filter(None, text.split(' '))]

tone_prefix = {"имитировать": "-", "даже если": "-", "снижение": "-",
"уменьшение": "-", "много": "+", "весьма": "+", "просто": "+", "сильно": "+",
"спад": "-", "все время": "+", "явный": "+", "снизить": "-", "совершенно": "+"
, "снизиться": "-", "ликвидировать": "-", "значительный": "+",
"разрушать": "-", "сильнейший": "+", "нельзя назвать": "-",
"колоссально": "+", "ничего": "-", "острый": "+", "повышать": "+",
"ослаблять": "-", "пресекать": "-", "масштабный": "+",
"невообразимый": "+", "настолько": "+", "якобы": "-", "вырасти": "+",
"редкостный": "+", "сильный": "+", "чрезвычайный": "+", "имитация": "-",
"намного": "+", "заметный рост": "+", "жуть как": "+", "увеличить": "+",
"необычайно": "+", "безусловный": "+", "противодействовать": "-",
"большой": "+", "крайне": "+", "перестать": "-",
"масштабность": "+", "разрушение": "-", "безумно": "+", "абсолютный": "+",
"особенно": "+", "жутко": "+", "преодолеть": "-", "запросто": "+",
"отсутствие": "-", "рост": "+", "порядочный": "+", "усилить": "+",
"не": "-", "недостаточно": "-", "избыток": "+", "лишиться": "-",
"абсолютно": "+", "дикий": "+", "совсем": "+", "невероятно": "+", "очень": "+",
"лишить": "-", "утратить": "-", "нет никакой": "+", "ослабить": "-",
"запредельный": "+", "утрачивать": "-", "полный": "+", "нарастание": "+",
"по-настоящему": "+", "немыслимый": "+", "гораааздо": "+", "не просто": "+",
"ликвидация": "-", "снять": "-", "преодоление": "-", "избавиться": "-",
"повышение": "+", "падение": "-", "полностью": "+", "вырастать": "+",
"предельно": "+", "нереальный": "+", "противодействие": "-", "разрушить": "-",
"совершенный": "+", "рекордно": "+", "серьезный": "+", "снижаться": "-",
"снимать": "-", "нет": "-", "достаточно": "+", "уменьшать": "-",
"поистине": "+", "никакой": "-", "наибольший": "+", "неимоверно": "+",
"уменьшить": "-", "стопроцентный": "+", "гораздо": "+", "нереально": "+",
"отсутствовать": "-", "невиданный": "+", "запрет": "-", "великий вероятность":
"+", "увеличивать": "+", "конец": "-", "лишаться": "-", "защита от": "-",
"избавление": "-", "без": "-", "потеря": "-", "жгучий": "+", "колоссальный":
"+", "терять": "-", "утрата": "-", "самый": "+", "лишать": "-",
"совсем-совсем": "+", "дефицит": "-", "чрезвычайно": "+", "нейтрализация": "-"
, "усиливать": "+", "колоссальнейший": "+", "избавляться": "-",
"высокий уровень": "+", "пресечение": "-", "небезосновательно": "+",
"значительно": "+", "отменять": "-", "вполне": "+", "отменить": "-",
"лишение": "-", "огромнейший": "+", "отмена": "-", "потерять": "-",
"усиление": "+", "не назвать": "-", "разительный": "+", "ослабление": "-",
"увеличение": "+", "повысить": "+"}

abs_stop_words = {"на", 'ещ', 'fitch', 'на', 'как', 'из', 'мы','вы', 'тег'
,'тот', 'если', 'быть', 'это', 'что', 'ещё', 'ваш', 'ff', 'да', 'за', 'ты', 'да'
,'по', 'ли', 'или', 'том', 'они', 'для', 'кто', 'тип', 'там', 'он', 'ru', 'наш',
'свой', 'lt'}
