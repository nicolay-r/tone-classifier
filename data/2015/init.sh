#!/bin/bash
../x2pg_table.py bank_train.xml
../x2pg_table.py bank_test.xml
../x2pg_table.py bank_test_etalon.xml
../x2pg_data.py bank_train.xml
../x2pg_data.py bank_test.xml
../x2pg_data.py bank_test_etalon.xml

../x2pg_table.py ttk_train.xml
../x2pg_table.py ttk_test.xml
../x2pg_table.py ttk_test_etalon.xml
../x2pg_data.py ttk_train.xml
../x2pg_data.py ttk_test.xml
../x2pg_data.py ttk_test_etalon.xml
