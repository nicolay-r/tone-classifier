# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm/
# Root of the problem and training data
DATA_ROOT=../models/
# SVM prediction script
SVM_PREDICT=../models/core/
MODEL_CORE=../models/core/

#remove TASK_TYPE

# Defining a default model
MODEL_OPTIONS=	-t 0
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
# Test
#
user_tf_idf_bank_balanced_2016: TASK_TYPE = bank
user_tf_idf_bank_balanced_2016: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
user_tf_idf_bank_balanced_2016: TEST_TABLE = bank_test_user
user_tf_idf_bank_balanced_2016: TRAIN_TABLE = bank_train_balanced_2016
user_tf_idf_bank_balanced_2016: MODEL_OPTIONS= -t 0 -c 0.5
user_tf_idf_bank_balanced_2016: MODEL_NAME = tf_idf
user_tf_idf_bank_balanced_2016: ETALON_RESULT = $(USERCOLLECTION)$(TASK_TYPE)_etalon_user.xml
user_tf_idf_bank_balanced_2016: refresh_user_collection
user_tf_idf_bank_balanced_2016: core

#
# BANK task 2015
#
bag_of_words_bank_imbalanced: TASK_TYPE = bank
bag_of_words_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
bag_of_words_bank_imbalanced: TEST_TABLE = bank_test_noname
bag_of_words_bank_imbalanced: TRAIN_TABLE = bank_train_noname
bag_of_words_bank_imbalanced: MODEL_NAME = bag_of_words
bag_of_words_bank_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
bag_of_words_bank_imbalanced: core

tf_idf_bank_imbalanced: TASK_TYPE = bank
tf_idf_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_imbalanced: TEST_TABLE = bank_test_noname
tf_idf_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_bank_imbalanced: MODEL_NAME = tf_idf
tf_idf_bank_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
tf_idf_bank_imbalanced: core

tf_idf_dict_bank_imbalanced: TASK_TYPE = bank
tf_idf_dict_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_dict_bank_imbalanced: TEST_TABLE = bank_test_noname
tf_idf_dict_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_dict_bank_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_bank_imbalanced: core

tf_idf_bank_balanced: TASK_TYPE = bank
tf_idf_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced: MODEL_NAME = tf_idf
tf_idf_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced: core

bag_of_words_bank_balanced: TASK_TYPE = bank
bag_of_words_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
bag_of_words_bank_balanced: TEST_TABLE = bank_test_noname
bag_of_words_bank_balanced: TRAIN_TABLE = bank_train_balanced
bag_of_words_bank_balanced: MODEL_NAME = bag_of_words
bag_of_words_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
bag_of_words_bank_balanced: core

tf_idf_bank_balanced_cost0.1: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.1: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.1: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.1: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.1: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.1: MODEL_OPTIONS = -t 0 -c 0.1
tf_idf_bank_balanced_cost0.1: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.1: core

tf_idf_bank_balanced_cost0.2: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.2: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.2: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.2: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.2: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.2: MODEL_OPTIONS = -t 0 -c 0.2
tf_idf_bank_balanced_cost0.2: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.2: core

tf_idf_bank_balanced_cost0.3: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.3: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.3: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.3: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.3: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.3: MODEL_OPTIONS = -t 0 -c 0.3
tf_idf_bank_balanced_cost0.3: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.3: core

tf_idf_bank_balanced_cost0.4: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.4: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.4: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.4: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.4: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.4: MODEL_OPTIONS = -t 0 -c 0.4
tf_idf_bank_balanced_cost0.4: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.4: core

tf_idf_bank_balanced_cost0.5: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.5: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.5: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.5: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.5: MODEL_OPTIONS = -t 0 -c 0.5
tf_idf_bank_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.5: core

tf_idf_bank_balanced_cost0.6: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.6: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.6: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.6: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.6: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.6: MODEL_OPTIONS = -t 0 -c 0.6
tf_idf_bank_balanced_cost0.6: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.6: core

tf_idf_bank_balanced_cost0.7: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.7: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.7: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.7: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.7: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.7: MODEL_OPTIONS = -t 0 -c 0.7
tf_idf_bank_balanced_cost0.7: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.7: core

