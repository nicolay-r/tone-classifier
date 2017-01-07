#!/usr/bin/python

# global
import sys
import json
import psycopg2
import xml.etree.cElementTree as ET
import xml.dom.minidom as minidom

# configs
import configs


def to_pretty(xml_tree):
    rough_string = ET.tostring(xml_tree.getroot(), 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t')


def data2xml(root_node, data_cursor, table_name):
    database_node = ET.SubElement(root_node, "database")

    # Getting columns
    row_cols = [desc[0] for desc in data_cursor.description]

    row = data_cursor.fetchone()
    while row is not None:
        # Create table element
        table_node = ET.SubElement(database_node, "table", name=table_name)
        for i in range(0, len(row)):
            text = str(row[i])

            if row[i] is None:
                text = 'NULL'

            subelement = ET.SubElement(table_node, "column", name=row_cols[i])
            subelement.text = text.decode('utf-8')

        # Go to next line
        row = data_cursor.fetchone()


def export_and_save(connection, table, out_filename):
    # Export
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM %s;" % (table))
    root_node = ET.Element("pma_xml_export")
    data2xml(root_node, cursor, table)
    tree = ET.ElementTree(root_node)
    # Save
    with open(out_filename, "w") as out:
        out.write(to_pretty(tree).encode('utf-8'))


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

export_and_save(connection,
                config["prediction_table"],
                arguments["out_filepath"])
