#!/usr/bin/python

import psycopg2
import sys


args = sys.argv
if (len(args) == 1):
    print "Usage ./extract.py <filepath>"
    exit(0)

filepath = sys.argv[1]

table = (filepath.split('.'))[0]

# Connect to a database
settings = "dbname=romipdata user=postgres password=postgres host=localhost"
connection = psycopg2.connect(settings)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS %s (
            term VARCHAR(100),
            tone REAL)"""%(table));
cursor.execute("DELETE FROM %s;"%(table));
connection.commit()

# Reading file
processed = 0
ignored = 0
term  = ""
with open(filepath, "r") as f:
    for line in f.readlines():
        words = line.split(' ')
        if (len(words) >= 2):
            term += words[0]
            rank = words[1]
            cursor.execute("INSERT INTO %s(term, tone) VALUES('%s', '%s')"%(table,
                term.replace("'", "''"), rank));
            processed += 1
            term = ""
        elif (len(words) == 1):
            term += words[0]
        else:
            ignored += 1
        print "\rprocessed:%d; ignored:%d"%(processed, ignored),

cursor.close()
connection.commit()
connection.close()
