#!/usr/bin/python

def create_table_as(conn, table, template):
    # drop if existed
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS %s'%(table))
    conn.commit()
    # create new table
    cursor.execute('CREATE TABLE %s AS TABLE %s'%(
        table, template))
    conn.commit()

def add_row(conn, table, columns, row):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO %s(%s) VALUES (%s)"%(
        table, ','.join(columns), ",".join(
        [str(v).replace('\'', '\'\'') if not (v is None) else 'Null'
        for v in row])))
    conn.commit()
