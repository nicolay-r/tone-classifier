import theano
import numpy as np
import theano.tensor as T
import pickle


class LSTM1leTheano:

    def __init__(self, i_size, bptt_truncate=-1, hl_size=400):
        self.hl_size = hl_size
        self.i_size = i_size
        self.bptt_truncate = bptt_truncate

        x = T.matrix(name='x')
        y = T.ivector(name='y')

        # Model implementation
        out_size = 3
        E = np.random.uniform(-np.sqrt(1.0/i_size), np.sqrt(1.0/i_size),
                              (hl_size, i_size))
        U = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (4, hl_size, hl_size))
        W = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (4, hl_size, hl_size))
        V = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (out_size, hl_size))

        c = np.zeros(hl_size)

        self.E = theano.shared(E.astype(theano.config.floatX), name='E')
        self.U = theano.shared(U.astype(theano.config.floatX), name='U')
        self.V = theano.shared(V.astype(theano.config.floatX), name='V')
        self.W = theano.shared(W.astype(theano.config.floatX), name='W')
        self.c = theano.shared(c.astype(theano.config.floatX), name='c')

        self.dE = theano.shared(E.astype(theano.config.floatX), name='dE')
        self.dU = theano.shared(U.astype(theano.config.floatX), name='dU')
        self.dV = theano.shared(V.astype(theano.config.floatX), name='dV')
        self.dW = theano.shared(W.astype(theano.config.floatX), name='dW')

        self.epoch = theano.shared(0)

        def forward_prop_step(x_iv, st_prev, E, U, W, V, c):
            # Reduce layer
            x_v = E.dot(x_iv)
            # LSTM Layer
            i_t = T.nnet.hard_sigmoid(U[0].dot(x_v) + W[0].dot(st_prev))
            f_t = T.nnet.hard_sigmoid(U[1].dot(x_v) + W[1].dot(st_prev))
            o_t = T.nnet.hard_sigmoid(U[2].dot(x_v) + W[2].dot(st_prev))
            g_t = T.tanh(U[3].dot(x_v) + W[3].dot(st_prev))

            c_t = c * f_t + g_t * i_t
            s_t = T.tanh(c_t) * o_t

            o_next = T.nnet.softmax(V.dot(s_t))[0]
            return [o_next, s_t]

        [o, s], updates = theano.scan(
                forward_prop_step,
                sequences=x,
                truncate_gradient=-1,
                outputs_info=[
                    None,
                    dict(initial=T.zeros(hl_size))],
                non_sequences=[self.E, self.U, self.W, self.V, self.c],
                strict=True)

        cost = T.sum(T.nnet.categorical_crossentropy(o, y))

        dE = T.grad(cost, self.E)
        dU = T.grad(cost, self.U)
        dV = T.grad(cost, self.V)
        dW = T.grad(cost, self.W)
        dc = T.grad(cost, self.c)

        reg_lambda = T.scalar(name='reg_lambda')

        # Functions
        self.forward_propagation = theano.function(inputs=[x], outputs=[o])
        self.calculate_loss = theano.function(inputs=[x, y], outputs=cost)
        self.sgd_step = theano.function(
                [x, y, reg_lambda],
                [],
                updates=[(self.E, self.E - reg_lambda * dE),
                         (self.U, self.U - reg_lambda * dU),
                         (self.W, self.W - reg_lambda * dW),
                         (self.V, self.V - reg_lambda * dV),
                         (self.c, self.c - reg_lambda * dc),
                         (self.dE, dE),
                         (self.dU, dU),
                         (self.dW, dW),
                         (self.dV, dV),
                         (self.epoch, self.epoch + 1)])

    def rollback_step(self, reg_lambda):
        self.E.set_value(self.E.get_value() + reg_lambda * self.dE.get_value())
        self.U.set_value(self.U.get_value() + reg_lambda * self.dU.get_value())
        self.W.set_value(self.W.get_value() + reg_lambda * self.dW.get_value())
        self.V.set_value(self.V.get_value() + reg_lambda * self.dV.get_value())

    def apply_step(self, reg_lambda):
        self.E.set_value(self.E.get_value() - reg_lambda * self.dE.get_value())
        self.U.set_value(self.U.get_value() - reg_lambda * self.dU.get_value())
        self.W.set_value(self.W.get_value() - reg_lambda * self.dW.get_value())
        self.V.set_value(self.V.get_value() - reg_lambda * self.dV.get_value())

    @staticmethod
    def load(filepath):
        """
        returns: RNNTheano
        """
        with open(filepath, 'r') as f:
            data = pickle.load(f)

            model = LSTM1leTheano(
                i_size=data['i_size'],
                hl_size=data['hl_size'],
                bptt_truncate=data['bptt_truncate'])

            model.E.set_value(data['E'].get_value())
            model.U.set_value(data['U'].get_value())
            model.W.set_value(data['W'].get_value())
            model.V.set_value(data['V'].get_value())
            model.epoch = data['epoch']

        return model

    def save(self, filepath):
        data = {'E': self.E,
                'U': self.U,
                'V': self.V,
                'W': self.W,
                'i_size': self.i_size,
                'hl_size': self.hl_size,
                'bptt_truncate': self.bptt_truncate,
                'epoch': self.epoch}
        with open(filepath, 'wb') as out:
            pickle.dump(data, out)
