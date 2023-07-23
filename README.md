# Lexicon Integration with Machine Learning for Sentiment Analysis

![](https://img.shields.io/badge/Python-2.7-brightgreen.svg)

This project represent a code for paper 
*[Methods of Lexicon Integration with Machine Learning for Sentiment Analysis System](
https://github.com/nicolay-r/tone-classifier/raw/master/doc/aidt_2017.pdf)*
and describes the application of `SVM` classifier and `Neural Networks`
classifiers for sentiment classification of Russian Twitter messages in the
banking and telecommunications domains of **SentiRuEval** competition.

## Installation

All dependencies described in `Makefile` and could be installed as follows:

```bash
make install
```

## Usage

For research purposes. Use `run/Makefile` to run workflow for
certain task (`bank` or `tcc`) and classifier (`svm`, `lr`), for example:
```bash
cd run && make svm_sre15_bank_w2v_bal
```

returns F-macro/micro result for SentiRuEval-2015 bank dataset using
w2v-based embedding model for balanced test collection.

All embedding classifier settings presented in `data/embedding` folder.

## Resources

* [SentiRuEval-2015] contest data;
* [SentiRuEval-2016] contest data & results of this approach (participant #1) in
comparation with the other participants.

## Papers

1. Russir posters ([2017][Russir-2017 poster], [2016][Russir-2016 poster])

2. [AIDT Journal 2017/2];

3. [Dialog-2016][Dialog-2016 article];

## How to cite

```bibtex
@article{rusnachenko2017methods,
  title={Методы интеграции лексиконов в машинное обучение для систем анализа тональности},
  author={Русначенко, Николай Леонидович and Лукашевич, Наталья Валентиновна},
  journal={Искусственный интеллект и принятие решений},
  number={2},
  pages={78--89},
  year={2017},
  publisher={Федеральное государственное учреждение" Федеральный исследовательский центр~…}
}
```

<!-- Links -->
[Russir-2017 poster]: doc/russir_2017_poster.pdf
[AIDT Journal 2017/2]: doc/aidt_2017.pdf

[Russir-2016 poster]: doc/russir_2016_poster.pdf
[SentiRuEval-2016]: https://drive.google.com/drive/u/0/folders/0BxlA8wH3PTUfV1F1UTBwVTJPd3c
[Dialog-2016 article]: http://www.dialog-21.ru/media/3469/rusnachenko.pdf

[SentiRuEval-2015]: http://goo.gl/qHeAVo

