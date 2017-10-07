# Root Folder of the LibSVM classifier library
SVM_ROOT=../models/classifiers/libsvm/
LIBLINEAR_ROOT=../models/classifiers/liblinear/
# Root of the problem and training data
DATA_ROOT=../models/
# SVM prediction script
PREDICT=../models/
MODEL_CORE=../models/core/

#remove TASK_TYPE

# Defining a default model
SVM_MODEL_OPTIONS=	-t 0 -c 0.4 -e 0.01 -q
LIBLINEAR_MODEL_OPTIONS= -s 7 -c 0.5
CLASSIFIER_LIBRARY= svm
MODEL_ROOT	=	$(DATA_ROOT)
MODEL_OUTDIR= 	$(MODEL_ROOT)/out/
MODEL_PROB	=	$(MODEL_OUTDIR)$(MODEL_NAME).prob
MODEL_TEST	=	$(MODEL_OUTDIR)$(MODEL_NAME).test
MODEL_PCONF	=	$(MODEL_OUTDIR)$(MODEL_NAME).pconf
MODEL_OUT	=	$(MODEL_OUTDIR)$(MODEL_NAME).out
MODEL_ERROR = 	$(MODEL_OUTDIR)$(MODEL_NAME).err.csv
MODEL_TRAIN	=	$(MODEL_OUTDIR)$(MODEL_NAME).train
MODEL_MODEL	=	$(MODEL_TRAIN).model

SENTIRUEVAL2015 = ../data/collections/SentiRuEval-2015/
SENTIRUEVAL2016 = ../data/collections/SentiRuEval-2016/
USERCOLLECTION = ../data/collections/user/

theano-train_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-train_sre16_bank_w2v_imb: TABLE = $(SENTIRUEVAL2016)/bank_train.csv
theano-train_sre16_bank_w2v_imb: MODEL_NAME = theano
theano-train_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-train_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-train_sre16_bank_w2v_imb: theano_core

theano-test_sre16_bank_w2v: TASK_TYPE = bank
theano-test_sre16_bank_w2v: TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
theano-test_sre16_bank_w2v: MODEL_NAME = theano_test
theano-test_sre16_bank_w2v: SETTING_NAME = sre16_imb
theano-test_sre16_bank_w2v: VECTORIZER_TYPE = w2v
theano-test_sre16_bank_w2v: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
theano-test_sre16_bank_w2v: theano_core_test

theano-diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
theano-diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
theano-diagnostic_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
theano-diagnostic_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-diagnostic_sre16_bank_w2v_imb: NETWORK_TYPE = rnn
theano-diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
theano-diagnostic_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-diagnostic_sre16_bank_w2v_imb: theano_diagnostic

gru-2l_diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
gru-2l_diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
gru-2l_diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
gru-2l_diagnostic_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
gru-2l_diagnostic_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
gru-2l_diagnostic_sre16_bank_w2v_imb: NETWORK_TYPE = gru-2l
gru-2l_diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
gru-2l_diagnostic_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
gru-2l_diagnostic_sre16_bank_w2v_imb: theano_diagnostic

keras-lstm_diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
keras-lstm_diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
keras-lstm_diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
keras-lstm_diagnostic_sre16_bank_w2v_imb: MODEL_NAME = keras
keras-lstm_diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
keras-lstm_diagnostic_sre16_bank_w2v_imb: keras_core

keras-lstm_diagnostic_sre16_tcc_w2v_imb: TASK_TYPE = tkk
keras-lstm_diagnostic_sre16_tcc_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
keras-lstm_diagnostic_sre16_tcc_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
keras-lstm_diagnostic_sre16_tcc_w2v_imb: MODEL_NAME = keras
keras-lstm_diagnostic_sre16_tcc_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
keras-lstm_diagnostic_sre16_tcc_w2v_imb: keras_core

theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: NETWORK_TYPE = lstm-1l-e
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-lstm-1le_diagnostic_sre16_bank_w2v_imb: theano_diagnostic