tf_idf_bank_balanced_cost0.8: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.8: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.8: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.8: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.8: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.8: MODEL_OPTIONS = -t 0 -c 0.8
tf_idf_bank_balanced_cost0.8: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.8: core

tf_idf_bank_balanced_cost0.9: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.9: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.9: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.9: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.9: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.9: MODEL_OPTIONS = -t 0 -c 0.9
tf_idf_bank_balanced_cost0.9: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.9: core

tf_idf_bank_balanced_cost1.0: TASK_TYPE = bank
tf_idf_bank_balanced_cost1.0: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost1.0: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost1.0: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost1.0: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost1.0: MODEL_OPTIONS = -t 0 -c 1.0
tf_idf_bank_balanced_cost1.0: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost1.0: core

tf_idf_dict_bank_balanced: TASK_TYPE = bank
tf_idf_dict_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_dict_bank_balanced: TEST_TABLE = bank_test_noname
tf_idf_dict_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_dict_bank_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_bank_balanced: core

#
# Bank task 2016
#
16_tf_idf_bank_imbalanced15: TASK_TYPE = bank
16_tf_idf_bank_imbalanced15: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced15: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced15: TRAIN_TABLE = bank_train_noname
16_tf_idf_bank_imbalanced15: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced15: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced15: core

16_tf_idf_bank_imbalanced16: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16: core

16_tf_idf_bank_imbalanced16_cost0.1: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.1: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.1: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.1: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.1: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.1: MODEL_OPTIONS=	-t 0 -c 0.1
16_tf_idf_bank_imbalanced16_cost0.1: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.1: core

16_tf_idf_bank_imbalanced16_cost0.2: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.2: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.2: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.2: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.2: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.2: MODEL_OPTIONS=	-t 0 -c 0.2
16_tf_idf_bank_imbalanced16_cost0.2: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.2: core

16_tf_idf_bank_imbalanced16_cost0.3: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.3: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.3: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.3: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.3: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.3: MODEL_OPTIONS=	-t 0 -c 0.3
16_tf_idf_bank_imbalanced16_cost0.3: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.3: core

16_tf_idf_bank_imbalanced16_cost0.4: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.4: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.4: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.4: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.4: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.4: MODEL_OPTIONS=	-t 0 -c 0.4
16_tf_idf_bank_imbalanced16_cost0.4: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.4: core

16_tf_idf_bank_imbalanced16_cost0.5: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.5: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.5: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_bank_imbalanced16_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.5: core

16_tf_idf_bank_imbalanced16_cost0.6: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.6: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.6: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.6: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.6: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.6: MODEL_OPTIONS=	-t 0 -c 0.6
16_tf_idf_bank_imbalanced16_cost0.6: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.6: core

16_tf_idf_bank_imbalanced16_cost0.7: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.7: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.7: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.7: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.7: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.7: MODEL_OPTIONS=	-t 0 -c 0.7
16_tf_idf_bank_imbalanced16_cost0.7: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.7: core

16_tf_idf_bank_imbalanced16_cost0.8: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.8: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.8: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.8: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.8: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.8: MODEL_OPTIONS=	-t 0 -c 0.8
16_tf_idf_bank_imbalanced16_cost0.8: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.8: core

16_tf_idf_bank_imbalanced16_cost0.9: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost0.9: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost0.9: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost0.9: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost0.9: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost0.9: MODEL_OPTIONS=	-t 0 -c 0.9
16_tf_idf_bank_imbalanced16_cost0.9: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost0.9: core

16_tf_idf_bank_imbalanced16_cost1.0: TASK_TYPE = bank
16_tf_idf_bank_imbalanced16_cost1.0: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_imbalanced16_cost1.0: TEST_TABLE = bank_test_2016
16_tf_idf_bank_imbalanced16_cost1.0: TRAIN_TABLE = bank_train_2016
16_tf_idf_bank_imbalanced16_cost1.0: MODEL_NAME = tf_idf
16_tf_idf_bank_imbalanced16_cost1.0: MODEL_OPTIONS=	-t 0 -c 1.0
16_tf_idf_bank_imbalanced16_cost1.0: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_imbalanced16_cost1.0: core

