#!/usr/bin/python

# local
import core.utils

# global
import sys
import json
import psycopg2
from inspect import getsourcefile
from os.path import abspath, dirname
# -----------------------------------------------------------------------------
LIBSVM_PATH = '/classifiers/libsvm/python'
sys.path.insert(0, dirname(abspath(getsourcefile(lambda: 0)))+LIBSVM_PATH)
LIBLINEAR_PATH = '/classifiers/liblinear/python'
sys.path.insert(0, dirname(abspath(getsourcefile(lambda: 0)))+LIBLINEAR_PATH)
# -----------------------------------------------------------------------------
import svmutil
import liblinearutil


def predict(lib_type, problem_filepath, model_filepath):
    if (lib_type == 'svm'):
        ids, p_label = svm_predict(problem_filepath, model_filepath)
    elif (lib_type == 'liblinear'):
        ids, p_label = liblinear_predict(problem_filepath, model_filepath)
    else:
        raise ValueError("library '{}' does not support".format(lib_type))

    print "-1: %s (%s%%)" % (p_label.count(-1),
                             p_label.count(-1) * 100.0 / len(p_label))
    print "0: %s (%s%%)" % (p_label.count(0),
                            p_label.count(0) * 100.0 / len(p_label))
    print "1: %s (%s%%)" % (p_label.count(1),
                            p_label.count(1) * 100.0 / len(p_label))

    return (ids, p_label)


def liblinear_predict(problem_filepath, model_filepath):
    """
    Using LibLinear to predict result of a problem

    Returns
    -------
        (ids, labels)
    """

    # Reading a problem
    ids, x = liblinearutil.svm_read_problem(problem_filepath)

    print "len(x) = ", len(x)

    # Preparing a model
    model = liblinearutil.load_model(model_filepath)

    # Predicting
    y = [-2] * len(x)
    p_label, p_acc, p_val = liblinearutil.predict(y, x, model)

    return (ids, p_label)


def svm_predict(problem_filepath, model_filepath):
    """
    Using LibSVM to predict result of a problem

    Returns
    -------
        (ids, labels)
    """

    # Reading a problem
    ids, x = svmutil.svm_read_problem(problem_filepath)

    print "len(x) = ", len(x)

    # Preparing a model
    model = svmutil.svm_load_model(model_filepath)

    # Predicting
    y = [-2] * len(x)
    p_label, p_acc, p_val = svmutil.svm_predict(y, x, model)

    return (ids, p_label)


def set_result(cursor, table, columns, row_index, label):
    cursor.execute("UPDATE %s SET %s WHERE id=%s" % (
                   table, ','.join(
                       map(lambda c: c + '=' + str(label), columns)),
                   row_index))


if len(sys.argv) == 1:
    print "%s\n%s\n%s\n%s" % (
        "usage:./%s <problem_file> <model_file> <config_file>" % (sys.argv[0]),
        "<library_type> -- available 'svm', 'liblinear'",
        "<problem_file> -- file with a problem to predict",
        "<model_file> -- file with a SVM model",
        "<config_file> -- .pconf file in model folder")
    exit(0)

arguments = {'library_type': sys.argv[1],
             'problem_file': sys.argv[2],
             'model_file': sys.argv[3],
             'config_file': sys.argv[4]}

with open(arguments['config_file']) as f:
    config = json.load(f)

# Database
connectionSettings = "dbname=%s user=%s "\
                     "password=%s host=%s" % (config['database'],
                                              core.utils.PGSQL_USER,
                                              core.utils.PGSQL_PWD,
                                              core.utils.PGSQL_HOST)
connection = psycopg2.connect(connectionSettings)

# Predict
ids, p_label = predict(arguments['library_type'],
                       arguments['problem_file'],
                       arguments['model_file'])

# Save
cursor = connection.cursor()
for message_index in range(0, len(ids)):
    row_id = ids[message_index]
    label = p_label[message_index]
    table = config['prediction_table']

    set_result(cursor, table, config['columns'], row_id, label)

    core.utils.show_progress("Filling answers in \'%s\' table" % (table),
                             message_index + 1,
                             len(ids))

cursor.close()
connection.commit()
connection.close()
