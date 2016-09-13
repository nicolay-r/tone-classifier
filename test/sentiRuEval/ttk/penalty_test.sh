#!/bin/bash

run="../../run/"
log="log.txt"
res="penalty_result"

# Создаем каталог с результатом работы
mkdir -p $res

for f in 10;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $run

    pushd .
        cd $run

        for model_type in \
            tf_idf_ttk_balanced_cost0.1 \
            tf_idf_ttk_balanced_cost0.2 \
            tf_idf_ttk_balanced_cost0.3 \
            tf_idf_ttk_balanced_cost0.4 \
            tf_idf_ttk_balanced_cost0.5 \
            tf_idf_ttk_balanced_cost0.6 \
            tf_idf_ttk_balanced_cost0.7 \
            tf_idf_ttk_balanced_cost0.8 \
            tf_idf_ttk_balanced_cost0.9 \
            tf_idf_ttk_balanced_cost1.0
        do
            echo 'Model:' $model_type
            make $model_type | grep -E 'F_R ' >> $f.res
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
