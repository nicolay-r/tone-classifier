#!/bin/bash

psql -U postgres -h localhost -W -d romipdata -f bank.sql

pushd .
    cd ../../pmieval
    ./pmieval.py bank_positive bank_negative bank_lexicon
popd
