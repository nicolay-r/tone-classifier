import json


def save(database, task_type, orig_table, out_table, out_filepath):
    config = {
        "database": database,
        "orig_table": orig_table,
        "out_table": out_table,
        # "columns": tweets.get_score_columns(task_type)
    }

    with open(out_filepath, "w") as out:
        json.dump(config, out)
