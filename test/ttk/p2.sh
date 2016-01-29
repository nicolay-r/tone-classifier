#!/bin/bash
# Скрипт вычисления результатов для контеста

svm="../../svm/"
log="log.txt"
res="result"

set -o xtrace

# Создаем каталог с результатом работы
mkdir -p $res
rm -rf "./$res/*"

for f in 6 7 8 9 10;
do
    echo "Test type: $f"
    # Копируем результаты настроек классификатора
    cp $f/*.conf $svm

    pushd .
        cd $svm
        echo "Calculating approximate result ..."
        make tf_idf_ttk_imbalanced | grep "F_R" >> $log
        echo "Apply 2016 model"
        make 16_tf_idf_ttk_imbalanced
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
    mv "$svm$log" "$out"
done
