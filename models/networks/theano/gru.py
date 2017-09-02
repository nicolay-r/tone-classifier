import pickle
import theano
import numpy as np
import theano.tensor as T


# GRU Network with 2 hidden layers
class GRU2LTheano:

    # Inspired by the following implementation:
    # https://github.com/dennybritz/rnn-tutorial-gru-lstm/blob/master/gru_theano.py

    def __init__(self, i_size, bptt_truncate=-1):
        hl_size = i_size

        x = T.matrix(name='x')
        y = T.ivector(name='y')

        self.hl_size = hl_size
        self.i_size = i_size
        self.bptt_truncate = bptt_truncate

        # Model implementation
        out_size = 3

        U = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (6, hl_size, hl_size))
        W = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (6, hl_size, hl_size))

        V = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (6, out_size, hl_size))

        self.U = theano.shared(U.astype(theano.config.floatX), name='U')
        self.V = theano.shared(V.astype(theano.config.floatX), name='V')
        self.W = theano.shared(W.astype(theano.config.floatX), name='W')

        self.dU = theano.shared(U.astype(theano.config.floatX), name='dU')
        self.dV = theano.shared(V.astype(theano.config.floatX), name='dV')
        self.dW = theano.shared(W.astype(theano.config.floatX), name='dW')

        self.epoch = theano.shared(0)

        def forward_prop_step(x_v, o, s_t1_prev, s_t2_prev, U, W, V):
            # GRU Layer 1
            z_t1 = T.nnet.hard_sigmoid(U[0].dot(x_v) + W[0].dot(s_t1_prev))
            r_t1 = T.nnet.hard_sigmoid(U[1].dot(x_v) + W[1].dot(s_t1_prev))
            c_t1 = T.tanh(U[2].dot(x_v) + W[2].dot(s_t1_prev * r_t1))
            s_t1 = (T.ones_like(z_t1) - z_t1) * c_t1 + z_t1 * s_t1_prev

            # GRU Layer 2
            z_t2 = T.nnet.hard_sigmoid(U[3].dot(s_t1) + W[3].dot(s_t2_prev))
            r_t2 = T.nnet.hard_sigmoid(U[4].dot(s_t1) + W[4].dot(s_t2_prev))
            c_t2 = T.tanh(U[5].dot(s_t1) + W[5].dot(s_t2_prev * r_t2))
            s_t2 = (T.ones_like(z_t2) - z_t2) * c_t2 + z_t2 * s_t2_prev

            o_t = T.nnet.softmax(V.dot(s_t2))[0]

            return [o_t, s_t1, s_t2]

        [o, s1, s2], updates = theano.scan(
                forward_prop_step,
                # iterate through ivector 'x'
                sequences=x,
                # use the full backpropagation (for T.grad)
                truncate_gradient=bptt_truncate,
                # initial output state, which computed recurently
                outputs_info=[
                    dict(initial=T.zeros(out_size)),
                    dict(initial=T.zeros(hl_size)),
                    dict(initial=T.zeros(hl_size))],
                non_sequences=[self.U, self.W, self.V],
                strict=True)

        # Check the forward propagation function
        # f = theano.function(inputs=[x], outputs=results, updates=updates)

        cost = T.sum(T.nnet.categorical_crossentropy(o, y))

        dU = T.grad(cost, self.U)
        dV = T.grad(cost, self.V)
        dW = T.grad(cost, self.W)

        reg_lambda = T.scalar(name='reg_lambda')

        # Functions
        self.forward_propagation = theano.function(inputs=[x], outputs=[o])
        self.calculate_loss = theano.function(inputs=[x, y], outputs=cost)
        self.sgd_step = theano.function(
                inputs=[x, y, reg_lambda],
                updates=[(self.U, self.U - reg_lambda * dU),
                         (self.W, self.W - reg_lambda * dW),
                         (self.V, self.V - reg_lambda * dV),
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

    @staticmethod
    def load(filepath):
        """
        returns: GRU2LTheano
        """
        with open(filepath, 'r') as f:
            data = pickle.load(f)

            model = GRU2LTheano(
                i_size=data['i_size'],
                hl_size=data['hl_size'],
                bptt_truncate=data['bptt_truncate'])

            model.U.set_value(data['U'].get_value())
            model.W.set_value(data['W'].get_value())
            model.V.set_value(data['V'].get_value())
            model.epoch = data['epoch']

        return model
