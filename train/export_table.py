#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import libxml2
from psycopg2 import connect
from db_converter import parse

if len(sys.argv) == 1:
        print 'usage: train_table <xmlFile> <pgDatabase>'
        exit(0)
# Getting SQL script from xmlFile
xmlFile = sys.argv[1]

doc = libxml2.parseFile(xmlFile)
ctx = doc.xpathNewContext()
ctx.xpathRegisterNs("pma", "http://www.phpmyadmin.net/some_doc_url/")

createTable = ctx.xpathEval("""/pma_xml_export/pma:structure_schemas/
        pma:database/pma:table""")[0].getContent()

createTable = createTable.replace('`', '\"')

# Convert mysql table to postgreSQL
with open(".mysql", "w") as f:
        f.write(createTable)

parse(".mysql", ".pgsql")

with open(".pgsql", "r") as f:
        createTable = f.read()

createTable = createTable.replace("AUTO_INCREMENT", "")

# Connecting to postgeSQL database
database = sys.argv[2]

connSettings = """dbname=%s user=%s password=%s host=%s"""%(
        database, "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()
cursor.execute(createTable)

cursor.close()

conn.commit()
conn.close()


