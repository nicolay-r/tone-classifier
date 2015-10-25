#!/usr/bin/python

import sys
import json
import libxml2
from svm import *
from svmutil import *
from psycopg2 import connect

def setResult(cursor, table, column, rowIndex, label):
    cursor.execute("UPDATE %s SET %s=%s WHERE (id=%s AND %s IS NOT NULL)"%(
        table, column, label, rowIndex, column))

argc = len(sys.argv)
if (argc == 1):
    print "%s\n%s\n%s\n%s"%(
        "usage: predict.py <problem_file> <model_file> <config_file>",
        "<problem_file> -- file with a problem to predict",
        "<model_file> -- file with a SVM model",
        "<config_file> -- .pconf file in model folder")
    exit(0)

with open(sys.argv[3]) as f:
    config = json.load(f)

# reading a problem
ids, x = svm_read_problem(sys.argv[1])

# preparing a model
m = svm_load_model(sys.argv[2])
# predicting
y = [0]*len(x)
p_label, p_acc, p_val = svm_predict(y, x, m)

# database
conn = connect(config['conn_settings'])
cursor = conn.cursor()

# prepare table for a results
cursor.execute('DROP TABLE IF EXISTS %s'%(config['out_table']))
conn.commit()
cursor = conn.cursor()
cursor.execute('CREATE TABLE %s AS TABLE %s'%(
    config['out_table'], config['orig_table']))
conn.commit()

# filling answers
print "Tests count:", len(ids)
for msgIndex in range(0, len(ids)):
    #print msgIndex
    rowId = ids[msgIndex]
    label = p_label[msgIndex]
    # setting answers
    for col in config['columns']:
        setResult(cursor, config['out_table'], col, rowId, label)



