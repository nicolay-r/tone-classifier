Description
-----------

This research project describes the application of SVM classifier and NN
classifiers for sentiment classification of Russian Twitter messages in the
banking and telecommunications domains of **SentiRuEval** competition.

Installation
------------

All dependencies described in `Makefile` and could be installed as follows:

`make install`

Usage
-----

For research purposes. Use `run/Makefile` to run workflow for
certain task (`bank` or `tcc`) and classifier (`svm`, `lr`), for example:

` cd run && make svm_sre15_bank_w2v_bal `

returns F-macro/micro result for SentiRuEval-2015 bank dataset using
w2v-based embedding model for balanced test collection.

All embedding classifier settings presented in `data/embedding` folder.

Papers
------

1. Russir posters ([2017][Russir-2017 poster], [2016][Russir-2016 poster])

1. [AIDT Journal 2017/2];

2. [Dialog-2016][Dialog-2016 article];

References
----------

* [SentiRuEval-2015] contest data;
* [SentiRuEval-2016] contest data & results of this approach (participant #1) in
comparation with the other participants.


<!-- Links -->
[Russir-2017 poster]: doc/russir_2017_poster.pdf
[AIDT Journal 2017/2]: doc/aidt_2017.pdf

[Russir-2016 poster]: doc/russir_2016_poster.pdf
[SentiRuEval-2016]: https://drive.google.com/drive/u/0/folders/0BxlA8wH3PTUfV1F1UTBwVTJPd3c
[Dialog-2016 article]: http://www.dialog-21.ru/media/3469/rusnachenko.pdf

[SentiRuEval-2015]: http://goo.gl/qHeAVo
