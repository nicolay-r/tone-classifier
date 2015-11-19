#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import io
import psycopg2
from pymystem3 import Mystem

most_positive = ['спасибо'.decode('utf-8'), 'ура'.decode('utf-8'), 'axa'.decode('utf-8')]
most_negative = ['ужас'.decode('utf-8')]

def filter_positive(text, mystem):
    words = filter(None, text.split(' '))
    lemmas = mystem.lemmatize(' '.join(words))

    result = False
    for l in lemmas:
        if (l in most_positive):
            result = True
            break

    if result:
        for w in words:
            print w,
        print '\n'
        for l in lemmas:
            print l,
        print '\n-'

    return result

def filter_negative(text, mystem):
    words = filter(None, text.split(' '))
    lemmas = mystem.lemmatize(' '.join(words))

    result = False
    for l in lemmas:
        if (l in most_negative):
            result = True
            break

    if result:
        for w in words:
            print w,
        print '\n'
        for l in lemmas:
            print l,
        print '\n-'

    return result

argc = len(argv)

if argc == 1:
    print 'usage: ./extract.py <filename.csv> <database> <table>'
    exit(0)

config = {
    "filepath" : argv[1],
    "database" : argv[2],
    "table" : argv[3]
    }

connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    config["database"], "postgres", "postgres", "localhost")

m = Mystem(entire_input=False)

conn = psycopg2.connect(connSettings)
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS %s"""%(config['table']));
cursor.execute("""CREATE TABLE IF NOT EXISTS %s (id bigint NOT NULL,
    text VARCHAR(512) NOT NULL)"""%(config['table']))
conn.commit();

added = 0
ignored = 0
with io.open(config["filepath"], 'rt', newline='\r\n') as f:
    # twit_id, text
    lines = f.readlines()
    for line in lines:
        row = line.split('";')
        tid = row[0][1:]
        ttext = row[3][1:]
        if ((config['table'] == 'positive' and
                filter_positive(ttext, m) == True) or
            (config['table'] == 'negative' and
                filter_negative(ttext, m) == True)):
            try:
                added += 1
                cursor.execute("INSERT INTO %s(id, text) VALUES ('%s', '%s')"%(
                    config['table'], tid, ttext.replace('\'', '\'\'')))
            except Exception, e:
                print str(e)
                ignored += 1
            conn.commit()

print "rows ignored: ", ignored
print "rows added: ", added
conn.close()
