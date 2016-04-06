# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm/
# Root of the problem and training data
DATA_ROOT=../models/
# SVM prediction script
SVM_PREDICT=../models/aux/

#remove TASK_TYPE

# Defining a default model
MODEL_OPTIONS=	-t 0
MODEL_ROOT	=	$(DATA_ROOT)$(MODEL_NAME)
MODEL_OUTDIR= 	$(MODEL_ROOT)/out/
MODEL_PROB	=	$(MODEL_OUTDIR)$(MODEL_NAME).prob
MODEL_TRAIN	=	$(MODEL_OUTDIR)$(MODEL_NAME).train
MODEL_TEST	=	$(MODEL_OUTDIR)$(MODEL_NAME).test
MODEL_PCONF	=	$(MODEL_OUTDIR)$(MODEL_NAME).pconf
MODEL_OUT	=	$(MODEL_OUTDIR)$(MODEL_NAME).out
MODEL_RESULT_OUT = $(MODEL_OUTDIR)$(MODEL_NAME).answer.out
MODEL_MODEL	=	$(MODEL_TRAIN).model

SENTIRUEVAL2015 = ../data/collections/SentiRuEval-2015/
SENTIRUEVAL2016 = ../data/collections/SentiRuEval-2016/
USERCOLLECTION = ../data/collections/user/

#
# Test
#
user_tf_idf_bank_imbalanced: TASK_TYPE = bank
user_tf_idf_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
user_tf_idf_bank_imbalanced: TEST_TABLE = bank_test_user
user_tf_idf_bank_imbalanced: TRAIN_TABLE = bank_train_noname
user_tf_idf_bank_imbalanced: MODEL_NAME = tf_idf
user_tf_idf_bank_imbalanced: ETALON_RESULT = $(USERCOLLECTION)$(TASK_TYPE)_etalon_user.xml
user_tf_idf_bank_imbalanced: core

#
# BANK task 2015
#
tf_idf_bank_imbalanced: TASK_TYPE = bank
tf_idf_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_bank_imbalanced: TEST_TABLE = bank_test_noname
tf_idf_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_bank_imbalanced: MODEL_NAME = tf_idf
tf_idf_bank_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
tf_idf_bank_imbalanced: core

tf_idf_dict_bank_imbalanced: TASK_TYPE = bank
tf_idf_dict_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_bank_imbalanced: TEST_TABLE = bank_test_noname
tf_idf_dict_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_dict_bank_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_bank_imbalanced: core

tf_idf_bank_balanced: TASK_TYPE = bank
tf_idf_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_bank_balanced: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced: MODEL_NAME = tf_idf
tf_idf_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced: core

tf_idf_bank_balanced_cost0.5: TASK_TYPE = bank
tf_idf_bank_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_bank_balanced_cost0.5: TEST_TABLE = bank_test_noname
tf_idf_bank_balanced_cost0.5: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced_cost0.5: MODEL_NAME = tf_idf
tf_idf_bank_balanced_cost0.5: MODEL_OPTIONS = -t 0 -c 0.5
tf_idf_bank_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_bank_balanced_cost0.5: core

tf_idf_dict_bank_balanced: TASK_TYPE = bank
tf_idf_dict_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_bank_balanced: TEST_TABLE = bank_test_noname
tf_idf_dict_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_dict_bank_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_bank_balanced: core

#
# Bank task 2016
#
16_tf_idf_bank_half_balanced: TASK_TYPE = bank
16_tf_idf_bank_half_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_half_balanced: TEST_TABLE = bank_test_2016
16_tf_idf_bank_half_balanced: TRAIN_TABLE = bank_train_balanced
16_tf_idf_bank_half_balanced: MODEL_NAME = tf_idf
16_tf_idf_bank_half_balanced: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_half_balanced: core

16_tf_idf_bank_balanced: TASK_TYPE = bank
16_tf_idf_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_balanced: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced: core

16_tf_idf_bank_balanced_cost0.75: TASK_TYPE = bank
16_tf_idf_bank_balanced_cost0.75: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_cost0.75: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_cost0.75: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced_cost0.75: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_cost0.75: MODEL_OPTIONS= -t 0 -c 0.75
16_tf_idf_bank_balanced_cost0.75: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_cost0.75: core

16_tf_idf_bank_balanced_cost0.5: TASK_TYPE = bank
16_tf_idf_bank_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_cost0.5: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_cost0.5: TRAIN_TABLE = bank_train_balanced_2016
16_tf_idf_bank_balanced_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_bank_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_cost0.5: core

16_tf_idf_bank_balanced_8k: TASK_TYPE = bank
16_tf_idf_bank_balanced_8k: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_8k: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_8k: TRAIN_TABLE = bank_train_balanced_2016_max
16_tf_idf_bank_balanced_8k: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_8k: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_8k: core

16_tf_idf_bank_balanced_8k_cost0.5: TASK_TYPE = bank
16_tf_idf_bank_balanced_8k_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_bank_balanced_8k_cost0.5: TEST_TABLE = bank_test_2016
16_tf_idf_bank_balanced_8k_cost0.5: TRAIN_TABLE = bank_train_balanced_2016_max
16_tf_idf_bank_balanced_8k_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_bank_balanced_8k_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_bank_balanced_8k_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_bank_balanced_8k_cost0.5: core

