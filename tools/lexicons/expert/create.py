#!/usr/bin/python

import sys
from psycopg2 import connect
import json

if len(sys.argv) == 1:
    print "usage: ./create.py <file> <output_table>"
    exit(0)

expert_file = sys.argv[1]
out_table = sys.argv[2]

lemmas = {}
tones = {'positive' : 1, 'negative' : -1, 'neutral' : 0}
with open(expert_file, "r") as f:
    for line in f.readlines():
        row = line.split(',')
        lemma = row[2].strip().decode('utf-8')
        tone = row[3].strip()

        if len(lemma.split(' ')) == 1 and tone in tones:
            print lemma, ' ', tones[tone]

            lemmas[lemma] = tones[tone]

# Create connection and save result
print 'Creete connection and save result'
with open(".conn", "r") as connection:
    conn = json.load(connection, encoding='utf8')

# Connect to a database
print 'Connect to a database'
settings = """dbname=%s user=%s password=%s host=%s"""%(
    conn['database'], conn["user"], conn["password"], conn["host"])
connection = connect(settings)
cursor = connection.cursor()

print settings
# Create result table
print 'Create result table'
max_term_length = 50
cursor.execute("""CREATE TABLE IF NOT EXISTS {table}(
                        term VARCHAR({max_length}),
                        tone REAL)""".format(table = out_table, max_length =
    max_term_length));
cursor.execute("DELETE FROM {table}".format(table = out_table));

# Save results
print 'Save results'
all_terms = {}
for pair in lemmas:
    p = (pair, lemmas[pair])
    if (len(p[0]) < max_term_length):
        term_tone = p[1]
        utf_term = p[0].encode('utf-8')

        if not (utf_term in all_terms):
            cursor.execute("""INSERT INTO {table} ({term}, {value})
                VALUES (\'{t}\', {v})""".format(term="term", value='tone',
                table=out_table, t=utf_term, v=term_tone));
            all_terms[utf_term] = term_tone
        elif (term_tone != all_terms[utf_term]):
            cursor.execute("""DELETE FROM {table} WHERE term = '{t}'""".format(
               table=out_table, t=utf_term))
            # set another impossible tone value to prevent an attemt of adding
            # this utf_term in a future
            all_terms[utf_term] = 2;

    connection.commit()
connection.close()
