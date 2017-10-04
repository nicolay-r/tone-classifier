import numpy as np
from keras.models import Model
from keras.layers import Embedding, Dense, Input
from keras.layers.recurrent import LSTM


# TODO: create replicated model with features support
def build(w2v_model, input_length):
    """
    Model based on single word2vec vocabulary

    w2v_model : gensim.models.word2vec.Word2Vec
        word2vec model

    input_length : int
        maximal amount of items per message

    returns : keras.models.Model
        compiled model
    """
    input_layer = Input(shape=(input_length,), dtype='int32')
    embedding_layer = Embedding(len(w2v_model.vocab),
                                w2v_model.vector_size,
                                weights=[__create_embedding_matrix(w2v_model)],
                                input_length=input_length,
                                trainable=False)
    lstm_layer = LSTM(200)
    dense_layer = Dense(3, activation='softmax')

    x = embedding_layer(input_layer)
    x = lstm_layer(x)
    network_output = dense_layer(x)

    model = Model(input_layer, network_output)

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model


# TODO: multiple w2v_models
def __create_embedding_matrix(w2v_model):
    """
    creates matrix (words_count, embedding_size) based on 'w2v_model'

    w2v_model: gensim.models.word2vec.Word2Vec
        word2vec model

    returns: np.ndarray
        shape (words_count, embedding_size)
    """
    words_count = len(w2v_model.vocab)
    matrix = np.zeros((words_count, w2v_model.vector_size))

    for word, info in w2v_model.vocab.items():
        index = info.index
        matrix[index] = w2v_model.syn0[index]

    return matrix