16_tf_idf_bank_balanced15: TASK_TYPE = bank
16_tf_idf_bank_balanced15: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced15: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced15: TRAIN_TABLE = bank_train_balanced
16_tf_idf_bank_balanced15: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced15: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced15: core

16_tf_idf_bank_balanced16: TASK_TYPE = bank
16_tf_idf_bank_balanced16: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16: core

16_tf_idf_bank_balanced16_cost0.1: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.1: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.1: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.1: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.1: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.1: MODEL_OPTIONS=	-t 0 -c 0.1
16_tf_idf_bank_balanced16_cost0.1: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.1: core

16_tf_idf_bank_balanced16_cost0.2: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.2: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.2: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.2: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.2: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.2: MODEL_OPTIONS=	-t 0 -c 0.2
16_tf_idf_bank_balanced16_cost0.2: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.2: core

16_tf_idf_bank_balanced16_cost0.3: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.3: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.3: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.3: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.3: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.3: MODEL_OPTIONS=	-t 0 -c 0.3
16_tf_idf_bank_balanced16_cost0.3: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.3: core

16_tf_idf_bank_balanced16_cost0.4: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.4: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.4: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.4: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.4: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.4: MODEL_OPTIONS=	-t 0 -c 0.4
16_tf_idf_bank_balanced16_cost0.4: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.4: core

16_tf_idf_bank_balanced16_cost0.5: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.5: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.5: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_bank_balanced16_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.5: core

16_tf_idf_bank_balanced16_cost0.6: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.6: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.6: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.6: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.6: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.6: MODEL_OPTIONS=	-t 0 -c 0.6
16_tf_idf_bank_balanced16_cost0.6: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.6: core

16_tf_idf_bank_balanced16_cost0.7: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.7: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.7: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.7: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.7: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.7: MODEL_OPTIONS=	-t 0 -c 0.7
16_tf_idf_bank_balanced16_cost0.7: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.7: core

16_tf_idf_bank_balanced16_cost0.8: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.8: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.8: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.8: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.8: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.8: MODEL_OPTIONS=	-t 0 -c 0.8
16_tf_idf_bank_balanced16_cost0.8: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.8: core

16_tf_idf_bank_balanced16_cost0.9: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost0.9: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost0.9: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost0.9: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost0.9: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost0.9: MODEL_OPTIONS=	-t 0 -c 0.9
16_tf_idf_bank_balanced16_cost0.9: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost0.9: core

16_tf_idf_bank_balanced16_cost1.0: TASK_TYPE = bank
16_tf_idf_bank_balanced16_cost1.0: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced16_cost1.0: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced16_cost1.0: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced16_cost1.0: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced16_cost1.0: MODEL_OPTIONS=	-t 0 -c 1.0
16_tf_idf_bank_balanced16_cost1.0: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced16_cost1.0: core

16_tf_idf_bank_balanced_8k: TASK_TYPE = bank
16_tf_idf_bank_balanced_8k: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_8k: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_8k: TRAIN_TABLE = bank_train_balanced_2016_max
16_tf_idf_bank_balanced_8k: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_8k: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_8k: core

16_tf_idf_bank_balanced_8k_cost0.5: TASK_TYPE = bank
16_tf_idf_bank_balanced_8k_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_8k_cost0.5: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_8k_cost0.5: TRAIN_TABLE = bank_train_balanced_2016_max
16_tf_idf_bank_balanced_8k_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_8k_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_bank_balanced_8k_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_8k_cost0.5: core

# TTK task 2015
#
tf_idf_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced: core

tf_idf_dict_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_dict_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_dict_ttk_imbalanced: TEST_TABLE = ttk_test_noname
tf_idf_dict_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_dict_ttk_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_ttk_imbalanced: core

