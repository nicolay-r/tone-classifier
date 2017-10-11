import numpy as np
import pandas as pd
from keras.models import Model
from keras.layers import Embedding, Dense, Input
from keras.layers.recurrent import LSTM
from keras.preprocessing import sequence
from os.path import join


class KerasLSTM_1L_1i_emb_lex:
    """ Represents concatenation of vectors from embedding with lexicon features
    """

    def __init__(self, w2v_models, max_sequence_length):
        """
        w2v_models : list
            list of word2vec models
        """
        self.W2V_MODELS = w2v_models
        self.TERMS_SEQUENCE_LENGTH = max_sequence_length
        self.lexicons = self.__create_lexicons()
        self.LEXICONS_COUNT = len(self.lexicons)

    def message_vectorizer(self, labeled_message, term_voc, doc_voc):
        """
        Vector builder

        labeled_message : dict
            dictionary with the following fields: {score, id, terms, features}
        term_voc : core.TermVocabulary
            vocabulary of terms
        doc_voc : core.DocVocabulary
            vocabulary of documents

        returns : []
            concatenation of embediding and feature vectors
        """
        # terms
        terms = labeled_message['terms']
        terms_vector = np.zeros(self.TERMS_SEQUENCE_LENGTH)

        i = 0
        offset = 0
        for model in self.W2V_MODELS:
            for term in terms:
                if i >= self.TERMS_SEQUENCE_LENGTH:
                    break
                if (term in model.vocab):
                    terms_vector[i] = model.vocab.get(term).index + offset
                i += 1
            offset += len(model.vocab)

        return {'terms': terms_vector}

    def fit(self, train_problem, epochs, batch_size):
        """
        Train model using 'train_problem'
        """
        # initialize model
        self.model = self.__build(
                self.W2V_MODELS,
                self.TERMS_SEQUENCE_LENGTH + self.LEXICONS_COUNT)

        # fit
        x_train, y_train = self.__problem_vectorizer(train_problem, 'train')
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, test_problem, batch_size):
        """
        returns : (nd.array, nd.array)
            network output and according message ids
        """
        x_test, ids = self.__problem_vectorizer(test_problem, 'test')
        y_test = self.model.predict(x_test, batch_size=batch_size)

        return (y_test, ids)

    @staticmethod
    def __problem_vectorizer(problem, collection_type):
        """
        problem: list [{label, vector}, ... ]
            List of vectorized messages. Each message presented as list where
            first element is a 'score' or 'id' (depending on the 'train' or
            'score' dataset accordingly) and the secont (latter) is a vector --
            embedded sentence (obtained by vectorizer)

        collection_type: str
            'test' or 'train'

        returns: (terms, lables)
        """
        terms = []

        labels = []
        for message in problem:

            terms.append(message[1])

            if (collection_type == 'train'):
                y = np.zeros(3)
                y[message[0] + 1] = 1
                labels.append(y)  # class as a label
            if (collection_type == 'test'):
                labels.append(message[0])  # message ID

        return np.vstack(terms), np.vstack(labels)

    @staticmethod
    def __create_embedding_matrix(w2v_models, lexicons):
        """
        creates matrix (words_count, embedding_size) based on list of word2vec
        models

        w2v_model : list
            list of gensim.models.word2vec.Word2Vec models

        returns: np.ndarray
            shape (words_count, embedding_size)
        """
        vector_size = max(m.vector_size for m in w2v_models)
        words_count = sum(len(m.vocab) for m in w2v_models)

        width = vector_size + len(lexicons)
        matrix = np.zeros((words_count, width))

        offset = 0
        for w2v_model in w2v_models:
            for word, info in w2v_model.vocab.items():
                index = info.index

                w = sequence.pad_sequences(
                    [w2v_model.syn0[index]], width, padding='post')

                lw = KerasLSTM_1L_1i_emb_lex.__lexicon_weights(word, lexicons)

                for i, e in enumerate(range(len(lw))):
                    w[0][w.shape[1] - len(lw) + i] = e

                matrix[offset + index] = w

            offset += len(w2v_model.vocab)

        return matrix

    @staticmethod
    def __lexicon_weights(term, lexicons):
        term = term.encode('utf-8')
        v = np.zeros(len(lexicons))
        for i, l in enumerate(lexicons):
            s = l[term == l['term']]
            if (len(s) > 0):
                v[i] = s['tone'].values[0]

        return v

    def __build(self, w2v_models, input_length):
        """
        w2v_models : list
            list of gensim.models.word2vec.Word2Vec models
        """
        input_1 = Input(shape=(input_length,),
                        dtype='int32',
                        name='terms_input')

        weights = self.__create_embedding_matrix(w2v_models, self.lexicons)

        embedding_layer = Embedding(
            weights.shape[0],
            weights.shape[1],
            weights=[weights],
            input_length=input_length,
            trainable=False)(input_1)

        lstm_layer = LSTM(200)(embedding_layer)

        network_output = Dense(3, activation='softmax')(lstm_layer)

        model = Model(input_1, network_output)

        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        print model.summary()

        return model

    def __create_lexicons(self):
        root = "../data/lexicons/"
        names = ["experts_lexicon.csv",
                 "feb_june_16_lexicon.csv",
                 "rubtsova_lexicon.csv",
                 "mtd_rus_lexicon.csv"]

        lexicons = []
        for name in names:
            fp = join(root, name)
            print "reading lexicon: {}".format(name)
            lexicons.append(pd.read_csv(fp, sep=','))

        return lexicons
