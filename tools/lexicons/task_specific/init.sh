#!/bin/bash

psql -U postgres -h localhost -W -d romipdata -f bank.sql
pushd .
    cd ../../pmieval
    ./pmieval.py bank_positive bank_negative bank_lexicon
popd

psql -U postgres -h localhost -W -d romipdata -f ttk.sql
pushd .
    cd ../../pmieval
    ./pmieval.py ttk_positive ttk_negative ttk_lexicon
popd
