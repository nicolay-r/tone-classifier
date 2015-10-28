# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm/
# Root of the problem and training data
DATA_ROOT=../models/

# Defining a default model
MODEL_OPTIONS=	-t 0
MODEL_ROOT	=	$(DATA_ROOT)$(TASK_TYPE)/$(MODEL_NAME)
MODEL_OUTDIR= 	$(MODEL_ROOT)/out/
MODEL_PROB	=	$(MODEL_OUTDIR)$(MODEL_NAME).prob
MODEL_TRAIN	=	$(MODEL_OUTDIR)$(MODEL_NAME).train
MODEL_TEST	=	$(MODEL_OUTDIR)$(MODEL_NAME).test
MODEL_PCONF	=	$(MODEL_OUTDIR)$(MODEL_NAME).pconf
MODEL_OUT	=	$(MODEL_OUTDIR)$(MODEL_NAME).out
MODEL_ETALON_OUT = $(MODEL_OUTDIR)$(MODEL_NAME).etalon.out
MODEL_MODEL	=	$(MODEL_TRAIN).model

baseline_bank_imbalanced: TASK_TYPE = bank
baseline_bank_imbalanced: MODEL_NAME = baseline
baseline_bank_imbalanced: core

tf_idf_bank_imbalanced: TASK_TYPE = bank
tf_idf_bank_imbalanced: MODEL_NAME = tf_idf
tf_idf_bank_imbalanced: core

core:
	mkdir -p $(MODEL_OUTDIR)
	# Extracting a problem for SVM
	$(MODEL_ROOT)/$(MODEL_NAME)_train.py romipdata bank_train_noname $(MODEL_PROB)
	# Extracting testing data
	$(MODEL_ROOT)/$(MODEL_NAME)_test.py romipdata bank_test_etalon_noname $(MODEL_TEST) $(MODEL_PCONF)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Predicting
	python/predict.py $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	../train/pg2x_data.py $(MODEL_PCONF) RomipData $(MODEL_OUT) $(MODEL_ETALON_OUT)
	# Estimating model
	cd ../eval/ && nodejs calc.js $(TASK_TYPE) ../svm/$(MODEL_OUT) ../svm/$(MODEL_ETALON_OUT)

