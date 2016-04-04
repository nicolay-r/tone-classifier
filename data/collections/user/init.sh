#!/bin/bash
../../x2pg_table.py bank_test_user.xml
../../x2pg_table.py bank_etalon_user.xml

../../x2pg_data.py bank_test_user.xml
../../x2pg_data.py bank_etalon_user.xml