# This flow allows to define the necessary amount of epochs
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_70.csv
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_30.csv
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_30.csv
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: NETWORK_TYPE = lstm-1l
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-lstm-1l_diagnostic_train_sre16_bank_w2v_imb: theano_diagnostic

theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: TASK_TYPE = tkk
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_70.csv
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_30.csv
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_train_30.csv
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: MODEL_NAME = theano_diagnostic
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: SETTING_NAME = sre16_imb
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: NETWORK_TYPE = lstm-1l
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: VECTORIZER_TYPE = w2v
theano-lstm-1l_diagnostic_train_sre16_tcc_w2v_imb: theano_diagnostic

theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: NETWORK_TYPE = lstm-1l
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-lstm-1l_diagnostic_sre16_bank_w2v_imb: theano_diagnostic

theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: TASK_TYPE = bank
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_train.csv
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)$(TASK_TYPE)_test.csv
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: MODEL_NAME = theano_diagnostic
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: SETTING_NAME = sre16_imb
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: NETWORK_TYPE = lstm-2l
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)$(TASK_TYPE)_etalon.csv
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: VECTORIZER_TYPE = w2v
theano-lstm-2l_diagnostic_sre16_bank_w2v_imb: theano_diagnostic

#
# SentiRuEval-2015
#
svm_sre15_bank_features-only_imb: TASK_TYPE = bank
svm_sre15_bank_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_features-only_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_features-only_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
svm_sre15_bank_features-only_imb: MODEL_NAME = features_only
svm_sre15_bank_features-only_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_features-only_imb: core

svm_sre15_bank_features-only_bal: TASK_TYPE = bank
svm_sre15_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
svm_sre15_bank_features-only_bal: MODEL_NAME = features_only
svm_sre15_bank_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_features-only_bal: core

lr_sre15_bank_features-only_imb: TASK_TYPE = bank
lr_sre15_bank_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_features-only_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_features-only_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
lr_sre15_bank_features-only_imb: MODEL_NAME = features_only
lr_sre15_bank_features-only_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_features-only_imb: core

lr_sre15_bank_features-only_bal: TASK_TYPE = bank
lr_sre15_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
lr_sre15_bank_features-only_bal: MODEL_NAME = features_only
lr_sre15_bank_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_features-only_bal: core

svm_sre15_bank_w2v_imb: TASK_TYPE = bank
svm_sre15_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
svm_sre15_bank_w2v_imb: MODEL_NAME = w2v
svm_sre15_bank_w2v_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_w2v_imb: core

svm_sre15_bank_w2v_bal: TASK_TYPE = bank
svm_sre15_bank_w2v_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_w2v_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_w2v_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
svm_sre15_bank_w2v_bal: MODEL_NAME = w2v
svm_sre15_bank_w2v_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_w2v_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_w2v_bal: core

lr_sre15_bank_w2v_imb: TASK_TYPE = bank
lr_sre15_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
lr_sre15_bank_w2v_imb: MODEL_NAME = w2v
lr_sre15_bank_w2v_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_w2v_imb: core

lr_sre15_bank_w2v_bal: TASK_TYPE = bank
lr_sre15_bank_w2v_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_w2v_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_w2v_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
lr_sre15_bank_w2v_bal: MODEL_NAME = w2v
lr_sre15_bank_w2v_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_w2v_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_w2v_bal: core

svm_sre15_bank_bow_imb: TASK_TYPE = bank
svm_sre15_bank_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_bow_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_bow_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
svm_sre15_bank_bow_imb: MODEL_NAME = bow
svm_sre15_bank_bow_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_bow_imb: core

svm_sre15_bank_bow_bal: TASK_TYPE = bank
svm_sre15_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_bow_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
svm_sre15_bank_bow_bal: MODEL_NAME = bow
svm_sre15_bank_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_bank_bow_bal: core

lr_sre15_bank_bow_imb: TASK_TYPE = bank
lr_sre15_bank_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_bow_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_bow_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
lr_sre15_bank_bow_imb: MODEL_NAME = bow
lr_sre15_bank_bow_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_bow_imb: core

