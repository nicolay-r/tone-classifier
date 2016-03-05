#!/bin/bash

svm="../../svm/"
log="log.txt"
res="result"

set -o xtrace

# Создаем каталог с результатом работы
mkdir -p $res

for f in 01 02 03 04 05 06 07 08 09 10;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $svm

    pushd .
        cd $svm

        for model_type in  16_tf_idf_ttk_imbalanced tf_idf_ttk_balanced 16_tf_idf_ttk_balanced_6k tf_idf_dict_ttk_balanced
        do
            echo 'Model:' $model_type >> $f.res
            make $model_type | grep -E 'F_R|Precision|Recall|Counts|F  ' >> $f.res
        done

    popd

    # Создаем каталог с результатами
    out="./$res/$f/"
    mkdir $out

    # Копируем все конфигурации, которые использовались при тестировании
    confs="msg.conf"
    cp "$svm$confs" "$out"
    confs="features.conf"
    cp "$svm$confs" "$out"

    # Копируем ответ
    mv "$svm$f.res" "$out"
done
