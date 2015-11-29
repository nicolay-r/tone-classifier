#!/usr/bin/python

import json
import twits

def save(task_type, orig_table, out_table, out_filepath):
    config = {
        "conn_settings": "dbname=romipdata user=postgres password=postgres host=localhost",
        "orig_table" : orig_table,
        "out_table" : out_table,
        "columns" : twits.get_score_columns(task_type)
    }

    #save config into out_file
    with open(out_filepath, "w") as out:
        json.dump(config, out)
