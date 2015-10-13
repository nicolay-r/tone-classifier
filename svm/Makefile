# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm-3.20/
# Root of the problem and training data
DATA_ROOT=../models/

# Defining a default model
MODEL=BASELINE_BANK
MODEL_NAME=baseline_bank

$(MODEL)_ROOT=$(DATA_ROOT)$(MODEL_NAME)/
$(MODEL)_PROB=$($(MODEL)_ROOT)$(MODEL_NAME).prob
$(MODEL)_TRAIN=$($(MODEL)_ROOT)$(MODEL_NAME).train
$(MODEL)_MODEL=$($(MODEL)_TRAIN).model
$(MODEL)_TEST=$($(MODEL)_ROOT)$(MODEL_NAME).test
$(MODEL)_OUT=$($(MODEL)_ROOT)$(MODEL_NAME).out

baseline_data:
	$(MODEL)=BASELINE_BANK
	$(MODEL_NAME)=baseline_bank
	# Training on data
	$(SVM_ROOT)svm-train $($(MODEL)_PROB) $($(MODEL)_MODEL)
	# Testing
	$(SVM_ROOT)svm-predict $($(MODEL)_TEST) $($(MODEL)_MODEL) $($(MODEL)_OUT)
