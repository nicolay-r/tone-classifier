#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import io
import json
import psycopg2
from pymystem3 import Mystem

def get_data(task_type):
    if (task_type == 'bank'):
        return bank
    else:
        return ttk

def get_tone(data, tone):
    if (tone == 'positive'):
        return data['positive']
    else:
        return data['negative']

def tone_filter(text, mystem, task_type, tone):
    words = filter(None, text.split(' '))
    lemmas = mystem.lemmatize(' '.join(words))
    special_words = get_tone(get_data(task_type), tone)
    result = False

    for l in lemmas:
        if (l in special_words):
            result = True
            break

    if result:
        #for w in words:
        #    print w,
        #print '\n'
        #for l in lemmas:
        #    print l,
        #print '\n-'
        pass

    return result

argc = len(argv)

if argc == 1:
    print 'usage: ./extract.py <filename.csv> <database> <table> <task_type>'
    exit(0)

config = {
    "filepath" : argv[1],
    "database" : argv[2],
    "table" : argv[3],
    "task_type" : argv[4]
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

# read config file
with io.open("extract.conf", "r") as f:
    settings = json.load(f, encoding='utf8')

bank = settings['bank']
ttk = settings['ttk']

added = 0
ignored = 0
with io.open(config["filepath"], 'rt', newline='\r\n') as f:
    # twit_id, text
    lines = f.readlines()
    for line in lines:
        row = line.split('";')
        tid = row[0][1:]
        ttext = row[3][1:]
        if ((config['table'] == config['task_type'] + '_positive' and
                tone_filter(ttext, m, config['task_type'], 'positive') == True) or
            (config['table'] == config['task_type'] + '_negative' and
                tone_filter(ttext, m, config['task_type'], 'negative') == True)):
            try:
                added += 1
                cursor.execute("INSERT INTO %s(id, text) VALUES ('%s', '%s')"%(
                    config['table'], tid, ttext.replace('\'', '\'\'')))
            except Exception, e:
               #print str(e)
                ignored += 1
            conn.commit()
        print "\r added:%d, ignored:%d"%(added, ignored),

print ""
print "rows ignored: ", ignored
print "rows added: ", added
conn.close()
