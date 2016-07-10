import xml.etree.cElementTree as ET
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
