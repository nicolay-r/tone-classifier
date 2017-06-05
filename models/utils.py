# -*- coding: utf-8 -*-

# global
import sys
import json
import pandas as pd

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


def vectorization_core(vectorizer, init_term_vocabulary=True,
                       merge_doc_vocabularies=False):
    """
    Main function of collection vectorization

    vectorizer : message vectorization function
    returns : None
    """
    if (sys.argv < 8):
        exit(0)

    config = {'task_type': sys.argv[1],
              'database': sys.argv[2],  # save the output results
              'train_table': sys.argv[3],
              'test_table': sys.argv[4],
              'train_output': sys.argv[5],
              'test_output': sys.argv[6],
              'pconf_output': sys.argv[7]}
    message_configpath = configs.TWITTER_MESSAGE_PARSER_CONFIG
    features_configpath = configs.FEATURES_CONFIG

    # Create vocabulary of terms
    if init_term_vocabulary is True:
        term_vocabulary = core.indexer.create_term_vocabulary(
                                [config['train_table'], config['test_table']],
                                message_configpath)
    else:
        term_vocabulary = TermVocabulary()

    features = Features(
                TwitterMessageParser(message_configpath, config['task_type']),
                features_configpath)

    doc_vocabulary = DocVocabulary()
    # Train problem
    train_problem = create_problem(config['task_type'],
                                   'train',
                                   config['train_table'],
                                   vectorizer,
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   features_configpath,
                                   message_configpath)

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
                                  features_configpath,
                                  message_configpath)

    result_table = config['test_table'] + '.result.csv'
    print 'Create a file for classifier results: {}'.format(result_table)
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
                   features_configpath, message_configpath):
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
        features_configpath : str
            Configuration path for Features class
        messsage_configpath : str
            Configuration path for TwitterMessageParser

    Returns:
    -------
        List of vectorized messages
    """
    message_parser = TwitterMessageParser(message_configpath, task_type)
    labeled_messages = []

    df = pd.read_csv(table_filepath, sep=',')
    for score in [-1, 0, 1]:
        print "Class:\t[%s, %s]" % (score, table_filepath)
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
        print "Vectors count: %s" % (len(problem))
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
