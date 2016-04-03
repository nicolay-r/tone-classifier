# Install all dependecies.
sudo apt-get install python-libxml2 python-psycopg2 python-pip postgresql-9.3 \
    g++ nodejs npm nodejs-legacy unzip
sudo pip install pymystem3

# Downloading and compile SVM library.
git clone https://github.com/cjlin1/libsvm
make -C libsvm
make -C libsvm/python

# Install eval package -- script which estimates a model result quality.
cd eval
npm install
