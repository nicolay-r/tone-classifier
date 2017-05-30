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
SVM_MODEL_OPTIONS=	-t 0 -c 1 -m 200 -e 0.0001 -q
LIBLINEAR_MODEL_OPTIONS= -s 7 -c 0.5
CLASSIFIER_LIBRARY= svm
MODEL_ROOT	=	$(DATA_ROOT)
MODEL_OUTDIR= 	$(MODEL_ROOT)/out/
MODEL_PROB	=	$(MODEL_OUTDIR)$(MODEL_NAME).prob
MODEL_TEST	=	$(MODEL_OUTDIR)$(MODEL_NAME).test
MODEL_PCONF	=	$(MODEL_OUTDIR)$(MODEL_NAME).pconf
MODEL_OUT	=	$(MODEL_OUTDIR)$(MODEL_NAME).out
MODEL_TRAIN	=	$(MODEL_OUTDIR)$(MODEL_NAME).train
MODEL_MODEL	=	$(MODEL_TRAIN).model

SENTIRUEVAL2015 = ../data/collections/SentiRuEval-2015/
SENTIRUEVAL2016 = ../data/collections/SentiRuEval-2016/
USERCOLLECTION = ../data/collections/user/

#
# SentiRuEval-2015
#

svm_sre15_bank_features-only_imb: TASK_TYPE = bank
svm_sre15_bank_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_features-only_imb: TEST_TABLE = bank_test_noname
svm_sre15_bank_features-only_imb: TRAIN_TABLE = bank_train_noname
svm_sre15_bank_features-only_imb: MODEL_NAME = features_only
svm_sre15_bank_features-only_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_features-only_imb: core

svm_sre15_bank_features-only_bal: TASK_TYPE = bank
svm_sre15_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_features-only_bal: TEST_TABLE = bank_test_noname
svm_sre15_bank_features-only_bal: TRAIN_TABLE = bank_train_balanced
svm_sre15_bank_features-only_bal: MODEL_NAME = features_only
svm_sre15_bank_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_features-only_bal: core

lr_sre15_bank_features-only_imb: TASK_TYPE = bank
lr_sre15_bank_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_features-only_imb: TEST_TABLE = bank_test_noname
lr_sre15_bank_features-only_imb: TRAIN_TABLE = bank_train_noname
lr_sre15_bank_features-only_imb: MODEL_NAME = features_only
lr_sre15_bank_features-only_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_features-only_imb: core

lr_sre15_bank_features-only_bal: TASK_TYPE = bank
lr_sre15_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_features-only_bal: TEST_TABLE = bank_test_noname
lr_sre15_bank_features-only_bal: TRAIN_TABLE = bank_train_balanced
lr_sre15_bank_features-only_bal: MODEL_NAME = features_only
lr_sre15_bank_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_features-only_bal: core

svm_sre15_bank_w2v_imb: TASK_TYPE = bank
svm_sre15_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_w2v_imb: TEST_TABLE = bank_test_noname
svm_sre15_bank_w2v_imb: TRAIN_TABLE = bank_train_noname
svm_sre15_bank_w2v_imb: MODEL_NAME = w2v
svm_sre15_bank_w2v_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_w2v_imb: core

svm_sre15_bank_w2v_bal: TASK_TYPE = bank
svm_sre15_bank_w2v_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_w2v_bal: TEST_TABLE = bank_test_noname
svm_sre15_bank_w2v_bal: TRAIN_TABLE = bank_train_balanced
svm_sre15_bank_w2v_bal: MODEL_NAME = w2v
svm_sre15_bank_w2v_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_w2v_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_w2v_bal: core

lr_sre15_bank_w2v_imb: TASK_TYPE = bank
lr_sre15_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_w2v_imb: TEST_TABLE = bank_test_noname
lr_sre15_bank_w2v_imb: TRAIN_TABLE = bank_train_noname
lr_sre15_bank_w2v_imb: MODEL_NAME = w2v
lr_sre15_bank_w2v_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_w2v_imb: core

lr_sre15_bank_w2v_bal: TASK_TYPE = bank
lr_sre15_bank_w2v_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_w2v_bal: TEST_TABLE = bank_test_noname
lr_sre15_bank_w2v_bal: TRAIN_TABLE = bank_train_balanced
lr_sre15_bank_w2v_bal: MODEL_NAME = w2v
lr_sre15_bank_w2v_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_w2v_bal: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_w2v_bal: core

svm_sre15_bank_bow_imb: TASK_TYPE = bank
svm_sre15_bank_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_bow_imb: TEST_TABLE = bank_test_noname
svm_sre15_bank_bow_imb: TRAIN_TABLE = bank_train_noname
svm_sre15_bank_bow_imb: MODEL_NAME = bow
svm_sre15_bank_bow_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_bow_imb: core

