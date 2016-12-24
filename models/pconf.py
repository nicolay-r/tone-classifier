import json


def save(database, columns, prediction_table, out_filepath):
    config = {"database": database,
              "columns": columns,
              "prediction_table": prediction_table,
              "etalon_table": 'TODO'}

    with open(out_filepath, "w") as out:
        json.dump(config, out)
