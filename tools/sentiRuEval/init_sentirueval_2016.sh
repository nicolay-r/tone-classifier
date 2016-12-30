#!/bin/bash

SCRIPTS=./scripts/
DATA=../../data/collections/SentiRuEval-2016/

"$SCRIPTS"x2pg_table.py "$DATA"bank_train_2016.xml
"$SCRIPTS"x2pg_table.py "$DATA"bank_test_2016.xml
"$SCRIPTS"x2pg_table.py "$DATA"bank_etalon_2016.xml
"$SCRIPTS"x2pg_table.py "$DATA"ttk_train_2016.xml
"$SCRIPTS"x2pg_table.py "$DATA"ttk_test_2016.xml
"$SCRIPTS"x2pg_table.py "$DATA"ttk_etalon_2016.xml

"$SCRIPTS"x2pg_data.py "$DATA"bank_train_2016.xml
"$SCRIPTS"x2pg_data.py "$DATA"bank_test_2016.xml
"$SCRIPTS"x2pg_data.py "$DATA"bank_etalon_2016.xml
"$SCRIPTS"x2pg_data.py "$DATA"ttk_train_2016.xml
"$SCRIPTS"x2pg_data.py "$DATA"ttk_test_2016.xml
"$SCRIPTS"x2pg_data.py "$DATA"ttk_etalon_2016.xml
