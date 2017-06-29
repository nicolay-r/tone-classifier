Description
-----------

This project describes the application of SVM classifier for sentiment
classification of Russian Twitter messages in the banking and telecommunications
domains of SentiRuEval-2016 competition. A variety of features were implemented
to improve the quality of message classification, especially sentiment score
features based on a set of sentiment lexicons. We compare the result differences
between train collection types (balanced/imbalanced) and its volumes, and
advantages of applying lexicon-based features to each type of the training
classifier modification. Before SentiRuEval-2016, the classifier was tested on
the previous year collection of the same competition (SentiRuEval-2015) to
obtain a better settings set. The created system achieved the third place at
SentiRuEval-2016 in both tasks. The experiments performed after the
SentiRuEval-2016 evaluation allowed us to improve our results by searching for a
better 'Cost' parameter value of SVM classifier and extracting more information
from lexicons into new features. The final classifier achieved results close to
the top results of the competition.

**Key words:** Machine Learning, SVM, Sentiment Analysis, Lexicons, SentiRuEval 2016

Documentation
-------------

1. Methods of lexicon integration with machine learning for sentiment analysis system (AIDT Journal 2017/2)

2. Use of lexicons to improve quality of sentiment classification ([Dialog-2016 article]);

2. [Russir-2016 paper];

2. Diploma work ([Full documentation]).

References
----------

* [SentiRuEval-2015] contest data;
* [SentiRuEval-2016] contest data & results of this approach (participant #1) in
comparation with the other participants.


<!-- Links -->
[Dialog-2016 article]: http://www.dialog-21.ru/media/3469/rusnachenko.pdf
[Russir-2016 paper]: https://github.com/nicolay-r/tone-classifier/blob/master/doc/russir_paper.pdf
[Full documentation]: https://github.com/nicolay-r/tone-classifier/blob/master/doc/diploma.pdf
[SentiRuEval-2015]: http://goo.gl/qHeAVo
[SentiRuEval-2016]: https://drive.google.com/drive/u/0/folders/0BxlA8wH3PTUfV1F1UTBwVTJPd3c
