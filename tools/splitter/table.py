from psycopg2 import connect

class Table:
    def add_message(self, twitid, text):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO %s(twitid, text) SELECT \'%s\', \'%s\'
            WHERE NOT EXISTS(SELECT twitid FROM %s WHERE twitid=%s)"""%(
            self.table_name, twitid, text.replace('\'', '\'\''),
            self.table_name, twitid))
        self.conn.commit()

    def create(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS %s (
            twitid BIGINT PRIMARY KEY,
            text VARCHAR(256) DEFAULT NULL)"""%(self.table_name))
        cursor.close()
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def clean(self):
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM %s"""%(self.table_name))
        cursor.close()
        self.conn.commit()

    def __init__(self, connection_settings, table_name):
        self.conn = connect(connection_settings)
        self.table_name = table_name
