#!/usr/bin/python

def get_score_columns(task_type, cursor, table):
    cursor.execute("""SELECT sberbank, vtb, gazprom, alfabank,
        bankmoskvy, raiffeisen, uralsib, rshb FROM %s"""%(table))
    return [desc[0] for desc in cursor.description]

def get(task_type, cursor, table, score, limit):
    if (task_type == 'bank'):
        cursor.execute("""SELECT text, id, sberbank, vtb, gazprom, alfabank,
            bankmoskvy, raiffeisen, uralsib, rshb FROM %s WHERE
            (sberbank=\'%d\' OR vtb=\'%d\' OR gazprom=\'%d\' OR alfabank=\'%d\' OR bankmoskvy=\'%d\'
            OR raiffeisen=\'%d\' OR uralsib=\'%d\' OR rshb=\'%d\') LIMIT(\'%d\');"""%(table,
            score, score, score, score, score, score, score, score, limit))
    else:
        pass

