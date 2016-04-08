#
# Bank task, SentiRuEval 2015
#
bank_imbalanced: TASK_TYPE = bank
bank_imbalanced: TEST_TABLE = bank_test_2015
bank_imbalanced: TRAIN_TABLE = bank_train_2015
bank_imbalanced: MODEL_NAME = tf_idf
bank_imbalanced: ETALON_RESULT = ../data/2015/$(TASK_TYPE)_etalon.xml
bank_imbalanced: core
