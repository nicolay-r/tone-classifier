#!/usr/bin/python

import sys
import json
import libxml2
from svm import *
from svmutil import *
from psycopg2 import connect

def setResult(cursor, table, columns, rowIndex, label):
    cursor.execute("UPDATE %s SET %s WHERE id=%s"%(
        table, ','.join(map(lambda c: c + '=' + str(label), columns)),
        rowIndex))

argc = len(sys.argv)
if (argc == 1):
    print "%s\n%s\n%s\n%s"%(
        "usage: predict.py <problem_file> <model_file> <config_file>",
        "<problem_file> -- file with a problem to predict",
        "<model_file> -- file with a SVM model",
        "<config_file> -- .pconf file in model folder")
    exit(0)

args = {
    'problem_file' : sys.argv[1],
    'model_file' : sys.argv[2],
    'config_file' : sys.argv[3]
}

with open(args['config_file']) as f:
    config = json.load(f)

# reading a problem
ids, x = svm_read_problem(args['problem_file'])

# preparing a model
m = svm_load_model(args['model_file'])
# predicting
y = [-2]*len(x)
p_label, p_acc, p_val = svm_predict(y, x, m)

print "-1: %s (%s%%)"%(p_label.count(-1), p_label.count(-1)*100.0/len(p_label))
print "0: %s (%s%%)"%(p_label.count(0), p_label.count(0)*100.0/len(p_label))
print "1: %s (%s%%)"%(p_label.count(1), p_label.count(1)*100.0/len(p_label))

# database
conn = connect(config['conn_settings'])
cursor = conn.cursor()

# prepare table for a results
cursor.execute('DROP TABLE IF EXISTS %s'%(config['out_table']))
conn.commit()
cursor = conn.cursor()
print "result table:", config['out_table']
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
    setResult(cursor, config['out_table'],
        config['columns'], rowId, label)

cursor.close()
# commiting data
conn.commit()
conn.close()