lr_sre15_bank_bow_bal: TASK_TYPE = bank
lr_sre15_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_bow_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
lr_sre15_bank_bow_bal: MODEL_NAME = bow
lr_sre15_bank_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_bank_bow_bal: core

#sre16_bank_bow_bal: TASK_TYPE = bank
#sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
#sre16_bank_bow_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
#sre16_bank_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
#sre16_bank_bow_bal: MODEL_NAME = bow
#sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
#sre16_bank_bow_bal: core

svm_sre15_bank_tf-idf_imb: TASK_TYPE = bank
svm_sre15_bank_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_tf-idf_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_tf-idf_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
svm_sre15_bank_tf-idf_imb: MODEL_NAME = tf_idf
svm_sre15_bank_tf-idf_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_tf-idf_imb: core

svm_sre15_bank_tf-idf_bal: TASK_TYPE = bank
svm_sre15_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
svm_sre15_bank_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced
svm_sre15_bank_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre15_bank_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_bank_tf-idf_bal: core

lr_sre15_bank_tf-idf_imb: TASK_TYPE = bank
lr_sre15_bank_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_tf-idf_imb: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_tf-idf_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train.csv
lr_sre15_bank_tf-idf_imb: MODEL_NAME = tf_idf
lr_sre15_bank_tf-idf_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_tf-idf_imb: core

lr_sre15_bank_tf-idf_bal: TASK_TYPE = bank
lr_sre15_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2015)/bank_test.csv
lr_sre15_bank_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/bank_train_balanced.csv
lr_sre15_bank_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre15_bank_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_bank_tf-idf_bal: core

svm_sre16_bank_tf-idf_bal: TASK_TYPE = bank
svm_sre16_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
svm_sre16_bank_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
svm_sre16_bank_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre16_bank_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_bank_tf-idf_bal: core

svm_sre16_bank_w2v_bal: TASK_TYPE = bank
svm_sre16_bank_w2v_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_w2v_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
svm_sre16_bank_w2v_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
svm_sre16_bank_w2v_bal: MODEL_NAME = w2v
svm_sre16_bank_w2v_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_w2v_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_bank_w2v_bal: core

svm_sre16_bank_w2v_imb: TASK_TYPE = bank
svm_sre16_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
svm_sre16_bank_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train.csv
svm_sre16_bank_w2v_imb: MODEL_NAME = w2v
svm_sre16_bank_w2v_imb: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_bank_w2v_imb: core

svm_sre16_bank_features-only_bal: TASK_TYPE = bank
svm_sre16_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
svm_sre16_bank_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
svm_sre16_bank_features-only_bal: MODEL_NAME = features_only
svm_sre16_bank_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_bank_features-only_bal: core

lr_sre16_bank_features-only_bal: TASK_TYPE = bank
lr_sre16_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
lr_sre16_bank_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
lr_sre16_bank_features-only_bal: MODEL_NAME = features_only
lr_sre16_bank_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_bank_features-only_bal: core

lr_sre16_bank_tf-idf_bal: TASK_TYPE = bank
lr_sre16_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
lr_sre16_bank_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
lr_sre16_bank_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre16_bank_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_bank_tf-idf_bal: core

svm_sre16_bank_bow_bal: TASK_TYPE = bank
svm_sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_bow_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
svm_sre16_bank_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
svm_sre16_bank_bow_bal: MODEL_NAME = bow
svm_sre16_bank_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_bank_bow_bal: core

lr_sre16_bank_bow_bal: TASK_TYPE = bank
lr_sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_bow_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
lr_sre16_bank_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
lr_sre16_bank_bow_bal: MODEL_NAME = bow
lr_sre16_bank_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_bank_bow_bal: core

sre16_bank_features_only_bal: TASK_TYPE = bank
sre16_bank_features_only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre16_bank_features_only_bal: TEST_TABLE = $(SENTIRUEVAL2016)/bank_test.csv
sre16_bank_features_only_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/bank_train_balanced.csv
sre16_bank_features_only_bal: MODEL_NAME = features_only
sre16_bank_features_only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
sre16_bank_features_only_bal: core

