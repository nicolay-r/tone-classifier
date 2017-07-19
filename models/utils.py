# -*- coding: utf-8 -*-

# global
import io
import sys
import json
import logging
import pandas as pd
import numpy as np

# core
import core
import core.utils
import core.indexer
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.features import Features
from core.msg import TwitterMessageParser

# configs
import configs

TTK_TASK = 'ttk'
BANK_TASK = 'bank'
LOGGER_FORMAT = '[%(asctime)-15s] %(message)s'


def init_logger():
    logging.basicConfig(filemode='w',
                        format=LOGGER_FORMAT,
                        level=logging.DEBUG)


# TODO: pass here the output filepath based on the parameter from argv.
def train_network(model, X, y, output, reg_lambda=0.1, eps=10e-4,
                  callback=None, epoch_delta=5):
    """
    Train neural network model, based on the 'train' set.

    Arguments:
    ---------
        model : RNNTheano
            neural network model which will be trained
        X : np.ndarray
            array of sentences. Each sentence presented as embedding vector
            of the size which corresponds to the 'model' input
        y : np.array
            describes the class of each sentence presented in 'X' dataset
        reg_lambda : float
            regression parameter for sgd.
        eps : float
        callback : func
            callback which calls every certain amount of 'epoch_delta'
        epoch_delta: int
            amount of epochs will be passed before 'callback' has been called.
        output : str
            output filepath where to store the model.
    Returns:
    -------
        None
    """
    i_rl = reg_lambda
    p_loss = model.calculate_loss(X, y)
    c_loss = 0
    rl_div = 0.5
    unrolled_steps = 0
    it = 0
    logging.info("initial loss: %f" % (p_loss))

    epoch = 0
    while abs(p_loss - c_loss) > eps:

        p = np.random.permutation(len(X))
        X = X[p]
        y = y[p]

        model.sgd_step(X, y, reg_lambda)
        c_loss = model.calculate_loss(X, y)
        logging.info("current loss on step %d: %f" % (it, c_loss))
        unrolled_steps += 1
        if (c_loss >= p_loss):
            model.rollback_step(reg_lambda)
            reg_lambda *= rl_div
            logging.info("rollback sgd_step, where loss=%f. reg_lambda=%f" %
                         (model.calculate_loss(X, y), reg_lambda))
            unrolled_steps = 0
        else:
            if (unrolled_steps % 10 == 0 and reg_lambda < i_rl):
                reg_lambda /= rl_div
                logging.info("increase reg_lambda: %f" % reg_lambda)
            logging.info('save model: {}'.format(output))
            model.save(output)
            p_loss = c_loss
            c_loss = 0
            epoch += 1
            if (epoch % epoch_delta == 0 and callback is not None):
                callback()

        it += 1


def vectorization_core(vectorizer, init_term_vocabulary=True,
                       merge_doc_vocabularies=False):
    """
    Main function of collection vectorization

    vectorizer : message vectorization function
    returns : None
    """
    init_logger()

    if (sys.argv < 8):
        exit(0)

    config = {'task_type': sys.argv[1],
              'database': sys.argv[2],  # save the output results
              'train_table': sys.argv[3],
              'test_table': sys.argv[4],
              'train_output': sys.argv[5],
              'test_output': sys.argv[6],
              'pconf_output': sys.argv[7]}

    with io.open(configs.TWITTER_MESSAGE_PARSER_CONFIG, "r") as f:
        message_settings = json.load(f, encoding='utf-8')

    with io.open(configs.FEATURES_CONFIG, 'r') as f:
        features_settings = json.load(f, encoding='utf-8')

    # Create vocabulary of terms
    if init_term_vocabulary is True:
        term_vocabulary = core.indexer.create_term_vocabulary(
                                [config['train_table'], config['test_table']],
                                message_settings)
    else:
        term_vocabulary = TermVocabulary()

    features = Features(
               TwitterMessageParser(message_settings, config['task_type']),
               features_settings)

    doc_vocabulary = DocVocabulary()
    # Train problem
    train_problem = create_problem(config['task_type'],
                                   'train',
                                   config['train_table'],
                                   vectorizer,
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   message_settings)

    if not merge_doc_vocabularies:
        doc_vocabulary = DocVocabulary()
    # Test problem
    test_problem = create_problem(config['task_type'],
                                  'test',
                                  config['test_table'],
                                  vectorizer,
                                  features,
                                  term_vocabulary,
                                  doc_vocabulary,
                                  message_settings)

    result_table = config['test_table'] + '.result.csv'
    logging.info('Create a file for classifier results: {}'.format(
                 result_table))
    result_df = pd.read_csv(config['test_table'], sep=',')
    result_df.to_csv(result_table, sep=',')

    # Save
    save_problem(train_problem, config['train_output'])
    save_problem(test_problem, config['test_output'])
    save_predict_config(columns=get_score_columns(config['task_type']),
                        prediction_table=result_table,
                        out_filepath=config['pconf_output'])


