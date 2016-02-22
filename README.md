# Installing:

Tested under Ubuntu 14.04.3 x64.

## Main application
```
#!bash
# Install all dependecies.
sudo apt-get install python-libxml2 python-psycopg2 python-pip postgresql-9.3 g++ node nodejs npm nodejs-legacy
pip install pymystem3 

# Downloading and compile SVM library.
git clone https://github.com/cjlin1/libsvm
make -C libsvm
make -C libsvm/python

# Copy builded libraries and *.py files in svm folder.
cp libsvm/python/*.py ./svm/python
cp libsvm/libsvm.so.2 ./svm/

# Install eval package -- script which estimates a model result quality.
cd eval
npm install
```
Useful links in case of building errors:

Eval script build errors [LibxmlJs issue](https://github.com/gwicke/libxmljs/commit/7e1ceaf96021926871e07a397d53de63c136a22b)

## Setup lexicons:

###  Lexicon based on train data:

```
#!bash
cd tools/balancer/2015
psql -U postgres -h localhost -W -d romipdata -f train_split.sql
```

After that to produce a lexicon, use 'pmieval' tool

```
#!bash
cd tools/pmieval
./pmieval.py bank_train_positive bank_train_negative bank_train_lexicon
./pmieval.py ttk_train_positive ttk_train_negative ttk_train_lexicon

```

### Lexicon based on downloaded stream twitter data:

Use 'splitter' and configuration file splitter.conf, and 'pmieval' tool which
produces jan16_lexicon based on positive twits table (jan16_positive) and
negative (jan16_negative)

```
#!bash
cd tools/splitter
./splitter.py data
cd ../pmieval
./pmieval.py jan16_positive jan16_negative jan16_lexicon
```
## Additional scripts
Install Tweepy
```
#!bash
pip install 'pip>1.5' --upgradeimport urllib
pip install tweepy
pip install six --upgrade
```

# References:
Contest training data, [gdrive folder](http://goo.gl/qHeAVo)

Lanyrd's MySQL to PostgreSQL conversion script, [github project](https://github.com/lanyrd/mysql-postgresql-converter)

