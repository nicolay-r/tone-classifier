# Root Folder of the LibSVM classifier library
SVM_ROOT=../libsvm-3.20/
# Root of the problem and training data
DATA_ROOT=../models/

# Models
# REPLACE WITH $(MODEL)_*
BASELINE_BANK_ROOT=$(DATA_ROOT)baseline_bank/
BASELINE_BANK_PROB=$(BASELINE_BANK_ROOT)baseline_bank.prob
BASELINE_BANK_TRAIN=$(BASELINE_BANK_ROOT)baseline_bank.train
BASELINE_BANK_MODEL=$(BASELINE_BANK_TRAIN).model
BASELINE_BANK_TEST=$(BASELINE_BANK_ROOT)baseline_bank.test
BASELINE_BANK_OUT=$(BASELINE_BANK_ROOT)baseline_bank.out

baseline_data:
	# Training on data
	$(SVM_ROOT)svm-train $(BASELINE_BANK_PROB) $(BASELINE_BANK_MODEL)
	# Testing
	$(SVM_ROOT)svm-predict $(BASELINE_BANK_TEST) $(BASELINE_BANK_MODEL) $(BASELINE_BANK_OUT)