tf_idf_ttk_balanced: TASK_TYPE = ttk
tf_idf_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_balanced: TEST_TABLE = ttk_test_noname
tf_idf_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_ttk_balanced: MODEL_NAME = tf_idf
tf_idf_ttk_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_balanced: core

tf_idf_ttk_imbalanced_cost0.1: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.1: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.1: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.1: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.1: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.1: MODEL_OPTIONS= -t 0 -c 0.1
tf_idf_ttk_imbalanced_cost0.1: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.1: core

tf_idf_ttk_imbalanced_cost0.2: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.2: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.2: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.2: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.2: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.2: MODEL_OPTIONS= -t 0 -c 0.2
tf_idf_ttk_imbalanced_cost0.2: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.2: core

tf_idf_ttk_imbalanced_cost0.3: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.3: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.3: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.3: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.3: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.3: MODEL_OPTIONS= -t 0 -c 0.3
tf_idf_ttk_imbalanced_cost0.3: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.3: core

tf_idf_ttk_imbalanced_cost0.4: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.4: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.4: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.4: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.4: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.4: MODEL_OPTIONS= -t 0 -c 0.4
tf_idf_ttk_imbalanced_cost0.4: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.4: core

tf_idf_ttk_imbalanced_cost0.5: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.5: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.5: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.5: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.5: MODEL_OPTIONS= -t 0 -c 0.5
tf_idf_ttk_imbalanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.5: core

tf_idf_ttk_imbalanced_cost0.6: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.6: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.6: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.6: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.6: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.6: MODEL_OPTIONS= -t 0 -c 0.6
tf_idf_ttk_imbalanced_cost0.6: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.6: core

tf_idf_ttk_imbalanced_cost0.7: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.7: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.7: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.7: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.7: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.7: MODEL_OPTIONS= -t 0 -c 0.7
tf_idf_ttk_imbalanced_cost0.7: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.7: core

tf_idf_ttk_imbalanced_cost0.8: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.8: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.8: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.8: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.8: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.8: MODEL_OPTIONS= -t 0 -c 0.8
tf_idf_ttk_imbalanced_cost0.8: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.8: core

tf_idf_ttk_imbalanced_cost0.9: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost0.9: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost0.9: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost0.9: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost0.9: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost0.9: MODEL_OPTIONS= -t 0 -c 0.9
tf_idf_ttk_imbalanced_cost0.9: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost0.9: core

tf_idf_ttk_imbalanced_cost1.0: TASK_TYPE = ttk
tf_idf_ttk_imbalanced_cost1.0: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced_cost1.0: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced_cost1.0: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced_cost1.0: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced_cost1.0: MODEL_OPTIONS= -t 0 -c 1.0
tf_idf_ttk_imbalanced_cost1.0: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced_cost1.0: core

tf_idf_dict_ttk_balanced: TASK_TYPE = ttk
tf_idf_dict_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
tf_idf_dict_ttk_balanced: TEST_TABLE = ttk_test_noname
tf_idf_dict_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_dict_ttk_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_ttk_balanced: core

# TTK task 2016
#
16_tf_idf_ttk_imbalanced15: TASK_TYPE = ttk
16_tf_idf_ttk_imbalanced15: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_imbalanced15: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_imbalanced15: TRAIN_TABLE = ttk_train_noname
16_tf_idf_ttk_imbalanced15: MODEL_NAME = tf_idf
16_tf_idf_ttk_imbalanced15: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_imbalanced15: core

16_tf_idf_ttk_imbalanced16: TASK_TYPE = ttk
16_tf_idf_ttk_imbalanced16: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_imbalanced16: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_imbalanced16: TRAIN_TABLE = ttk_train_2016
16_tf_idf_ttk_imbalanced16: MODEL_NAME = tf_idf
16_tf_idf_ttk_imbalanced16: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_imbalanced16: core

16_tf_idf_ttk_balanced15: TASK_TYPE = ttk
16_tf_idf_ttk_balanced15: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced15: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced15: TRAIN_TABLE = ttk_train_balanced
16_tf_idf_ttk_balanced15: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced15: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced15: core

