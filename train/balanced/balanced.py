#!/usr/bin/python

from sys import argv
import psycopg2

argc = len(argv)

if argc == 1:
    print 'usage: ./balanced.py <filename.csv> <database> <table>'
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

with open(config["filepath"]) as f:
    # twit_id, text
    lines = f.readlines()
    for line in lines:
        row = line.split(';')
        tid = row[0]
        ttext = row[3]
        print ttext
        cursor.execute("INSERT INTO %s(id, text) VALUES (%s, %s)"%(
                config['table'], tid.replace('\"', '\''), ttext.replace('\"', '\'')))

conn.commit()
conn.close()
