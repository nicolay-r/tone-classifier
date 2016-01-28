#!/bin/bash
../x2pg_table.py bank_train_2016.xml
../x2pg_table.py bank_test_2016.xml
../x2pg_table.py ttk_train_2016.xml
../x2pg_table.py ttk_test_2016.xml

../x2pg_data.py bank_train_2016.xml
../x2pg_data.py bank_test_2016.xml
../x2pg_data.py ttk_train_2016.xml
../x2pg_data.py ttk_test_2016.xml