svm_sre16_tcc_tf-idf_bal: TASK_TYPE = ttk
svm_sre16_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
svm_sre16_tcc_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
svm_sre16_tcc_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre16_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_tcc_tf-idf_bal: core

lr_sre16_tcc_tf-idf_bal: TASK_TYPE = ttk
lr_sre16_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
lr_sre16_tcc_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
lr_sre16_tcc_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre16_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_tcc_tf-idf_bal: core

lr_sre16_tcc_features-only_bal: TASK_TYPE = ttk
lr_sre16_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
lr_sre16_tcc_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
lr_sre16_tcc_features-only_bal: MODEL_NAME = features_only
lr_sre16_tcc_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_tcc_features-only_bal: core

svm_sre16_tcc_features-only_bal: TASK_TYPE = ttk
svm_sre16_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
svm_sre16_tcc_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
svm_sre16_tcc_features-only_bal: MODEL_NAME = features_only
svm_sre16_tcc_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_tcc_features-only_bal: core

svm_sre16_tcc_bow_bal: TASK_TYPE = ttk
svm_sre16_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_bow_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
svm_sre16_tcc_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
svm_sre16_tcc_bow_bal: MODEL_NAME = bow
svm_sre16_tcc_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
svm_sre16_tcc_bow_bal: core

lr_sre16_tcc_bow_bal: TASK_TYPE = ttk
lr_sre16_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_bow_bal: TEST_TABLE = $(SENTIRUEVAL2016)/ttk_test.csv
lr_sre16_tcc_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2016)/ttk_train_balanced.csv
lr_sre16_tcc_bow_bal: MODEL_NAME = bow
lr_sre16_tcc_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon.csv
lr_sre16_tcc_bow_bal: core

svm_sre15_tcc_tf-idf_imb: TASK_TYPE = ttk
svm_sre15_tcc_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_tf-idf_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_tf-idf_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
svm_sre15_tcc_tf-idf_imb: MODEL_NAME = tf_idf
svm_sre15_tcc_tf-idf_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_tf-idf_imb: core

svm_sre15_tcc_features-only_imb: TASK_TYPE = ttk
svm_sre15_tcc_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_features-only_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_features-only_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
svm_sre15_tcc_features-only_imb: MODEL_NAME = features_only
svm_sre15_tcc_features-only_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_features-only_imb: core

lr_sre15_tcc_features-only_imb: TASK_TYPE = ttk
lr_sre15_tcc_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_features-only_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_features-only_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
lr_sre15_tcc_features-only_imb: MODEL_NAME = features_only
lr_sre15_tcc_features-only_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_features-only_imb: core

lr_sre15_tcc_tf-idf_imb: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_tf-idf_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
lr_sre15_tcc_tf-idf_imb: MODEL_NAME = tf_idf
lr_sre15_tcc_tf-idf_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_tf-idf_imb: core

lr_sre15_tcc_tf-idf-delta_imb: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf-delta_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf-delta_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_tf-idf-delta_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
lr_sre15_tcc_tf-idf-delta_imb: MODEL_NAME = tf_idf_delta
lr_sre15_tcc_tf-idf-delta_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_tf-idf-delta_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_tf-idf-delta_imb: core

sre15_tcc_w2v_imb: TASK_TYPE = ttk
sre15_tcc_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_tcc_w2v_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
sre15_tcc_w2v_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
sre15_tcc_w2v_imb: MODEL_NAME = w2v
sre15_tcc_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
sre15_tcc_w2v_imb: core

svm_sre15_tcc_bow_imb: TASK_TYPE = ttk
svm_sre15_tcc_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_bow_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_bow_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
svm_sre15_tcc_bow_imb: MODEL_NAME = bow
svm_sre15_tcc_bow_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_bow_imb: core

