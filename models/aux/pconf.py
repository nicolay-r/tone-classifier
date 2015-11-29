#!/usr/bin/python

import json

def save(task_type, orig_table, out_table, out_filepath):
    if (task_type=='bank'):
        config = {
                "conn_settings": "dbname=romipdata user=postgres password=postgres host=localhost",
                "orig_table" : orig_table,
                "out_table" : out_table,
                "columns" : ["sberbank", "alfabank", "vtb", "gazprom",
                    "bankmoskvy", "raiffeisen", "uralsib", "rshb"]
            }
    else:
        config = {}

    #save config into out_file
    with open(out_filepath, "w") as out:
        json.dump(config, out)
