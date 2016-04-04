# Установка зависимостей.
sudo apt-get install python-libxml2 python-psycopg2 python-pip postgresql-9.3 \
    g++ nodejs npm nodejs-legacy unzip
sudo pip install pymystem3

# Загрузка и компиляция библиотеки LibSVM.
git clone https://github.com/cjlin1/libsvm
make -C libsvm
make -C libsvm/python

# Установка пакета eval -- скрипт оценки качества работы модели.
cd eval
npm install
