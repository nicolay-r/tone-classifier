#!/usr/bin/python

# global
import sys
import json
import psycopg2

# configs
import configs

if len(sys.argv) == 1:
    print "usage: {} <pconf> <out>".format(
            sys.argv[0])
    exit(0)

arguments = {'pconf': sys.argv[1],
             'out_filepath': sys.argv[2]}

with open(arguments['pconf']) as f:
    config = json.load(f)

connectionSettings = "dbname=%s user=%s password=%s host=%s" % (
                                config['database'],
                                configs.CONNECTION_SETTINGS['user'],
                                configs.CONNECTION_SETTINGS['password'],
                                configs.CONNECTION_SETTINGS['host'])
connection = psycopg2.connect(connectionSettings)
cursor = connection.cursor()

outputquerry = "COPY {table} TO STDOUT WITH CSV HEADER".format(
                table=config['prediction_table'])

with open(arguments['out_filepath'], 'w') as out:
    cursor.copy_expert(outputquerry, out)
