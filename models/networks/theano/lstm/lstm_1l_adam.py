import theano
import numpy as np
import theano.tensor as T
import pickle


class LSTM1lAdamTheano:
    """
    Implementation of the LSTM network with one layer, and using 'adam'
    for network optimization during the training process.
    Original article: https://arxiv.org/pdf/1412.6980.pdf
    """

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
                              (4, hl_size, hl_size))
        W = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (4, hl_size, hl_size))
        V = np.random.uniform(-np.sqrt(1.0/hl_size), np.sqrt(1.0/hl_size),
                              (out_size, hl_size))

        c = np.zeros(hl_size)

        self.U = theano.shared(U.astype(theano.config.floatX), name='U')
        self.V = theano.shared(V.astype(theano.config.floatX), name='V')
        self.W = theano.shared(W.astype(theano.config.floatX), name='W')
        self.c = theano.shared(c.astype(theano.config.floatX), name='c')

        self.eU = theano.shared(np.zeros(U.shape).astype(theano.config.floatX),
                                name='eU')
        self.eV = theano.shared(np.zeros(V.shape).astype(theano.config.floatX),
                                name='eV')
        self.eW = theano.shared(np.zeros(W.shape).astype(theano.config.floatX),
                                name='eW')
        self.ec = theano.shared(np.zeros(c.shape).astype(theano.config.floatX),
                                name='ec')

        self.mU = theano.shared(np.zeros(U.shape).astype(theano.config.floatX),
                                name='mU')
        self.mV = theano.shared(np.zeros(V.shape).astype(theano.config.floatX),
                                name='mV')
        self.mW = theano.shared(np.zeros(W.shape).astype(theano.config.floatX),
                                name='mW')
        self.mc = theano.shared(np.zeros(c.shape).astype(theano.config.floatX),
                                name='mc')

        self.vU = theano.shared(np.zeros(U.shape).astype(theano.config.floatX),
                                name='vU')
        self.vV = theano.shared(np.zeros(V.shape).astype(theano.config.floatX),
                                name='vV')
        self.vW = theano.shared(np.zeros(W.shape).astype(theano.config.floatX),
                                name='vW')
        self.vc = theano.shared(np.zeros(c.shape).astype(theano.config.floatX),
                                name='vc')

        self.epoch = theano.shared(0)
        self.t = theano.shared(1)

        def forward_prop_step(x_v, st_prev, U, W, V, c):
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
                non_sequences=[self.U, self.W, self.V, self.c],
                strict=True)

        cost = T.sum(T.nnet.categorical_crossentropy(o, y))

        dU = T.grad(cost, self.U)
        dV = T.grad(cost, self.V)
        dW = T.grad(cost, self.W)
        dc = T.grad(cost, self.c)

        reg_lambda = T.scalar(name='reg_lambda')
        decay = T.scalar(name='decay')
        betta_1 = T.scalar(name='betta_1')
        betta_2 = T.scalar(name='betta_2')

        # adam
        eU = decay * self.eU + (1 - decay) * dU ** 2
        eV = decay * self.eV + (1 - decay) * dV ** 2
        eW = decay * self.eW + (1 - decay) * dW ** 2
        ec = decay * self.ec + (1 - decay) * dc ** 2

        mU = betta_1 * self.mU + (1 - betta_1) * dU
        mV = betta_1 * self.mU + (1 - betta_1) * dV
        mW = betta_1 * self.mU + (1 - betta_1) * dW
        mc = betta_1 * self.mU + (1 - betta_1) * dc

        vU = betta_2 * self.vU + (1 - betta_2) * dU ** 2
        vV = betta_2 * self.vU + (1 - betta_2) * dV ** 2
        vW = betta_2 * self.vU + (1 - betta_2) * dW ** 2
        vc = betta_2 * self.vU + (1 - betta_2) * dc ** 2

        mU_cap = mU / (1 - betta_1 ** self.t)
        mV_cap = mV / (1 - betta_1 ** self.t)
        mW_cap = mW / (1 - betta_1 ** self.t)
        mc_cap = mc / (1 - betta_1 ** self.t)

        vU_cap = vU / (1 - betta_2 ** self.t)
        vV_cap = vV / (1 - betta_2 ** self.t)
        vW_cap = vW / (1 - betta_2 ** self.t)
        vc_cap = vc / (1 - betta_2 ** self.t)

        # Functions
        self.forward_propagation = theano.function(inputs=[x], outputs=[o])
        self.calculate_loss = theano.function(inputs=[x, y], outputs=cost)
        self.sgd_step = theano.function(
            [x, y, reg_lambda, theano.Param(decay, default=0.9),
             theano.Param(betta_1, default=0.999),
             theano.Param(betta_2, default=0.9)],
            [],
            updates=[
                (self.U, self.U - reg_lambda * dU * mU_cap / (T.sqrt(vU_cap) + 1e-6)),
                (self.W, self.W - reg_lambda * dW * mW_cap / (T.sqrt(vW_cap) + 1e-6)),
                (self.V, self.V - reg_lambda * dV * mV_cap / (T.sqrt(vV_cap) + 1e-6)),
                (self.c, self.c - reg_lambda * dc * mc_cap / (T.sqrt(vc_cap) + 1e-6)),

                (self.eU, eU),
                (self.eW, eW),
                (self.eV, eV),
                (self.ec, ec),

                (self.mU, mU),
                (self.mW, mW),
                (self.mV, mV),
                (self.mc, mc),

                (self.vU, vU),
                (self.vW, vW),
                (self.vV, vV),
                (self.vc, vc),

                (self.t, self.t + 1),
                (self.epoch, self.epoch + 1)])

    @staticmethod
    def load(filepath):
        """
        returns: RNNTheano
        """
        with open(filepath, 'r') as f:
            data = pickle.load(f)

            model = LSTM1lAdamTheano(
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
