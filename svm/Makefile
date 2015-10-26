# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm/
# Root of the problem and training data
DATA_ROOT=../models/

# Defining a default model
MODEL_OPTIONS=
MODEL_ROOT=$(DATA_ROOT)$(TASK_TYPE)/$(MODEL_NAME)/
MODEL_PROB=$(MODEL_ROOT)$(MODEL_NAME).prob
MODEL_TRAIN=$(MODEL_ROOT)$(MODEL_NAME).train
MODEL_MODEL=$(MODEL_TRAIN).model
MODEL_TEST=$(MODEL_ROOT)$(MODEL_NAME).test
MODEL_PCONF=$(MODEL_ROOT)$(MODEL_NAME).pconf
MODEL_OUT=$(MODEL_ROOT)$(MODEL_NAME).out


baseline_bank: TASK_TYPE = bank
baseline_bank: MODEL = BASELINE_BANK
baseline_bank: MODEL_NAME = baseline_bank
baseline_bank: ETALON_RESULT = ../train/data/bank_test_etalon.xml
baseline_bank: core

core:
	mkdir -p $(MODEL_ROOT)
	# Extracting a problem for SVM
	$(DATA_ROOT)$(TASK_TYPE)/$(MODEL_NAME)_train.py romipdata bank_train_noname $(MODEL_PROB)
	# Extracting testing data
	$(DATA_ROOT)$(TASK_TYPE)/$(MODEL_NAME)_test.py romipdata bank_test_etalon_noname $(MODEL_TEST) $(MODEL_PCONF)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Predicting
	python/predict.py $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_PCONF)
	# Exporting Result into XML
	../train/pg2x_data.py $(MODEL_PCONF) RomipData $(MODEL_OUT)
	# Estimating model
	cd ../eval/ && nodejs calc.js $(TASK_TYPE) ../svm/$(MODEL_OUT) ../svm/$(ETALON_RESULT)

