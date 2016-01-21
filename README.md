## **Installing:** ##
1. Compile libsvm library
```
#!bash
git clone https://github.com/cjlin1/libsvm
cd libsvm/python
make
cp *.py ../../svm/python
cp ../libsvm.so.2 ../../svm/
```

2. Install eval package -- script to estimate a model quality.
```
#!bash
cd eval
node install
```

3. Install Tweepy

p install 'pip>1.5' --upgradeimport urllib
pip install tweepy
pip install six --upgrade

## **Setup lexicons:** ##

1. Setup lexicon based on train data:

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

2. Setup lexicon based on downloaded stream twitter data:

Use 'splitter' and configuration file splitter.conf
```
#!bash
cd tools/splitter
```

## **References:** ##
Contest training data, [gdrive folder](http://goo.gl/qHeAVo)

Lanyrd's MySQL to PostgreSQL conversion script, [github project](https://github.com/lanyrd/mysql-postgresql-converter)

