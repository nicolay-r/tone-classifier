#!/usr/bin/python
# -*- coding: utf-8 -*-
# global
import sys
import logging
from os.path import join

# local
import utils
import utils_keras as uk
import model_w2v
import eval as ev
import configs

# network models
# from networks.keras.lstm_1l import KerasLSTM_1L as K
# from networks.keras.lstm_2l_2i_concat import KerasLSTM_2L_2i_concat as K
# from networks.keras.lstm_1l_2i_concat import KerasLSTM_1L_2i_concat as K
# from networks.keras.lstm_1l_sum import KerasLSTM_1L_sum as K
from networks.keras.lstm_1l_1i_emb_lex import KerasLSTM_1L_1i_emb_lex as K


if __name__ == "__main__":
    utils.init_logger()
    config = {'task_type': sys.argv[1],
              'test_table': sys.argv[2],
              'train_table': sys.argv[3],
              'etalon_table': sys.argv[4]}

    MAX_SEQUENCE_LENGTH = 40
    EPOCHS = 20
    BATCH_SIZE = 8
    OUTPUT_FILEPATH = join(configs.NETWORK_MODELS_ROOT, "keras_output.txt")

    keras_model = K(model_w2v.W2V_MODELS, MAX_SEQUENCE_LENGTH)

    # prepare
    train_problem, test_problem = uk.prepare_problem(
        keras_model.message_vectorizer,
        config['task_type'],
        config['train_table'],
        config['test_table'],
        config['etalon_table'])

    # fit
    logging.info("Fitting model ...")
    keras_model.fit(train_problem, EPOCHS, BATCH_SIZE)

    # predict
    logging.info("Predicting results ...")
    y_test, ids = keras_model.predict(test_problem, BATCH_SIZE)

    # check
    result_table = config['test_table'] + '.result.csv'
    uk.prepare_result_table(config['test_table'], result_table)
    uk.fill_test_results(y_test, config['task_type'], result_table)

    logging.info("Check results ...")
    result = ev.check(
            config['task_type'],
            result_table,
            config['etalon_table'])

    # output
    ev.show(result, OUTPUT_FILEPATH)
