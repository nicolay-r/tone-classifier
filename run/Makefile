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
# SentiRuEval-2015
#

sre15_bank_features-only_imb: TASK_TYPE = bank
sre15_bank_features-only_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_features-only_imb: TEST_TABLE = bank_test_noname
sre15_bank_features-only_imb: TRAIN_TABLE = bank_train_noname
sre15_bank_features-only_imb: MODEL_NAME = features_only
sre15_bank_features-only_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
sre15_bank_features-only_imb: core

sre15_bank_w2v_imb: TASK_TYPE = bank
sre15_bank_w2v_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_w2v_imb: TEST_TABLE = bank_test_noname
sre15_bank_w2v_imb: TRAIN_TABLE = bank_train_noname
sre15_bank_w2v_imb: MODEL_NAME = w2v
sre15_bank_w2v_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
sre15_bank_w2v_imb: core

sre15_bank_bow_imb: TASK_TYPE = bank
sre15_bank_bow_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_bow_imb: TEST_TABLE = bank_test_noname
sre15_bank_bow_imb: TRAIN_TABLE = bank_train_noname
sre15_bank_bow_imb: MODEL_NAME = bow
sre15_bank_bow_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
sre15_bank_bow_imb: core

sre15_bank_tf-idf_imb: TASK_TYPE = bank
sre15_bank_tf-idf_imb: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_tf-idf_imb: TEST_TABLE = bank_test_noname
sre15_bank_tf-idf_imb: TRAIN_TABLE = bank_train_noname
sre15_bank_tf-idf_imb: MODEL_NAME = tf_idf
sre15_bank_tf-idf_imb: ETALON_RESULT = $(SENTIRUEVAL2015)$(TASK_TYPE)_etalon.xml
sre15_bank_tf-idf_imb: core

sre15_bank_tf-idf_bal: TASK_TYPE = bank
sre15_bank_tf-idf_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_tf-idf_bal: TEST_TABLE = bank_test_noname
sre15_bank_tf-idf_bal: TRAIN_TABLE = bank_train_balanced
sre15_bank_tf-idf_bal: MODEL_NAME = tf_idf
sre15_bank_tf-idf_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
sre15_bank_tf-idf_bal: core

sre15_bank_bow_bal: TASK_TYPE = bank
sre15_bank_bow_bal: VOCABULARY_PATH = $(DATA_ROOT)/core/$(TASK_TYPE).voc
sre15_bank_bow_bal: TEST_TABLE = bank_test_noname
sre15_bank_bow_bal: TRAIN_TABLE = bank_train_balanced
sre15_bank_bow_bal: MODEL_NAME = bag_of_words
sre15_bank_bow_bal: ETALON_RESULT = $(SENTIRUEVAL2015)/$(TASK_TYPE)_etalon.xml
sre15_bank_bow_bal: core

core:
	echo $(MODEL_OPTIONS)
	mkdir -p $(MODEL_OUTDIR)
	# Extracting data
	$(MODEL_ROOT)/model_$(MODEL_NAME).py $(TASK_TYPE) romipdata $(TRAIN_TABLE) $(TEST_TABLE) $(MODEL_PROB) $(MODEL_TEST) $(MODEL_PCONF)
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
