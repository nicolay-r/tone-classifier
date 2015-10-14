# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm-3.20/
# Root of the problem and training data
DATA_ROOT=../models/

# Defining a default model
MODEL_OPTIONS=
MODEL_ROOT=$(DATA_ROOT)$(MODEL_NAME)/
MODEL_PROB=$(MODEL_ROOT)$(MODEL_NAME).prob
MODEL_TRAIN=$(MODEL_ROOT)$(MODEL_NAME).train
MODEL_MODEL=$(MODEL_TRAIN).model
MODEL_TEST=$(MODEL_ROOT)$(MODEL_NAME).test
MODEL_OUT=$(MODEL_ROOT)$(MODEL_NAME).out


baseline_bank: MODEL = BASELINE_BANK
baseline_bank: MODEL_NAME = baseline_bank
baseline_bank: core

baseline_bank_np_only: MODEL = BASELINE_BANK_NP_ONLY
baseline_bank_np_only: MODEL_NAME = baseline_bank_np_only
baseline_bank_np_only: core

core:
	mkdir -p $(MODEL_ROOT)
	# Extracting a problem for SVN
	$(DATA_ROOT)$(MODEL_NAME).py romipdata bank_train_noname $(MODEL_PROB)
	# Extracting testing data
	$(DATA_ROOT)$(MODEL_NAME).py romipdata bank_test_etalon_noname $(MODEL_TEST)
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Testing
	$(SVM_ROOT)svm-predict $(MODEL_OPTIONS) $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_OUT)
