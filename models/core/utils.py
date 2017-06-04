# -*- coding: utf-8 -*-

"""
File contains necessary utils for module
"""

from math import exp


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