lr_sre15_tcc_bow_imb: TASK_TYPE = ttk
lr_sre15_tcc_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_bow_imb: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_bow_imb: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train.csv
lr_sre15_tcc_bow_imb: MODEL_NAME = bow
lr_sre15_tcc_bow_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_bow_imb: core

svm_sre15_tcc_bow_bal: TASK_TYPE = ttk
svm_sre15_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_bow_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
svm_sre15_tcc_bow_bal: MODEL_NAME = bow
svm_sre15_tcc_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_bow_bal: core

lr_sre15_tcc_bow_bal: TASK_TYPE = ttk
lr_sre15_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_bow_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_bow_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
lr_sre15_tcc_bow_bal: MODEL_NAME = bow
lr_sre15_tcc_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_bow_bal: core

svm_sre15_tcc_tf-idf_bal: TASK_TYPE = ttk
svm_sre15_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
svm_sre15_tcc_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre15_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_tf-idf_bal: core

lr_sre15_tcc_features-only_bal: TASK_TYPE = ttk
lr_sre15_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
lr_sre15_tcc_features-only_bal: MODEL_NAME = features_only
lr_sre15_tcc_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_features-only_bal: core

svm_sre15_tcc_features-only_bal: TASK_TYPE = ttk
svm_sre15_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_features-only_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
svm_sre15_tcc_features-only_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
svm_sre15_tcc_features-only_bal: MODEL_NAME = features_only
svm_sre15_tcc_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_features-only_bal: core

lr_sre15_tcc_tf-idf_bal: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf_bal: TEST_TABLE = $(SENTIRUEVAL2015)/ttk_test.csv
lr_sre15_tcc_tf-idf_bal: TRAIN_TABLE = $(SENTIRUEVAL2015)/ttk_train_balanced.csv
lr_sre15_tcc_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre15_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_tf-idf_bal: core

core:
	mkdir -p $(MODEL_OUTDIR)
	# Extracting data
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(TASK_TYPE) romipdata $(TRAIN_TABLE) $(TEST_TABLE) $(MODEL_PROB) $(MODEL_TEST) $(MODEL_PCONF)
	echo "$(CLASSIFIER_LIBRARY)"
	if [ "$(CLASSIFIER_LIBRARY)" = "liblinear" ]; then \
		$(LIBLINEAR_ROOT)train -q $(LIBLINEAR_MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL) ; \
	elif [ "$(CLASSIFIER_LIBRARY)" = "svm" ]; then \
		$(SVM_ROOT)svm-train -q $(SVM_MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL) ; \
	else \
		exit; \
	fi
	# Predicting
	$(PREDICT)predict.py $(CLASSIFIER_LIBRARY) $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF) $(MODEL_OUT)
	# Creating result folder
	mkdir -p result
	# Copy result into result directory
	cp $(MODEL_OUT) ./result
	# Estimating model
	cd ../models/ && ./eval.py $(TASK_TYPE) ../run/$(MODEL_OUT) ../run/$(ETALON_RESULT) ../run/$(MODEL_ERROR)

theano_core:
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(SETTING_NAME) $(VECTORIZER_TYPE) $(NETWORK_TYPE) $(TASK_TYPE) $(TABLE)

theano_diagnostic:
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(SETTING_NAME) $(VECTORIZER_TYPE) $(NETWORK_TYPE) $(TASK_TYPE) $(TEST_TABLE) $(TRAIN_TABLE) $(ETALON_RESULT)

keras_core:
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(TASK_TYPE) $(TEST_TABLE) $(TRAIN_TABLE) $(ETALON_RESULT)

theano_core_test:
	# Predicting
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(SETTING_NAME) $(VECTORIZER_TYPE) 'rnn' $(TASK_TYPE) $(TABLE) $(MODEL_OUT)
	# Estimating model
	cd ../models/ && ./eval.py $(TASK_TYPE) ../run/$(MODEL_OUT) ../run/$(ETALON_RESULT) ../run/$(MODEL_ERROR)

refresh_user_collection:
	cd $(USERCOLLECTION) && ./init.sh

clean_results:
	rm ./result/*.out
