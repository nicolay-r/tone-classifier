# importing libraries
from svm import *
from svmutil import *
# preparing a model
model = svm_load_model('train_collection.txt')
# problem reading
ids, x = svm_read_problem('test_collection.txt')
# predicting
p_label, p_acc, p_val = svm_predict(y, x, model)
# show class volumes
print "-1: %s "%(p_label.count(-1))
print "0: %s "%(p_label.count(0))
print "1: %s "%(p_label.count(1))