# TTK task 2015
#
tf_idf_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced: TEST_TABLE = ttk_test_noname
tf_idf_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_imbalanced: core

tf_idf_dict_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_dict_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_ttk_imbalanced: TEST_TABLE = ttk_test_noname
tf_idf_dict_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_dict_ttk_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_ttk_imbalanced: core

tf_idf_ttk_balanced: TASK_TYPE = ttk
tf_idf_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_ttk_balanced: TEST_TABLE = ttk_test_noname
tf_idf_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_ttk_balanced: MODEL_NAME = tf_idf
tf_idf_ttk_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_balanced: core

tf_idf_ttk_balanced_cost0.5: TASK_TYPE = ttk
tf_idf_ttk_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_ttk_balanced_cost0.5: TEST_TABLE = ttk_test_noname
tf_idf_ttk_balanced_cost0.5: TRAIN_TABLE = ttk_train_balanced
tf_idf_ttk_balanced_cost0.5: MODEL_NAME = tf_idf
tf_idf_ttk_balanced_cost0.5: MODEL_OPTIONS= -t 0 -c 0.5
tf_idf_ttk_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_ttk_balanced_cost0.5: core

tf_idf_dict_ttk_balanced: TASK_TYPE = ttk
tf_idf_dict_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_ttk_balanced: TEST_TABLE = ttk_test_noname
tf_idf_dict_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_dict_ttk_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_balanced: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
tf_idf_dict_ttk_balanced: core

# TTK task 2016
#
16_tf_idf_ttk_imbalanced: TASK_TYPE = ttk
16_tf_idf_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_imbalanced: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_imbalanced: TRAIN_TABLE = ttk_train_2016
16_tf_idf_ttk_imbalanced: MODEL_NAME = tf_idf
16_tf_idf_ttk_imbalanced: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_imbalanced: core

16_tf_idf_ttk_balanced: TASK_TYPE = ttk
16_tf_idf_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced: core

16_tf_idf_ttk_balanced_cost0.75: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.75: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.75: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.75: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.75: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.75: MODEL_OPTIONS=	-t 0 -c 0.75
16_tf_idf_ttk_balanced_cost0.75: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.75: core

16_tf_idf_ttk_balanced_cost0.5: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.5: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.5: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.5: MODEL_OPTIONS=	-t 0 -c 0.5
16_tf_idf_ttk_balanced_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.5: core

16_tf_idf_ttk_balanced_cost0.25: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.25: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.25: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.25: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.25: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.25: MODEL_OPTIONS=	-t 0 -c 0.25
16_tf_idf_ttk_balanced_cost0.25: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.25: core

16_tf_idf_ttk_balanced_cost0.05: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_cost0.05: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_cost0.05: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_cost0.05: TRAIN_TABLE = ttk_train_balanced_2016
16_tf_idf_ttk_balanced_cost0.05: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_cost0.05: MODEL_OPTIONS=	-t 0 -c 0.05
16_tf_idf_ttk_balanced_cost0.05: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_cost0.05: core

16_tf_idf_ttk_balanced_6k: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_6k: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_6k: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_6k: TRAIN_TABLE = ttk_train_balanced_2016_max
16_tf_idf_ttk_balanced_6k: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_6k: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_6k: core

16_tf_idf_ttk_balanced_6k_cost0.5: TASK_TYPE = ttk
16_tf_idf_ttk_balanced_6k_cost0.5: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
16_tf_idf_ttk_balanced_6k_cost0.5: TEST_TABLE = ttk_test_2016
16_tf_idf_ttk_balanced_6k_cost0.5: TRAIN_TABLE = ttk_train_balanced_2016_max
16_tf_idf_ttk_balanced_6k_cost0.5: MODEL_NAME = tf_idf
16_tf_idf_ttk_balanced_6k_cost0.5: MODEL_OPTIONS= -t 0 -c 0.5
16_tf_idf_ttk_balanced_6k_cost0.5: ETALON_RESULT = $(SENTIRUEVAL2016)/$(TASK_TYPE)_etalon_2016.xml
16_tf_idf_ttk_balanced_6k_cost0.5: core

core:
	echo $(MODEL_OPTIONS)
	mkdir -p $(MODEL_OUTDIR)
	# Build Vocabulary
	$(DATA_ROOT)/aux/indexer.py romipdata $(VOCABULARY_PATH) $(TRAIN_TABLE) $(TEST_TABLE)
	# Extracting a problem for SVM
	$(MODEL_ROOT)/$(MODEL_NAME)_train.py $(TASK_TYPE) romipdata $(TRAIN_TABLE) $(VOCABULARY_PATH) $(MODEL_PROB)
	# Extracting testing data
	$(MODEL_ROOT)/$(MODEL_NAME)_test.py $(TASK_TYPE) romipdata $(TEST_TABLE) $(VOCABULARY_PATH) $(MODEL_TEST) $(MODEL_PCONF)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Predicting
	$(SVM_PREDICT)predict.py $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	../data/pg2x_data.py $(MODEL_PCONF) $(MODEL_OUT) $(MODEL_RESULT_OUT)
	# Estimating model
	cd ../eval/ && nodejs calc.js $(TASK_TYPE) ../run/$(MODEL_OUT) ../run/$(ETALON_RESULT)