svm_sre15_bank_bow_bal: TASK_TYPE = bank
svm_sre15_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_bow_bal: TEST_TABLE = bank_test_noname
svm_sre15_bank_bow_bal: TRAIN_TABLE = bank_train_balanced
svm_sre15_bank_bow_bal: MODEL_NAME = bow
svm_sre15_bank_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_bank_bow_bal: core

lr_sre15_bank_bow_imb: TASK_TYPE = bank
lr_sre15_bank_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_bow_imb: TEST_TABLE = bank_test_noname
lr_sre15_bank_bow_imb: TRAIN_TABLE = bank_train_noname
lr_sre15_bank_bow_imb: MODEL_NAME = bow
lr_sre15_bank_bow_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_bow_imb: core

lr_sre15_bank_bow_bal: TASK_TYPE = bank
lr_sre15_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_bow_bal: TEST_TABLE = bank_test_noname
lr_sre15_bank_bow_bal: TRAIN_TABLE = bank_train_balanced
lr_sre15_bank_bow_bal: MODEL_NAME = bow
lr_sre15_bank_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_bank_bow_bal: core

#sre16_bank_bow_bal: TASK_TYPE = bank
#sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
#sre16_bank_bow_bal: TEST_TABLE = bank_test_2016
#sre16_bank_bow_bal: TRAIN_TABLE = bank_train_balanced_2016
#sre16_bank_bow_bal: MODEL_NAME = bow
#sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
#sre16_bank_bow_bal: core

svm_sre15_bank_tf-idf_imb: TASK_TYPE = bank
svm_sre15_bank_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_tf-idf_imb: TEST_TABLE = bank_test_noname
svm_sre15_bank_tf-idf_imb: TRAIN_TABLE = bank_train_noname
svm_sre15_bank_tf-idf_imb: MODEL_NAME = tf_idf
svm_sre15_bank_tf-idf_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
svm_sre15_bank_tf-idf_imb: core

svm_sre15_bank_tf-idf_bal: TASK_TYPE = bank
svm_sre15_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_bank_tf-idf_bal: TEST_TABLE = bank_test_noname
svm_sre15_bank_tf-idf_bal: TRAIN_TABLE = bank_train_balanced
svm_sre15_bank_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre15_bank_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_bank_tf-idf_bal: core

lr_sre15_bank_tf-idf_imb: TASK_TYPE = bank
lr_sre15_bank_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_tf-idf_imb: TEST_TABLE = bank_test_noname
lr_sre15_bank_tf-idf_imb: TRAIN_TABLE = bank_train_noname
lr_sre15_bank_tf-idf_imb: MODEL_NAME = tf_idf
lr_sre15_bank_tf-idf_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.csv
lr_sre15_bank_tf-idf_imb: core

lr_sre15_bank_tf-idf_bal: TASK_TYPE = bank
lr_sre15_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_bank_tf-idf_bal: TEST_TABLE = bank_test_noname
lr_sre15_bank_tf-idf_bal: TRAIN_TABLE = bank_train_balanced
lr_sre15_bank_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre15_bank_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_bank_tf-idf_bal: core

svm_sre16_bank_tf-idf_bal: TASK_TYPE = bank
svm_sre16_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_tf-idf_bal: TEST_TABLE = bank_test_2016
svm_sre16_bank_tf-idf_bal: TRAIN_TABLE = bank_train_balanced_2016
svm_sre16_bank_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre16_bank_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_bank_tf-idf_bal: core

svm_sre16_bank_features-only_bal: TASK_TYPE = bank
svm_sre16_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_features-only_bal: TEST_TABLE = bank_test_2016
svm_sre16_bank_features-only_bal: TRAIN_TABLE = bank_train_balanced_2016
svm_sre16_bank_features-only_bal: MODEL_NAME = features_only
svm_sre16_bank_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_bank_features-only_bal: core

lr_sre16_bank_features-only_bal: TASK_TYPE = bank
lr_sre16_bank_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_features-only_bal: TEST_TABLE = bank_test_2016
lr_sre16_bank_features-only_bal: TRAIN_TABLE = bank_train_balanced_2016
lr_sre16_bank_features-only_bal: MODEL_NAME = features_only
lr_sre16_bank_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_bank_features-only_bal: core

lr_sre16_bank_tf-idf_bal: TASK_TYPE = bank
lr_sre16_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_tf-idf_bal: TEST_TABLE = bank_test_2016
lr_sre16_bank_tf-idf_bal: TRAIN_TABLE = bank_train_balanced_2016
lr_sre16_bank_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre16_bank_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_bank_tf-idf_bal: core

svm_sre16_bank_bow_bal: TASK_TYPE = bank
svm_sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_bank_bow_bal: TEST_TABLE = bank_test_2016
svm_sre16_bank_bow_bal: TRAIN_TABLE = bank_train_balanced_2016
svm_sre16_bank_bow_bal: MODEL_NAME = bow
svm_sre16_bank_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_bank_bow_bal: core

