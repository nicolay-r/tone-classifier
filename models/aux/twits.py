#!/usr/bin/python

def get_score_columns(task_type):
    if (task_type == 'bank'):
        return ['sberbank', 'vtb', 'gazprom', 'alfabank', 'bankmoskvy', 'raiffeisen', 'uralsib', 'rshb']
    if (task_type == 'ttk'):
        return ['beeline', 'mts', 'megafon', 'tele2', 'rostelecom', 'komstar', 'skylink']

def get(task_type, cursor, table, score, limit):
    if (task_type == 'bank'):
        cursor.execute("""SELECT text, id, sberbank, vtb, gazprom, alfabank,
            bankmoskvy, raiffeisen, uralsib, rshb FROM %s WHERE
            (sberbank=\'%d\' OR vtb=\'%d\' OR gazprom=\'%d\' OR alfabank=\'%d\' OR bankmoskvy=\'%d\'
            OR raiffeisen=\'%d\' OR uralsib=\'%d\' OR rshb=\'%d\') LIMIT(\'%d\');"""%(table,
            score, score, score, score, score, score, score, score, limit))
    elif (task_type == 'ttk'):
        cursor.execute("""SELECT text, id, beeline, mts, megafon,
            tele2, rostelecom, komstar, skylink FROM %s WHERE
            (mts=\'%d\' OR megafon=\'%d\' OR tele2=\'%d\' OR rostelecom=\'%d\'
            OR komstar=\'%d\' OR skylink=\'%d\') LIMIT(\'%d\')"""%(table,
            score, score, score, score, score, score, limit))
