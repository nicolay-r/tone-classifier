def save(connection, out_table, result):
    cursor = connection.cursor(), max_term_length = 50
    cursor.execute("""CREATE TABLE IF NOT EXISTS {table} (
        term VARCHAR({max_length}),
        tone REAL)""".format(table = out_table, max_length = max_term_length));
    cursor.execute("DELETE FROM {table}".format(table = out_table));
    for pair in result:
        if (len(pair[0]) < max_term_length):
            cursor.execute("""INSERT INTO {table} ({term}, {value}) VALUES
                (\'{t}\', {v})""".format(term="term", value='tone',
                table=out_table, t=pair[0].encode('utf-8'), v=pair[1]));