lr_sre16_bank_bow_bal: TASK_TYPE = bank
lr_sre16_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_bank_bow_bal: TEST_TABLE = bank_test_2016
lr_sre16_bank_bow_bal: TRAIN_TABLE = bank_train_balanced_2016
lr_sre16_bank_bow_bal: MODEL_NAME = bow
lr_sre16_bank_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_bank_bow_bal: core

sre16_bank_features_only_bal: TASK_TYPE = bank
sre16_bank_features_only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre16_bank_features_only_bal: TEST_TABLE = bank_test_2016
sre16_bank_features_only_bal: TRAIN_TABLE = bank_train_balanced_2016
sre16_bank_features_only_bal: MODEL_NAME = features_only
sre16_bank_features_only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
sre16_bank_features_only_bal: core

svm_sre16_tcc_tf-idf_bal: TASK_TYPE = ttk
svm_sre16_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_tf-idf_bal: TEST_TABLE = ttk_test_2016
svm_sre16_tcc_tf-idf_bal: TRAIN_TABLE = ttk_train_balanced_2016
svm_sre16_tcc_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre16_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_tcc_tf-idf_bal: core

lr_sre16_tcc_tf-idf_bal: TASK_TYPE = ttk
lr_sre16_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_tf-idf_bal: TEST_TABLE = ttk_test_2016
lr_sre16_tcc_tf-idf_bal: TRAIN_TABLE = ttk_train_balanced_2016
lr_sre16_tcc_tf-idf_bal: MODEL_NAME = tf_idf
lr_sre16_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_tcc_tf-idf_bal: core

lr_sre16_tcc_features-only_bal: TASK_TYPE = ttk
lr_sre16_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_features-only_bal: TEST_TABLE = ttk_test_2016
lr_sre16_tcc_features-only_bal: TRAIN_TABLE = ttk_train_balanced_2016
lr_sre16_tcc_features-only_bal: MODEL_NAME = features_only
lr_sre16_tcc_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_tcc_features-only_bal: core

svm_sre16_tcc_features-only_bal: TASK_TYPE = ttk
svm_sre16_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_features-only_bal: TEST_TABLE = ttk_test_2016
svm_sre16_tcc_features-only_bal: TRAIN_TABLE = ttk_train_balanced_2016
svm_sre16_tcc_features-only_bal: MODEL_NAME = features_only
svm_sre16_tcc_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_tcc_features-only_bal: core

svm_sre16_tcc_bow_bal: TASK_TYPE = ttk
svm_sre16_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre16_tcc_bow_bal: TEST_TABLE = ttk_test_2016
svm_sre16_tcc_bow_bal: TRAIN_TABLE = ttk_train_balanced_2016
svm_sre16_tcc_bow_bal: MODEL_NAME = bow
svm_sre16_tcc_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre16_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
svm_sre16_tcc_bow_bal: core

lr_sre16_tcc_bow_bal: TASK_TYPE = ttk
lr_sre16_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre16_tcc_bow_bal: TEST_TABLE = ttk_test_2016
lr_sre16_tcc_bow_bal: TRAIN_TABLE = ttk_train_balanced_2016
lr_sre16_tcc_bow_bal: MODEL_NAME = bow
lr_sre16_tcc_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre16_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.csv
lr_sre16_tcc_bow_bal: core

svm_sre15_tcc_tf-idf_imb: TASK_TYPE = ttk
svm_sre15_tcc_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_tf-idf_imb: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_tf-idf_imb: TRAIN_TABLE = ttk_train_noname
svm_sre15_tcc_tf-idf_imb: MODEL_NAME = tf_idf
svm_sre15_tcc_tf-idf_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_tf-idf_imb: core

svm_sre15_tcc_features-only_imb: TASK_TYPE = ttk
svm_sre15_tcc_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_features-only_imb: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_features-only_imb: TRAIN_TABLE = ttk_train_noname
svm_sre15_tcc_features-only_imb: MODEL_NAME = features_only
svm_sre15_tcc_features-only_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_features-only_imb: core

lr_sre15_tcc_features-only_imb: TASK_TYPE = ttk
lr_sre15_tcc_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_features-only_imb: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_features-only_imb: TRAIN_TABLE = ttk_train_noname
lr_sre15_tcc_features-only_imb: MODEL_NAME = features_only
lr_sre15_tcc_features-only_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_features-only_imb: core

lr_sre15_tcc_tf-idf_imb: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf_imb: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_tf-idf_imb: TRAIN_TABLE = ttk_train_noname
lr_sre15_tcc_tf-idf_imb: MODEL_NAME = tf_idf
lr_sre15_tcc_tf-idf_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_tf-idf_imb: core

