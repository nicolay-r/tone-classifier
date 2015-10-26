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

## **References:** ##
Contest training data, [gdrive folder](http://goo.gl/qHeAVo)

Lanyrd's MySQL to PostgreSQL conversion script, [github project](https://github.com/lanyrd/mysql-postgresql-converter)

