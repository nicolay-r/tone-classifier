#!/bin/bash

run="../../run/"
log="log.txt"
res="result_2016"

set -o xtrace

# Создаем каталог с результатом работы
mkdir -p $res

for f in 02 01 00;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $run

    pushd .
        cd $run

        for model_type in  16_tf_idf_bank_imbalanced16  \
                           16_tf_idf_bank_balanced16    \
                           16_tf_idf_bank_balanced_30k  \
                           16_tf_idf_ttk_imbalanced16   \
                           16_tf_idf_ttk_balanced16     \
                           16_tf_idf_ttk_balanced_30k
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
    cp "$run$confs" "$out"
    confs="features.conf"
    cp "$run$confs" "$out"

    # Копируем ответ
    mv "$run$f.res" "$out"
done
