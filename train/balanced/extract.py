#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import io
import psycopg2
from pymystem3 import Mystem

def filter_positive():
    pass

def filter_negative():
    pass

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
    print "lines count: ", len(lines)
    for line in lines:
        added += 1
        row = line.split('";')
        tid = row[0][1:]
        ttext = row[3][1:]
        try:
            cursor.execute("INSERT INTO %s(id, text) VALUES ('%s', '%s')"%(
                config['table'], tid, ttext.replace('\'', '\'\'')))
        except Exception, e:
            print str(e)
            added -= 1
            ignored += 1
        conn.commit()
print "rows ignored: ", ignored
print "rows added: ", added
conn.close()
