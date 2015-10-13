#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import libxml2
from psycopg2 import connect, extensions
from db_converter import parse

if len(sys.argv) == 1:
        print 'usage: train_table <xmlFile>'
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
database = ctx.xpathEval("/pma_xml_export/database")[0].prop('name').lower()

connSettings = "dbname=%s user=%s password=%s host=%s"%(
        "postgres", "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()

try:
        conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor.execute("CREATE DATABASE %s;"%(database))
        cursor.close()
        conn.close()
except:
        pass

connSettings = "dbname=%s user=%s password=%s host=%s"%(
        database, "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()
cursor.execute(createTable)
cursor.close()
conn.commit()
conn.close()


