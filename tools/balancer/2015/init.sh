#!/bin/bash

# Скрипт создания вспомогательных таблиц с положительными и негативными твитами
# для задач bank и ttk на основе cvs файлов коллекции Рубцовой.

unzip ../../../data/rubtsova/collection.zip ../../../data/rubtsova/

./extract.py ../../../data/rubtsova/negative.csv romipdata bank_negative bank
./extract.py ../../../data/rubtsova/positive.csv romipdata bank_positive bank

./extract.py ../../../data/rubtsova/negative.csv romipdata ttk_negative ttk
./extract.py ../../../data/rubtsova/positive.csv romipdata ttk_positive ttk

