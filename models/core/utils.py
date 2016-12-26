# -*- coding: utf-8 -*-

"""
File contains necessary utils for module
"""

from math import exp

# -----------------------------------------------------------------------------
# PostgreSQL connection settings
# -----------------------------------------------------------------------------
PGSQL_USER = "postgres"
PGSQL_PWD = "postgres"
PGSQL_HOST = "localhost"
# -----------------------------------------------------------------------------


def show_progress(message, current, total):
    print "\r%s: %.2f%% [%d/%d]" % (message, float(current)*100/total, current,
                                    total),
    # Going to the next line in case of Finish
    if (current == total):
        print ""


def normalize(value, k=6):
    if (value >= 0):
        return 1.0 - exp(-abs(value/k))
    else:
        return - (1.0 - exp(-abs(value/k)))


def to_unicode(s):
    if isinstance(s, str):
        return unicode(s, 'utf-8')
    elif isinstance(s, unicode):
        return s


#
#   pgsql functions
#

def table_iterate(connection, sql_request):
    """
    Returns
    -------
        Table row
    """
    cursor = connection.cursor()
    cursor.execute(sql_request)
    row = cursor.fetchone()
    current_row = 0
    rowcount = cursor.rowcount
    while (row is not None):
        yield row
        row = cursor.fetchone()
        current_row += 1
        show_progress("Progress", current_row, rowcount)


def create_table_as(connection, table, template):
    """
    Initialize new table in storage wheter it's existed or not
    """
    # Drop if existed
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS %s' % (table))
    connection.commit()
    # Create new table
    cursor.execute('CREATE TABLE %s AS TABLE %s' % (table, template))
    connection.commit()


def add_row(connection, table, columns, row):
    """
    Add row into table with by defined columns
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO %s(%s) VALUES (%s)" % (
        table, ','.join(columns), ",".join(
            [str(v).replace('\'', '\'\'') if not (v is None) else 'Null'
             for v in row])))
    connection.commit()


def drop_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS %s' % (table_name))
    connection.commit()


def create_table_as(connection, original_table_name, out_table_name):
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE %s AS TABLE %s' % (out_table_name,
                                                    original_table_name))
    connection.commit()
