# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm/
# Root of the problem and training data
DATA_ROOT=../models/

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
MODEL_ETALON_OUT = $(MODEL_OUTDIR)$(MODEL_NAME).etalon.out
MODEL_MODEL	=	$(MODEL_TRAIN).model

tf_idf_bank_imbalanced: TASK_TYPE = bank
tf_idf_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_bank_imbalanced: ETALON_TABLE = bank_test_etalon_noname
tf_idf_bank_imbalanced: MODEL_NAME = tf_idf
tf_idf_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_bank_imbalanced: core

tf_idf_dict_bank_imbalanced: TASK_TYPE = bank
tf_idf_dict_bank_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_bank_imbalanced: ETALON_TABLE = bank_test_etalon_noname
tf_idf_dict_bank_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_imbalanced: TRAIN_TABLE = bank_train_noname
tf_idf_dict_bank_imbalanced: core

tf_idf_bank_balanced: TASK_TYPE = bank
tf_idf_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_bank_balanced: ETALON_TABLE = bank_test_etalon_noname
tf_idf_bank_balanced: MODEL_NAME = tf_idf
tf_idf_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_bank_balanced: core

tf_idf_dict_bank_balanced: TASK_TYPE = bank
tf_idf_dict_bank_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_bank_balanced: ETALON_TABLE = bank_test_etalon_noname
tf_idf_dict_bank_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_bank_balanced: TRAIN_TABLE = bank_train_balanced
tf_idf_dict_bank_balanced: core

tf_idf_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_ttk_imbalanced: ETALON_TABLE = ttk_test_etalon_noname
tf_idf_ttk_imbalanced: MODEL_NAME = tf_idf
tf_idf_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_ttk_imbalanced: core

tf_idf_dict_ttk_imbalanced: TASK_TYPE = ttk
tf_idf_dict_ttk_imbalanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_ttk_imbalanced: ETALON_TABLE = ttk_test_etalon_noname
tf_idf_dict_ttk_imbalanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_imbalanced: TRAIN_TABLE = ttk_train_noname
tf_idf_dict_ttk_imbalanced: core

tf_idf_ttk_balanced: TASK_TYPE = ttk
tf_idf_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_ttk_balanced: ETALON_TABLE = ttk_test_etalon_noname
tf_idf_ttk_balanced: MODEL_NAME = tf_idf
tf_idf_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_ttk_balanced: core

tf_idf_dict_ttk_balanced: TASK_TYPE = ttk
tf_idf_dict_ttk_balanced: VOCABULARY_PATH = $(DATA_ROOT)/aux/$(TASK_TYPE).voc
tf_idf_dict_ttk_balanced: ETALON_TABLE = ttk_test_etalon_noname
tf_idf_dict_ttk_balanced: MODEL_NAME = tf_idf_dict
tf_idf_dict_ttk_balanced: TRAIN_TABLE = ttk_train_balanced
tf_idf_dict_ttk_balanced: core


core:
	echo $(MODEL_OPTIONS)
	mkdir -p $(MODEL_OUTDIR)
	# Build Vocabulary
	$(DATA_ROOT)/aux/indexer.py romipdata $(VOCABULARY_PATH) $(TRAIN_TABLE) $(ETALON_TABLE)
	# Extracting a problem for SVM
	$(MODEL_ROOT)/$(MODEL_NAME)_train.py $(TASK_TYPE) romipdata $(TRAIN_TABLE) $(VOCABULARY_PATH) $(MODEL_PROB)
	# Extracting testing data
	$(MODEL_ROOT)/$(MODEL_NAME)_test.py $(TASK_TYPE) romipdata $(ETALON_TABLE) $(VOCABULARY_PATH) $(MODEL_TEST) $(MODEL_PCONF)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Predicting
	python/predict.py $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	../data/pg2x_data.py $(MODEL_PCONF) $(MODEL_OUT) $(MODEL_ETALON_OUT)
	# Estimating model
	cd ../eval/ && nodejs calc.js $(TASK_TYPE) ../svm/$(MODEL_OUT) ../svm/$(MODEL_ETALON_OUT)
