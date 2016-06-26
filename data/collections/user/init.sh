#!/bin/bash
./test_maker.py template.xml collection_description.json bank_test_user bank_test_user.xml
../../x2pg_table.py bank_test_user.xml
../../x2pg_data.py bank_test_user.xml
