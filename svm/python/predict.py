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
    print "usage: predict.py <config_file>\n<config_file> -- .pconf file in model folder"
    exit(0)

with open(sys.argv[1]) as f:
    config = json.load(f)

# reading a problem
y, ids = svm_read_problem(config['problem_file'])
# preparing a model
m = svm_load_model(config['model_file'])
# predicting
p_label, p_acc, p_val = svm_predict(y, x, m)

# answers
print p_label

# database
conn = connect(config['conn_settings'])
cursor = conn.cursor()

# prepare table for a results
cursor.execute('DROP TABLE %s'%(config['out_table']))
conn.commit()
cursor.execute('CREATE TABLE %s AS TABLE %s'%(
    config['out_table'], config['orig_table']))
conn.commit()

# filling answers
for msgIndex in range(0, len(ids)):
    rowId = ids[msgIndex]
    label = p_label[msgIndex]
    # setting answers
    for col in config['columns']:
        setResult(cursor, config['out_table'], col, rowId, label)





