#!/usr/bin/python

import json
from psycopg2 import connect
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom
import sys
import io

def insert_message(database_node, message_json, table_name, message_index):

    table_node = ET.SubElement(database_node, "table", name=table_name)

    ET.SubElement(table_node, "column", name="id").text = str(message_index)
    ET.SubElement(table_node, "column", name="twitid").text = str(message_index)
    ET.SubElement(table_node, "column", name="date").text = str(message_index)
    ET.SubElement(table_node, "column", name="text").text = message_json["text"]

    for field in ['sberbank', 'alfabank', 'vtb', 'gazprom', 'bankmoskvy',
            'raiffeisen', 'uralsib', 'rshb']:
        if field in message_json:
            tone = '0'
        else:
            tone = 'NULL'
        ET.SubElement(table_node, "column", name=field).text = tone

def to_pretty(xml_tree):
    rough_string = ET.tostring(xml_tree.getroot(), 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t')

argc = len(sys.argv)
if (argc < 4):
    print "usage: ./collection_maker <template_filepath> <description_filepath> <tablename> <out>"
    exit(0)

template_filepath = sys.argv[1]
description_filepath = sys.argv[2]
tablename = sys.argv[3]
out = sys.argv[4]

# reading template
tree = ET.parse(template_filepath)
root = tree.getroot()
database_node = root.find('database')

# reading collection desctiption
with io.open(description_filepath, 'r') as f:
    messages = json.load(f, encoding='utf-8')

message_index = 1
for message in messages["messages"]:
    insert_message(database_node, message, tablename, message_index)
    message_index += 1

# save
with open(out, "w") as out:
    xml = to_pretty(tree).replace("$table", tablename).replace("ns0", "pma")
    out.write(xml.encode("utf-8"))
