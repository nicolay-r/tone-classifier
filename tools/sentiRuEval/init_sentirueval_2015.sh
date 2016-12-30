#!/bin/bash

SCRIPTS=./scripts/
DATA=../../data/collections/SentiRuEval-2015/

"$SCRIPTS"x2pg_table.py "$DATA"bank_train.xml
"$SCRIPTS"x2pg_table.py "$DATA"bank_test.xml
"$SCRIPTS"x2pg_table.py "$DATA"bank_etalon.xml
"$SCRIPTS"x2pg_data.py  "$DATA"bank_train.xml
"$SCRIPTS"x2pg_data.py  "$DATA"bank_test.xml
"$SCRIPTS"x2pg_data.py  "$DATA"bank_etalon.xml

"$SCRIPTS"x2pg_table.py "$DATA"ttk_train.xml
"$SCRIPTS"x2pg_table.py "$DATA"ttk_test.xml
"$SCRIPTS"x2pg_table.py "$DATA"ttk_etalon.xml
"$SCRIPTS"x2pg_data.py  "$DATA"ttk_train.xml
"$SCRIPTS"x2pg_data.py  "$DATA"ttk_test.xml
"$SCRIPTS"x2pg_data.py  "$DATA"ttk_etalon.xml
