#!/usr/bin/python

import json
from psycopg2 import connect
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom
import sys

def to_pretty(xml_tree):
    rough_string = ET.tostring(xml_tree.getroot(), 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t')

def data2xml(root_node, data_cursor, database_name, table_name):
    database_node = ET.SubElement(root_node, "database", name=database_name)

    # getting columns
    row_cols = [desc[0] for desc in cursor.description]

    row = data_cursor.fetchone()
    while row is not None:
        # create table element
        table_node = ET.SubElement(database_node, "table", name=table_name)
        for i in range(0, len(row)):
            text = str(row[i])
            if row[i] is None:
                text = 'NULL'
            if (row_cols[i] != 'text'):
                ET.SubElement(table_node, "column", name=row_cols[i]).text = text
        # go to next line
        row = data_cursor.fetchone()

argc = len(sys.argv)
if (argc == 1):
    print "usage: ./pg2x_data <pconf_filepath> <xml_database_name> <output>"
    exit(0)

with open(sys.argv[1]) as f:
    config = json.load(f)

conn = connect(config["conn_settings"])
cursor = conn.cursor()

cursor.execute("SELECT * FROM %s;"%(config["out_table"]))

root_node = ET.Element("pma_xml_export")
# converting data into xml_tree
data2xml(root_node, cursor, sys.argv[2], config["out_table"])

tree = ET.ElementTree(root_node)

# save xml
with open(sys.argv[3], "w") as out:
    out.write(to_pretty(tree))
