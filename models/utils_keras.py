from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

import logging
import utils
import pandas as pd
import numpy as np
from model_rnn import load_embeddings


def prepare_problem(vectorizer, task_type, train_table, test_table,
                    etalon_table):
    """
    Main function of vectorization for neural network
    """
    message_settings, features_settings = load_embeddings()

    features = Features(
            TwitterMessageParser(message_settings, task_type),
            features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    train_problem = utils.create_problem(task_type, 'train', train_table,
                                         vectorizer, features, term_vocabulary,
                                         doc_vocabulary, message_settings)

    test_problem = utils.create_problem(task_type, 'test', test_table,
                                        vectorizer, features, term_vocabulary,
                                        doc_vocabulary, message_settings)

    return (train_problem, test_problem)


def process_problem(problem, collection_type):
    """
    problem: list [{label, vector}, ... ]
        List of vectorized messages. Each message presented as list where
        first element is a 'score' or 'id' (depending on the 'train' or 'score'
        dataset accordingly) and the secont (latter) is a vector -- embedded
        sentence (obtained by vectorizer)
    collection_type: str
        'test' or 'train'
    """
    vectors = []
    labels = []
    for message in problem:

        if (collection_type == 'train'):
            y = np.zeros(3)
            y[message[0] + 1] = 1
            labels.append(y)  # class as a label
            vectors.append(message[1])

        if (collection_type == 'test'):
            labels = message[0]  # message ID
            vectors.append(message[1])

    return np.vstack(vectors), np.vstack(labels)


def fill_test_results(model, y_test, task_type, result_table):
    """
        X : np.ndarray
            represents test dataset
        y_test : np.ndarray (None, 3)
            answers
        task_type : str
            'bank' or 'tcc'
        result_table : str
            output table which should be filled with the predicted result
    """
    # TODO: remove duplicated code at predict.py
    logging.info("Filling answers in {} ...".format(result_table))
    df = pd.read_csv(result_table, sep=',')
    sentiment_columns = utils.get_score_columns(task_type)
    for msg_index, row_index in enumerate(df.index):
        label = np.argmax(y_test[msg_index]) - 1
        for column in sentiment_columns:
            if not df[column].isnull()[row_index]:
                df.loc[row_index, column] = label

    # Rewriting table with the filled results
    df.to_csv(result_table, sep=',')
    del df


def prepare_result_table(test_table, result_table):
    logging.info('Create a file for classifier results: {}'.format(
            result_table))
    result_df = pd.read_csv(test_table, sep=',')
    result_df.to_csv(result_table, sep=',')
