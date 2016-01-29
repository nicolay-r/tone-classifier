#!/bin/bash
# Скрипт вычисления результатов для контеста

svm="../../svm/"
res="result"

set -o xtrace

# Создаем каталог с результатом работы
mkdir -p $res
rm -rf "./$res/*"

for f in 1;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $svm

    pushd .
    cd $svm
        for mode in 16_tf_idf_bank_balanced
        do
            echo "Testing: $mode"
            # make $mode | grep "-1:|0:|1:" > log.out
            make $mode
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

    # Копируем ответ и лог выполнения
    outfile="result.out"
    mv "$svm$outfile" "$out"
done
