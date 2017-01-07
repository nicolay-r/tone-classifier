Description
-----------

This project describes the application of SVM classifier for sentiment
classification of Russian Twitter messages in the banking and
telecommunications domains of SentiRuEval-2016 competition. A variety of
features were implemented to improve the quality of message classification,
especially sentiment score features based on a set of sentiment lexicons. We
compare the result differences between train collection types
(balanced/imbalanced) and its volumes, and advantages of applying lexicon-based
features to each type of the training classifier modification. Before
SentiRuEval-2016, the classifier was tested on the previous year collection of
the same competition (SentiRuEval-2015) to obtain a better settings set. The
created system achieved the third place at SentiRuEval-2016 in both tasks. The
experiments performed after the SentiRuEval-2016 evaluation allowed us to
improve our results by searching for a better 'Cost' parameter value of SVM
classifier and extracting more information from lexicons into new features. The
final classifier achieved results close to the top results of the competition.

**Key words:** Machine Learning, SVM, Sentiment Analysis, Lexicons, SentiRuEval
2016

Documentation
-------------

1. Use of lexicons to improve quality of sentiment classification ([Dialog-2016
   article]);

2. Diploma work ([Full documentation]).

References
----------
* [SentiRuEval-2015] contest data;
* [SentiRuEval-2016] contest data & results of this approach (participant #1)
  in comparation with the other participants;
* Corpora of short Twittter messages (sentiment labeled), Yu. Rubtsova
  ([sentiment corpora]);
* LibSVM -- SVM classifier library [libsvm];
* Lanyrd's MySQL to PostgreSQL conversion script, [lanyrd project].

Installing
----------

Tested under Ubuntu 14.04.3 x64.

1. Install all dependecies.
```
#!bash
sudo apt-get install python-libxml2 python-psycopg2 python-pip postgresql-9.3 \
    g++ nodejs npm nodejs-legacy unzip
sudo pip install pymystem3
```

2. Downloading and compile SVM library.
```
#!bash
git clone https://github.com/cjlin1/libsvm
make -C libsvm
make -C libsvm/python
```

3. Install eval package -- script which estimates a model result quality.
```
cd eval
npm install
```
Eval script build errors ([LibxmlJs issue])

Setup lexicons
--------------

###  Lexicon based on train data

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

### Lexicon based on downloaded stream twitter data

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

Using Streaming Twitter API for collecting Twitter messages
-----------------------------------------------------------
Install Tweepy
```
#!bash
pip install 'pip>1.5' --upgradeimport urllib
pip install tweepy
pip install six --upgrade
```

Use 'twitter/consumer.py'

<!-- Links -->
[Full documentation]: https://github.com/nicolay-r/tone-classifier/blob/master/doc/diploma/diploma.pdf
[Dialog-2016 article]: http://www.dialog-21.ru/media/3469/rusnachenko.pdf
[sentiment corpora]: http://study.mokoron.com/
[SentiRuEval-2015]: http://goo.gl/qHeAVo
[SentiRuEval-2016]: https://drive.google.com/drive/u/0/folders/0BxlA8wH3PTUfV1F1UTBwVTJPd3c
[LibxmlJs issue]: https://github.com/gwicke/libxmljs/commit/7e1ceaf96021926871e07a397d53de63c136a22b
[lanyrd project]: https://github.com/lanyrd/mysql-postgresql-converter
[libsvm]: https://github.com/cjlin1/libsvm
