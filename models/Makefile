BASELINE_BANK_DIR=baseline_bank

baseline_bank:
	mkdir $(BASELINE_BANK_DIR)
	# Extracting a problem for SVN
	./baseline_bank.py romipdata bank_train_noname $(BASELINE_BANK_DIR)/baseline_bank.prob
	# Extracting testing data
	./baseline_bank.py romipdata bank_test_etalon_noname $(BASELINE_BANK_DIR)/baseline_bank.test

clean:
	rm -rf $(BASELINE_BANK_DIR)
