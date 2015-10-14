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


baseline_data: MODEL = BASELINE_BANK
baseline_data: MODEL_NAME = baseline_bank
baseline_data: core

core:
	# Training on data
	$(SVM_ROOT)svm-train $(MODEL_OPTIONS) $(MODEL_PROB) $(MODEL_MODEL)
	# Testing
	$(SVM_ROOT)svm-predict $(MODEL_OPTIONS) $(MODEL_TEST) $(MODEL_MODEL) $(MODEL_OUT)
