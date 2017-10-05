import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense
from keras.layers.recurrent import LSTM


class KerasLSTM_1L:

    def __init__(self, w2v_model, max_sequence_length):
        self.W2V_MODEL = w2v_model
        self.MAX_SEQUENCE_LENGTH = max_sequence_length
        # build model
        self.model = self.__build(w2v_model, self.MAX_SEQUENCE_LENGTH)

    def message_vectorizer(self, labeled_message, term_voc, doc_voc):
        """
        Vector builder
        Arguments:
        ---------
            labeled_message -- dictionary with the following fields:
                            {score, id, terms, features}
            term_voc -- vocabulary of terms
            doc_voc -- vocabulary of documents
        Returns
        ------
            vector: np.array
        """
        # features = labeled_message['features']
        # vector = model_features_only.feature_vectorizer(features, term_voc)

        terms = labeled_message['terms']
        vector = np.zeros(self.MAX_SEQUENCE_LENGTH)

        for i in range(min(len(terms), self.MAX_SEQUENCE_LENGTH)):
            term = terms[i]
            if (term in self.W2V_MODEL.vocab):
                vector[i] = self.W2V_MODEL.vocab.get(term).index

        return vector

    def fit(self, train_problem, epochs, batch_size):
        """
        Train model using 'train_problem'
        """
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
        """
        vectors = []
        labels = []
        for message in problem:

            vectors.append(message[1])

            if (collection_type == 'train'):
                y = np.zeros(3)
                y[message[0] + 1] = 1
                labels.append(y)  # class as a label
            if (collection_type == 'test'):
                labels.append(message[0])  # message ID

        return np.vstack(vectors), np.vstack(labels)

    def __build(self, w2v_model, input_length):
        """
        Model based on single word2vec vocabulary

        w2v_model : gensim.models.word2vec.Word2Vec
            word2vec model

        input_length : int
            maximal amount of items per message

        returns : keras.models.Model
            compiled model
        """
        # input_layer = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
        embedding_layer = Embedding(
            len(w2v_model.vocab),
            w2v_model.vector_size,
            weights=[self.__create_embedding_matrix(w2v_model)],
            input_length=input_length,
            trainable=False)
        lstm_layer = LSTM(200)
        dense_layer = Dense(3, activation='softmax')

        model = Sequential()
        model.add(embedding_layer)
        model.add(lstm_layer)
        model.add(dense_layer)

        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        print model.summary()

        return model

    @staticmethod
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