def create_problem(task_type, collection_type, table_filepath, vectorizer,
                   features, term_vocabulary, doc_vocabulary,
                   message_settings):
    """
    Creates problem (vectors from messages with additional features)

    Arguments:
    ---------
        task_type : BANK_TASK or TTK_TASK
            According to SentiRuEval competiiton
        collection_type : str, 'train' or 'test'
            It affects on the generated vector prefixes (tone score for 'train'
            task, and 'id' for 'test' task respectively)
        table_filepath : str
            Path to the 'csv' file
        vectorizer : func
            Function for producing vector from terms
        features : core.Features
            object of Features class
        term_vocabulary : core.TermVocabulary
            Vocabulary of terms
        messsage_settings : dict
            Configuration settings for TwitterMessageParser

    Returns: list
    -------
        List of vectorized messages. Each message presented as list where
        first element is a 'score' or 'id' (depending on the 'train' or 'score'
        dataset accordingly) and the secont (latter) is a vector -- embedded
        sentence.
    """
    message_parser = TwitterMessageParser(message_settings, task_type)
    labeled_messages = []

    df = pd.read_csv(table_filepath, sep=',')
    for score in [-1, 0, 1]:
        logging.info("Reading tweets: [class: %s, file: %s]" % (
            score, table_filepath))
        # getting tweets with the same score
        filtered_df = tweets_filter(df, get_score_columns(task_type), score)

        for row in filtered_df.index:
            text = filtered_df['text'][row]
            index = filtered_df['twitid'][row]

            message_parser.parse(text)
            terms = message_parser.get_terms()
            doc_vocabulary.add_doc(terms, str(score))
            labeled_message = {'score': score,
                               'id': index,
                               'terms': to_unicode(terms),
                               'features': features.vectorize(text)}
            labeled_messages.append(labeled_message)

            term_vocabulary.insert_terms(
                    labeled_message['features'].iterkeys())

    # Create vectors
    problem = []
    for labeled_message in labeled_messages:
        vector = vectorizer(labeled_message, term_vocabulary, doc_vocabulary)
        if (collection_type == 'train'):
            problem.append([labeled_message['score'], vector])
        elif (collection_type == 'test'):
            problem.append([labeled_message['id'], vector])
        else:
            raise ValueError(
                    'Unexpected collection_type={}'.format(collection_type))

    return problem


def get_score_columns(task_type):
    return configs.DATA_TCC_FIELDS if task_type == TTK_TASK else \
        configs.DATA_BANK_FIELDS


def to_unicode(terms):
    """
    Converts list of 'str' into list of 'unicode' strings
    """
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms


def save_problem(problem, filepath):
    """
    Save problem using the format, supported by classifier libraries
    """
    with open(filepath, "w") as out:
        logging.info("Vectors count: %s" % (len(problem)))
        for vector in problem:
            out.write("%s " % (vector[0]))
            for index, value in sorted(vector[1].iteritems()):
                out.write("%s:%s " % (index, value))
            out.write("\n")


def tweets_filter(df, score_columns, score):
    ids = []
    for row in range(len(df)):
        for column in score_columns:
            if (not df[column].isnull()[row] and df[column][row] == score):
                ids.append(df['twitid'][row])

    return df[df['twitid'].isin(ids)]


def save_predict_config(columns, prediction_table, out_filepath):
    config = {"columns": columns, "prediction_table": prediction_table}

    with open(out_filepath, "w") as out:
        json.dump(config, out)
