#!/bin/bash

./full_extract.py ../../../data/rubtsova/negative.csv romipdata rubtsova_negative
./full_extract.py ../../../data/rubtsova/positive.csv romipdata rubtsova_positive
pushd .
    cd ../../pmieval
    ./pmieval.py rubtsova_positive rubtsova_negative rubtsova_lexicon
popd
