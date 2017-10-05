import numpy as np
from keras.models import Model
from keras.layers import Embedding, Dense, Input, concatenate
from keras.layers.recurrent import LSTM
from keras.preprocessing import sequence


class KerasLSTM_1L_2i_concat:

    def __init__(self, w2v_models, max_sequence_length):
        """
        w2v_models : list
            list of word2vec models
        """
        self.FEATURES_COUNT = None
        self.W2V_MODELS = w2v_models
        self.TERMS_SEQUENCE_LENGTH = max_sequence_length

    def message_vectorizer(self, labeled_message, term_voc, doc_voc):
        """
        Vector builder

        labeled_message : dict
            dictionary with the following fields: {score, id, terms, features}
        term_voc : core.TermVocabulary
            vocabulary of terms
        doc_voc : core.DocVocabulary
            vocabulary of documents

        returns : dict
            {'terms' : np.array, 'features' : np.array}
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

        # features
        features = labeled_message['features']
        features_vector = self.__feature_vectorizer(features)

        if (self.FEATURES_COUNT is None):
            self.FEATURES_COUNT = len(features_vector)
        else:
            assert(self.FEATURES_COUNT == len(features_vector))

        return {'terms': terms_vector, 'features': features_vector}

    def fit(self, train_problem, epochs, batch_size):
        """
        Train model using 'train_problem'
        """
        # initialize model
        self.model = self.__build(
                self.W2V_MODELS,
                self.TERMS_SEQUENCE_LENGTH,
                self.FEATURES_COUNT)

        # fit
        x_train_terms, x_train_features, y_train = self.__problem_vectorizer(
            train_problem, 'train')
        self.model.fit(
                {'terms_input': x_train_terms,
                 'features_input': x_train_features},
                y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, test_problem, batch_size):
        """
        returns : (nd.array, nd.array)
            network output and according message ids
        """
        x_test_terms, x_test_features, ids = self.__problem_vectorizer(
            test_problem, 'test')

        y_test = self.model.predict(
                {'terms_input': x_test_terms,
                 'features_input': x_test_features},
                batch_size=batch_size)

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

        returns: (terms, features, lables)
        """
        terms = []
        features = []

        labels = []
        for message in problem:

            terms.append(message[1]['terms'])
            features.append(message[1]['features'])

            if (collection_type == 'train'):
                y = np.zeros(3)
                y[message[0] + 1] = 1
                labels.append(y)  # class as a label
            if (collection_type == 'test'):
                labels.append(message[0])  # message ID

        return np.vstack(terms), np.vstack(features), np.vstack(labels)

    @staticmethod
    def __create_embedding_matrix(w2v_models):
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

        matrix = np.zeros((words_count, vector_size))

        offset = 0
        for w2v_model in w2v_models:
            for word, info in w2v_model.vocab.items():
                index = info.index
                matrix[offset + index] = sequence.pad_sequences(
                    [w2v_model.syn0[index]], vector_size, padding='post')
            offset += len(w2v_model.vocab)

        return matrix

    @staticmethod
    def __feature_vectorizer(features):
        """
        Produces vector of features
        returns: np.ndarray
        """
        vector = np.zeros(len(features))

        i = 0
        for feature_name in sorted(features.keys()):
            vector[i] = features[feature_name]
            i += 1

        return vector

    def __build(self, w2v_models, terms_input_length, features_input_length):
        """
        w2v_models : list
            list of gensim.models.word2vec.Word2Vec models
        """
        input_1 = Input(shape=(terms_input_length,),
                        dtype='int32',
                        name='terms_input')

        weights = self.__create_embedding_matrix(w2v_models)

        embedding_layer = Embedding(
            weights.shape[0],
            weights.shape[1],
            weights=[weights],
            input_length=terms_input_length,
            trainable=False)(input_1)
        lstm_layer_1 = LSTM(200, return_sequences=True)(embedding_layer)
        lstm_layer_2 = LSTM(200)(lstm_layer_1)

        input_2 = Input(shape=(features_input_length,),
                        dtype='float32',
                        name='features_input')

        dense_layer = Dense(10, activation='tanh')(input_2)

        merged_layer = concatenate([lstm_layer_2, dense_layer])

        network_output = Dense(3, activation='softmax')(merged_layer)

        model = Model(inputs=[input_1, input_2], outputs=network_output)

        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        print model.summary()

        return model
