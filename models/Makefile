BASELINE_BANK_DIR=bank/baseline/out
TF_IDF_BANK_DIR=bank/tf_idf/out


baseline_bank:
	mkdir $(BASELINE_BANK_DIR)
	# Extracting a problem for SVM
	./bank/baseline/baseline_train.py romipdata bank_train_noname $(BASELINE_BANK_DIR)/baseline_bank.prob
	# Extracting testing data
	./bank/baseline/baseline_test.py romipdata bank_test_etalon_noname $(BASELINE_BANK_DIR)/baseline_bank.test $(BASELINE_BANK_DIR)/baseline_bank.pconf

tf_idf_bank:
	mkdir $(TF_IDF_BANK_DIR)
	# Extracting a problem for SVM
	./bank/tf_idf/tf_idf_train.py romipdata bank_train_noname $(TF_IDF_BANK_DIR)/tf_idf.prob
	# Extracting testing data
	./bank/tf_idf/tf_idf_test.py romipdata bank_test_etalon_noname $(TF_IDF_BANK_DIR)/tf_idf.test $(TF_IDF_BANK_DIR)/tf_idf.pconf


clean:
	rm -rf $(BASELINE_BANK_DIR) $(TF_IDF_BANK_DIR)
