BASELINE_BANK_DIR=bank/baseline_bank

baseline_bank:
	mkdir $(BASELINE_BANK_DIR)
	# Extracting a problem for SVN
	./bank/baseline_bank_train.py romipdata bank_train_noname $(BASELINE_BANK_DIR)/baseline_bank.prob
	# Extracting testing data
	./bank/baseline_bank_test.py romipdata bank_test_etalon_noname $(BASELINE_BANK_DIR)/baseline_bank.test $(BASELINE_BANK_DIR)/baseline_bank.pconf

clean:
	rm -rf $(BASELINE_BANK_DIR)
