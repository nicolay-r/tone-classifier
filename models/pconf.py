import json


def save(database, columns, table, out_filepath):
    config = {"database": database,
              "columns": columns,
              "table": table,
              "out_filepath": out_filepath}

    with open(out_filepath, "w") as out:
        json.dump(config, out)
