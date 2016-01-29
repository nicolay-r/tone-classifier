#!/bin/bash

svm="../svm/"
res="result"

mkdir -p result
rm ./result/*

for f in d1
do
    echo "Test type: $f"
    echo "cp $f/*.conf $svm"
    cp $f/*.conf $svm
    cd $svm
    for mode in tf_idf_bank_balanced tf_idf_ttk_balanced
    # for mode in tf_idf_bank_imbalanced tf_idf_dict_bank_imbalanced tf_idf_ttk_imbalanced tf_idf_dict_ttk_imbalanced tf_idf_bank_balanced tf_idf_dict_bank_balanced tf_idf_ttk_balanced tf_idf_dict_ttk_balanced
    do
        echo "Testing: $mode"
        make $mode | grep "F_R" >> $f.res
    done
    cd ../test
    mv $svm$f.res result/
done