lr_sre15_tcc_tf-idf-delta_imb: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf-delta_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf-delta_imb: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_tf-idf-delta_imb: TRAIN_TABLE = ttk_train_noname
lr_sre15_tcc_tf-idf-delta_imb: MODEL_NAME = tf_idf_delta
lr_sre15_tcc_tf-idf-delta_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_tf-idf-delta_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_tf-idf-delta_imb: core

sre15_tcc_w2v_imb: TASK_TYPE = ttk
sre15_tcc_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_tcc_w2v_imb: TEST_TABLE = ttk_test_noname
sre15_tcc_w2v_imb: TRAIN_TABLE = ttk_train_noname
sre15_tcc_w2v_imb: MODEL_NAME = w2v
sre15_tcc_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
sre15_tcc_w2v_imb: core

svm_sre15_tcc_bow_imb: TASK_TYPE = ttk
svm_sre15_tcc_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_bow_imb: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_bow_imb: TRAIN_TABLE = ttk_train_noname
svm_sre15_tcc_bow_imb: MODEL_NAME = bow
svm_sre15_tcc_bow_imb: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_bow_imb: core

lr_sre15_tcc_bow_imb: TASK_TYPE = ttk
lr_sre15_tcc_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_bow_imb: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_bow_imb: TRAIN_TABLE = ttk_train_noname
lr_sre15_tcc_bow_imb: MODEL_NAME = bow
lr_sre15_tcc_bow_imb: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_bow_imb: core

svm_sre15_tcc_bow_bal: TASK_TYPE = ttk
svm_sre15_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_bow_bal: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_bow_bal: TRAIN_TABLE = ttk_train_balanced
svm_sre15_tcc_bow_bal: MODEL_NAME = bow
svm_sre15_tcc_bow_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_bow_bal: core

lr_sre15_tcc_bow_bal: TASK_TYPE = ttk
lr_sre15_tcc_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_bow_bal: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_bow_bal: TRAIN_TABLE = ttk_train_balanced
lr_sre15_tcc_bow_bal: MODEL_NAME = bow
lr_sre15_tcc_bow_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_bow_bal: core

svm_sre15_tcc_tf-idf_bal: TASK_TYPE = ttk
svm_sre15_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_tf-idf_bal: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_tf-idf_bal: TRAIN_TABLE = ttk_train_balanced
svm_sre15_tcc_tf-idf_bal: MODEL_NAME = tf_idf
svm_sre15_tcc_tf-idf_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_tf-idf_bal: core

lr_sre15_tcc_features-only_bal: TASK_TYPE = ttk
lr_sre15_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_features-only_bal: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_features-only_bal: TRAIN_TABLE = ttk_train_balanced
lr_sre15_tcc_features-only_bal: MODEL_NAME = features_only
lr_sre15_tcc_features-only_bal: CLASSIFIER_LIBRARY = liblinear
lr_sre15_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
lr_sre15_tcc_features-only_bal: core

svm_sre15_tcc_features-only_bal: TASK_TYPE = ttk
svm_sre15_tcc_features-only_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
svm_sre15_tcc_features-only_bal: TEST_TABLE = ttk_test_noname
svm_sre15_tcc_features-only_bal: TRAIN_TABLE = ttk_train_balanced
svm_sre15_tcc_features-only_bal: MODEL_NAME = features_only
svm_sre15_tcc_features-only_bal: CLASSIFIER_LIBRARY = svm
svm_sre15_tcc_features-only_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.csv
svm_sre15_tcc_features-only_bal: core

lr_sre15_tcc_tf-idf_bal: TASK_TYPE = ttk
lr_sre15_tcc_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
lr_sre15_tcc_tf-idf_bal: TEST_TABLE = ttk_test_noname
lr_sre15_tcc_tf-idf_bal: TRAIN_TABLE = ttk_train_balanced
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
		$(LIBLINEAR_ROOT)train $(LIBLINEAR_MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL) ; \
	elif [ "$(CLASSIFIER_LIBRARY)" = "svm" ]; then \
		$(SVM_ROOT)svm-train $(SVM_MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL) ; \
	else \
		exit; \
	fi
	# Predicting
	$(PREDICT)predict.py $(CLASSIFIER_LIBRARY) $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	$(MODEL_ROOT)pg2csv_data.py $(MODEL_PCONF) $(MODEL_OUT)
	# Creating result folder
	mkdir -p result
	# Copy result into result directory
	cp $(MODEL_OUT) ./result
	# Estimating model
	cd ../models/ && ./calc.py $(TASK_TYPE) ../run/$(MODEL_OUT) ../run/$(ETALON_RESULT)


refresh_user_collection:
	cd $(USERCOLLECTION) && ./init.sh

clean_results:
	rm ./result/*.out
