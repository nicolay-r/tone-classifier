import theano
import numpy as np
import theano.tensor as T
import pickle


class LSTM2lTheano:

    def __init__(self, i_size, bptt_truncate=-1):
        hl_size = i_size

        self.hl_size = hl_size
        self.i_size = i_size
        self.bptt_truncate = bptt_truncate

        x = T.matrix(name='x')
        y = T.ivector(name='y')

        # Model implementation
        out_size = 3
        U = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (8, hl_size, hl_size))
        W = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (8, hl_size, hl_size))
        V = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (out_size, hl_size))

        c = np.zeros(hl_size)

        self.U = theano.shared(U.astype(theano.config.floatX), name='U')
        self.V = theano.shared(V.astype(theano.config.floatX), name='V')
        self.W = theano.shared(W.astype(theano.config.floatX), name='W')
        self.c = theano.shared(c.astype(theano.config.floatX), name='c')

        self.dU = theano.shared(U.astype(theano.config.floatX), name='dU')
        self.dV = theano.shared(V.astype(theano.config.floatX), name='dV')
        self.dW = theano.shared(W.astype(theano.config.floatX), name='dW')

        self.epoch = theano.shared(0)

        def forward_prop_step(x_v, o, st1_prev, st2_prev, U, W, V, c):

            # LSTM Layer 1
            i_t1 = T.nnet.hard_sigmoid(U[0].dot(x_v) + W[0].dot(st1_prev))
            f_t1 = T.nnet.hard_sigmoid(U[1].dot(x_v) + W[1].dot(st1_prev))
            o_t1 = T.nnet.hard_sigmoid(U[2].dot(x_v) + W[2].dot(st1_prev))
            g_t1 = T.tanh(U[3].dot(x_v) + W[3].dot(st1_prev))

            c_t1 = c * f_t1 + g_t1 * i_t1
            s_t1 = T.tanh(c_t1) * o_t1

            # LSTM Layer 2
            i_t2 = T.nnet.hard_sigmoid(U[4].dot(s_t1) + W[4].dot(st2_prev))
            f_t2 = T.nnet.hard_sigmoid(U[5].dot(s_t1) + W[5].dot(st2_prev))
            o_t2 = T.nnet.hard_sigmoid(U[6].dot(s_t1) + W[6].dot(st2_prev))
            g_t2 = T.tanh(U[7].dot(s_t1) + W[7].dot(st2_prev))

            c_t2 = c * f_t2 + g_t2 * i_t2
            s_t2 = T.tanh(c_t2) * o_t2

            o_next = T.nnet.softmax(V.dot(s_t2))[0]
            return [o_next, s_t1, s_t2]

        [o, s_t1, s_t2], updates = theano.scan(
                forward_prop_step,
                sequences=x,
                truncate_gradient=-1,
                outputs_info=[
                    dict(initial=T.zeros(out_size)),
                    dict(initial=T.zeros(hl_size)),
                    dict(initial=T.zeros(hl_size))],
                non_sequences=[self.U, self.W, self.V, self.c],
                strict=True)

        cost = T.sum(T.nnet.categorical_crossentropy(o, y))

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
                updates=[(self.U, self.U - reg_lambda * dU),
                         (self.W, self.W - reg_lambda * dW),
                         (self.V, self.V - reg_lambda * dV),
                         (self.c, self.c - reg_lambda * dc),
                         (self.dU, dU),
                         (self.dW, dW),
                         (self.dV, dV),
                         (self.epoch, self.epoch + 1)])

    def rollback_step(self, reg_lambda):
        self.U.set_value(self.U.get_value() + reg_lambda * self.dU.get_value())
        self.W.set_value(self.W.get_value() + reg_lambda * self.dW.get_value())
        self.V.set_value(self.V.get_value() + reg_lambda * self.dV.get_value())

    def apply_step(self, reg_lambda):
        self.U.set_value(self.U.get_value() - reg_lambda * self.dU.get_value())
        self.W.set_value(self.W.get_value() - reg_lambda * self.dW.get_value())
        self.V.set_value(self.V.get_value() - reg_lambda * self.dV.get_value())


    @staticmethod
    def load(filepath):
        """
        returns: LSTM2lTheano
        """
        with open(filepath, 'r') as f:
            data = pickle.load(f)

            model = LSTM2lTheano(
                i_size=data['i_size'],
                hl_size=data['hl_size'],
                bptt_truncate=data['bptt_truncate'])

            model.U.set_value(data['U'].get_value())
            model.W.set_value(data['W'].get_value())
            model.V.set_value(data['V'].get_value())
            model.epoch = data['epoch']

        return model

    def save(self, filepath):
        data = {'U': self.U,
                'V': self.V,
                'W': self.W,
                'i_size': self.i_size,
                'hl_size': self.hl_size,
                'bptt_truncate': self.bptt_truncate,
                'epoch': self.epoch}
        with open(filepath, 'wb') as out:
            pickle.dump(data, out)
