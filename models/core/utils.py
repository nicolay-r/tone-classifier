# -*- coding: utf-8 -*-

"""
File contains necessary utils for module
"""

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
        show_progress("Request: '{}', Progress:".format(sql_request),
                      current_row,
                      rowcount)
