#!/bin/bash
./x2pg_table.py data/bank_train.xml
./x2pg_table.py data/bank_test.xml
./x2pg_table.py data/bank_test_etalon.xml
./x2pg_data.py data/bank_train.xml
./x2pg_data.py data/bank_test.xml
./x2pg_data.py data/bank_test_etalon.xml

./x2pg_table.py data/ttk_train.xml
./x2pg_table.py data/ttk_test.xml
./x2pg_table.py data/ttk_test_etalon.xml
./x2pg_data.py data/ttk_train.xml
./x2pg_data.py data/ttk_test.xml
./x2pg_data.py data/ttk_test_etalon.xml
