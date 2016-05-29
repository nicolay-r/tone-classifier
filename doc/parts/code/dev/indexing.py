vocabulary = TermVocabulary()
mystem = Mystem(entire_input=False)
for table in config['tables']:
    cursor.execute("""SELECT text FROM %s;"""%(table))
    row = cursor.fetchone(), current_row = 0, rowcount = cursor.rowcount
    while (row is not None):
        message = Message(text=row[0], mystem=mystem, configpath="msg.conf")
        message.process()
        terms = message.get_terms()
        for t in terms:
            vocabulary.insert_term(t)
        row = cursor.fetchone(), current_row += 1
