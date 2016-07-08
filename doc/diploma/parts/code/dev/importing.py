# Parse XML file
doc = libxml2.parseFile(xmlFile)
ctx = doc.xpathNewContext()
# Create connection
conn = psycopg2.connect(connSettings)
cursor = conn.cursor()
# Reading data from XML file
tables = ctx.xpathEval("/pma/database/table")
for table in tables:
    row = getRow(table)
    insertRow(cursor, table.prop("name"), row)