16_tf_idf_ttk_balanced16: TASK_TYPE = ttk
16_tf_idf_ttk_balanced16: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced16: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced16: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced16: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced16: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced16: core

16_tf_idf_ttk_balanced_cost0.1: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.1: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.1: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.1: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.1: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.1: MODEL_OPTIONS=	-t 0 -c 0.1
16_tf_idf_ttk_balanced_cost0.1: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.1: core

16_tf_idf_ttk_balanced_cost0.2: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.2: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.2: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.2: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.2: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.2: MODEL_OPTIONS=	-t 0 -c 0.2
16_tf_idf_ttk_balanced_cost0.2: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.2: core

16_tf_idf_ttk_balanced_cost0.3: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.3: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.3: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.3: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.3: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.3: MODEL_OPTIONS=	-t 0 -c 0.3
16_tf_idf_ttk_balanced_cost0.3: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.3: core

16_tf_idf_ttk_balanced_cost0.4: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.4: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.4: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.4: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.4: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.4: MODEL_OPTIONS=	-t 0 -c 0.4
16_tf_idf_ttk_balanced_cost0.4: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.4: core

16_tf_idf_ttk_balanced_cost0.5: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.5: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.5: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_ttk_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.5: core

16_tf_idf_ttk_balanced_cost0.6: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.6: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.6: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.6: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.6: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.6: MODEL_OPTIONS=	-t 0 -c 0.6
16_tf_idf_ttk_balanced_cost0.6: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.6: core

16_tf_idf_ttk_balanced_cost0.7: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.7: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.7: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.7: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.7: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.7: MODEL_OPTIONS=	-t 0 -c 0.7
16_tf_idf_ttk_balanced_cost0.7: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.7: core

16_tf_idf_ttk_balanced_cost0.8: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.8: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.8: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.8: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.8: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.8: MODEL_OPTIONS=	-t 0 -c 0.8
16_tf_idf_ttk_balanced_cost0.8: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.8: core

16_tf_idf_ttk_balanced_cost0.9: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.9: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.9: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.9: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.9: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.9: MODEL_OPTIONS=	-t 0 -c 0.9
16_tf_idf_ttk_balanced_cost0.9: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.9: core

16_tf_idf_ttk_balanced_cost1.0: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost1.0: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost1.0: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost1.0: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost1.0: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost1.0: MODEL_OPTIONS=	-t 0 -c 1.0
16_tf_idf_ttk_balanced_cost1.0: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost1.0: core

16_tf_idf_ttk_balanced_6k: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_6k: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_6k: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_6k: TRAIN_TABLE = ttk_train_balanced_2016_max
16_tf_idf_ttk_balanced_6k: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_6k: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_6k: core

16_tf_idf_ttk_balanced_6k_cost0.5: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_6k_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_6k_cost0.5: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_6k_cost0.5: TRAIN_TABLE = ttk_train_balanced_2016_max
16_tf_idf_ttk_balanced_6k_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_6k_cost0.5: MODEL_OPTIONS= -t 0 -c 0.5
16_tf_idf_ttk_balanced_6k_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_6k_cost0.5: core

core:
	echo $(MODEL_OPTIONS)
	mkdir -p $(MODEL_OUTDIR)
	# Extracting data
	$(MODEL_ROOT)/$(MODEL_NAME)_model.py $(TASK_TYPE) romipdata $(TRAIN_TABLE) $(TEST_TABLE) $(MODEL_PROB) $(MODEL_TEST) $(MODEL_PCONF)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Predicting
	$(SVM_PREDICT)predict.py $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	$(MODEL_CORE)pg2x_data.py $(MODEL_PCONF) $(MODEL_OUT)
	# Creating result folder
	mkdir -p result
	# Copy result into result directory
	cp $(MODEL_OUT) ./result
	# Estimating model
	cd ../eval/ && nodejs calc.js $(TASK_TYPE) ../run/$(MODEL_OUT) ../run/$(ETALON_RESULT)


refresh_user_collection:
	cd $(USERCOLLECTION) && ./init.sh

clean_results:
	rm ./result/*.out
