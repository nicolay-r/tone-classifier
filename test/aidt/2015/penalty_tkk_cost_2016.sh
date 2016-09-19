#!/bin/bash

run="../../../run/"
log="log.txt"
res="result_penalty_tkk_2016"

set -o xtrace

# Создаем каталог с результатом работы
mkdir -p $res

for f in 01 02 03 04 05 06;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $run

    pushd .
        cd $run

        for model_type in   16_tf_idf_ttk_balanced_cost0.1  \
                            16_tf_idf_ttk_balanced_cost0.2  \
                            16_tf_idf_ttk_balanced_cost0.3  \
                            16_tf_idf_ttk_balanced_cost0.4  \
                            16_tf_idf_ttk_balanced_cost0.5  \
                            16_tf_idf_ttk_balanced_cost0.6  \
                            16_tf_idf_ttk_balanced_cost0.7  \
                            16_tf_idf_ttk_balanced_cost0.8  \
                            16_tf_idf_ttk_balanced_cost0.9  \
                            16_tf_idf_ttk_balanced_cost1.0
        do
            echo 'Model:' $model_type >> $f.res
            make $model_type | grep -E 'F_R ' >> $f.res
        done

    popd

    # Создаем каталог с результатами
    out="./$res/$f/"
    mkdir -p $out

    # Копируем все конфигурации, которые использовались при тестировании
    confs="msg.conf"
    cp "$run$confs" "$out"
    confs="features.conf"
    cp "$run$confs" "$out"

    # Копируем ответ
    mv "$run$f.res" "$out"
done
